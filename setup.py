from setuptools import setup, find_packages
import heurekacz

VERSION = (0, 0, 1)
__version__ = VERSION
__versionstr__ = '.'.join(map(str, VERSION))

setup(
    name = 'heurekacz',
    version = __versionstr__,
    description = 'Heureka.cz python libs',
    long_description = '\n'.join((
        'Heureka.cz python libs',
        '',
        'Overeno zakazniky',
    )),
    author = 'Vitek Pliska',
    author_email='whit@jizak.cz',
    license = 'BSD',
    url='http://github.com/whit/python-heurekacz/',

    packages = find_packages(
        where = '.',
        exclude = ('docs', 'tests')
    ),

    include_package_data = True,

    # TODO: REPLACE
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 2.5",
        "Programming Language :: Python :: 2.6",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    install_requires = [
        'setuptools>=0.6b1',
    ],
    setup_requires = [
    ],
)
