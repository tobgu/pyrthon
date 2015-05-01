from pyrsistent import v, m, s


def test_list_becomes_a_pvector():
    x = [1, 2]

    assert type(x) is type(v())
    assert x == v(1, 2)


def test_list_comprehension_becomes_a_pvector():
    x = [i for i in range(2)]

    assert type(x) is type(v())
    assert x == v(0, 1)


def test_dict_becomes_a_pmap():
    x = {'a': 1}

    assert type(x) is type(m())
    assert x == m(a=1)


def test_dict_comprehension_becomes_a_pmap():
    x = {k: v for k, v in [('a', 1)]}

    assert type(x) is type(m())
    assert x == m(a=1)


def test_set_becomes_a_pset():
    x = {'a'}

    assert type(x) is type(s())
    assert x == s('a')


def test_set_function_becomes_a_pset_when_no_argument():
    x = set()

    assert type(x) is type(s())
    assert x == s()


def test_set_function_becomes_a_set_when_arguments_are_present():
    x = set([])
    x.add(1)

    assert x == set([1])
    assert type(x) is not type(s())


def test_set_comprehension_becomes_a_pmap():
    x = {i for i in ['a']}

    assert type(x) is type(s())
    assert x == s('a')