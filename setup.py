from setuptools import find_packages,setup
# install packages from requirements
from typing import List

HYPEN_E_DOT='-e .'



# main purpose of this function is to read packages from requirements.txt file and install it
# we will take input requiremts.txt file and return as list which is string
def get_requirements(file_path)->List[str]:
    requirements=[]
    # open file_path which is requirements.txt file
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()

        requirements = [req.replace('\n','') for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
        return requirements


setup(
    name='src',
    version='0.0.1',
    author='nikhil',
    author_email='nikhilmogre1998@gmail.com',
    # we are calling the function and from there we are raplacing '\n' to ''
    install_requires=get_requirements('requirements.txt'),
    # find the packages and install it
    packages=find_packages()
)