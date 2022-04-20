# HOW-TOs

## Build package and publish project

Dependency:

```bash
pip install twine
```

Build:

```bash
# build package
python3 setup.py sdist build
# publish
python3 -m twine upload dist/*
```