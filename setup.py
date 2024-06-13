from setuptools import setup, find_packages # type: ignore

readme: str
with open(file="./README.md", mode="r",  encoding="utf-8") as file:
    readme = file.read()
setup(
    name="binary-s",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[],
    author="mateuss",
    author_email="mateus.rodrigues.sistema@gmail.com",
    description="Binary system composed only of 's'",
    long_description=readme,
    long_description_content_type="text/markdown",
    url="https://github.com/mateus-rodriguess/binary-s",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.10",
)
