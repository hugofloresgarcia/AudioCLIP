import os
from setuptools import setup, find_packages

INTERNAL_PYPI = "https://pypi.spotify.net/simple"


setup(
    name="audioclip",
    description="audioclip",
    version="0.0.1",
    packages=find_packages(exclude=["test", "*.test", "*.test.*"]),
    install_requires=["pytorch-ignite"],
    extras_require={"tests": ["pytest"]},
)
