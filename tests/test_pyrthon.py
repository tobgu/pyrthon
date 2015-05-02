from pyrsistent import v, m, s


def test_literal_list_becomes_a_pvector():
    x = [1, 2]

    assert type(x) is type(v())
    assert x == v(1, 2)


def test_literal_list_with_function_call_becomes_a_pvector():
    x = [1, 2].append(3)

    assert type(x) is type(v())
    assert x == v(1, 2, 3)


def test_function_list_becomes_a_list():
    x = list()

    assert type(x) is not type(v())


def test_list_comprehension_becomes_a_pvector():
    x = [i for i in range(2)]

    assert type(x) is type(v())
    assert x == v(0, 1)


def test_literal_dict_becomes_a_pmap():
    x = {'a': 1}

    assert type(x) is type(m())
    assert x == m(a=1)


def test_literal_dict_with_function_call_becomes_a_pvector():
    x = {'a': 1}.set('b', 2)

    assert type(x) is type(m())
    assert x == m(a=1, b=2)


def test_dict_comprehension_becomes_a_pmap():
    x = {k: v for k, v in [('a', 1)]}

    assert type(x) is type(m())
    assert x == m(a=1)


def test_function_dict_becomes_a_dict():
    x = dict()

    assert type(x) is not type(m())


def test_set_becomes_a_pset():
    x = {'a'}

    assert type(x) is type(s())
    assert x == s('a')


def test_literal_set_with_function_call_becomes_a_pset():
    x = {'a'}.add('b')

    assert type(x) is type(s())
    assert x == s('a', 'b')


def test_empty_set_function_with_function_call_becomes_a_pset():
    x = set().add('b')

    assert type(x) is type(s())
    assert x == s('b')


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