from pyrsistent import v

def test_substitution_when_module_registered_via_wild_card_match_and_function_imported_via_wildcard():
    x = []
    assert type(x) is type(v())