import unittest
from unittest.mock import patch

from zahl_eingabe import eingabe_zahl


class TestEingabeZahl(unittest.TestCase):

    @patch('builtins.input', side_effect=['5.0'])
    def test_float_to_int(self, mock_input):
        result = eingabe_zahl("Geben sie eine Zahl ein: ")
        self.assertEqual(result, 5)

    @patch('builtins.input' , side_effect=['3.5'])
    def test_float(self, mock_input):
        result = eingabe_zahl("Geben Sie eine zahl ein: ")
        self.assertEqual(result, 3.5)

    @patch('builtins.input', side_effect=['-2'])
    def test_int(self, mock_input):
        result = eingabe_zahl("Geben Sie eine Zahl ein: ")
        self.assertEqual(result, -2)

    @patch('builtins.input', side_effect=['100'])
    def test_mit_min_value(self, mock_input):
        result = eingabe_zahl("Geben Sie eine Zahl ein: ", min_val=50)
        self.assertEqual(result, 100)

    @patch('builtins.input', side_effect=['20'])
    def test_mit_min_value_error(self, mock_input):
        result = eingabe_zahl("Geben Sie eine Zahl ein: ", min_val=10)
        self.assertEqual(result, 20)

    @patch('builtins.input', side_effect=['200'])
    def test_mit_max_value(self, mock_input):
        result = eingabe_zahl("Geben Sie eine Zahl ein: ", max_val=250)
        self.assertEqual(result, 200)

    @patch('builtins.input', side_effect=['50'])
    def test_mit_max_value_error(self, mock_input):
        result = eingabe_zahl("Geben Sie eine zahl ein: ", max_val=100)
        self.assertEqual(result, 50)


if __name__ == '__main__':
    unittest.main()
