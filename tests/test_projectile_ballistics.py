import pytest
from gameplay import projectile_ballistics as mod

CASES = [
    ("lag", 'm.lag_compensate((10, 0), (2, 0), 0.5) == approx((9.0, 0.0))'),
    ("pen", 'm.penetration_loss(2, 1, 1) == approx(2.0)'),
    ("substep", 'm.substep_count(20, 0.1, 0.5) == 2'),
    ("drop", 'm.gravity_drop(1, 2) == approx(1.0)'),
    ("layer", 'm.layer_order(2, 1) == (1, 2)'),
    ("spread", 'm.spread_order([3, 1, 2]) == [1, 2, 3]'),
    ("rollback", 'm.rollback_state(100, True) == (100, True)'),
    ("platform", 'm.platform_local_velocity((5, 0), (2, 0)) == (3, 0)'),
    ("hash", 'm.path_hash([(0, 0), (1, 2)]) == "0,0|1,2"'),
    ("id", 'm.bullet_id("p1", 7) == "p1:7"'),
    ("hit", 'm.hit_time(10, 2) == approx(5.0)'),
    ("pierce", 'm.pierce_budget(2, 5) == approx(3.0)'),
    ("cos", 'm.angle_cos(1, 0) == approx(1.0)'),
    ("step", 'm.trajectory_step((0, 0), (2, 4), 1, 2) == approx((2.0, 3.0))'),
    ("dup", 'm.duplicate_guard({1, 2}, 3) is True')
]

@pytest.mark.parametrize("name,expr", CASES, ids=[c[0] for c in CASES])
def test_contract(name, expr):
    assert eval(expr, {"m": mod, "approx": pytest.approx})
