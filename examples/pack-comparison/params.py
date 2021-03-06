"""
Parameters for the 2013 Nissan Leaf battery cell and module.
"""

# Surface area of the battery cell [m²]
a_surf = 0.067569

# Heat capacity of the battery cell [J/(kg K)]
# cp_cell = 900
# cp_cell = 1100
# cp_cell = 1300
cp_cell = 1600

# Heat capacity of the battery module [J/(kg K)]
cp_module = 900

# Coulombic efficiency of the battery cell for charge and discharge [-]
eta_chg = 0.98
eta_dis = 1.00

# Convective heat transfer coefficient [W/(m² K)]
# h_conv = 10
# h_conv = 12
h_conv = 9.5

# Convective heat transfer coefficient for module tests [W/(m² K)]
# h_conv = 15

# Mass of a single battery cell [kg]
m_cell = 0.799

# Mass of a single battery module [kg]
# value is m_cell * 4
m_module = 3.196

# Total capacity of the battery cell [Ah]
# note that rated capacity for the battery cell is stated as 33.1 Ah
# according to email from Hsin, use 32-33 Ah for HPPC tests
# according to email from Hsin, use 30.6 Ah for discharge tests
# q_cell = 32.0
q_cell = 30.6

# Total capacity of the battery module [Ah]
q_module = 65.4
# q_module = 61.2

# Ambient temperature [K]
tinf = 298.15

# Ambient temperature for US06 drive cycle tests [K]
# tinf = 295.15
