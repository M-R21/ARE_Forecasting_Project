import unittest
from src.data.load_data import load_data

class TestDataLoading(unittest.TestCase):
    def test_load_data(self):
        data = load_data('data/raw/ARE_data.tsv')
        self.assertIsNotNone(data)

if __name__ == '__main__':
    unittest.main()
