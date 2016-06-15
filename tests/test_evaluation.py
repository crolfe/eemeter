from datetime import datetime, timedelta

from eemeter.evaluation import Period


def test_period_both_closed():
    p = Period(datetime(2014, 1, 1), datetime(2014, 1, 2))
    assert p.start == datetime(2014, 1, 1)
    assert p.end == datetime(2014, 1, 2)
    assert p.timedelta == timedelta(days=1)
    assert p.closed

    assert datetime(2013, 1, 1) not in p
    assert datetime(2014, 1, 1) in p
    assert datetime(2014, 1, 1, 12) in p
    assert datetime(2014, 1, 2) in p
    assert datetime(2015, 1, 1) not in p

    assert Period(datetime(2013, 1, 1), datetime(2013, 1, 2)) not in p
    assert Period(datetime(2013, 1, 1), datetime(2014, 1, 1)) not in p
    assert Period(datetime(2013, 1, 1), datetime(2014, 1, 1, 12)) not in p
    assert Period(datetime(2013, 1, 1), datetime(2014, 1, 2)) not in p
    assert Period(datetime(2013, 1, 1), datetime(2014, 1, 3)) not in p

    assert Period(datetime(2014, 1, 1), datetime(2014, 1, 1, 12)) in p
    assert Period(datetime(2014, 1, 1), datetime(2014, 1, 2)) in p
    assert Period(datetime(2014, 1, 1), datetime(2014, 1, 3)) not in p

    assert Period(datetime(2014, 1, 1, 12), datetime(2014, 1, 1, 13)) in p
    assert Period(datetime(2014, 1, 1, 12), datetime(2014, 1, 2)) in p
    assert Period(datetime(2014, 1, 1, 12), datetime(2014, 1, 3)) not in p

    assert Period(datetime(2014, 1, 2), datetime(2014, 1, 3)) not in p

    assert Period(datetime(2014, 1, 3), datetime(2014, 1, 4)) not in p


def test_period_start_closed():
    p = Period(start=datetime(2014, 1, 1))
    assert p.start == datetime(2014, 1, 1)
    assert p.end is None
    assert p.timedelta is None
    assert not p.closed

    assert datetime(2013, 1, 1) not in p
    assert datetime(2014, 1, 1) in p
    assert datetime(2014, 1, 1, 12) in p
    assert datetime(2014, 1, 2) in p
    assert datetime(2015, 1, 1) in p

    assert Period(datetime(2013, 1, 1), datetime(2013, 1, 2)) not in p
    assert Period(datetime(2013, 1, 1), datetime(2014, 1, 1)) not in p
    assert Period(datetime(2013, 1, 1), datetime(2014, 1, 1, 12)) not in p
    assert Period(datetime(2013, 1, 1), datetime(2014, 1, 2)) not in p
    assert Period(datetime(2013, 1, 1), datetime(2014, 1, 3)) not in p

    assert Period(datetime(2014, 1, 1), datetime(2014, 1, 1, 12)) in p
    assert Period(datetime(2014, 1, 1), datetime(2014, 1, 2)) in p
    assert Period(datetime(2014, 1, 1), datetime(2014, 1, 3)) in p

    assert Period(datetime(2014, 1, 1, 12), datetime(2014, 1, 1, 13)) in p
    assert Period(datetime(2014, 1, 1, 12), datetime(2014, 1, 2)) in p
    assert Period(datetime(2014, 1, 1, 12), datetime(2014, 1, 3)) in p

    assert Period(datetime(2014, 1, 2), datetime(2014, 1, 3)) in p

    assert Period(datetime(2014, 1, 3), datetime(2014, 1, 4)) in p


def test_period_end_closed():
    p = Period(end=datetime(2014, 1, 2))
    assert p.start is None
    assert p.end == datetime(2014, 1, 2)
    assert p.timedelta is None
    assert not p.closed

    assert datetime(2013, 1, 1) in p
    assert datetime(2014, 1, 1) in p
    assert datetime(2014, 1, 1, 12) in p
    assert datetime(2014, 1, 2) in p
    assert datetime(2015, 1, 1) not in p

    assert Period(datetime(2013, 1, 1), datetime(2013, 1, 2)) in p
    assert Period(datetime(2013, 1, 1), datetime(2014, 1, 1)) in p
    assert Period(datetime(2013, 1, 1), datetime(2014, 1, 1, 12)) in p
    assert Period(datetime(2013, 1, 1), datetime(2014, 1, 2)) in p
    assert Period(datetime(2013, 1, 1), datetime(2014, 1, 3)) not in p

    assert Period(datetime(2014, 1, 1), datetime(2014, 1, 1, 12)) in p
    assert Period(datetime(2014, 1, 1), datetime(2014, 1, 2)) in p
    assert Period(datetime(2014, 1, 1), datetime(2014, 1, 3)) not in p

    assert Period(datetime(2014, 1, 1, 12), datetime(2014, 1, 1, 13)) in p
    assert Period(datetime(2014, 1, 1, 12), datetime(2014, 1, 2)) in p
    assert Period(datetime(2014, 1, 1, 12), datetime(2014, 1, 3)) not in p

    assert Period(datetime(2014, 1, 2), datetime(2014, 1, 3)) not in p

    assert Period(datetime(2014, 1, 3), datetime(2014, 1, 4)) not in p


def test_period_both_open():
    p = Period()
    assert p.start is None
    assert p.end is None
    assert p.timedelta is None
    assert not p.closed
    assert datetime(2013, 1, 1) in p
    assert datetime(2014, 1, 1) in p
    assert datetime(2014, 1, 1, 12) in p
    assert datetime(2014, 1, 2) in p
    assert datetime(2015, 1, 1) in p
    assert p in p

    assert Period(datetime(2014, 1, 1), datetime(2014, 1, 2)) in p


def test_period_name():
    p = Period(name="baseline")
    assert p.name == "baseline"
