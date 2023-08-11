from plotnineseqsuite.tool import extract


def test_extract():
    seqs = ['TTGTGAAAGAC', 'AAGTAAACTAA', 'TAATAAACAAA', 'TAATAAACAAA', 'CTGTAAATATT', 'TAGAAAGGTAT']
    result = extract(seqs, start=1, end=4)
