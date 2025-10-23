#tests/test_smoke.py
import importlib.util
import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

def test_import():
    spec = importlib.util.spec_from_file_location(
        "monte_carlo_blackjack", os.path.join("monte_carlo_blackjack.py")
    )
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)

def test_card_helpers():
    from monte_carlo_blackjack import hand_value
    v, soft = hand_value([1, 9])  # A + 9 = 20 soft
    assert v == 20 and soft is True

    v2, soft2 = hand_value([10, 13])  # 10 + K = 20 hard
    assert v2 == 20 and soft2 is False

