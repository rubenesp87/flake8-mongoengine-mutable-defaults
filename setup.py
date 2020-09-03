import setuptools

setuptools.setup(
    name="flake8-mongoengine-mutable-defaults",
    license="MIT",
    version="0.0.1",
    description="MongoEngine mutable default argument checker",
    author="Olema",
    author_email="ruben@telemaco.es",
    url="https://github.com/rubenesp87/flake8-mutable-defaults",
    py_modules=["mongoengine_mutable_defaults"],
    install_requires=["flake8"],
    entry_points={
        "flake8.extension": [
            "PCK0 = mongoengine_mutable_defaults:MongoEngineDefaultChecker"
        ]
    },
    classifiers=["Topic :: Software Development :: Quality Assurance"],
)
