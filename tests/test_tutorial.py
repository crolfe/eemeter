from eemeter.examples import get_example_project
from eemeter.meter import DefaultResidentialMeter, DataCollection


def test_tutorial():
    project = get_example_project("94087")
    meter = DefaultResidentialMeter()
    results = meter.evaluate(DataCollection(project=project))

    json_data = results.json()
    assert "consumption" in json_data
    assert "weather_source" in json_data
    assert "gross_savings" in json_data
