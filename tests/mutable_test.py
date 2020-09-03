import ast
import pathlib
import pytest

from mongoengine_mutable_defaults import MongoEngineDefaultChecker


def test_mutable_defaults():

    filename = pathlib.Path(__file__).absolute().parent / "default.py"
    fileObject = open(str(filename), "r")
    tree = ast.parse(fileObject.read())

    assert len(list(MongoEngineDefaultChecker(tree, str(filename)).run())) == 2
