from simu import tax_direct

def test_tax_direct():

# https://www.service-public.gouv.fr/simulateur/calcul/droits-succession#main

    assert tax_direct(0) == 0
    assert tax_direct(50000) == 0
    assert tax_direct(100000) == 0
    assert tax_direct(105000) == 250
    assert tax_direct(108072) == 403.6
    assert tax_direct(109000) == 496.4
    assert tax_direct(113000) == 940.95
    assert tax_direct(200000) == 18194.35
    assert tax_direct(700000) == 122961.95
    assert tax_direct(1500000) == 412678.15
    assert tax_direct(2000000) == 617394.3
