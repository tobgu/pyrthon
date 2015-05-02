import sys
import pyrthon._import_hook as import_hook


def register(*matchers):
    if import_hook.importer not in sys.meta_path:
        sys.meta_path.insert(0, import_hook.importer)

    import_hook.importer.add_matchers(matchers)