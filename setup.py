from os import path
from setuptools import setup, find_packages

HERE = path.abspath(path.dirname(__file__))

with open(path.join(HERE, "VERSION"), encoding="utf-8") as f:
    VERSION = f.read().strip()

setup(author="Andrew Michaud",
      author_email="bots+knowsska@mail.andrewmichaud.com",

      entry_points={
          "console_scripts": ["knowsska_bot = knowsska_bot.__main__:main"]
      },

      install_requires=["botskeleton>=3.3.6"],

      license="BSD3",

      name="knowsska_bot",

      packages=find_packages(),
      python_requires=">=3.6",

      url="https://github.com/alixnovosi/knowsska_bot",

      version=VERSION)
