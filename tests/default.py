def foo(default=None):
    pass


def bar(default=None):
    pass


def EmbeddedDocumentField(default=None):
    pass


EmbeddedDocumentField(default=foo())

EmbeddedDocumentField(default=foo)

EmbeddedDocumentField(default=123)

EmbeddedDocumentField(default={})

EmbeddedDocumentField()

foo(default=bar())

foo(default=EmbeddedDocumentField(default=bar()))
