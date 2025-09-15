"""auto_import module test"""

from auto_import import auto_import


def test_auto_import_with_real_routers():
    """test auto_import with real routers"""

    modules = auto_import("tests/test_dir")

    assert len(modules) == 2

    modules = auto_import("tests/wrong")
    assert len(modules) == 0
