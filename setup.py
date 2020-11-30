"""lambdata - a collection of Data Science functions"""
import setuptools

REQUIRED = [
    "numpy",
    "pandas"
]

with open("README.md", "r") as fh:
    LONG_DESCRIPTION = fh.read()

setuptools.setup(
    name= 'lambdata-ren-curry',
    version= '0.0.1',
    description= LONG_DESCRIPTION, 
    long_description_content= 'text/markdown',
    url= 'https://github.com/ren-curry/lambdata-ren-curry',
    packages=setuptools.find_packages(), # How we want to find our REQUIRED packages
    python_requires=">=3.6", # What versions of Python we are compatible with
    install_requires= REQUIRED,
    classifiers= [
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ]

)