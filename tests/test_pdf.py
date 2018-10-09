import unittest
from unittest.mock import patch
from gsutil.pdf import Pdf


class TestPdf(unittest.TestCase):

    @patch('gsutil.pdf.Pdf.DIR_NAME', './tests')
    def test_extract_text(self):
        pdf = Pdf('test.pdf')
        text = pdf.extract_text()
        self.assertEqual(text, 'This is a pdf file for test.')


if __name__ == "__main__":
    unittest.main()
