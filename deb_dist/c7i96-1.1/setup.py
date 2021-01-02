import os
from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="c7i96",
    version="1.1",
    author="John Thornton",
    author_email="<jt@gnipsel.com>",
    description="Mesa configuration tool for 7i96",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jethornton/7i96",
    download_url="https://github.com/jethornton/7i96/tarball/master",
    python_requires='>=3',
    packages=['c7i96'],
    include_package_data=True,
    entry_points={
        'gui_scripts': ['c7i96 = c7i96.c7i96:main',],
    },
    data_files = [
        ('share/applications/', ['7i96 Configurator.desktop'])
    ],
    classifiers=[
        "License :: OSI Approved :: MIT License",
    ],
)

