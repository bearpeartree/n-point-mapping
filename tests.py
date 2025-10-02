from main import check_recomb
from main import check_current_gamete

def test_check_parental_combo():
    test_gamete = "A+/B/C+"
    
    assert check_recomb(test_gamete, 'A', 'C') == "parental"


def test_check_parental_2_combo():
    test_gamete = "A/B/C+"

    assert check_recomb(test_gamete, 'A', 'B') == "parental"


def test_check_recombi_combo():
    test_gamete = "vg/cv+/e+"

    assert check_recomb(test_gamete, 'cv', 'vg') == "recombinental"


def test_check_recombi_2_combo():
    assert check_recomb("A/B/C+", 'A', 'C') == "recombinental"


def test_check_current_gamete():
    tester = "A/B/C+"

    assert check_current_gamete('A', 'B', 'C', tester) == ("parental", "recombinental", "recombinental")


def test_check_current_gamete_all_parental():
    tester = "vg/e/c"

    assert check_current_gamete('vg', 'e', 'c', tester) == ("parental", "parental", "parental")


