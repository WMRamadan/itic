"""Setup file for itic."""

##############################################################################
# Python imports.
from pathlib    import Path
from setuptools import setup

##############################################################################
# Import the library itself to pull details out of it.
import itic

##############################################################################
# Work out the location of the README file.
def readme():
    """Return the full path to the README file.
    :returns: The path to the README file.
    :rtype: ~pathlib.Path
    """
    return Path( __file__ ).parent.resolve() / "README.md"

##############################################################################
# Load the long description for the package.
def long_desc():
    """Load the long description of the package from the README.
    :returns: The long description.
    :rtype: str
    """
    with readme().open( "r", encoding="utf-8" ) as rtfm:
        return rtfm.read()

##############################################################################
# Setup.
setup(

    name                          = "itic",
    version                       = itic.__version__,
    description                   = str( itic.__doc__ ),
    long_description              = long_desc(),
    long_description_content_type = "text/markdown",
    url                           = "https://github.com/wmramadan/itic",
    author                        = itic.__author__,
    author_email                  = itic.__email__,
    maintainer                    = itic.__maintainer__,
    maintainer_email              = itic.__email__,
    packages                      = ["iti"],
    install_requires              = [ "typer==0.3.2", "rich==12.6.0", "pillow==9.0.1" ],
    python_requires               = ">=3.9",
    keywords                      = "image to image converter",
    entry_points                  = {
        "console_scripts": "itic=itic.itic:main"
    },
    license                       = (
        "License :: OSI Approved :: MIT License"
    ),
    classifiers                   = [
        "License :: OSI Approved :: MIT License",
        "Environment :: Console",
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Other Audience",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Multimedia :: Graphics :: Graphics Conversion",
        "Topic :: Utilities",
        "Typing :: Typed"
    ]

)