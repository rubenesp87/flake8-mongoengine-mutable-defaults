import ast
import pytest

from flake8_mutable_defaults import MutableDefaultChecker


@pytest.mark.parametrize(
    "code,error_count",
    [
        ("def foo(default=a()): bar(default=abc)", 0),
        ("def foo(): bar(default={})", 0),
        ("def foo(): bar(default=abc())", 1),
        ("def foo(): bar(abc())", 0),
    ],
    ids=("default var", "default dict", "default func", "default func without pos"),
)
def test_mutable_defaults(code, error_count):
    tree = ast.parse(code)
    assert len(list(MutableDefaultChecker(tree, "filename").run())) == error_count
