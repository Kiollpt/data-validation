from pprint import pprint
from frictionless import describe,describe_schema,describe_resource
from frictionless import Resource,Schema,Layout
from frictionless import extract_resource
from frictionless import validate_resource,validate_schema

# define schema
custom_schema = {'fields': [{'name': 'ad_network', 'type': 'string'},
            {'name': 'date', 'type': 'date'},
            {'name': 'app_name', 'type': 'string'},
            {'name': 'unit_id', 'type': 'integer'},
            {'name': 'request', 'type': 'number'},
            {'name': 'revenue', 'type': 'number'},
            {'name': 'imp', 'type': 'number'}
        ]}


def redefine_report(report):
    schema = Schema(custom_schema)
    result = []
    for field_pos, code in report:
        col = schema.field_names[field_pos-1]
        col_type = schema.get_field(col)["type"]
        wording = (col, code, col_type)
        result.append(wording)
    return result


def validation(msg: dict, spec=["fieldPosition","code"]):
    res = Resource(data=msg, schema=custom_schema)
    report = validate_resource(res, skip_errors=["#header"],spec=spec)
    result = redefine_report(report.flatten(spec=spec))
    pprint(result)

def main():
    d = [{
    "ad_network":"FOO",
    "date":"2019-06-05",
    "app_name":"LINETV",
    "unit_id":"55665201314",
    "request":"100",
    "revenue":"0.00365325",
    "imp":10
    }]

    validation(msg=d)
main()