import setuptools


with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="PyAutoAPI",
    version="0.0.2",
    description="Easily and automatically turn a database into an API",
    author="jay3ss",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jay3ss/pyautoapi",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.10",
)
