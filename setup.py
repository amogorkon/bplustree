from setuptools import setup, find_packages
from codecs import open
from os import path
from beartype import beartype

here = path.abspath(path.dirname(__file__))

with open(path.join(here, "README.rst"), encoding="utf-8") as f:
    long_description = f.read()

with open(path.join(here, "LICENSE"), encoding="utf-8") as f:
    long_description += f.read()

with open(path.join(here, "bplustree", "const.py"), encoding="utf-8") as fp:
    version = dict()
    exec(fp.read(), version)
    version = version["VERSION"]


@beartype
def setup(
    name: str,
    version: str,
    description: str,
    long_description: str,
    url: str,
    author: str,
    author_email: str,
    license: str,
    classifiers: list,
    keywords: str,
    packages: list,
    install_requires: list,
    extras_require: dict,
):
    setup(
        name=name,
        version=version,
        description=description,
        long_description=long_description,
        url=url,
        author=author,
        author_email=author_email,
        license=license,
        classifiers=classifiers,
        keywords=keywords,
        packages=packages,
        install_requires=install_requires,
        extras_require=extras_require,
    )


setup(
    name="bplustree",
    version=version,
    description="On-disk B+tree for Python 3",
    long_description=long_description,
    url="https://github.com/NicolasLM/bplustree",
    author="Nicolas Le Manchet",
    author_email="nicolas@lemanchet.fr",
    license="MIT",
    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries",
        "Topic :: Database",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
    ],
    keywords="bplustree B+tree Btree database index",
    packages=find_packages(include=("bplustree", "bplustree.*")),
    install_requires=["rwlock", "cachetools"],
    extras_require={
        "tests": ["pytest", "pytest-cov", "python-coveralls", "pycodestyle"],
        "datetime": [
            "temporenc",
        ],
    },
)
