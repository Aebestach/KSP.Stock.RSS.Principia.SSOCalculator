# with open('output.txt', 'r') as f:
#     lines = f.readlines()
#
# with open('output1.txt', 'w') as f:
#     for line in lines:
#         f.write(line)
#         if 'GravitationalParameter' in line:
#             f.write('    SiderealOrbitalPeriod = \n')


# names = []
# with open('output.txt', 'r') as f:
#     lines = f.readlines()
#     for line in lines:
#         if 'name' in line:
#             name = line.split('=')[1].strip()
#             names.append(name)
#
# with open('output2.txt', 'w') as f:
#     for name in names:
#         f.write(name + '\n')


# with open('RSSPlanetData.cfg', 'r') as f:
#     data = f.read()
#     blocks = data.split('body')
#     names = []
#     for block in blocks:
#         lines = block.split('\n')
#         for line in lines:
#             if 'name' in line:
#                 name = line.split('=')[1].strip()
#                 names.append(name)
#     print(names)


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
    'RealSolarSystem': real_solar_system_names
}

