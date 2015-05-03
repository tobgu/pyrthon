import code
import ast
from pyrthon._transformer import transform


class PyrsistentConsole(code.InteractiveConsole):
    def runsource(self, source, filename='<input>', symbol='single'):
        try:
            code_object = self.compile(source, filename, symbol)
        except (OverflowError, SyntaxError, ValueError):
            code_object = ''

        if code_object is None:
            # This means it's incomplete
            return True

        try:
            tree = transform(source)
            tree = ast.Interactive(tree.body)
            code_object = compile(tree, filename, symbol, self.compile.compiler.flags, 1)
        except (OverflowError, SyntaxError, ValueError):
            # This means there's a syntax error
            self.showsyntaxerror(filename)
            return False

        # This means it was successfully compiled; `runcode` takes care of any runtime failures
        self.runcode(code_object)
        return False
