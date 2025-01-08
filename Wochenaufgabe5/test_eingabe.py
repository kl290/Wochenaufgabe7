import unittest
from unittest.mock import patch

from eingabe import eingabe_zahl


class TestEingabeZahl(unittest.TestCase):

    @patch('builtins.input', return_value='5')
    def test_gueltige_eingabe(self, mock_input):
        result = eingabe_zahl("Gib eine Zahl ein: ")
        self.assertEqual(result, 5.0)

    @patch('builtins.input', side_effect=['abc', '3.14'])
    def test_ungueltige_eingabe(self, mock_input):
        result = eingabe_zahl("Gib eine Zahl ein: ")
        self.assertEqual(result, 3.14)


if __name__ == '__main__':
    unittest.main()
