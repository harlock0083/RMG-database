#!/usr/bin/env python
# encoding: utf-8

name = "xo1247R"
shortDesc = u""
longDesc = u"""
xo1247R
"""

entry(
    index = 1,
    label = "CH3 + H <=> CH4",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(1.801e+14, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (7.93e+24, 'cm^6/(mol^2*s)'),
            n = -2.17,
            Ea = (0, 'kcal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.124,
        T3 = (1800, 'K'),
        T1 = (33.1, 'K'),
        T2 = (90000, 'K'),
        efficiencies = {'C': 2, 'O=C=O': 2, 'O': 3.42, 'C=O': 2.5, '[O][O]': 0.59, 'N#N': 0.59},
    ),
)

entry(
    index = 2,
    label = "O2 + H <=> HO2",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(
            A = (4.565e+12, 'cm^3/(mol*s)'),
            n = 0.44,
            Ea = (0, 'kcal/mol'),
            T0 = (1, 'K'),
        ),
        arrheniusLow = Arrhenius(
            A = (6.37e+20, 'cm^6/(mol^2*s)'),
            n = -1.72,
            Ea = (0.525, 'kcal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.5,
        T3 = (30, 'K'),
        T1 = (90000, 'K'),
        T2 = (90000, 'K'),
        efficiencies = {'C': 2, 'O=C=O': 3.45, 'O': 15.81, 'C=O': 2.5, '[H][H]': 1.87, '[O][O]': 0.75, 'N#N': 0.96},
    ),
)

entry(
    index = 3,
    label = "HO2 + CH3 <=> CH4 + O2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (126900, 'cm^3/(mol*s)'),
        n = 2.228,
        Ea = (-3.022, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 4,
    label = "H2 <=> H + H",
    degeneracy = 1,
    kinetics = ThirdBody(
        arrheniusLow = Arrhenius(
            A = (4.58e+19, 'cm^3/(mol*s)'),
            n = -1.4,
            Ea = (104.39, 'kcal/mol'),
            T0 = (1, 'K'),
        ),
        efficiencies = {'C': 2, 'O=C=O': 3.83, 'O': 12.02, 'C=O': 2.5, '[H][H]': 2.55, 'N#N': 1.01},
    ),
)

entry(
    index = 5,
    label = "HO2 + H <=> O2 + H2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.945e+06, 'cm^3/(mol*s)'),
        n = 2.087,
        Ea = (-1.455, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 6,
    label = "CH4 + H <=> CH3 + H2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (478100, 'cm^3/(mol*s)'),
        n = 2.5,
        Ea = (9.588, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 7,
    label = "HO2 + H <=> OH + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5.888e+13, 'cm^3/(mol*s)'), n=0, Ea=(0.3, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 8,
    label = "O2 + H <=> O + OH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (9.841e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (15.31, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 9,
    label = "O + H2 <=> H + OH",
    degeneracy = 1,
    kinetics = MultiArrhenius(
        arrhenius = [
            Arrhenius(
                A = (3.848e+12, 'cm^3/(mol*s)'),
                n = 0,
                Ea = (7.95, 'kcal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (6.687e+14, 'cm^3/(mol*s)'),
                n = 0,
                Ea = (19.18, 'kcal/mol'),
                T0 = (1, 'K'),
            ),
        ],
    ),
)

entry(
    index = 10,
    label = "O + O <=> O2",
    degeneracy = 1,
    kinetics = ThirdBody(
        arrheniusLow = Arrhenius(
            A = (6.16e+15, 'cm^6/(mol^2*s)'),
            n = -0.5,
            Ea = (0, 'kcal/mol'),
            T0 = (1, 'K'),
        ),
        efficiencies = {'C=O': 2.5, 'C': 2, '[H][H]': 2.5, 'O=C=O': 3.8, 'O': 12},
    ),
)

entry(
    index = 11,
    label = "H + O <=> OH",
    degeneracy = 1,
    kinetics = ThirdBody(
        arrheniusLow = Arrhenius(A=(4.71e+18, 'cm^6/(mol^2*s)'), n=-1, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
        efficiencies = {'C': 2, 'O=C=O': 5.01, 'O': 15.8, 'C=O': 2.5, '[H][H]': 2.5, 'N#N': 1.32},
    ),
)

entry(
    index = 12,
    label = "HO2 + O <=> O2 + OH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.609e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (-0.445, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 13,
    label = "CH4 + O <=> CH3 + OH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.786e+08, 'cm^3/(mol*s)'),
        n = 1.56,
        Ea = (8.485, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 14,
    label = "O + OH <=> HO2",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.493, 0.855, 1.48], 'atm'),
        arrhenius = [
            Arrhenius(
                A = (5.651e+18, 'cm^3/(mol*s)'),
                n = -2.71,
                Ea = (1.114, 'kcal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (9.286e+18, 'cm^3/(mol*s)'),
                n = -2.703,
                Ea = (1.17, 'kcal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (1.51e+19, 'cm^3/(mol*s)'),
                n = -2.696,
                Ea = (1.247, 'kcal/mol'),
                T0 = (1, 'K'),
            ),
        ],
    ),
)

entry(
    index = 15,
    label = "OH + H2 <=> H2O + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.256e+08, 'cm^3/(mol*s)'),
        n = 1.51,
        Ea = (3.437, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 16,
    label = "OH + OH <=> H2O + O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (31610, 'cm^3/(mol*s)'),
        n = 2.42,
        Ea = (-1.928, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 17,
    label = "H2O <=> H + OH",
    degeneracy = 1,
    kinetics = ThirdBody(
        arrheniusLow = Arrhenius(
            A = (6.06e+27, 'cm^3/(mol*s)'),
            n = -3.322,
            Ea = (120.8, 'kcal/mol'),
            T0 = (1, 'K'),
        ),
        efficiencies = {'C': 2, 'O=C=O': 4.67, 'O': 0, 'C=O': 2.5, '[H][H]': 3.77, '[O][O]': 1.5, 'N#N': 2.46},
    ),
)

entry(
    index = 18,
    label = "H2O + H2O <=> H2O + H + OH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7.528e+25, 'cm^3/(mol*s)'),
        n = -2.44,
        Ea = (120.2, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 19,
    label = "HO2 + H <=> H2O + O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.632e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 20,
    label = "HO2 + OH <=> O2 + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7.347e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (-1.093, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 21,
    label = "CH4 + OH <=> H2O + CH3",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (983900, 'cm^3/(mol*s)'),
        n = 2.182,
        Ea = (2.446, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 22,
    label = "CH3 + O <=> CH2O + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5.722e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 23,
    label = "CH3 + OH <=> CH2O + H2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.735e+09, 'cm^3/(mol*s)'),
        n = 0.734,
        Ea = (-2.177, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 24,
    label = "O2 + CH3 <=> CH2O + OH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (99.77, 'cm^3/(mol*s)'),
        n = 2.86,
        Ea = (9.768, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 25,
    label = "HO2 + CH3 <=> CH3O + OH",
    degeneracy = 1,
    duplicate = True,
    kinetics = Arrhenius(
        A = (8.821e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (-0.59, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 26,
    label = "O2 + CH3 <=> CH3O + O",
    degeneracy = 1,
    duplicate = True,
    kinetics = Arrhenius(
        A = (8.104e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (28.297, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 27,
    label = "CH3O <=> CH2O + H",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(1.13e+10, 's^-1'), n=1.21, Ea=(24.075, 'kcal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (6.02e+16, 'cm^3/(mol*s)'),
            n = -0.547,
            Ea = (18.024, 'kcal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.341,
        T3 = (28, 'K'),
        T1 = (1000, 'K'),
        T2 = (2340, 'K'),
        efficiencies = {'C=O': 2.5, 'C': 2, '[H][H]': 2, 'O=C=O': 2, 'O': 6},
    ),
)

entry(
    index = 28,
    label = "CH3O + H <=> CH2O + H2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.79e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0.596, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 29,
    label = "CH3O + H <=> CH3 + OH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.88e+14, 'cm^3/(mol*s)'),
        n = -0.264,
        Ea = (-0.026, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 30,
    label = "CH3O + O <=> CH2O + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.78e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 31,
    label = "CH3O + OH <=> H2O + CH2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.81e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 32,
    label = "O2 + CH3O <=> HO2 + CH2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.32e+10, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (2.603, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 33,
    label = "CH3 + CH3O <=> CH4 + CH2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.4e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 34,
    label = "O2 + CH3 <=> CH3O + O",
    degeneracy = 1,
    duplicate = True,
    kinetics = PDepArrhenius(
        pressures = ([0.493, 0.855, 1.48], 'atm'),
        arrhenius = [
            Arrhenius(
                A = (5.002e+07, 'cm^3/(mol*s)'),
                n = 1.541,
                Ea = (27.151, 'kcal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (5.007e+07, 'cm^3/(mol*s)'),
                n = 1.541,
                Ea = (27.151, 'kcal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (5.015e+07, 'cm^3/(mol*s)'),
                n = 1.541,
                Ea = (27.152, 'kcal/mol'),
                T0 = (1, 'K'),
            ),
        ],
    ),
)

entry(
    index = 35,
    label = "CH3 + O <=> CH3O",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.493, 0.855, 1.48], 'atm'),
        arrhenius = [
            Arrhenius(
                A = (1.667e+32, 'cm^3/(mol*s)'),
                n = -5.813,
                Ea = (9.751, 'kcal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (3.999e+31, 'cm^3/(mol*s)'),
                n = -5.581,
                Ea = (9.763, 'kcal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (6.906e+30, 'cm^3/(mol*s)'),
                n = -5.312,
                Ea = (9.689, 'kcal/mol'),
                T0 = (1, 'K'),
            ),
        ],
    ),
)

entry(
    index = 36,
    label = "HO2 + CH3 <=> CH3O + OH",
    degeneracy = 1,
    duplicate = True,
    kinetics = PDepArrhenius(
        pressures = ([0.493, 0.855, 1.48], 'atm'),
        arrhenius = [
            Arrhenius(
                A = (4.245e+13, 'cm^3/(mol*s)'),
                n = -0.157,
                Ea = (0.36, 'kcal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (4.423e+13, 'cm^3/(mol*s)'),
                n = -0.162,
                Ea = (0.38, 'kcal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (4.747e+13, 'cm^3/(mol*s)'),
                n = -0.17,
                Ea = (0.415, 'kcal/mol'),
                T0 = (1, 'K'),
            ),
        ],
    ),
)

entry(
    index = 37,
    label = "HCO + H <=> CH2O",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(
            A = (1.913e+14, 'cm^3/(mol*s)'),
            n = -0.033,
            Ea = (-0.142, 'kcal/mol'),
            T0 = (1, 'K'),
        ),
        arrheniusLow = Arrhenius(
            A = (4.19e+34, 'cm^6/(mol^2*s)'),
            n = -5.533,
            Ea = (6.128, 'kcal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.782,
        T3 = (271, 'K'),
        T1 = (2760, 'K'),
        T2 = (6570, 'K'),
        efficiencies = {'C=O': 2.84, 'C': 2, 'O=C=O': 2, 'O': 6},
    ),
)

entry(
    index = 38,
    label = "CH2O + H <=> HCO + H2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7.149e+07, 'cm^3/(mol*s)'),
        n = 1.9,
        Ea = (2.742, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 39,
    label = "CH2O + O <=> HCO + OH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.244e+11, 'cm^3/(mol*s)'),
        n = 0.57,
        Ea = (2.762, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 40,
    label = "CH2O + OH <=> H2O + HCO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (8.338e+07, 'cm^3/(mol*s)'),
        n = 1.63,
        Ea = (-1.055, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 41,
    label = "O2 + CH2O <=> HO2 + HCO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (329700, 'cm^3/(mol*s)'),
        n = 2.5,
        Ea = (36.46, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 42,
    label = "CH3 + CH2O <=> CH4 + HCO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(32.13, 'cm^3/(mol*s)'), n=3.36, Ea=(4.31, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 43,
    label = "HCO + CH3O <=> CH2O + CH2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.717e+14, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using average of templates [Y_rad;Cmethyl_Orad] + [CO_pri_rad;XH_s_Rrad] for rate rule [CO_pri_rad;Cmethyl_Orad]\nMultiplied by reaction path degeneracy 3',
    ),
    longDesc = 
u"""
Estimated using average of templates [Y_rad;Cmethyl_Orad] + [CO_pri_rad;XH_s_Rrad] for rate rule [CO_pri_rad;Cmethyl_Orad]
Multiplied by reaction path degeneracy 3
""",
)

entry(
    index = 44,
    label = "HCO <=> CO + H",
    degeneracy = 1,
    kinetics = ThirdBody(
        arrheniusLow = Arrhenius(
            A = (4.8e+17, 'cm^3/(mol*s)'),
            n = -1.2,
            Ea = (17.734, 'kcal/mol'),
            T0 = (1, 'K'),
        ),
        efficiencies = {'C': 2.6, 'O=C=O': 2, 'O': 15.31, 'C=O': 3.29, '[H][H]': 1.31, '[O][O]': 1.32, 'N#N': 1.31},
    ),
)

entry(
    index = 45,
    label = "HCO + H <=> CO + H2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(8.482e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 46,
    label = "HCO + O <=> CO + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.01e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 47,
    label = "HCO + OH <=> H2O + CO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.199e+14, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 48,
    label = "O2 + HCO <=> HO2 + CO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7.562e+10, 'cm^3/(mol*s)'),
        n = 0.521,
        Ea = (-0.521, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 49,
    label = "CH2O <=> CO + H2",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(3.7e+13, 's^-1'), n=0, Ea=(71.976, 'kcal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(A=(4.4e+38, 'cm^3/(mol*s)'), n=-6.1, Ea=(94, 'kcal/mol'), T0=(1, 'K')),
        alpha = 0.932,
        T3 = (197, 'K'),
        T1 = (1540, 'K'),
        T2 = (10300, 'K'),
        efficiencies = {'C=O': 2.5, 'C': 2, 'O=C=O': 2, 'O': 6},
    ),
)

entry(
    index = 50,
    label = "CH3 + O <=> CO + H + H2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.384e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 51,
    label = "HCO + CH3 <=> CH4 + CO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5.3e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 52,
    label = "CH2 + H <=> CH3",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(2.13e+13, 'cm^3/(mol*s)'), n=0.32, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (1.39e+34, 'cm^6/(mol^2*s)'),
            n = -5.04,
            Ea = (7.4, 'kcal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.405,
        T3 = (258, 'K'),
        T1 = (2810, 'K'),
        T2 = (9910, 'K'),
        efficiencies = {'C=O': 2.5, 'C': 2, 'O=C=O': 2, 'O': 6},
    ),
)

entry(
    index = 53,
    label = "CH2 + O <=> CO + H + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(8e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 54,
    label = "CH2 + OH <=> CH2O + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.899e+13, 'cm^3/(mol*s)'),
        n = 0.12,
        Ea = (-0.162, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 55,
    label = "HO2 + CH2 <=> CH2O + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 56,
    label = "CH2 + H2 <=> CH3 + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.265e+06, 'cm^3/(mol*s)'),
        n = 2,
        Ea = (7.23, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 57,
    label = "O2 + CH2 <=> CO + H + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.643e+12, 'cm^3/(mol*s)'), n=0, Ea=(1, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 58,
    label = "O2 + CH2 <=> CH2O + O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.6e+12, 'cm^3/(mol*s)'), n=0, Ea=(1, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 59,
    label = "O2 + CH2 <=> H2O + CO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5.2e+11, 'cm^3/(mol*s)'), n=0, Ea=(1, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 60,
    label = "CH2 + CH2O <=> HCO + CH3",
    degeneracy = 1,
    kinetics = Arrhenius(A=(0.074, 'cm^3/(mol*s)'), n=4.21, Ea=(1.12, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 61,
    label = "CH3 + OH <=> H2O + CH2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (44640, 'cm^3/(mol*s)'),
        n = 2.57,
        Ea = (3.998, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 62,
    label = "CH4 + CH2 <=> CH3 + CH3",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.483e+06, 'cm^3/(mol*s)'),
        n = 2,
        Ea = (8.27, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 63,
    label = "HO2 + CH2 <=> O2 + CH3",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (340400, 'cm^3/(mol*s)'),
        n = 1.61,
        Ea = (4.377, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [X_H;CH2_triplet] for rate rule [Orad_O_H;CH2_triplet]',
    ),
    longDesc = 
u"""
Estimated using template [X_H;CH2_triplet] for rate rule [Orad_O_H;CH2_triplet]
""",
)

entry(
    index = 64,
    label = "CH2 + OH <=> CH3 + O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.806e+10, 'cm^3/(mol*s)'),
        n = 0.75,
        Ea = (-0.445, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Xrad_H;Y_1centerbirad] for rate rule [OH_rad_H;CH2_triplet]',
    ),
    longDesc = 
u"""
Estimated using template [Xrad_H;Y_1centerbirad] for rate rule [OH_rad_H;CH2_triplet]
""",
)

entry(
    index = 65,
    label = "CH2 + CH3O <=> CH3 + CH2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (9.03e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [CH2_triplet;Cmethyl_Rrad] for rate rule [CH2_triplet;Cmethyl_Orad]\nMultiplied by reaction path degeneracy 3',
    ),
    longDesc = 
u"""
Estimated using template [CH2_triplet;Cmethyl_Rrad] for rate rule [CH2_triplet;Cmethyl_Orad]
Multiplied by reaction path degeneracy 3
""",
)

entry(
    index = 66,
    label = "CO + O <=> CO2",
    degeneracy = 1,
    kinetics = Lindemann(
        arrheniusHigh = Arrhenius(A=(1.88e+11, 'cm^3/(mol*s)'), n=0, Ea=(2.43, 'kcal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (1.4e+21, 'cm^6/(mol^2*s)'),
            n = -2.1,
            Ea = (5.5, 'kcal/mol'),
            T0 = (1, 'K'),
        ),
        efficiencies = {'C=O': 2.5, 'C': 2, 'O=C=O': 3.8, 'O': 12},
    ),
)

entry(
    index = 67,
    label = "O2 + CO <=> CO2 + O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.533e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (47.7, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 68,
    label = "CO + OH <=> CO2 + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (61870, 'cm^3/(mol*s)'),
        n = 2.053,
        Ea = (-0.356, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 69,
    label = "HO2 + CO <=> CO2 + OH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (157000, 'cm^3/(mol*s)'),
        n = 2.18,
        Ea = (17.944, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 70,
    label = "HCO + O <=> CO2 + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.001e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 71,
    label = "O2 + CH2 <=> CO2 + H + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.844e+12, 'cm^3/(mol*s)'), n=0, Ea=(1, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 72,
    label = "O2 + CH2 <=> CO2 + H2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.836e+12, 'cm^3/(mol*s)'), n=0, Ea=(1, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 73,
    label = "CO + CH3O <=> CO2 + CH3",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6e+12, 'cm^3/(mol*s)'), n=0, Ea=(11, 'kcal/mol'), T0=(1, 'K')),
)

