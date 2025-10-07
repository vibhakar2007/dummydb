from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="dummydb",
    version="0.1.6",
    packages=find_packages(),
    install_requires=[
        # No external dependencies for now
    ],
    author="Vibhakar S",
    author_email="vibhakarsenth@gmail.com",
    url="https://github.com/vibhakar2007/dummydb",
    license="MIT",
    description="A lightweight in-memory database for Python — perfect for testing and prototyping.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
)
