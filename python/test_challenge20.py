from challenge20 import fix_gift_list


def test_fix_gift_list():
    assert fix_gift_list(
        ["book", "train", "kite", "train"], ["train", "book", "kite", "ball", "kite"]
    ) == {"missing": {"ball": 1, "kite": 1}, "extra": {"train": 1}}


def test_no_missing_or_extra():
    assert fix_gift_list(["book", "train", "kite"], ["book", "train", "kite"]) == {
        "missing": {},
        "extra": {},
    }


def test_all_missing():
    assert fix_gift_list([], ["book", "train", "kite"]) == {
        "missing": {"book": 1, "train": 1, "kite": 1},
        "extra": {},
    }


def test_all_extra():
    assert fix_gift_list(["book", "train", "kite"], []) == {
        "missing": {},
        "extra": {"book": 1, "train": 1, "kite": 1},
    }


def test_with_duplicates():
    assert fix_gift_list(["train", "train", "kite"], ["train", "kite", "kite"]) == {
        "missing": {"kite": 1},
        "extra": {"train": 1},
    }
