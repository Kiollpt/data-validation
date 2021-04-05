import unittest
from src import validation, missing_keys


class TestValidation(unittest.TestCase):

    def test_missing(self):
        data = [{"app_tool": "iphone"}]
        schema = {'fields': [{'name': 'app_name', 'type': 'string'}]}
        self.assertTrue(missing_keys(data, schema))

    def test_str(self):
        data = [{"app_name": 123}]
        schema = {'fields': [{'name': 'app_name', 'type': 'string'}]}
        expected = "type-error"
        result = validation(data, schema)[0]

        self.assertEqual(result[1], expected)

    def test_number(self):
        data = [{"app_number": "WRONG"}]
        schema = {'fields': [{'name': 'app_number', 'type': 'number'}]}
        expected = "type-error"
        result = validation(data, schema)[0]

        self.assertEqual(result[1], expected)

    def test_datetime(self):
        data = [{"app_date": "2021-04"}]
        schema = {'fields': [{'name': 'app_date', 'type': 'date'}]}
        expected = "type-error"
        result = validation(data, schema)[0]

        self.assertEqual(result[1], expected)

    def test_message(self):
        data = [{
            "ad_network": "FOO",
            "date": "2019-06",
            "app_name": "LINETV",
            "unit_id": "55665201314",
            "request": 100,
            "revenue": 0.00365325,
            "imp": "bb"
        }]

        # define schema
        custom_schema = {'fields': [{'name': 'ad_network', 'type': 'string'},
                                    {'name': 'date', 'type': 'date'},
                                    {'name': 'app_name', 'type': 'string'},
                                    {'name': 'unit_id', 'type': 'string'},
                                    {'name': 'request', 'type': 'number'},
                                    {'name': 'revenue', 'type': 'number'},
                                    {'name': 'imp', 'type': 'number'}
                                    ]}

        expected = ["type-error", "type-error"]
        result = validation(data, custom_schema)
        test_type = [r[1] for r in result]
        self.assertEqual(test_type, expected)
