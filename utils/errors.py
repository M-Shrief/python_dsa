from typing import Any
def wrong_value(got: Any, want: Any)->str:
    """Returns simple message, showing the value we got and the value we want.
    Note: it may become more verbose and not clear if used while coding, sometimes it's better to write the error string directly."""
    return f"Got: {got}, Want: {want}"