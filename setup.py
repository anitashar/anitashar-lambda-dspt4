

# setup.py file
from setuptools import find_packages, setup
with open("README.md", "r") as fh:
    long_description = fh.read()
setup(
    name="aniutility",
    version="1.1",
    author="Anita",
    author_email="anitashar2006@gmail.com",
    description="my_func",
    long_description=long_description,
    long_description_content_type="text/markdown",
    # required if using a md file for long desc
    # license="MIT",
    url="https://github.com/anitashar/anitashar-lambda-dspt4",
    # keywords="",
    packages=find_packages()  # ["my_lambdata"]
)
