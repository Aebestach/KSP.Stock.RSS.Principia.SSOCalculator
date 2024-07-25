def ReadPlanetData(galaxy,Planet):
    # 定义变量
    Radius = 0
    GravitationalParameter = 0
    SiderealOrbitalPeriod = 0
    J2 = 0
    if galaxy=='Stock':
        PlanetData = 'PlanetData/StockPlanetData.cfg'
    else:
        PlanetData = 'PlanetData/RSSPlanetData.cfg'

    with open(PlanetData, 'r') as file:
        for line in file:
            if Planet in line:
                planet=Planet
                for line in file:
                    if '{' in line:
                        continue
                    if '}' in line:
                        break

                    key, value = line.split('=')

                    key = key.strip()
                    value = value.strip()
                    if key == 'Radius':
                        Radius = value
                    elif key == 'GravitationalParameter':
                        GravitationalParameter = value
                    elif key == 'SiderealOrbitalPeriod':
                        SiderealOrbitalPeriod = value
                    elif key == 'J2':
                        J2 = value

    return (Radius,GravitationalParameter,SiderealOrbitalPeriod,J2),planet

def ReadPlanetName():

    def read_names_from_file(filename):
        names = []

        with open(filename, 'r') as f:
            in_body = False

            for line in f:
                line = line.strip()
                if line == 'body':
                    in_body = True
                elif line == '}' and in_body:
                    in_body = False
                elif in_body and line.startswith('name'):
                    name = line.split('=')[1].strip()
                    names.append(name)
        return names

    stock_names = read_names_from_file('PlanetData/StockPlanetData.cfg')
    real_solar_system_names = read_names_from_file('PlanetData/RSSPlanetData.cfg')

    choice2Items = {
    'Stock': stock_names,
    'RealSolarSystem': real_solar_system_names}

    return choice2Items

# self.choice2Items = {
#     "Stock": ['Kerbin', 'Eve', 'Moho', 'Duna', 'Jool', 'Dres', 'Eeloo', 'Gilly', 'Mun', 'Minmus', 'Ike', 'Laythe', 'Vall', 'Tylo', 'Bop', 'Pol'],
#     "RealSolarSystem": ['Jupiter', 'Saturn', 'Neptune', 'Uranus', 'Earth', 'Venus', 'Mars', 'Mercury', 'Ganymede', 'Titan', 'Callisto', 'Io', 'Moon', 'Europa', 'Triton', 'Eris', 'Pluto', 'Titania', 'Oberon', 'Rhea', 'Iapetus', 'Charon', 'Umbriel', 'Ariel', 'Dione', 'Ceres', 'Tethys', 'Vesta', 'Enceladus', 'Miranda', 'Mimas', 'Phobos', 'Deimos'],
# }