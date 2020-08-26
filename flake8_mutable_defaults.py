import ast


__version__ = "1.2.0"


mutable_types = [ast.Call]


class MutableDefaultChecker(object):
    """Mutable default argument checker.
    Flake8 extension that alerts when a mutable type is used
    as an argument's default value.
    """

    name = "flake-mutable-defaults"
    version = __version__
    _error_tmpl = "{} - mutable default arg of type {}"
    _code = "M511"

    def __init__(self, tree, filename):
        self.tree = tree

    def run(self):
        for node in ast.walk(self.tree):

            if isinstance(node, ast.keyword):
                if getattr(node, "arg", None) and node.arg == "default":
                    if any(
                        [
                            isinstance(node.value, mutable_type)
                            for mutable_type in mutable_types
                        ]
                    ):
                        error_msg = self._error_tmpl.format(
                            self._code, ast.Call.__name__
                        )
                        yield (
                            node.arg,
                            node.value.func.id,
                            error_msg,
                            type(self),
                        )
