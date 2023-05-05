import re
import sys
from typing import List, Dict

from numpy import array, ndarray
from pandas import Series

AA_NAMESPACE = ['A', 'R', 'N', 'D', 'C', 'Q', 'E', 'G', 'H', 'I', 'L', 'K', 'M', 'F', 'P', 'S', 'T', 'W', 'Y', 'V']
DNA_NAMESPACE = ['A', 'C', 'G', 'T']
RNA_NAMESPACE = ['A', 'U', 'G', 'C']


def letter_matrix(seqs: List[str]) -> ndarray:
    seq_len = list(map(lambda x: len(x), seqs))
    first_len = seq_len[0]
    if not all(list(map(lambda x: x == first_len, seq_len))):
        raise Exception('Sequences in alignment must have identical lengths')
    chars = list(map(lambda x: list(x), seqs))
    return array(chars)


def guess_seq_type(seq: List[str]) -> str:
    seq = set(seq)
    if len(seq & (set(AA_NAMESPACE) | set(DNA_NAMESPACE) | set(RNA_NAMESPACE))) == 0:
        raise Exception(
            'Could not get guess seq_type. Please explicitly define sequence type or use "OTHER" with custom namespaces.')
    dat = (seq & set(AA_NAMESPACE)) - (set(DNA_NAMESPACE) | set(RNA_NAMESPACE))
    if len(dat) > 0:
        return 'AA'
    elif 'U' in seq:
        return 'RNA'
    return 'DNA'


def find_namespace(letter_mat: ndarray = None, seq_type: str = 'AUTO', namespace: List[str] = None) -> Dict:
    if seq_type == 'OTHER':
        if namespace is None:
            raise Exception('seq_type of "other" must have a defined namespace')
        non_alphanumeric = list(map(lambda letter: re.match(
            "[^-a-zA-Z0-9\u03bb\u03b1\u03b2\u0393\u03b3\u0394\u03b4\u03b5\u03b6\u03b7\u03b8\u0398\u03b9\u03ba\u039b\u03bc\u039e\u03be\u03a0\u03c0\u03c1\u03c3\u03c4\u03c5\u03a6\u03c6\u03c7\u03c8\u03a8\u03a9\u03c9]",
            letter) is not None, namespace))
        if any(non_alphanumeric):
            raise Exception('All letters in the namespace must be alphanumeric')
    else:
        if namespace is not None:
            raise Exception('For custom namespaces please set seq_type to "OTHER"')
        if seq_type == 'AUTO':
            letter_as_list = letter_mat.flatten().tolist()
            seq_type = guess_seq_type(letter_as_list)
        namespace = getattr(sys.modules[__name__], '%s_NAMESPACE' % seq_type)
    return {'namespace': namespace, 'seq_type': seq_type}


def new_range(old_vals: Series, new_min=0, new_max=1) -> Series:
    old_min = old_vals.min()
    old_max = old_vals.max()
    return (((old_vals - old_min) * (new_max - new_min)) / (old_max - old_min)) + new_min
