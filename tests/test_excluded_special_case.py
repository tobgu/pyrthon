from pyrsistent import v

def test_substitution_when_module_registered_via_custom_matcher():
    x = []
    assert type(x) is type(v())