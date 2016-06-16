import os
import tempfile

from datetime import datetime

import pytest
import pytz
import six

from numpy.testing import assert_allclose

from eemeter.parsers import ESPIUsageParser


@pytest.fixture
def natural_gas_xml(fixture_file, request):
    return fixture_file('natural_gas.xml')


@pytest.fixture
def electricity_xml(fixture_file):
    return fixture_file('electricity.xml')


@pytest.fixture
def electricity_xml_2(fixture_file):
    return fixture_file('electricity2.xml')


@pytest.fixture
def natural_gas_parser(natural_gas_xml):
    return ESPIUsageParser(natural_gas_xml)


@pytest.fixture
def electricity_parser(electricity_xml):
    return ESPIUsageParser(electricity_xml)


@pytest.fixture
def electricity_parser_2(electricity_xml_2):
    return ESPIUsageParser(electricity_xml_2)


def test_init(natural_gas_xml):
    fd, filepath = tempfile.mkstemp()
    os.write(fd, six.b(natural_gas_xml))
    os.close(fd)

    # read from file-like object
    with open(filepath, 'r') as f:
        natural_gas_parser = ESPIUsageParser(f)
        timezone = natural_gas_parser.get_timezone()

    # TODO: add assertions
    # read from filepath
    natural_gas_parser = ESPIUsageParser(filepath)
    natural_gas_parser.get_timezone()


def test_local_time_parameters(natural_gas_parser):
    timezone = natural_gas_parser.get_timezone()
    assert timezone.zone == "US/Pacific"


def test_get_usage_point_entry_element(natural_gas_parser):
    element = natural_gas_parser.get_usage_point_entry_element()
    assert element.tag == "{http://www.w3.org/2005/Atom}entry"


def test_get_meter_reading_entry_element(natural_gas_parser):
    element = natural_gas_parser.get_meter_reading_entry_element()
    assert element.tag == "{http://www.w3.org/2005/Atom}entry"


def test_get_usage_summary_entry_elements(natural_gas_parser):
    entry_elements = natural_gas_parser.get_usage_summary_entry_elements()
    assert len(entry_elements) == 0


def test_get_reading_type_interval_block_groups(electricity_parser):
    parser = electricity_parser
    data = [ib for ib in parser.get_reading_type_interval_block_groups()]
    assert len(data) == 2  # ignores second two
    assert data[0]['reading_type']['uom'] == 'Wh'
    assert data[0]['reading_type']['interval_length'].total_seconds() == 3600
    assert data[0]['reading_type']['default_quality'] == 'validated'
    assert data[0]['reading_type']['power_of_ten_multiplier'] == -3
    assert data[0]['reading_type'][
        'commodity'] == 'electricity SecondaryMetered'
    assert data[0]['reading_type']['data_qualifier'] == 'normal'
    assert data[0]['reading_type']['time_attribute'] == 'none'
    assert data[0]['reading_type']['flow_direction'] == 'forward'
    assert data[1]['reading_type']['flow_direction'] == 'reverse'
    assert data[0]['reading_type']['measuring_period'] == 'sixtyMinute'
    assert data[0]['reading_type']['kind'] == 'energy'
    assert data[0]['reading_type']['accumulation_behavior'] == 'deltaData'
    assert len(data[0]['interval_blocks']) == 2
    interval_block_data = data[0]['interval_blocks'][0]
    assert interval_block_data["interval"]["duration"].total_seconds() == 86400
    assert interval_block_data["interval"]["start"].tzinfo.zone == "UTC"

    interval_reading_data = interval_block_data["interval_readings"][0]
    assert interval_reading_data["duration"].total_seconds() == 3600
    assert interval_reading_data["reading_quality"] == 'revenue-quality'
    assert interval_reading_data["value"] == 437400
    assert interval_reading_data["start"].tzinfo.zone == "UTC"


def test_get_consumption_records(natural_gas_parser):
    records = [r for r in natural_gas_parser.get_consumption_records()]
    assert len(records) == 2
    record = records[0]

    assert record['unit_name'] == 'therm'
    assert record['end'].tzinfo.zone == 'UTC'
    assert record['start'].tzinfo.zone == 'UTC'
    assert record['fuel_type'] == 'natural_gas'
    assert_allclose(record['value'], 1.0365954, rtol=1e-3, atol=1e-3)
    assert not record['estimated']


def test_get_consumption_data_objects_natural_gas(natural_gas_parser):
    cds = [cd for cd in natural_gas_parser.get_consumption_data_objects()]
    assert len(cds) == 1
    cd = cds[0]
    assert_allclose(cd.data[0], 1.0365954, rtol=1e-3, atol=1e-3)
    assert_allclose(cd.estimated[0], False, rtol=1e-3, atol=1e-3)
    assert cd.fuel_type == "natural_gas"
    assert cd.unit_name == "therm"


def test_get_consumption_data_objects_electricity(electricity_parser):
    cds = [cd for cd in electricity_parser.get_consumption_data_objects()]
    assert len(cds) == 1
    cd = cds[0]
    assert_allclose(cd.data[0], 0.4142, rtol=1e-3, atol=1e-5)
    assert_allclose(cd.estimated[0], False, rtol=1e-3, atol=1e-3)
    assert cd.data.index[0].to_datetime() == datetime(
        2015, 11, 1, 9, 0, 0, tzinfo=pytz.UTC)
    assert cd.data.index[24].to_datetime() == datetime(
        2016, 3, 21, 7, 0, 0, tzinfo=pytz.UTC)
    assert cd.fuel_type == "electricity"
    assert cd.unit_name == "kWh"


def test_get_consumption_data_objects_electricity_2(electricity_parser_2):
    cds = [cd for cd in electricity_parser_2.get_consumption_data_objects()]
    assert len(cds) == 1
    cd = cds[0]
    assert_allclose(cd.data[0], 0.214, rtol=1e-3, atol=1e-3)
    assert_allclose(cd.estimated[0], False, rtol=1e-3, atol=1e-3)
    assert cd.fuel_type == "electricity"
    assert cd.unit_name == "kWh"


def test_has_solar(electricity_parser, electricity_parser_2):
    assert electricity_parser.has_solar()
    assert not electricity_parser_2.has_solar()
