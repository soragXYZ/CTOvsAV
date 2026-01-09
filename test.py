from simu import tax_direct, tax_first_degree, tax_av

# https://www.service-public.gouv.fr/simulateur/calcul/droits-succession#main

def test_tax_direct():

    assert tax_direct(0) == 0
    assert tax_direct(50_000) == 0
    assert tax_direct(100_000) == 0
    assert tax_direct(105_000) == 250
    assert tax_direct(108_072) == 403.6
    assert tax_direct(109_000) == 496.4
    assert tax_direct(113_000) == 940.95
    assert tax_direct(200_000) == 18_194.35
    assert tax_direct(700_000) == 122_961.95
    assert tax_direct(1_500_000) == 412_678.15
    assert tax_direct(2_000_000) == 617_394.3

def test_second_degree():

    assert tax_first_degree(0) == 0
    assert tax_first_degree(15_000) == 0
    assert tax_first_degree(16_000) == 23.8
    assert tax_first_degree(20_000) == 1423.8
    assert tax_first_degree(30_000) == 4923.8
    assert tax_first_degree(50_000) == 12_887.6
    assert tax_first_degree(100_000) == 35_387.6

def test_av():
    assert tax_av(0) == 0
    assert tax_av(152_500) == 0
    assert tax_av(252_500) == 20_000
    assert tax_av(352_500) == 40_000
    assert tax_av(852_500) == 140_000
    assert tax_av(1_000_000) == 186_093.75
