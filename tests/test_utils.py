import unittest
import json
import os
import tempfile
from pathlib import Path
import sys

# Add src to path
sys.path.insert(0, str(Path(__file__).parent.parent / 'src'))

import utils


class TestUtils(unittest.TestCase):

    def test_save_and_load_json(self):
        """Test saving and loading JSON data"""
        test_data = {"key": "value", "number": 42}

        with tempfile.NamedTemporaryFile(mode='w', suffix='.json', delete=False) as f:
            temp_path = f.name

        try:
            # Test save
            utils.save_to_json(test_data, temp_path)

            # Test load
            loaded_data = utils.load_from_json(temp_path)
            self.assertEqual(loaded_data, test_data)
        finally:
            os.unlink(temp_path)

    def test_separate_city_country(self):
        """Test separating city and country from location string"""
        # Test normal case
        city, country = utils.separate_city_country("London, England, United Kingdom")
        self.assertEqual(city, "London")
        self.assertEqual(country, "United Kingdom")

        # Test single part
        city, country = utils.separate_city_country("London")
        self.assertEqual(city, "London")
        self.assertIsNone(country)

        # Test empty string
        city, country = utils.separate_city_country("")
        self.assertEqual(city, "")
        self.assertIsNone(country)

    def test_clean_descriptions(self):
        """Test cleaning job descriptions"""
        descriptions = [
            "Great job opportunity\n\n• Benefit 1\n• Benefit 2",
            "   Spaced text   ",
            "",
            "Normal description"
        ]

        cleaned = utils.clean_descriptions(descriptions)

        # Should remove duplicates and clean formatting
        self.assertIsInstance(cleaned, list)
        self.assertGreater(len(cleaned), 0)


if __name__ == '__main__':
    unittest.main()