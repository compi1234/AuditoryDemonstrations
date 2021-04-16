from setuptools import setup, find_packages

setup(
    name="AuditoryDemonstrations",
    version="0.0.1",
    url="https://github.com/compi1234/AuditoryDemonstrations",

    author="Dirk Van Compernolle",
    author_email="compi@esat.kuleuven.be",

    description="{\em Hi}",
    license = "free",
    
    packages = ['utils'],
    py_modules = [],
    # a dictionary refering to required data not in .py files
    package_data = {},
    
    install_requires=['numpy','pandas','matplotlib'],

    classifiers=['Development Status: Pure Development',
                 'Programming Language :: Python :: 3.7',
                 'Programming Language :: Python :: 3.8'],
                 
    include_package_data=True

)