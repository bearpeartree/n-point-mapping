from main import check_recomb


def test_check_parental_combo():
    test_gamete = "A+/B/C+"
    
    assert check_recomb(test_gamete, 'A', 'C') == "parental"


def test_check_parental_2_combo():
    test_gamete = "A/B/C+"

    assert check_recomb(test_gamete, 'A', 'B') == "parental"