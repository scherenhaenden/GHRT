#!/usr/bin/env python3
"""GHRT-VPT *toy* benchmark, using only the Python standard library.

This script verifies algebra and illustrates parameter tension. It does not
calculate a gravitational bounce or predict a physically accessible universe.
Reference cosmology: H0=67.4 km/s/Mpc, Omega_m=0.315, Omega_L=0.685.
"""
from __future__ import annotations

import math

C = 299_792_458.0  # m/s
HBAR = 1.054_571_817e-34  # J*s
HBAR_EV_S = 6.582_119_569e-16  # eV*s
HBAR_C_EV_M = 1.973_269_804e-7  # eV*m
EV_J = 1.602_176_634e-19  # J/eV
K_B_EV_K = 8.617_333_262_145e-5  # eV/K
K_B_SI = 1.380_649e-23  # J/K
G_SI = 6.67430e-11  # m3 kg-1 s-2
MPC_M = 3.085_677_581_491_367e22  # m
MPL_REDUCED_EV = 2.435e27

OMEGA_M = 0.315
OMEGA_L = 0.685
H0_S = 67.4 * 1000.0 / MPC_M
H_INF_S = H0_S * math.sqrt(OMEGA_L)
H_INF_EV = HBAR_EV_S * H_INF_S
RHO_CRIT_KG_M3 = 3.0 * H0_S**2 / (8.0 * math.pi * G_SI)
U_LAMBDA_SI = OMEGA_L * RHO_CRIT_KG_M3 * C**2
# u_SI = (E_eV * EV_J)^4 / (HBAR*C)^3
E_STAR_EV = (U_LAMBDA_SI * (HBAR*C)**3)**0.25 / EV_J

A = 0.180
EPS = 0.001
Y_BARRIER = math.sqrt((1.0 - math.sqrt(1.0-4.0*A))/2.0)
Y_TRUE = math.sqrt((1.0 + math.sqrt(1.0-4.0*A))/2.0)


def w(y: float, a: float=A) -> float:
    return a*y*y/2.0 - y**4/4.0 + y**6/6.0


DELTA_W = -w(Y_TRUE)
BARRIER_W = w(Y_BARRIER)
SIGMA_COEFF = 9.0 / (64.0*math.sqrt(3.0))
B_COEFF = 27.0*math.pi**2*SIGMA_COEFF**4 / (2.0*DELTA_W**3)
# Reverse-engineer f from a target dimensionless nucleation rate: NOT a prediction.
B_TARGET = 4.0*math.log(E_STAR_EV/H_INF_EV) - math.log(EPS)
F_EV = E_STAR_EV * (B_TARGET/B_COEFF)**0.25
M_CHI_EV = math.sqrt(A)*E_STAR_EV**2 / F_EV
MASS_H_RATIO = M_CHI_EV/H_INF_EV

SIGMA_EV3 = SIGMA_COEFF * F_EV * E_STAR_EV**2
DU_EV4 = DELTA_W * E_STAR_EV**4
R_NUC_M = (3.0*SIGMA_EV3/DU_EV4)*HBAR_C_EV_M

RHO_TO_EST4 = OMEGA_M/OMEGA_L
DELTA_A_TEST = 0.01
M_TEST_EV = F_EV*math.sqrt(RHO_TO_EST4/DELTA_A_TEST)
BETA_TEST = MPL_REDUCED_EV * (F_EV*Y_TRUE) / (M_TEST_EV**2)
DELTA_A_PLANCK = RHO_TO_EST4*(F_EV/MPL_REDUCED_EV)**2


def photon_temperature_k(energy_fraction: float=1.0) -> float:
    """Max equilibrium g*=2 photon temperature of supplied uLambda fraction."""
    return (30.0*energy_fraction/(math.pi**2*2.0))**0.25*E_STAR_EV/K_B_EV_K


