import matplotlib.pyplot as plt
import numpy as np

# https://www.service-public.gouv.fr/particuliers/vosdroits/F35794

# Son / grand son / parents => FIRST DEGREE
TAX_DIRECT_DEDUCTION = 100_000
TAX_DIRECT_5 = 0.05
TAX_DIRECT_5_MAX = 8_072
TAX_DIRECT_10 = 0.1
TAX_DIRECT_10_MAX = 12_109
TAX_DIRECT_15 = 0.15
TAX_DIRECT_15_MAX = 15_932
TAX_DIRECT_20 = 0.2
TAX_DIRECT_20_MAX = 552_324
TAX_DIRECT_30 = 0.3
TAX_DIRECT_30_MAX = 902_838
TAX_DIRECT_40 = 0.4
TAX_DIRECT_40_MAX = 1_805_677
TAX_DIRECT_45 = 0.45

# Brother / Sister
TAX_BS_DEDUCTION = 15_932
TAX_BS_35 = 0.35
TAX_BS_35_MAX = 24_430
TAX_BS_45 = 0.45

# AV
TAX_AV_DEDUCTION = 152_500
TAX_AV_20 = 0.2
TAX_AV_20_MAX = 700_000
TAX_AV_3125 = 0.3125

# Return tax for the given capital with direct bloodline
def tax_direct(capital) -> float:

    results = 0.0

    # 0
    if capital <= TAX_DIRECT_DEDUCTION:
        result = 0.0
    
    # 5
    elif TAX_DIRECT_DEDUCTION < capital and capital <= TAX_DIRECT_DEDUCTION + TAX_DIRECT_5_MAX:
        result = (capital-TAX_DIRECT_DEDUCTION)*TAX_DIRECT_5

    # 10
    elif TAX_DIRECT_DEDUCTION + TAX_DIRECT_5_MAX < capital and capital <= TAX_DIRECT_DEDUCTION + TAX_DIRECT_10_MAX:
        result = (capital - TAX_DIRECT_5_MAX - TAX_DIRECT_DEDUCTION)*TAX_DIRECT_10 + TAX_DIRECT_5_MAX*TAX_DIRECT_5

    # 15
    elif TAX_DIRECT_DEDUCTION + TAX_DIRECT_10_MAX < capital and capital <= TAX_DIRECT_DEDUCTION + TAX_DIRECT_15_MAX:
        result = (capital - TAX_DIRECT_10_MAX - TAX_DIRECT_DEDUCTION)*TAX_DIRECT_15 + (TAX_DIRECT_10_MAX-TAX_DIRECT_5_MAX)*TAX_DIRECT_10 + TAX_DIRECT_5_MAX*TAX_DIRECT_5

    # 20
    elif TAX_DIRECT_DEDUCTION + TAX_DIRECT_15_MAX < capital and capital <= TAX_DIRECT_DEDUCTION + TAX_DIRECT_20_MAX:
        result = (capital - TAX_DIRECT_15_MAX - TAX_DIRECT_DEDUCTION)*TAX_DIRECT_20 + (TAX_DIRECT_15_MAX-TAX_DIRECT_10_MAX)*TAX_DIRECT_15 + (TAX_DIRECT_10_MAX-TAX_DIRECT_5_MAX)*TAX_DIRECT_10 + TAX_DIRECT_5_MAX*TAX_DIRECT_5

    # 30
    elif TAX_DIRECT_DEDUCTION + TAX_DIRECT_20_MAX < capital and capital <= TAX_DIRECT_DEDUCTION + TAX_DIRECT_30_MAX:
        result = (capital - TAX_DIRECT_20_MAX - TAX_DIRECT_DEDUCTION)*TAX_DIRECT_30 + (TAX_DIRECT_20_MAX-TAX_DIRECT_15_MAX)*TAX_DIRECT_20 + (TAX_DIRECT_15_MAX-TAX_DIRECT_10_MAX)*TAX_DIRECT_15 + (TAX_DIRECT_10_MAX-TAX_DIRECT_5_MAX)*TAX_DIRECT_10 + TAX_DIRECT_5_MAX*TAX_DIRECT_5

    # 40
    elif TAX_DIRECT_DEDUCTION + TAX_DIRECT_30_MAX < capital and capital <= TAX_DIRECT_DEDUCTION + TAX_DIRECT_40_MAX:
        result = (capital - TAX_DIRECT_30_MAX - TAX_DIRECT_DEDUCTION)*TAX_DIRECT_40 + (TAX_DIRECT_30_MAX-TAX_DIRECT_20_MAX)*TAX_DIRECT_30 + (TAX_DIRECT_20_MAX-TAX_DIRECT_15_MAX)*TAX_DIRECT_20 + (TAX_DIRECT_15_MAX-TAX_DIRECT_10_MAX)*TAX_DIRECT_15 + (TAX_DIRECT_10_MAX-TAX_DIRECT_5_MAX)*TAX_DIRECT_10 + TAX_DIRECT_5_MAX*TAX_DIRECT_5

    # 45
    else:
        result = (capital - TAX_DIRECT_40_MAX - TAX_DIRECT_DEDUCTION)*TAX_DIRECT_45 + (TAX_DIRECT_40_MAX-TAX_DIRECT_30_MAX)*TAX_DIRECT_40 + (TAX_DIRECT_30_MAX-TAX_DIRECT_20_MAX)*TAX_DIRECT_30 + (TAX_DIRECT_20_MAX-TAX_DIRECT_15_MAX)*TAX_DIRECT_20 + (TAX_DIRECT_15_MAX-TAX_DIRECT_10_MAX)*TAX_DIRECT_15 + (TAX_DIRECT_10_MAX-TAX_DIRECT_5_MAX)*TAX_DIRECT_10 + TAX_DIRECT_5_MAX*TAX_DIRECT_5

    return round(result, 2)

# Return tax for the given capital with brother / sister
def tax_first_degree(capital) -> float:

    results = 0.0

    # 0
    if capital <= TAX_BS_DEDUCTION:
        result = 0.0
    
    # 35
    elif TAX_BS_DEDUCTION < capital and capital <= TAX_BS_DEDUCTION + TAX_BS_35_MAX:
        result = (capital-TAX_BS_DEDUCTION)*TAX_BS_35
    
    # 45
    else:
        result = (capital-TAX_BS_35_MAX-TAX_BS_DEDUCTION)*TAX_BS_45 + TAX_BS_35_MAX*TAX_BS_35

    return round(result, 2)

def tax_av(capital) -> float:

    results = 0.0

    # 0
    if capital <= TAX_AV_DEDUCTION:
        result = 0.0
    
    # 20
    elif TAX_AV_DEDUCTION < capital and capital <= TAX_AV_DEDUCTION + TAX_AV_20_MAX:
        result = (capital-TAX_AV_DEDUCTION)*TAX_AV_20
    
    # 31.25
    else:
        result = (capital-TAX_AV_20_MAX-TAX_AV_DEDUCTION)*TAX_AV_3125 + TAX_AV_20_MAX*TAX_AV_20

    return round(result, 2)
