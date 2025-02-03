"""Python setup file."""
from setuptools import setup

setup(
    name='citadels',
    version='0.1',
    packages=['citadels'],
    install_requires=[
        "pandas",
        "openpyxl",
    ],
    entry_points={
        'console_scripts': [
            'citadels = citadels.__main__:main',
        ],
    },
)