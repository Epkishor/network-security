from setuptools import find_packages,setup
from typing import List

def get_requirements()->List[str]:
    """
    This function will return list of requirements

    
    """
    requirement_list:List[str]=[]
    try:
        with open('requirements.txt','r') as file:
            #read lines from file
            lines = file.readlines()
            #Process each line
            for line in lines:
                requirement = line.strip()
                ## ignore the empty line and ignore -e .
                if requirement and requirement != '-e .':
                    requirement_list.append(requirement)
    except FileNotFoundError:
        print('requirements.txt file not found') 
    
    return requirement_list

print(get_requirements())

setup(
    name ="Network security",
    version ="0.0.1",
    author ="Kishor pant",
    author_email = "kishorpant887@gmail.com",
    packages=find_packages(include=["networksecurity", "networksecurity.*"]),
    install_requires = get_requirements()
    
)
            