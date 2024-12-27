from .mfu import MFU
from ..utils import errors


class TestMFU:
    def test_put(self):
        mfu = MFU[int](3)

        mfu.put("one", 1)
        mfu.put("two", 2)
        mfu.put("three", 3)

        assert mfu.get("one") == 1, errors.wrong_value(mfu.get("one") , 1)
        assert mfu.get("two") == 2, errors.wrong_value(mfu.get("two") , 2)
        mfu.get("one")
        mfu.get("two")
        mfu.get("two")
        mfu.get("three")

        # Score: one.freq= 2, two.freq= 3, three.freq=1
        assert mfu.get_top() == 2, errors.wrong_value(mfu.get_top(), 2)

        mfu.put("four", 4)
        assert mfu.get("four") == 4, errors.wrong_value(mfu.get("four"), 4)

        assert mfu.get("two") is None, "Should've been evicted"

        mfu.get('one')
        mfu.get('one')
        mfu.get('three')
        mfu.get('four')
        mfu.get('four')
        # Freqs -> one.freq = 4, three.freq = 2, four.freq = 3;

        mfu.put('five', 5)
        assert mfu.get("five") == 5, errors.wrong_value(mfu.get("five"), 5)
        assert mfu.get("one") is None, "Should've been evicted"

    def test_get(self):
        mfu = MFU[int](3)

        mfu.put("one", 1)
        mfu.put("two", 2)
        mfu.put("three", 3)

        assert mfu.get("one") == 1, errors.wrong_value(mfu.get("one") , 1)
        assert mfu.get("two") == 2, errors.wrong_value(mfu.get("two") , 2)
        mfu.get("one")
        mfu.get("two")
        mfu.get("two")
        mfu.get("three")

        # Score: one.freq= 2, two.freq= 3, three.freq=1
        assert mfu.get_top() == 2, errors.wrong_value(mfu.get_top(), 2)

        mfu.put('four', 4)
        assert mfu.get('four') == 4, errors.wrong_value(mfu.get('four'), 4)

        assert mfu.get('two') is None, "Should've been evicted"

        mfu.get('one')
        mfu.get('one')
        mfu.get('three')
        mfu.get('four')
        mfu.get('four')
        # Freqs -> one.freq = 4, three.freq = 2, four.freq = 3;

        mfu.put('five', 5)
        assert mfu.get("five") == 5, errors.wrong_value(mfu.get("five"), 5)
        assert mfu.get("one") is None, "Should've been evicted"

        assert mfu.get('three') == 3, errors.wrong_value(mfu.get('three'), 3)