from plotnine import ggplot, facet_wrap
from numpy import random, array

import patchworklib as pw
from plotnineseqsuite.logo import geom_logo
from plotnineseqsuite.theme import theme_seq
from numpy import allclose


def test_logo_data():
    seqs = ['TTGTGAAAGAC', 'AAGTAAACTAA', 'TAATAAACAAA', 'TAATAAACAAA', 'CTGTAAATATT', 'TAGAAAGGTAT']
    logo_dict = geom_logo(seqs)._geom_logo__logo_data(seqs, 'akrobat_bold')
    assert logo_dict['logo_data'].size == 942 * 6
    assert logo_dict['seq_type'] == 'DNA'


def test_geom_logo():
    seqs = ['TTGTGAAAGAC', 'AAGTAAACTAA', 'TAATAAACAAA', 'TAATAAACAAA', 'CTGTAAATATT', 'TAGAAAGGTAT']
    seqs1 = ["KHEEEEWTDDDLVES", "VWDHIEVSDDEDETH", "TSADVKMSSSEEVSW",
             "SADVKMSSSEEVSWI", "RAAMFPETLDEGMQI", "AAPEEAETLAETEPE",
             "EAETLAETEPERHLG", "GDVEGSQSQDEGEGS", "QEEEILGSDDDEQED",
             "DYLFEPHSGEEYTRD", "FLDSLGFSTREEGDL", "QDNGAEDSGDTEDEL",
             "GAEDSGDTEDELRRV", "GEDPYAGSTDENTDS", "EDPYAGSTDENTDSE",
             "AGSTDENTDSEEHQE", "EFDTNYATDDDIVFE", "KSNIVLLSAEEKKEQ",
             "PPQDQESSPIENDSS", "DDDDDDNSDEEDNDD", "PKIEEERSEEEGTPP",
             "QVAAIAETDESAESE", "SEHDSDESSDDDSDS", "EHDSDESSDDDSDSE",
             "DESSDDDSDSEEPSK", "SKESEHDSDESSDDD", "NAIRYIESLQELLRE",
             "HKAELQGSDEDEHVR", "NEAYEMPSEEGYQDY", "SEGGADDSAEEGDLL",
             "TSGEDTLSDSDDEDD", "GEDTLSDSDDEDDEE", "ELRTAKDSDDDDDVA",
             "GSVSEDNSEDEISNL", "AGKGGAASGSDSADK", "KRSRAIHSSDEGEDQ",
             "RSRAIHSSDEGEDQA", "KFVIRPATAADCSDI", "FYKRRGASDLSSEEG",
             "RRGASDLSSEEGWRL", "AAQQTKGSYMEVEDN", "MEVEDNRSQVETDDL",
             "VDGTGDTSSEEDEDE", "DGTGDTSSEEDEDEE", "VEEEPLNSEDDVSDE",
             "LNSEDDVSDEEGQEL", "DDIDLFGSDDEEESE", "GSDDEEESEEAKRLR",
             "KEEEEGISQESSEEE", "IACEEEFSDSEEEGE", "CEEEFSDSEEEGEGG",
             "TSVTPDVSDNEPDHY", "YRIQEQESSGEEDSD", "RIQEQESSGEEDSDL",
             "GDDEDACSDTEATEA", "ESETNQNSSSDSEAE", "SETNQNSSSDSEAER",
             "ETNQNSSSDSEAERR", "LGLPEEETELDNLTE", "KNSRVTFSEDDEIIN",
             "MPLQPNASLNEEEGT", "PRMRRQRSAPDLKES", "NLNENQASEEEDELG",
             "LFRLSEHSSPEEEAS", "AGESLDQSMEEEEEE", "ADRPPSMSSHDTASP",
             "EDAVHEDSGDEDGED", "IACDEEFSDSEDEGE", "CDEEFSDSEDEGEGG",
             "VDGSGDTSSNEEIGS", "DGSGDTSSNEEIGST", "VEEDPLNSGDDVSEQ",
             "LNSGDDVSEQDVPDL", "PYPSPVLSEEEDLPL", "DSPALEVSDSESDEA",
             "PALEVSDSESDEALV", "TKRPEGRTYADYESV", "RTYADYESVNECMEG",
             "PTEENEMSSEADMEC", "TNGDGEISTSELREA"]
    logo_dict = geom_logo(seqs1)._geom_logo__logo_data(seqs1, 'akrobat_bold')
    assert logo_dict['logo_data'].size == 7644 * 6
    assert logo_dict['seq_type'] == 'AA'
    ggplot() + geom_logo(data=seqs1, font='akrobat_bold')+theme_seq()
    ggplot() + geom_logo(data=seqs, method='probability')+theme_seq()



def test_CUSTOM_geom_logo():
    seqs = random.randint(-2, 2, size=(4, 4))
    ggplot()+geom_logo(data=seqs, method='custom', seq_type='DNA')+theme_seq()


