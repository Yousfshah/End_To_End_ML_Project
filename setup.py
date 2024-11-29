from setuptools import setup, find_packages
from typing import List
HYPEN_E_DOT= "-e ."

def get_requirements(file_path:str)->List[str]:
    "This Function Will Return The List of Reqirements"

    requirements= []

    with open(file_path) as file_obj:
        requirements= file_obj.readlines()
        requirements= [req.replace('\n', "") for req in requirements]
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

        return requirements


setup(
    name="ML_APP",
    version="1.0.0",
    author="Yousuf Shah",
    author_email="contact.ys09@gmail.com",
    description="An End-To-End Machine Learning Application.",
    url="https://github.com/Yousfshah/End_To_End_ML_Project",
    packages= find_packages(), 
    install_requires= get_requirements("requirements.txt"), 

)
