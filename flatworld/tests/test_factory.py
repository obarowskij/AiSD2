from flatworld.functions.factory import point_in_polygon
import pytest
from flatworld.functions.models import Point

@pytest.mark.parametrize(
    "points, factory, expected",
    [
        (
            [
                Point(0, 3),
                Point(1, 1),
                Point(2, 2),
                Point(4, 4),
                Point(0, 0),
                Point(1, 2),
                Point(3, 1),
                Point(3, 3),
            ],
            Point(-2,-2),
            False,
        ),
        (
            [
                Point(-157, 159),
                Point(-154, 182),
                Point(18, 181),
                Point(168, 66),
                Point(132, -101),
                Point(-8, -152),
                Point(-159, -156),
                Point(-157, 159),
            ],
            Point(-56, -149),
            True,
        ),
    ],
)
def test_graham_scan(points, factory, expected):
    isInPolygon = point_in_polygon(factory, points)
    assert isInPolygon == expected
