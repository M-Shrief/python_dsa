from .mru import MRU
from ..utils import errors

class TestMRU:

    def test_put(self):
        mru = MRU[int](3)
        mru.put("one", 1)
        mru.put("two", 2)
        mru.put("three", 3)

        assert mru.get_size() == 3, "Size should be 3"
        
        assert mru.get("one") == 1, errors.wrong_value(mru.get("one"), 1)     
        assert mru.get("two") == 2, errors.wrong_value(mru.get("two"), 2)     
        assert mru.get("three") == 3, errors.wrong_value(mru.get("three"), 3)     

        assert mru.get_top().key == "one", errors.wrong_value(mru.get_top().key, "one") # pyright: ignore[reportOptionalMemberAccess]

        mru.put('four', 4)
        assert mru.get("three") is None, "Should be None"
        assert mru.get('four') == 4, errors.wrong_value(mru.get('four'), 4)
    
        mru.put('five', 5)
        assert mru.get("four") is None, "Should be None"
        assert mru.get('five') == 5, errors.wrong_value(mru.get('five'), 5)

        assert mru.get("two") == 2, errors.wrong_value(mru.get("two"), 2)     
        
        assert mru.get("three") is None, "Should be None"
        assert mru.get("four") is None, "Should be None"