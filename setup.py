from setuptools import setup

setup(
    name="search",
    version="0.9",
    author="balancy",
    author_email="balancy@gmail.com",
    install_requires=["beautifulsoup4", "lxml", "requests", "terminaltables"],
    packages=["search"],
)
