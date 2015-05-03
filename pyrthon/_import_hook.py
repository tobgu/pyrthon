import imp
import os
import types
import sys
from pyrthon._transformer import transform


class PyrsistentImporter(object):
    def __init__(self):
        self._match_expressions = []

    def module_matches(self, name):
        for expr in self._match_expressions:
            if callable(expr):
                if expr(name):
                    return True

            else:
                if expr.endswith('*') and name.startswith(expr[:-1]):
                    return True

                if expr == name:
                    return True

        return False

    def add_matchers(self, matchers):
        self._match_expressions.extend(matchers)

    def find_module(self, name, path=None):
        if self.module_matches(name):
            return self

        return None

    def load_module(self, name):
        try:
            suffix = name.split('.')[-1]
            fd, pathname, (suffix, mode, type_) = imp.find_module(suffix)
        except ImportError:
            return None

        module = types.ModuleType(name) #create empty module object

        with fd:
            if type_ == imp.PY_SOURCE:
                filename = pathname
            elif type_ == imp.PY_COMPILED:
                filename = pathname[:-1]
            elif type_ == imp.PKG_DIRECTORY:
                filename = os.path.join(pathname, '__init__.py')
                module.__path__ = [pathname]
            else:
                return imp.load_module(name, fd, pathname, (suffix, mode, type_))

            if filename != pathname:
                try:
                    with open(filename, 'U') as real_file:
                        src = real_file.read()
                except IOError: #fallback
                    return imp.load_module(name, fd, pathname, (suffix, mode, type_))
            else:
                src = fd.read()

        module.__file__ = filename
        inlined = transform(src)
        code = compile(inlined, filename, 'exec')
        sys.modules[name] = module
        exec(code,  module.__dict__)

        return module

importer = PyrsistentImporter()


