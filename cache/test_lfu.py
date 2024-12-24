from .lfu import LFU
from ..utils import errors


class TestLFU:
    def test_put(self):
        lfu = LFU[int](3)

        lfu.put("one", 1)
        lfu.put("two", 2)
        lfu.put("three", 3)

        assert lfu.get("one") == 1, errors.wrong_value(lfu.get("one") , 1)
        assert lfu.get("two") == 2, errors.wrong_value(lfu.get("two") , 2)

        assert lfu.get_top() == 3, errors.wrong_value(lfu.get_top(), 3)

        lfu.put("four", 4)
        assert lfu.get("four") == 4, errors.wrong_value(lfu.get("four"), 4)

        assert lfu.get("three") is None, "Should've been evicted"

        lfu.get('one')
        lfu.get('one')
        lfu.get('two')
        lfu.get('four')
        lfu.get('four')
        # Freqs -> one.freq = 3, two.freq = 2, four.freq = 3;

        lfu.put('five', 5)
        assert lfu.get("five") == 5, errors.wrong_value(lfu.get("five"), 5)
        assert lfu.get("two") is None, "Should've been evicted"

    def test_get(self):
        lfu = LFU[int](3)

        lfu.put("one", 1)
        lfu.put("two", 2)
        lfu.put("three", 3)

        assert lfu.get("one") == 1, errors.wrong_value(lfu.get("one"), 1)
        assert lfu.get("two") == 2, errors.wrong_value(lfu.get("two"), 2)

        assert lfu.get_top() == 3, errors.wrong_value(lfu.get_top(), 3)

        lfu.put('four', 4)
        assert lfu.get('four') == 4, errors.wrong_value(lfu.get('four'), 4)

        assert lfu.get('three') is None, "Should've been evicted"

        lfu.get('one')
        lfu.get('one')
        lfu.get('two')
        lfu.get('four')
        lfu.get('four')
        # Freqs -> one.freq = 3, two.freq = 2, four.freq = 3;

        lfu.put('five', 5)
        assert lfu.get("five") == 5, errors.wrong_value(lfu.get("five"), 5)
        assert lfu.get("two") is None, "Should've been evicted"