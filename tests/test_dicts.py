import pytest

from utils.dicts import get_val

DICT = {"vcs": "mercurial"}
@pytest.mark.parametrize('collection, key, default, expected',
[
    (DICT, "vcs", None, "mercurial"),
    ({}, "vcs", None, "git"),
    ({}, "vcs", "boo", "boo"),

])
def test_get_val(collection, key, default, expected):
    if default:
        assert get_val(collection, key, default) == expected
    else:
        assert get_val(collection, key) == expected
