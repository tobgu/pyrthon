import os
from setuptools import setup
from pyrthon._version import __version__


f = open(os.path.join(os.path.dirname(__file__), 'README.rst'))
readme = f.read()
f.close()


setup(
    name='pyrthon',
    version=__version__,
    description='Literal syntax for Pyrsistent data structures',
    long_description=readme,
    author='Tobias Gustafsson',
    author_email='tobias.l.gustafsson@gmail.com',
    url='http://github.com/tobgu/pyrthon/',
    license='LICENSE.mit',
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
    ],
    test_suite='tests',
    scripts=[],
    install_requires=['pyrsistent'],
    packages=['pyrthon']
)
