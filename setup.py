import re
from os.path import dirname, join
from setuptools import find_packages, setup

with open(join(dirname(__file__), "src/word_ps", "__init__.py")) as fp:
    for line in fp:
        m = re.search(r'^\s*__version__\s*=\s*([\'"])([^\'"]+)\1\s*$', line)
        if m:
            version = m.group(2)
            break
    else:
        raise RuntimeError("Unable to find own __version__ string")

requirements = [
    'nltk>=3.6.0'
]

extras = {
    "testing": [
        "pytest>=4.4.0",
    ]
}

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
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    install_requires=requirements,
    extras_require=extras,
    python_requires=">=3.7.0",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)