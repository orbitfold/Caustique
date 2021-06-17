  
from setuptools import setup, find_packages

setup(
    name='Caustique',
    version='0.0.1',
    url='https://github.com/orbitfold/Caustique.git',
    author='Vytautas Jancauskas',
    author_email='unaudio@gmail.com',
    description='Causal Inference Tools',
    packages=find_packages(),    
    install_requires=['numpy', 'matplotlib', 'pandas'],
)
