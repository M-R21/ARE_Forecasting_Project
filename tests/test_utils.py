import unittest
from src.utils.config import load_config

class TestConfig(unittest.TestCase):
    def test_load_config(self):
        config = load_config('config.yaml')
        self.assertIn('data', config)

if __name__ == '__main__':
    unittest.main()
