"""
add_bread is a function that takes a dictionary describing a `person`
and a string of their favourite bread, and returns that object with a
new property (`fave_bread`) set to a value of their favourite bread.

If no favourite bread is given then the default fave_bread is 'granary'.

Unfortunately, it looks like the function has a couple of issues with
the way it's written.

Can you work out what needs changing to make the function pass all the tests?
"""


def add_bread(person, loaf):
    person['fave_bread'] = loaf
    return person


# Do not change code below this line

def test_adds_favourite_bread():
    person_1 = {'name': 'Joe'}
    person_2 = {'name': 'Paul'}
    assert add_bread(person_1, 'rye') == {'name': 'Joe', 'fave_bread': 'rye'}
    assert add_bread(person_2, 'granary') == {
        'name': 'Paul', 'fave_bread': 'granary'}
