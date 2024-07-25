import numpy as np
import ReadFile
import math

#Thanks @Nazfib for the formula and source code support!
def calculate_sun_sync_orbit(galaxy, planet, alt, ecc, j2):
    alt = float(alt)
    ecc = float(ecc)

    (R_E, μ, T_year, J2), planet = ReadFile.ReadPlanetData(galaxy, planet)
    if galaxy == 'Stock':
        J2 = float(j2)
    R_E = float(R_E)
    μ = float(μ)
    T_year = float(T_year)
    J2 = float(J2)

    ρ = 2 * np.pi / T_year
    SMA = alt + R_E
    p = SMA * (1 - ecc * ecc)
    period = 2 * np.pi * np.sqrt(SMA * SMA * SMA / μ)
    ΔΩ = period * ρ
    cosi = (ΔΩ * p * p) / (-3 * np.pi * J2 * R_E * R_E)
    inc = np.arccos(cosi)

    if galaxy == 'Stock':
        C20 = -1 * (J2 * math.sqrt(5)) / 5
        return (planet, ('%.4f' % np.rad2deg(inc)) , ('%.2f' % SMA), ecc, ('%.17e' % C20))
    else:
        return planet, ('%.4f' % np.rad2deg(inc)), ('%.2f' % SMA), ecc
