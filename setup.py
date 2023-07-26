from setuptools import find_packages,setup
from typing import List


HYPHEN_E='-e .'
def get_requirements(file_path:str)-> List[str]:
    requirements=[]
    with open('requirements.txt') as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace('\n',' ')for req in requirements]


        if HYPHEN_E in requirements:
            requirements.remove(HYPHEN_E)

    return requirements        

setup(
    name="MLPROject",
    version='0.0.1',
    author="Raghav",
    author_email="s.raghavsharma2012@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')

)