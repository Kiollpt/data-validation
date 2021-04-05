from pprint import pprint
from frictionless import Resource, Schema
from frictionless import validate_resource
from typing import List


def redefine_report(report: List[tuple], 
                    custom_schema: dict) -> List[tuple]:
    schema = Schema(custom_schema)
    result = []
    for field_pos, code in report:
        col = schema.field_names[field_pos - 1]
        col_type = schema.get_field(col)["type"]
        wording = (col, code, col_type)
        result.append(wording)
    return result


def validation(msg: List[dict], custom_schema: dict,
               spec=["fieldPosition", "code"]) -> List[tuple]:

    res = Resource(data=msg, schema=custom_schema)
    report = validate_resource(res, skip_errors=["#header"], spec=spec)
    #print(report.flatten(spec=spec))
    result = redefine_report(report.flatten(spec=spec), custom_schema)
    #pprint(result)
    return result


def missing_keys(msg: List[dict], custom_schema: dict) -> bool:
    keys = Schema(custom_schema).field_names
    if all(col in keys for col in msg[0]):
        return False
    else:
        return True


def main():
    d = [{
        "ad_network": "FOO",
        "date": "2019-06-05",
        "app_name": "LINETV",
        "unit_id": "55665201314",
        "request": "100",
        "revenue": "0.00365325",
        "imp": "bb"
    }]

    # define schema
    custom_schema = {'fields': [{'name': 'ad_network', 'type': 'string'},
                                {'name': 'date', 'type': 'date'},
                                {'name': 'app_name', 'type': 'string'},
                                {'name': 'unit_id', 'type': 'integer'},
                                {'name': 'request', 'type': 'number'},
                                {'name': 'revenue', 'type': 'number'},
                                {'name': 'imp', 'type': 'number'}
                                ]}

    result = validation(d, custom_schema)
    pprint(result)
    print(missing_keys(d, custom_schema))


if __name__ == "__main__":
    main()
