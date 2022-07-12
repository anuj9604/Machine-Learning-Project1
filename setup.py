from pkg_resources import require
from setuptools import setup
from typing import List

##declaring variables for setup function
PROJECT_NAME="housing-predictor"
VERSION="0.0.2"
AUTHOR="Anuj Khare"
DESCRIPTION="This is a very rudimentary project"
REQUIREMENT_FILE_NAME="requirements.txt"

def get_requirements_list()->List[str]:
    """This function is going to return list of requirements in requirements.txt file
    
    return: This function is going to return a list which contains name of libraries mentioned in requirements.txt file"""
    with open(REQUIREMENT_FILE_NAME) as requirement_file:
        requirement_file.readlines()

setup(
    name=PROJECT_NAME,
    version=VERSION,
    author=AUTHOR,
    description=DESCRIPTION,
    packages=["housing"],
    install_requires=get_requirements_list()
)