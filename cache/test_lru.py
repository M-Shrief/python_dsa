from .lru import LRU
from ..utils import errors

class TestLRU:

    def test_put(self):
        lru = LRU[int](3)

        lru.put('one', 1)
        lru.put('two', 2)
        lru.put('three', 3)

        assert lru.get_size() == 3, errors.wrong_value(lru.get_size(), 3)

        assert lru.get("one") == 1, errors.wrong_value(lru.get("one"), 1)
        assert lru.get("two") == 2, errors.wrong_value(lru.get("two"), 2)
        assert lru.get("three") == 3, errors.wrong_value(lru.get("three"), 3)

        lru.put("four", 4)
        assert lru.get_top().val == 4, errors.wrong_value(lru.get_top().val, 4)
        assert lru.get("one") is None, "Should be None"

        lru.put("five", 5)
        assert lru.get_top().val == 5, errors.wrong_value(lru.get_top().val, 5)
        assert lru.get("two") is None, "Should be None"

    def test_get(self):
        lru = LRU[int](3)

        lru.put('one', 1)
        lru.put('two', 2)
        lru.put('three', 3)

        assert lru.get("one") == 1, errors.wrong_value(lru.get("one"), 1)
        assert lru.get_top().val == 1, errors.wrong_value(lru.get_top().val, 1)

        assert lru.get("two") == 2, errors.wrong_value(lru.get("two"), 2)
        assert lru.get_top().val == 2, errors.wrong_value(lru.get_top().val, 2)

        assert lru.get("three") == 3, errors.wrong_value(lru.get("three"), 3)
        assert lru.get_top().val == 3, errors.wrong_value(lru.get_top().val, 3)

        lru.put("four", 4)
        assert lru.get("four") == 4, errors.wrong_value(lru.get("four"), 4)
        assert lru.get_top().val == 4, errors.wrong_value(lru.get_top().val, 4)
        assert lru.get("one") is None, "Should be None"

        lru.put("five", 5)
        assert lru.get("five") == 5, errors.wrong_value(lru.get("five"), 5)
        assert lru.get_top().val == 5, errors.wrong_value(lru.get_top().val, 5)
        assert lru.get("two") is None, "Should be None"
        