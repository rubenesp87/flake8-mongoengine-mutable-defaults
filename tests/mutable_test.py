import ast
import pytest

from mongoengine_mutable_defaults import MongoEngineDefaultChecker


@pytest.mark.parametrize(
    "code,error_count",
    [
        ("def foo(default=a()): bar(default=abc)", 0),
        ("def foo(): bar(default={})", 0),
        ("def foo(): bar(default=abc())", 1),
        ("def foo(): bar(abc())", 0),
        ("def foo(): bar(document_type=cde, default=abc())", 1),
    ],
    ids=(
        "default var",
        "default dict",
        "default func",
        "default func without pos",
        "default and document_type func",
    ),
)
def test_mutable_defaults(code, error_count):
    tree = ast.parse(code)
    assert len(list(MongoEngineDefaultChecker(tree, "filename").run())) == error_count
