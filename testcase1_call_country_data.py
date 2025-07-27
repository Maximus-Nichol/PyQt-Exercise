import unittest
from country_picker import call_country_data  # adjust import as needed

class TestCountryCall(unittest.TestCase):
    def test_call_country_data(self):
        sample_data = [
            {
                "name": "Ukraine",
                "flags": {"png": "https://flagcdn.com/w320/ua.png"}
            },
            {
                "name": "Peru",
                "flags": {"png": "https://flagcdn.com/w320/pe.png"}
            }
        ]
        
        expected_names = ["Peru", "Ukraine"]
        expected_flags = {
            "Ukraine": "https://flagcdn.com/w320/ua.png",
            "Peru": "https://flagcdn.com/w320/pe.png"
        }
        
        names, flags = call_country_data(sample_data)
        self.assertEqual(names, expected_names)
        self.assertEqual(flags, expected_flags)

if __name__ == "__main__":
    unittest.main()
