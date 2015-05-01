import imp
import os
import types
import sys
from pyrton._transformer import transform


class PyrsistentImporter(object):
    def __init__(self):
        self._match_expressions = []
        self._cache = {}

    def module_matches(self, name):
        return name in self._match_expressions

    def add_matchers(self, matchers):
        self._match_expressions.extend(matchers)

    def find_module(self, name, path=None):
        if not self.module_matches(name):
            return None

        # TODO: Is all this caching stuff really needed or could we
        #       just move this code the load_module?
        try:
            suffix = name.split('.')[-1]
            self._cache[name] = imp.find_module(suffix)
        except ImportError:
            return None

        return self

    def load_module(self, name):
        print "Called load %s" % name

        module = types.ModuleType(name) #create empty module object
        fd, pathname, (suffix, mode, type_) = self._cache[name]
        print "Called load %s" % ((fd, pathname, (suffix, mode, type_)),)

        with fd:
            if type_ == imp.PY_SOURCE:
                filename = pathname
            elif type_ == imp.PY_COMPILED:
                filename = pathname[:-1]
            elif type_ == imp.PKG_DIRECTORY:
                filename = os.path.join(pathname, '__init__.py')
                module.__path__ = [pathname]
            else:
                return imp.load_module(name, fd, pathname,
                                       (suffix, mode, type_))
            if not filename == pathname:
                try:
                    with open(filename, 'U') as realfile:
                        src = realfile.read()
                except IOError: #fallback
                    return imp.load_module(name, fd, pathname,
                                           (suffix, mode, type_))
            else:
                src = fd.read()

        module = types.ModuleType(name)
        module.__file__ = filename
        inlined = transform(src)
        code = compile(inlined, filename, 'exec')
        sys.modules[name] = module
        exec(code,  module.__dict__)

        return module

# TODO: Initialization function that inserts itself in meta_path if not already present and then
#       registers regexps that are used to match which modules that should be affected which calls

importer = PyrsistentImporter()


