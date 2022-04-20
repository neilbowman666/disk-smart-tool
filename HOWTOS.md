# HOW-TOs

## Build package and publish to PyPI

Dependency:

```bash
# for source package
pip install twine
# (optional) for wheel package
pip install wheel
```

Build:

```bash
# build source package
python3 setup.py sdist build
# (optional) build wheel package
python3 setup.py bdist_wheel
# publish package
python3 -m twine upload dist/*
```