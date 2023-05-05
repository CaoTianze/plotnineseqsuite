from plotnineseqsuite.common import *


def test_letter_matrix():
    assert (letter_matrix(['aa', 'cd']) == array([['a', 'a'], ['c', 'd']])).all()


def test_guess_seq_type():
    type1 = guess_seq_type(['A', 'C'])
    assert type1 == 'DNA'
    type2 = guess_seq_type(['A', 'U'])
    assert type2 == 'RNA'
    type3 = guess_seq_type(['A', 'R'])
    assert type3 == 'AA'


def test_find_namespace():
    namespace = find_namespace(letter_mat=array([['A', 'A'], ['C', 'U']]), seq_type='AUTO')
    assert namespace['namespace'] == ['A', 'U', 'G', 'C']
    assert namespace['seq_type'] == 'RNA'
