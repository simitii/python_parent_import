import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="parent_import",
    version="0.0.1",
    author="Samet Demir",
    author_email="demir.samet@hotmail.com",
    description="This package makes it easier to import from parent directory.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/simitii/python_parent_import",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.5',
)