from .hashmap import Hashmap
from ..utils import errors

class TestHashmap:

    def test_put_and_get(self):
        hm = Hashmap[int](3)
        assert hm.put("one", 1) is True
        assert hm.put("two", 2) is True
        assert hm.put("three", 3) is True

        one = hm.get("one")
        two = hm.get("two")
        three = hm.get("three")

        assert one == 1, errors.wrong_value(one, 1)
        assert two == 2, errors.wrong_value(two, 2)
        assert three == 3, errors.wrong_value(three, 3)

        assert hm.get_size() == 3, "Size should be 3"

        assert hm.put("four", 4) is False

    # Need to test private functions, but without exposing them.