T_LAMBDA_K = photon_temperature_k()
T_DU_K = photon_temperature_k(DELTA_W)
T_BBN_EV = 5.96e6
GSTAR_BBN = 10.75
BBN_ENERGY_RATIO = (math.pi**2/30.0)*GSTAR_BBN*(T_BBN_EV/E_STAR_EV)**4
TAU_YR = 3.0 / (4.0*math.pi*EPS*H_INF_S) / (365.25*24.0*3600.0)
P_100_TRILLION_YR = math.exp(-100e12/TAU_YR)
T_GH_K = HBAR*H_INF_S/(2.0*math.pi*K_B_SI)
E_LANDAUER_J = K_B_SI*T_GH_K*math.log(2.0)

PROJECTILE_KG = 1e-3
SPEED_C = 0.1
GAMMA = 1.0/math.sqrt(1.0-SPEED_C**2)
PROJECTILE_J = (GAMMA-1.0)*PROJECTILE_KG*C**2
PROJECTILE_TNT_T = PROJECTILE_J/(4.184e9)
CLASSICAL_J = 0.5*PROJECTILE_KG*(SPEED_C*C)**2


def close(actual: float, expected: float, tolerance: float=0.02) -> bool:
    return abs(actual-expected) <= tolerance*abs(expected)


assert close(Y_BARRIER, 0.48520600665, 1e-8)
assert close(Y_TRUE, 0.87439986911, 1e-8)
assert close(DELTA_W, 0.002840086392, 1e-8)
assert close(B_COEFF, 252724.00372, 1e-8)
assert close(E_STAR_EV, 0.0022403653, 0.002)
assert close(B_TARGET, 285.75, 0.001)
assert close(F_EV, 0.00041082, 0.002)
assert close(M_CHI_EV, 0.0051835, 0.003)
assert close(MASS_H_RATIO, 4.35e30, 0.01)
assert close(R_NUC_M, 0.00138514, 0.005)
assert close(M_TEST_EV, 0.00279, 0.01)
assert close(BETA_TEST, 1.13e29, 0.01)
assert close(DELTA_A_PLANCK, 1.31e-62, 0.02)
assert close(T_LAMBDA_K, 28.87, 0.002)
assert close(T_DU_K, 6.66, 0.005)
assert close(BBN_ENERGY_RATIO, 1.771e38, 0.005)
assert close(T_GH_K, 2.20e-30, 0.005)
assert close(PROJECTILE_TNT_T, 108.2, 0.005)

if __name__ == "__main__":
    print("GHRT-VPT exploratory benchmark — not empirical validation")
    for label, number in (
        ("H0 [s^-1]", H0_S),
        ("H_infinity [s^-1]", H_INF_S),
        ("uLambda [J/m^3]", U_LAMBDA_SI),
        ("E_star [eV]", E_STAR_EV),
        ("y_barrier", Y_BARRIER),
        ("y_true", Y_TRUE),
        ("W(barrier)", BARRIER_W),
        ("Delta W", DELTA_W),
        ("B coefficient", B_COEFF),
        ("B target (chosen epsilon)", B_TARGET),
        ("f [eV]", F_EV),
        ("m_chi [eV]", M_CHI_EV),
        ("m_chi/(hbar H)", MASS_H_RATIO),
        ("R_nucleation_flat [m]", R_NUC_M),
        ("M test [eV]", M_TEST_EV),
        ("beta test", BETA_TEST),
        ("Delta a for M_Pl", DELTA_A_PLANCK),
        ("T all Lambda [K]", T_LAMBDA_K),
        ("T Delta U [K]", T_DU_K),
        ("BBN energy ratio", BBN_ENERGY_RATIO),
        ("mean worldline lifetime [yr]", TAU_YR),
        ("P worldline after 10^14 yr", P_100_TRILLION_YR),
        ("T Gibbons-Hawking [K]", T_GH_K),
        ("E Landauer [J/bit]", E_LANDAUER_J),
        ("0.1c 1g impact [t TNT]", PROJECTILE_TNT_T),
        ("classical impact [J]", CLASSICAL_J),
    ):
        print(f"{label:38s} {number:.9e}")
    print("Arithmetic assertions passed. These are model-dependent toy values.")
