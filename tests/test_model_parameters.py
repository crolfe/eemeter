import numpy as np
import pytest

from eemeter.models.parameters import ParameterType


def _values_error(values, spec):
    return ("Values provided ({}) do not match parameter specification:"
            " {}").format(values, spec)


def test_parameter_type():
    class TestParameters(ParameterType):
        parameters = ["param1", "param2"]

    def check_vals(tp):
        assert tp.to_list() == [0, 1]
        assert all(tp.to_array() == np.array([0, 1]))
        assert tp.to_dict()["param1"] == 0
        assert tp.to_dict()["param2"] == 1
        assert len(tp.to_dict()) == 2
        assert len(tp.json()) == 2

    check_vals(TestParameters([0, 1]))

    check_vals(TestParameters(np.array([0, 1])))

    check_vals(TestParameters({"param1": 0, "param2": 1}))

    # too few params
    with pytest.raises(TypeError) as e:
        TestParameters([])
    assert e.value.args[0] == _values_error([], ["param1", "param2"])

    # too many params
    with pytest.raises(TypeError) as e:
        TestParameters([0, 0, 0])
    assert e.value.args[0] == _values_error([0, 0, 0], ["param1", "param2"])

    # too few params
    with pytest.raises(TypeError) as e:
        TestParameters({})
    assert e.value.args[0] == _values_error({}, ["param1", "param2"])

    # wrong params
    with pytest.raises(KeyError) as e:
        TestParameters({"wrong1": 0, "wrong2": 0})
    assert e.value.args[0] == "param1"

    # wrong type
    with pytest.raises(TypeError) as e:
        TestParameters(0)

    msg = ("Should initialize with either a list or dictionary of"
           " parameter values, but got values=0 instead")
    print(e.value.args[0])
    assert e.value.args[0] == msg
