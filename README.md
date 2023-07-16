# SSOCalculator.Stock_RSS_Principia


[English](https://github.com/Aebestach/SSOCalculator.Stock_RSS_Principia/blob/main/README.md) | [简体中文](https://www.bilibili.com/read/cv25055752)
<div align=center> <img src="https://imgur.com/Kp0oF8q.jpg"><p>Initial Page</p></div>


## Introduce

In the Kerbal Space Program, planets are regular spheres. After adding [Principia](https://forum.kerbalspaceprogram.com/topic/162200-wip181-191-1101-1110%E2%80%932-1122%E2%80%935-principia%E2%80%94version-%E4%BC%8A%E8%97%A4-released-2023-06-18%E2%80%94n-body-and-extended-body-gravitation/), planets like Kerbin do not have **sun-synchronous** orbits.<br>And this tool can generate configuration file of Principia, so as to add the second-order spherical harmonic coefficient j2 to the stock planet to help players successfully enter the sun-synchronous orbit of the stock planet. At the same time, this tool also supports the calculation of relevant parameters of the **sun-synchronous** orbit in the RealSolarSystem environment. 


## Dependencies

1. The newly generated `StockPlanet_GravityModels.cfg` file requires support from [Kopernicus](https://github.com/Kopernicus/Kopernicus).
2. If you want to enter a sun-synchronous orbit, you **must** have the support of [Principia](https://forum.kerbalspaceprogram.com/topic/162200-wip181-191-1101-1110%E2%80%932-1122%E2%80%935-principia%E2%80%94version-%E4%BC%8A%E8%97%A4-released-2023-06-18%E2%80%94n-body-and-extended-body-gravitation/).


## Tutorial

1. Open `SSOCalculator.exe`
2. Choose the language option you need. (Tips: can only be selected once)
3. First select the `System`, then select the corresponding `Planet`.
	* If you choose **RealSolarSystem**, then you only need to enter the `Altitude(m)` (excluding the planet radius) and `Eccentricity`, and click **Calculate** to get the **Satellite Orbital Parameters** want. (`SMA` = Semi-major Axis)<div align=center><img src="https://imgur.com/FGgMNT3.jpg"><p>Example of Earth’s sun-synchronous orbit</p></div>

	* If you choose **Stock**, then you need to enter the `Altitude(m)` (excluding the planet radius) and `Eccentricity`, and `j2`. <br>***( Note: The j2 term can refer to the j2 parameter of a planet similar to your choice in [sol_gravity_model.proto.txt](https://github.com/mockingbirdnest/Principia/blob/2018011702-Clifford/astronomy/sol_gravity_model.proto.txt).)***<br>After clicking **Calculate**, you will get the **Satellite Orbital Parameters** want. (`SMA` = Semi-major Axis)<div align=center><img src="https://imgur.com/kKa4iAS.jpg"><p>Example of Earth’s sun-synchronous orbit</p></div>

4. In the **Stock** environment, once the orbit parameters are correctly generated, you will find that the **Generate Configuration File** button is enabled. Next, you only need to click it to generate the `StockPlanet_GravityModels.cfg` file. Then put it anywhere in **GameData**.<br>***(Note:The generated file is in the current directory.)***
<div align=center><img src="https://imgur.com/1A2FlWn.jpg"><p>Configuration generation successful case</p></div>
<div align=center><img src="https://imgur.com/4LWTmG9.jpg"><p>GameData content</p></div>

5. The **Clear** button is for one-click clearing of the `Altitude(m)`, `Eccentricity`, and `j2` parameters.


## To-Do List

1. Some planets `SiderealOrbitalPeriod` in `PlanetData\RSSPlanetData.cfg` are incomplete and need to be fixed.
2. Considering adding a button, the purpose of this button is to append the content of the generated configuration. (To be determined)


## Warning
1. This tool does not take into account whether the orbit composed of the altitude and eccentricity you entered is below a safe value, and you need to verify it in the game.


## Credits
[@SirMortimer](https://github.com/SirMortimer)      Kopernicus configuration file.
<br>[@Nazfib](https://github.com/Nazfib)      Code help for calculating sun-synchronous orbit inclination and other formulas.
<br>[@Charon_S丶](https://space.bilibili.com/347787037/?spm_id_from=333.999.0.0)      KSP players have provided help for adding second-order spherical harmonic coefficient terms.
<br>[@PrincipiaTeam](https://github.com/mockingbirdnest/Principia)      Provide file support for planetary data in the RSS environment.
<br>NewBing     The planetary rotation period under RSS is provided.
