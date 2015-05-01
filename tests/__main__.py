import pytest

# Some special measures needed to make the tests running as intended since
# py.test does some magic on it's own.
#
# Explicit import of test module required for correct pyrton treatment before
# running tests.
from pyrton import init
init('tests.test_pyrton')
import tests.test_pyrton

pytest.main()