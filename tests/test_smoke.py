# tests/test_smoke.py
import importlib

def test_import():
    # can the script be imported as a module?
    spec = importlib.util.spec_from_file_location("mc_bj", "monte_carlo_blackjack.py")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)

def test_card_helpers():
    # very quick sanity checks
    from monte_carlo_blackjack import hand_value
    v, soft = hand_value([1, 9])  # A + 9 = 20 soft
    assert v == 20 and soft is True

    v2, soft2 = hand_value([10, 13])  # 10 + K = 20 hard
    assert v2 == 20 and soft2 is False

