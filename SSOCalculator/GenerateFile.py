import math

def ReadPlanetName(Planet,J2):

    name = Planet
    reference_radius = 0
    J2=float(J2)
    C20 = -1 * (J2 * math.sqrt(5)) / 5

    with open('PlanetData/StockPlanetData.cfg', 'r') as file:
        for line in file:
            if Planet in line:
                for line in file:
                    if '{' in line:
                        continue
                    if '}' in line:
                        break
                    key, value = line.split('=')

                    key = key.strip()
                    value = value.strip()
                    if key == 'Radius':
                        reference_radius = value

        GeneratePrincipiaGM(name, reference_radius, C20)


def GeneratePrincipiaGM(name,reference_radius,C20):

    #Thanks to GitHub user @KspTweaks for this code!
    KopernicusConfig = """@Kopernicus {
  @Body[Vall] {
    @Orbit {
      semiMajorAxis = 49700595.866835564
    }
  }
  @Body[Tylo] {
    @Orbit {
      semiMajorAxis = 90867761.53320013
    }
  }
  @Body[Bop] {
    @Orbit {
      inclination = 165
      semiMajorAxis = 141820511.8491002
    }
  }
}"""


    with open('StockPlanet_GravityModels.cfg', 'w') as file:
        file.write('principia_gravity_model {\n')
        file.write('  body {\n')
        file.write('    name                    = ' + name + '\n')
        file.write('    reference_radius        = ' + str(float(reference_radius)/1e3) + ' km\n')
        file.write('\n')
        file.write('    geopotential_row {\n')
        file.write('      degree = 2\n')
        file.write('      geopotential_column {\n')
        file.write('        order = 0\n')
        file.write('        cos   = %.17e\n' % C20)
        file.write('        sin   = 0.00000000000000000e+00\n')
        file.write('      }\n')
        file.write('    }\n')
        file.write('  }\n')
        file.write('}\n')
        file.write(KopernicusConfig)