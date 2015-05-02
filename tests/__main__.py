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
# Explicit import of test module required for correct pyrton treatment before
# running tests. Also some variants of imports that should and should not trigger
# literal replacement are tested.

from pyrton import register

# Three different module matching methods exist
register('tests.test_pyrton',                         # Explicit
         'tests.test_included*',                      # Trailing wild card
         lambda name: name.endswith('special_case'))  # Custom module name matcher

# Main tests, should trigger on explicit name
import tests.test_pyrton

# Should trigger on wild card
import tests.test_included_substitution

# Should not trigger
import tests.test_excluded_no_substitution

# Should trigger on special case match function
import tests.test_excluded_special_case

pytest.main()