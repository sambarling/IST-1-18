import unittest
import csv
from main import GeoAPI


class TestGeoAPI(unittest.TestCase):
    def setUp(self):
        self.GeoAPI = GeoAPI()

    def test_GET_1(self):
        self.assertEqual(self.GeoAPI.root("xa0642146", "xa0208288"), "xa0059(+1.78%)")

    def test_GET_2(self):
        self.assertEqual(self.GeoAPI.root("xa0343143", "xa0448283"), "xa0281(+1.90%)")

    def test_GET_3(self):
        self.assertEqual(self.GeoAPI.root("xa0888140", "xa0622278"), "xa0970(+1.45%)")


if __name__ == '__main__':
    unittest.main()
