from fastapi import APIRouter, Depends
from apps.nusatrip.constants import Url
from apps.nusatrip.models import NusatripRequest
from apps.nusatrip.constants import Mappingrc
import requests
import xmltodict

router = APIRouter()

@router.get('/flight_search')
def flight_search(params: NusatripRequest.FlightSearchParam = Depends()):
    parameters = params.dict()
    r = requests.get(Url.URL_DEV+'/flight_search', params = parameters)
    print("Ini response", r.text)
    print(parameters)
    trimmedXml = r.text[r.text.find("?>")+2:]
    dictResult = xmltodict.parse(trimmedXml)

    if dictResult["response"]["messages"] == None:
        resp = dict(msg="success")
        return resp
    else:
        nusatripResponseCode = dictResult["response"]["messages"]["message"]["code"]
        if nusatripResponseCode.startswith('9') == True:
            rc =  Mappingrc.RCMAP_POSTPAID["INVALID_PARAM"]
        resp = dict(
            rc = rc,
            msg = dictResult["response"]["messages"]["message"]["message"],
            sn = '',
            data = dict(
                request = parameters,
                response = dictResult,
                info1 = dict(
                    customer_no = '',
                    customer_name = '',
                    blth = '',
                    ref_no = 0,
                    bill = 0,
                    penalty = 0,
                    admin = 0,
                    total_payment = 0
                ),
                info2 = dict()
            )
        )
        return resp
    # resp = dict(
    # rc=rc_biller,
    # msg=msg_biller,
    # sn=sn,
    # data=dict(request=payload, response=r, info1=info1, info2=info2, param=param)
    # )
