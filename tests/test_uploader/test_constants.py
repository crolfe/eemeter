from eemeter.uploader import constants
from unittest import TestCase


class ConstantsTestCase(TestCase):

    def test_STANDARD_PROJECT_ATTRIBUTE_KEYS(self):
        for data in constants.STANDARD_PROJECT_ATTRIBUTE_KEYS.values():
            assert "name" in data
            assert "display_name" in data
            assert data["data_type"] in ["FLOAT", "INTEGER", "DATE",
                                         "DATETIME", "BOOLEAN", "CHAR"]

    def test_STANDARD_PROJECT_DATA_COLUMN_NAMES(self):
        assert len(constants.STANDARD_PROJECT_DATA_COLUMN_NAMES) == 9
