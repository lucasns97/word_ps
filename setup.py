# LIBS
import re
from os.path import dirname, join
from setuptools import find_packages, setup

# CONFIG
APP_DIR = "app/"
SRC_DIR = f"{APP_DIR}src/"
REQUIREMENT_FILENAMES = {
    "app": "requirements.txt",
    "extra.testing": "requirements-testing.txt"
}

# METHODS
def get_version():
    """
    Returns version from __init__.py file in SRC directory.

    Returns:
    --------
        string: Version number
    """
    with open(join(dirname(__file__), SRC_DIR, "__init__.py")) as fp:
        for line in fp:
            m = re.search(r'^\s*__version__\s*=\s*([\'"])([^\'"]+)\1\s*$', line)
            if m:
                version = m.group(2)
                break
        else:
            raise RuntimeError("Unable to find own __version__ string")

    return version

def get_requirements(filename):
    """
    Returns requirements from file in APP directory.

    Params:
    -------
        filename (str): Path to requirements file
    
    Returns:
    --------
        list: List of requirements
    """
    with open(join(dirname(__file__), APP_DIR, filename)) as fp:
        return [line.strip() for line in fp if line.strip() and not line.strip().startswith("#")]

# Get version
VERSION = get_version()

# Get requirements
INSTALL_REQUIREMENTS = get_requirements(REQUIREMENT_FILENAMES.get('app'))
EXTRAS_REQUIREMENTS = {
    "testing": get_requirements(REQUIREMENT_FILENAMES.get('extra.testing'))
}

# Run setup
setup(
    name="word_ps",
    version="0.1.3",
    author="Lucas Nunes Sequeira",
    author_email="lucasnseq@gmail.com",
    description="Tools for word similarity",
    license="MIT",
    url="https://github.com/lucasns97/word_ps",
    project_urls={
        "Bug Tracker": "https://github.com/lucasns97/word_ps/issues",
    },
    package_dir={"": "app/src"},
    packages=find_packages(where="app/src"),
    install_requires=INSTALL_REQUIREMENTS,
    extras_require=EXTRAS_REQUIREMENTS,
    python_requires=">=3.7.0",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)