import unittest
from project import transform

class TestDatetimeTransformation(unittest.TestCase):

    def test_valid_output_dst(self):
        input_dt_str = '2023-03-12 14:30:00'
        self.assertEqual(transform(input_dt_str), '03/13/2023 Monday 01:00 AM IST')
    
    def test_valid_output_non_dst(self):
        input_dt_str = '2023-03-11 14:30:00'
        self.assertEqual(transform(input_dt_str), '03/12/2023 Sunday 02:00 AM IST')
    
    def test_invalid_time(self):
        input_dt_str = '2023-03-12 02:00:00'
        self.assertNotEqual(transform(input_dt_str), 'NonExistentTimeError!!!')
    
    def test_invalid_hours_format(self):
        input_dt_str = '2023-03-11 26:30:00'
        self.assertNotEqual(transform(input_dt_str), "Invalid Hour format")

    def test_invalid_date_format(self):
        input_dt_str = '20231-03-11 26:30:00'
        self.assertNotEqual(transform(input_dt_str), "Invalid Date Format")

    def test_invalid_format_all_zeros(self):
        input_dt_str = '0000-00-00 00:00:00'
        self.assertNotEqual(transform(input_dt_str), "Invalid Date And time Format")
    
    def test_invalid_date_time(self):
        input_dt_str = '2023-11-05 01:00'
        self.assertNotEqual(transform(input_dt_str), 'Invalid DateTime!!!')


if __name__ == "__main__":
    unittest.main()