'''
The setup.py file is an essential part of packaging and distributing 
python project . It is used by setuptools (or distutils in older python
versions) to define the configuration of your project, such as its meta
data, dependencies and more.
'''
from setuptools import find_packages , setup
from typing import List

def get_requirements()->List[str]:
    '''
    This function will return list of requirements.
    '''
    requirement_lst:List[str]=[]
    try:
        with open('requirements.txt','r') as file:
            #Read lines form the file
            lines=file.readlines()
            #process each line
            for line in lines:
                requirement= line.strip()
                #ignore empty line
                if requirement and requirement!='-e .':
                    requirement_lst.append(requirement)

    except FileNotFoundError:
        print("requirement file is not found.")
    return requirement_lst

print(get_requirements())

setup(
    name='NetworkSecurity',
    version='0.0.1',
    author='Nishtha Jain',
    author_email='nishthajain0306@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements()
)