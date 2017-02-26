import pytest

# Some special measures needed to make the tests running as intended since
# py.test does some magic on it's own.
# - Need to make an explicit import of the modules here instead of letting
#   py.test pick them up.
# - Cannot use the expressions to be substituted directly in the assert since
#   the assert is magic when running under py.test.
#
# Perhaps py.test should not be used for testing this project at all...
#
# Explicit import of test module required for correct pyrthon treatment before
# running tests. Also some variants of imports that should and should not trigger
# literal replacement are tested.

from pyrthon import register

# Three different module matching methods exist
register('tests.test_pyrthon',                        # Explicit
         'tests.test_included*',                      # Trailing wild card
         lambda name: name.endswith('special_case'))  # Custom module name matcher

# Main tests, should trigger on explicit name
import tests.test_pyrthon

# Should trigger on wild card
import tests.test_included_substitution

# Should trigger on wild card
from tests.test_included_wildcard_import import test_substitution_when_module_registered_via_wild_card_match_and_function_imported_via_wildcard

# Should not trigger
import tests.test_excluded_no_substitution

# Should trigger on special case match function
import tests.test_excluded_special_case

# TODO: Add tests for from ... import ...

pytest.main()
