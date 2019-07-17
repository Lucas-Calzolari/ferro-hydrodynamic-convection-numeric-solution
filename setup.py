import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="ferro-hydrodynamic-convection-numeric-solution",
    version="0.0.1",
    author="Lucas Calzolari",
    author_email="lucascpds@gmail.com",
    description="Some numeric fluid simulations",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Lucas-Calzolari/ferro-hydrodynamic-convection-numeric-solution",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)