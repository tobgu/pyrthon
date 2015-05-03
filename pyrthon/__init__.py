import sys
import pyrthon._import_hook as import_hook


def register(*matchers):
    """
    Register modules for literal substitution. Matchers can be specified in three ways:

        * Exact module name, eg:
          register('foo.bar')
        * Prefix with wild card. All submodules of the prefix. Eg.
          register('foo.*')
        * Custom matcher function that returns true if the module should return true:
          register(lambda name: name.startswith('foo') and name.endswith('baz'))

    This function must be called before the referred modules are imported.
    """
    if import_hook.importer not in sys.meta_path:
        sys.meta_path.insert(0, import_hook.importer)

    import_hook.importer.add_matchers(matchers)