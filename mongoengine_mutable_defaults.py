import ast


__version__ = "0.0.1"


MUTABLE_TYPE = ast.Call
FUNCTIONS = ["EmbeddedDocumentField"]
ARGUMENTS = ["default"]


class MongoEngineDefaultChecker(object):  # type: ignore
    """ MongoEngine default argument checker.
    Flake8 extension that alerts when a mutable type Call is used
    as an argument's default value.
    """

    name = "flake8-mongoengine-mutable-defaults"
    version = __version__
    _error_tmpl = "{} - mongoengine mutable default arg of type {}"
    _code = "X101"

    def __init__(self, tree, filename):
        self.tree = tree

    def run(self):
        for node in ast.walk(self.tree):
            check_keys = False
            if isinstance(node, MUTABLE_TYPE):
                if isinstance(node.func, ast.Name) and node.func.id in FUNCTIONS:
                    check_keys = True
                elif (
                    isinstance(node.func, ast.Attribute) and node.func.attr in FUNCTIONS
                ):
                    check_keys = True
                else:
                    continue

            if (
                check_keys
                and getattr(node, "keywords", None)
                and len(node.keywords) > 0
            ):
                for key in node.keywords:
                    if isinstance(key.value, MUTABLE_TYPE) and key.arg in ARGUMENTS:
                        error_msg = self._error_tmpl.format(
                            self._code, ast.Call.__name__
                        )
                        yield (
                            node.func.lineno,
                            node.func.col_offset,
                            error_msg,
                            type(self),
                        )
