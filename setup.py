from setuptools import setup ,find_packages 

with open("requirements.txt") as requirement_file:
    requirements = requirement_file.read().split()

setup(
    name='Tour_Guide',
    version='1.0.0',
    description='this package is for tour guide program',
    install_requires=requirements,
    packages=find_packages(exclude='test*'),
    setup_requires=['wheel'],
    entry_points={
        'console_scripts': [
            'abc = srs.main:main'
        ],
    },
)
