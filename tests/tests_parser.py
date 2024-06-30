import unittest
from hl7_processing import parse_hl7_message, hl7_to_json

class testhl7parser(unittest.TestCase):

    def test_valid_message(self):
        message = """MSH|^~\&|ADT1|MCM|LABADT|MCM|198808181126|SECURITY|ADT^A01|MSG00001|P|2.3
EVN|A01|198808181123
PID|0001|00001122|1122^Doe^John|L|NML^Norma Leah|MRN^Married|19480203|M||C|101 Main St.^^Ann Arbor^MI^44444|GL|(313)555-1212|(313)555-1212||S||123456789|9-87654^3|
PV1|1|I|2000^2012^01||||004777^MEET^PAUL^J.|||SUR||||ADM|A0|"""
        parsed_message = parse_hl7_message(message)
        self.assertIsNotNone(parsed_message)
        json_output = hl7_to_json(parsed_message)
        self.assertIn("MSH", json_output)

    def test_invalid_message(self):
        message = "INVALID MESSAGE"
        parsed_message = parse_hl7_message(message)
        self.assertIsNone(parsed_message)

if __name__ == '__main__':
    unittest.main()