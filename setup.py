from setuptools import find_packages, setup
from typing import List

var = "-e."

def get_requirements(filepath:str) -> List[str]:

    requirements = []
    with open(filepath) as f:
        requirements = f.readlines()
        requirements = [req.replace("/n", "") for req in requirements]

    if var in requirements:
        requirements.remove(var)

    return requirements


setup(
    name="Diamond_Price_Predition",
    version="0.0.1",
    author="Nishchal Jinturkar",
    author_email="nishchaljinturkar30@gmail.com",
    install_requires=get_requirements("requirements.txt"),
    packages=find_packages()
)