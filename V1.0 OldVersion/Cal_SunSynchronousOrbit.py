import numpy as np
import math

# Earth Data
# R_E = 6371e3
# μ = 3.9860043543609598e14
# J2 = 1.08263e-3
# ρ = 1.990_968_71e-7


# Kerbin Data
R_E = 600e3
μ = 3.5316000e12
T_year = 9_203_545
ρ = 2 * np.pi / T_year

# Data that can be modified(default)
J2 = 0.002
alt = 200e3
ecc = 0

print('————————请输入以下数据————————')
J2 = input('J2摄动值: ')
alt = input('卫星轨道高度(m): ')
ecc = input('卫星偏心率: ')

J2 = float(J2)
alt = float(alt)
ecc = float(ecc)

SMA = alt + R_E
p = SMA * (1 - ecc * ecc)
period = 2 * np.pi * np.sqrt(SMA * SMA * SMA / μ)
ΔΩ = period * ρ
cosi = (ΔΩ * p * p) / (-3 * np.pi * J2 * R_E * R_E)
inc = np.arccos(cosi)


print('\n\n—————————卫星轨道参数—————————')
print('轨道高度:'.ljust(5), '%.2f' % alt, 'm')
print('半长轴: '.ljust(6), '%.2f' % SMA, 'm')
print('倾角: '.ljust(7), '%.4f' % np.rad2deg(inc),'°')
print('偏心率: '.ljust(6), ecc)

print('\n\n——————Principia引力模型配置参数——————')
C20 = -1 * (J2 * math.sqrt(5)) / 5
print('二阶球谐项系数C(2,0): %.17e' % C20)
input("\n\n程序运行结束，可以按任意键退出！")
