import unittest
from project import transform

class TestDatetimeTransformation(unittest.TestCase):

    def test_valid_output(self):
        input_dt_str = '2023-03-11 14:30:00'
        out_time = 'EST'
        self.assertEqual(transform(input_dt_str, out_time), '03/11/2023 03:30 PM EST')
    
    def test_invalid_timezone(self):
        input_dt_str = '2023-03-11 14:30:00'
        out_time = 'GST'
        self.assertNotEqual(transform(input_dt_str, out_time), 'EST')
    
    def test_invalid_hours_format(self):
        input_dt_str = '2023-03-11 26:30:00'
        out_time = 'EST'
        self.assertNotEqual(transform(input_dt_str, out_time), "Invalid Hour format")

    def test_invalid_date_format(self):
        input_dt_str = '20231-03-11 26:30:00'
        out_time = 'EST'
        self.assertNotEqual(transform(input_dt_str, out_time), "Invalid Date Format")

    def test_invalid_format_all_zeros(self):
        input_dt_str = '0000-00-00 00:00:00'
        out_time = 'EST'
        self.assertNotEqual(transform(input_dt_str, out_time), "Invalid Date And time Format")


if __name__ == "__main__":
    unittest.main()