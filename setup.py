import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="gimpify",
    version="0.0.1",
    author="watxaut",
    author_email="watxaut@gmail.com",
    description="Just a package to create automatic face image montages",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/watxaut/gimpify",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
)
