import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="sssg",
    version="0.0.1",
    author="AndrewNeo",
    author_email="andrew@andrewneo.com",
    description="Simple static site generator with Jinja",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pypa/simplestaticsitegen",
    packages=setuptools.find_packages(),
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
)
