Introduction
============

.. _Pyrsistent: https://www.github.com/tobgu/pyrsistent/

Pyrthon is a utility library that substitutes python collection literals with their Pyrsistent_ counterparts.

Instead of writing this:

.. code:: python

    from pyrsistent import pvector
    x = pvector([1, 2, 3])
    y = x.set(0, 17)

You can simply write this:

.. code:: python

    x = [1, 2, 3]
    y = x.set(0, 17)

The results will be equivalent.

Examples
--------

In *foo/main.py*:

.. code:: python

    # Register any modules under 'foo' for pyrsistent substitution before any
    # imports from 'foo' modules.
    #
    # Registration can be done in three ways:
    # * Exact module name.
    #   register('foo.bar')
    # * Prefix with wild card. All submodules of the prefix.
    #   register('foo.*')
    # * Custom matcher function that returns true if substitution should be applied in the module.
    #   register(lambda name: name.startswith('foo') and name.endswith('baz'))

    from pyrthon import register
    register('foo.*')

    from foo.app import run

    if __name__ == '__main__':
        run()


In *foo/app.py*:

.. code:: python

    # All literal collection declarations in this module will now be mapped to
    # corresponding pyrsistent collections.

    def run():
        x = [1, 2, 3]    # -> pvector([1, 2, 3])
        y = {'a': 1}     # -> pmap({'a': 1})
        z = {'a'}        # -> pset(['a'])

        # It's not possible to declare an empty set in python using a literal.
        # Therefore some special treatment is required.
        p = set()   # -> pset([]), pyrsistent pset
        q = set([]) # -> set(), regular python set

        # To declare regular python lists, dicts and sets just use the function syntax
        a = list([1, 2, 3])    # -> [1, 2, 3]
        b = dict(a=1)          # -> {'a': 1}
        c = set(['a'])         # -> set(['a'])

        print('Hello functional world!')

Pyrthon also has basic shell support. Just import *pyrthon.console* and you're good to go:

.. code:: python

    >>> import pyrthon.console
    Pyrsistent data structures enabled
    >>> [1, 2, 3]
    pvector([1, 2, 3])
    >>> {'a': 1}
    pmap({'a': 1})
    >>> {'a'}
    pset(['a'])


It's also possible to use pyrthon from Jupyter/IPython notebooks. For that an extension must be loaded.
This can be done from the console or a cell:

.. code:: shell

    % load_ext pyrthon


Installation
------------

pip install pyrthon

How it works
------------

Pyrthon works by Python AST manipulation and import hooks. All literal lists and list comprehensions,
dicts and dict comprehensions, sets and set comprehensions in selected modules are substituted to produce
the equivalent Pyrsistent data structure upon module import.

Limitations and quirks
----------------------

This library is currently in experimental status.

If combined with other frameworks that manipulate the AST or performs other "magic" transformations to your
code the result may not be as expected.

Usage in tests executed with pytest requires some additional work since no explicit import of the test files
is ever performed. Also the assert used by pytest is heavily manipulated compared to the original assert and
prevents direct substitution of literals. Normally this should not matter for the sake of testing though since
a pvector compares to a list, a pmap to a dict and a pset to a set but it's good to know.

Because substitution is performed on import Pyrthon currently requires at least two python files in any application
and library. One file, in which no substitutions will take place, will have to register all modules on which
transformations should be applied before those modules are imported. The file containing the main entry point for
a program/library would be a good point to perform this registration.

Compatibility
-------------

Pyrthon is developed and tested on Python 2.7, 3.4 and PyPy (Python 2.7 compatible).

Contributors
------------

Tobias Gustafsson https://github.com/tobgu

Todd Iverson https://github.com/yardsale8 (IPython/Jupyter support)

Contributing
------------

If you experience problems please log them on GitHub. If you want to contribute code, please submit a pull request.
