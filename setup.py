from setuptools import setup

import codecs
import os.path


def read(rel_path: str) -> str:
    """ Open file and return it's contents
    Args:
        rel_path (str): Relative path to  file to read

    Returns:
        str: A string containing the file contents
     """
    here = os.path.abspath(os.path.dirname(__file__))
    with codecs.open(os.path.join(here, rel_path), 'r') as fp:
        return fp.read()


def get_version(rel_path: str) -> str:
    """ Search a file for a string assignment to __version__

    Args:
        rel_path (str): Relative path to  file to search for a version number

    Returns:
        str: the version string
     """
    for line in read(rel_path).splitlines():
        if line.startswith('__version__'):
            delim = '"' if '"' in line else "'"
            return line.split(delim)[1]
    else:
        raise RuntimeError("Unable to find version string.")


dependencies = [

]

extra_dependencies = {
    "dev": [
        # Docs
        "sphinx",

        # Testing
        "pytest",

        # misc
        "bump2version"
    ]
}

setup(
    name="minecraft-bds-server",
    author="Tim Gardener",
    description="Minecraft BDS server manager",
    long_description=read("README.md"),
    long_description_content_type="text/markdown",
    packages=["bds"],
    package_dir={'': 'src'},
    python_requires=[">=3.8"],
    install_requires=dependencies,
    extras_require=extra_dependencies,
    version=get_version("src/bds/__init__.py")
)
