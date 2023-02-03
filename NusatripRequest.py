from pydantic import create_model, Field

# Fligh Search Parameters
flightSearchParamDict = {
    "token": (str, ...),
    "version":(str, ...), 
    "adultNum":(int, ...), 
    "departure":(str, ...),
    "arrival":(str, ...),
    "departDate":(str, ...),
    "partial":(int, ...),
    "sl": (int, Field(..., alias='__sl')),
    "format":(str, ...),
    "childNum":(int, None),
    "infantNum":(int, None),
    "returnDate":(str, None),
    "t":(int, None),
    "cabinType":(str, None),
    "currency":(str, None),
    "lang":(str, None),
    "entityId":(str, None),
    "customerId":(str, None),
    "showTaxAndFees":(str, None)
}

FlightSearchParam = create_model("Query", **flightSearchParamDict)
