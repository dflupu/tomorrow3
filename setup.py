from setuptools import setup, find_packages
from os import path

this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name="tomorrow3",
    version="1.2.2",
    author="Daniel Lupu",
    author_email="lupu.daniel.f@gmail.com",
    packages=find_packages(),
    license="MIT License (See LICENSE)",
    url="https://github.com/dflupu/tomorrow3",
    description="simplified tomorrow for python3",
    long_description=long_description,
    long_description_content_type='text/markdown'
)
