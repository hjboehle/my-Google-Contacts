"""module setup.py"""

from setuptools import setup, find_packages


setup(
    name="my_google_project",
    version="0.1.0",
    description="My Python project",
    author="Hans Jürgen Böhle",
    author_email="web@boehle.info",
    url="https://github.com/hjboehle/my-Google-Contacts",
    packages=find_packages(),
    install_requires=[
        "setuptools",
        "requests",
    ],
    test_suite="tests",
    python_requires=">=3.6",
)
