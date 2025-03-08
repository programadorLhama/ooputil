# setup.py
from setuptools import setup, find_packages

setup(
    name="ooputil",
    version="0.2.4",
    description="Library for OOP utilities",
    author="Rafael da Rocha Ferreira",
    author_email="programadorlhama@gmail.com",
    packages=find_packages(include=["ooputil", "ooputil.*"]),
    install_requires=[],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)