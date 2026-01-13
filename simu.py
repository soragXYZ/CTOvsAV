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

# CSG CRDS
TAX_CSG_CRDS_AV = 0.172
TAX_CSG_CRDS_CTO = 0.186

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

def calculate_return(capital, years, yieldR) -> float:
    return capital*pow(1+yieldR, years)


def main():

    other_capital = 300_000
    AV_management_fees = 0.005
    cYield = 0.05

    # Values to display in X axis, between min and max
    duration_min, duration_max = 10, 40

    resol_x = duration_max - duration_min + 1

    # Values to display in Y axis, between min and max
    round_caps = [
        100_000,
        250_000,
        500_000,
        1_000_000,
        2_000_000,
        5_000_000,
        10_000_000,
        15_000_000,
    ]

    resol_y = 50

    capital_min, capital_max = min(round_caps), max(round_caps)
    capitals = np.geomspace(capital_min, capital_max, resol_y)
    
    durations = np.linspace(duration_min, duration_max, resol_x)

    heatmap = []

    for capital in capitals:

        relatives = []

        for duration in durations:

            cto_capital = calculate_return(capital, duration, cYield)
            cto_first_degree_tax = tax_direct(cto_capital + other_capital)
            final_cto_first_degree = other_capital + cto_capital - cto_first_degree_tax

            # print(
            #     "CTO Capital:", cto_capital,
            #     "\nCTO first degree tax:", cto_first_degree_tax,
            #     "\nFinal CTO first degree", final_cto_first_degree,
            # )

            AV_capital_gross = calculate_return(capital, duration, cYield-AV_management_fees)
            AV_capital = AV_capital_gross-(AV_capital_gross-capital)*TAX_CSG_CRDS_AV
            AV_tax = tax_av(AV_capital)

            av_transmission = AV_capital - AV_tax
            other_tax = tax_direct(other_capital)
            final_av = av_transmission + other_capital - other_tax
            
            # print(
            #     "AV after anual fees", AV_capital_gross,
            #     "\nAV after anual fees and CSG CDRS", AV_capital,
            #     "\nAV after anual fees and CSG CDRS and tax", av_transmission,
            #     "\nFinal AV", final_av,
            # )

            AV_vs_CTO = (final_av - final_cto_first_degree) / (max(final_av, final_cto_first_degree)) * 100
            # print(AV_vs_CTO)

            relatives.append(round(AV_vs_CTO, 2))
        
        heatmap.append(relatives)

    ext = [durations[0], durations[-1], 0, resol_y - 1]

    fig, ax = plt.subplots()
    im = ax.imshow(heatmap, origin="lower", extent=ext, aspect="auto", cmap = 'seismic')

    # Line where CTO = AV
    plt.contour(heatmap, levels=[0], colors="black", linewidths=2, extent=ext)

    # Set y labels
    y_idx, y_labels = [], []
    for rc in round_caps:

        idx = (np.abs(capitals - rc)).argmin()
        y_idx.append(idx)

        label = f"{rc/1e6:g} M€" if rc >= 1_000_000 else f"{int(rc/1000)} k€"
        y_labels.append(label)
    
    ax.set_yticks(y_idx, y_labels)

    # Legends and title
    plt.xlabel("Durée de détention (années)")
    plt.ylabel("Capital initial")
    ax.set_title(
        "Rendement " + str(cYield*100) + "%. Frais UC " + str(AV_management_fees*100) + "%. " + str(int(other_capital/1000)) + "k hors enveloppe"
    )

    plt.colorbar(im, label="Avantage relatif (%) : Bleu = CTO, rouge = AV")
    plt.show()


if __name__ == "__main__":
    main()