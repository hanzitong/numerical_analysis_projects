
import numpy as np
import pytest
import random
from smart_tether import tensions
from smart_tether import c_bounds


def test_van_der_pol():
    h = random.uniform(1., 50.)
    v = random.uniform(-50., 50.)
    s_margin = random.uniform(0.1, 1.)
    msg = f"h = {h}, v = {v}, s_margin = {s_margin}"

    c_upper = c_bounds.calc_c_upper(h, v, s_margin)
    s_expect = np.sqrt(h * h + v * v) + s_margin
    s_actual = tensions.calc_tether_length(h, v, c_upper)

    assert s_actual == pytest.approx(s_expect, rel=1e-2), msg





