import re


def extract_data(input_string):
    # Use regular expressions to find all body blocks
    body_blocks = re.findall(r'body\s*{[^}]*}', input_string)
    output = []
    for block in body_blocks:
        # Extract the desired fields from each block
        name = re.search(r'name\s*:\s*"([^"]*)"', block).group(1)
        mean_radius = re.search(r'mean_radius\s*:\s*"([^"]*)"', block).group(1)
        gravitational_parameter = re.search(r'gravitational_parameter\s*:\s*"([^"]*)"', block).group(1)

        # Check if j2 is present in the block, and set its value to 0 if it is not
        j2_match = re.search(r'j2\s*:\s*([^\s]*)', block)
        if j2_match:
            j2 = j2_match.group(1)
        else:
            j2 = '0'

        # Convert gravitational_parameter from km^3/s^2 to m^3/s^2
        gravitational_parameter = float(gravitational_parameter.split()[0]) * 1e9

        # Convert mean_radius from km to m
        mean_radius = float(mean_radius.split()[0]) * 1e3

        # Format the output string for this body
        output.append(
            f'body\n{{\n    name = {name}\n    Radius = {mean_radius}\n    GravitationalParameter = {gravitational_parameter}\n    J2 = {j2}\n}}')

    # Join all body blocks into a single string
    output_string = '\n\n'.join(output)

    return output_string


# Read the input data from a file named 'input.txt'
with open('sol_gravity_model.proto.txt', 'r') as f:
    input_string = f.read()

output_string = extract_data(input_string)

# Write the output string to a file named 'output.txt'
with open('output.txt', 'w') as f:
    f.write(output_string)