def test_narray_data():
    seqs = array([[2, 7, 0, 6, 14, 14, 0, 0],
                 [13, 0, 7, 0, 0, 0, 0, 1],
                 [0, 5, 5, 1, 0, 2, 0, 6],
                 [0, 4, 4, 9, 2, 0, 16, 9]])
    ggplot() + geom_logo(data=seqs, method='bits', seq_type='DNA') + theme_seq()

def test_facet():
    seq1 = array([[1,1,0,0],
                 [0,1,0,1],
                 [0,1,1,0],
                 [0,0,1,1]])
    seq2 = array([[0,1,0,1],
                 [0,1,0,1],
                 [0,1,1,0],
                 [1,0,1,0]])
    seq3 = array([[0,1,1,1],
                 [1,1,1,1],
                 [1,1,0,1],
                 [1,0,0,0]])
    ggplot() + geom_logo(data={'ad':seq1,'cc':seq2,'45':seq3}, method='probability', seq_type='DNA')+ theme_seq()+facet_wrap('~seq_group')

def test_compute_bits():
    pfm = array([[0.1666667, 0.6666667, 0.3333333, 0.1666667, 0.8333333, 1, 0.8333333, 0.1666667, 0.5000000, 0.8333333,
                  0.5000000],
                 [0.6666667, 0.3333333, 0.0000000, 0.8333333, 0.0000000, 0, 0.0000000, 0.1666667, 0.3333333, 0.1666667,
                  0.3333333],
                 [0.0000000, 0.0000000, 0.6666667, 0.0000000, 0.1666667, 0, 0.1666667, 0.1666667, 0.1666667, 0.0000000,
                  0.0000000],
                 [0.1666667, 0.0000000, 0.0000000, 0.0000000, 0.0000000, 0, 0.0000000, 0.5000000, 0.0000000, 0.0000000,
                  0.1666667]])
    R_i = array(
        [0.38769702, 0.72103044, 0.72103044, 0.98930374, 0.98930374, 1.63932624, 0.98930374, 0., 0.18017829, 0.98930374,
         0.18017829])
    Nseqs = array([6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6])
    seqs = ['TTGTGAAAGAC', 'AAGTAAACTAA', 'TAATAAACAAA', 'TAATAAACAAA', 'CTGTAAATATT', 'TAGAAAGGTAT']
    assert allclose(geom_logo(seqs)._geom_logo__compute_bits(pfm, 4, Nseqs), R_i)


def test_make_pfm():
    seqs = ['TTGTGAAAGAC', 'AAGTAAACTAA', 'TAATAAACAAA', 'TAATAAACAAA', 'CTGTAAATATT', 'TAGAAAGGTAT']
    pfm_dict = geom_logo(seqs)._geom_logo__make_PFM(seqs)
    pfm = array([[0.1666667, 0.6666667, 0.3333333, 0.1666667, 0.8333333, 1, 0.8333333, 0.1666667, 0.5000000, 0.8333333,
                  0.5000000],
                 [0.1666667, 0.0000000, 0.0000000, 0.0000000, 0.0000000, 0, 0.0000000, 0.5000000, 0.0000000, 0.0000000,
                  0.1666667],
                 [0.0000000, 0.0000000, 0.6666667, 0.0000000, 0.1666667, 0, 0.1666667, 0.1666667, 0.1666667, 0.0000000,
                  0.0000000],
                [0.6666667, 0.3333333, 0.0000000, 0.8333333, 0.0000000, 0, 0.0000000, 0.1666667, 0.3333333, 0.1666667,
                 0.3333333]])
    R_i = array(
        [0.38769702, 0.72103044, 0.72103044, 0.98930374, 0.98930374, 1.63932624, 0.98930374, 0., 0.18017829, 0.98930374,
         0.18017829])
    assert allclose(pfm_dict['bits'], R_i)
    assert pfm_dict['seq_type'] == 'DNA'
    assert allclose(pfm_dict['pfm'], pfm)

def test_probability_method():
    seqs = ['TTGTGAAAGAC', 'AAGTAAACTAA', 'TAATAAACAAA', 'TAATAAACAAA', 'CTGTAAATATT', 'TAGAAAGGTAT']
    height_info = geom_logo(seqs)._geom_logo__probability_method(seqs=seqs, reverse=False, seq_type='AUTO', namespace=None)
    assert height_info['height_df'].size == 26 * 4
    assert height_info['seq_type'] == 'DNA'


def test_bits_method():
    seqs = ['TTGTGAAAGAC', 'AAGTAAACTAA', 'TAATAAACAAA', 'TAATAAACAAA', 'CTGTAAATATT', 'TAGAAAGGTAT']
    height_info = geom_logo(seqs)._geom_logo__bits_method(seqs=seqs, reverse=False, seq_type='AUTO', namespace=None)
    assert height_info['height_df'].size == 22 * 4
    assert height_info['seq_type'] == 'DNA'