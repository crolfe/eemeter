import pytest

from eemeter.config.yaml_parser import load
from eemeter.meter import DataCollection


def test_sequential_meter():
    meter_yaml = """
        !obj:eemeter.meter.Sequence {
            sequence: [
                !obj:eemeter.meter.DummyMeter {
                    input_mapping: { "value": {}, },
                    output_mapping: { "result": {"name":"value1"}, }, },
                !obj:eemeter.meter.DummyMeter {
                    input_mapping: { "value": { "name": "value1"}, },
                    output_mapping: { "result": {}, },
                },
                !obj:eemeter.meter.DummyMeter {
                    input_mapping: { "value": {}, },
                    output_mapping: { "result": {"name": "result1"}, },
                },
            ]
        }
    """

    meter = load(meter_yaml)
    data_collection = DataCollection(value=10)
    result = meter.evaluate(data_collection)

    assert result.get_data("value") is None
    assert result.get_data("value1").value == 10
    assert result.get_data("result").value == 10
    assert result.get_data("result1").value == 10


def test_conditional_meter():
    meter_yaml = """
        !obj:eemeter.meter.Condition {
            condition: {
                "name": "electricity_present"
            },
            success: !obj:eemeter.meter.DummyMeter {
                input_mapping: {"value": {"name": "success"}},
                output_mapping: {"result": {}},
            },
            failure: !obj:eemeter.meter.DummyMeter {
                input_mapping: {"value": {"name": "failure"}},
                output_mapping: {"result": {}},
            },
        }
        """
    meter = load(meter_yaml)

    data_collection = DataCollection(electricity_present=True,
                                     success="success", failure="failure")
    assert meter.evaluate(data_collection).get_data(
        "result").value == "success"
    data_collection = DataCollection(electricity_present=False,
                                     success="success", failure="failure")
    assert meter.evaluate(data_collection).get_data(
        "result").value == "failure"


def test_conditional_meter_without_params():
    meter_yaml = """
        !obj:eemeter.meter.Condition {
            condition: {
                "name": "electricity_present",
            }
        }
        """
    meter = load(meter_yaml)
    data_collection = DataCollection(electricity_present=True)
    assert meter.evaluate(data_collection).count() == 0
    data_collection = DataCollection(electricity_present=False)
    assert meter.evaluate(data_collection).count() == 0


def test_switch():
    meter_yaml = """
        !obj:eemeter.meter.Switch {
            target: {name: target},
            cases: {
                1: !obj:eemeter.meter.DummyMeter {
                    input_mapping: { value: {name: value_one} },
                    output_mapping: { result: {} },
                },
                2: !obj:eemeter.meter.DummyMeter {
                    input_mapping: { value: {name: value_two} },
                    output_mapping: { result: {} },
                },
                3: !obj:eemeter.meter.DummyMeter {
                    input_mapping: { value: {name: value_three} },
                    output_mapping: { result: {} },
                },
            },
            default: !obj:eemeter.meter.DummyMeter {
                input_mapping: { value: {name: value_default} },
                output_mapping: { result: {} },
            }
        }
    """

    meter = load(meter_yaml)

    data_collection = DataCollection(target=1, value_one=1, value_two=2,
                                     value_three=3, value_default=4)
    result1 = meter.evaluate(data_collection)
    data_collection = DataCollection(target=2, value_one=1, value_two=2,
                                     value_three=3, value_default=4)
    result2 = meter.evaluate(data_collection)
    data_collection = DataCollection(target=3, value_one=1, value_two=2,
                                     value_three=3, value_default=4)
    result3 = meter.evaluate(data_collection)
    data_collection = DataCollection(target=4, value_one=1, value_two=2,
                                     value_three=3, value_default=4)
    result4 = meter.evaluate(data_collection)
    data_collection = DataCollection(value_one=1, value_two=2, value_three=3,
                                     value_default=4)
    result5 = meter.evaluate(data_collection)

    assert 1 == result1.get_data("result").value
    assert 2 == result2.get_data("result").value
    assert 3 == result3.get_data("result").value
    assert 4 == result4.get_data("result").value
    assert result5.get_data("result") is None


def test_for():
    meter_yaml = """
        !obj:eemeter.meter.For {
            variable: {
                name: value,
            },
            iterable: {
                name: iterable,
            },
            meter: !obj:eemeter.meter.DummyMeter {
                input_mapping: { value: {} },
                output_mapping: { result: {} },
            }
        }
    """
    meter = load(meter_yaml)
    iterable = [
        {
            "value": 1, "tags": ["one"]
        }, {
            "value": 2, "tags": ["two"]
        }]
    data_collection = DataCollection(iterable=iterable)
    result = meter.evaluate(data_collection)

    assert 1 == result.get_data("result", tags=["one"]).value
    assert 2 == result.get_data("result", tags=["two"]).value


def test_tag_filter():
    meter_yaml = """
        !obj:eemeter.meter.TagFilter {
            meter: !obj:eemeter.meter.DummyMeter {
                input_mapping: { value: {} },
                output_mapping: { result: {} },
            }
        }
    """

    meter = load(meter_yaml)
    data_collection = DataCollection()

    with pytest.raises(NotImplementedError):
        meter.evaluate(data_collection)


def test_fuel_type_tag_filter():
    meter_yaml = """
        !obj:eemeter.meter.FuelTypeTagFilter {
            fuel_type_search_name: active_fuel_type,
            input_mapping: {
                active_fuel_type: {},
            },
            meter: !obj:eemeter.meter.Sequence {
                sequence: [
                    !obj:eemeter.meter.DummyMeter {
                        input_mapping: {
                            value: { name: active_fuel_type }
                        },
                        output_mapping: { result: { name: result1 } },
                    },
                    !obj:eemeter.meter.DummyMeter {
                        input_mapping: {
                            value: {}
                        },
                        output_mapping: { result: { name: result2 } },
                    }
                ]
            }
        }
    """

    meter = load(meter_yaml)
    data_collection = DataCollection(active_fuel_type="electricity")
    data_collection_include = DataCollection(value="value_include")
    data_collection_exclude = DataCollection(value="value_exclude")
    data_collection.add_data_collection(
        data_collection_include,
        tagspace=["electricity"])
    data_collection.add_data_collection(
        data_collection_exclude,
        tagspace=["natural_gas"])

    output_data_collection = meter.evaluate(data_collection)
    assert output_data_collection.get_data("result1").value == "electricity"
    assert output_data_collection.get_data("result2").value == "value_include"
