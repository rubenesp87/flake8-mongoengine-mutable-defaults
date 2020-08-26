import setuptools

setuptools.setup(
    name="flake8-mutable-defaults",
    license="MIT",
    version="0.0.1",
    description="Mutable default argument checker",
    author="Olema",
    author_email="ruben@telemaco.es",
    url="https://github.com/rubenesp87/flake8-mutable-defaults",
    py_modules=["flake8_mutable_defaults"],
    install_requires=["flake8"],
    entry_points={
        "flake8.extension": ["PCK0 = flake8_mutable_defaults:MutableDefaultChecker"]
    },
    classifiers=["Topic :: Software Development :: Quality Assurance"],
)
