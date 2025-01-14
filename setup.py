from setuptools import find_packages, setup
from typing import List

notins = "-e ."

def get_requirements(file_path: str) -> List[str]:
    """
    Reads the requirements.txt file and returns a list of requirements.
    """
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()  # Read lines from the file object
        requirements = [req.strip() for req in requirements]  # Remove newline characters
        if notins in requirements:
            requirements.remove(notins)  # Remove the `notins` if present
    return requirements

setup(
    name="mlproject",
    version="0.001",
    author="sarang",
    author_email="sarang36910@gmail.com",  # Use `author_email` for the email address
    packages=find_packages(),
    install_requires=get_requirements('requirement.txt'),
)
