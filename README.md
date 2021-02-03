# flake8-mongoengine-mutable-defaults
[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=rubenesp87_flake8-mongoengine-mutable-defaults&metric=alert_status)](https://sonarcloud.io/dashboard?id=rubenesp87_flake8-mongoengine-mutable-defaults)

## Background
Mutable defaults in python are bad:
https://florimond.dev/blog/articles/2018/08/python-mutable-defaults-are-the-source-of-all-evil/

We want to detect the incorrect usage of defaults for Mongo fields, especially the `Embedded` family of fields.  We should only allow constant or callable values to defaults.

But even worse it turns out are mutable default arguments to mongo EmbeddedDocumentField.  We discovered some extremely bad bugs that lead to some models leaking data to each other via default arguments.

### Example
```console
EmbeddedDocumentField(default=foo())

./backend/domains/user/models.py:252:16: X101 - mongoengine mutable default arg of type Call
```