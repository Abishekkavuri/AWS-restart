# Define the preproinsulin sequence
preproInsulin = (
    "malwmrllpllallalwgpdpaaafvnqhlcgshlvealylvcgergffytpktr"
    "reaedlqvgqvelgggpgagslqplalegslqkrgiveqcctsicslyqlenycn"
)

# Extract the sequence for chain A of human insulin
# The chain A sequence is a substring of the preproinsulin sequence
# For this example, let's assume chain A corresponds to a certain substring
ainsulin = preproInsulin[24:54]

# Print the sequence of human insulin chain A
print("The sequence of human insulin, chain A: " + ainsulin)

# Amino acid weights
aaWeights = {
    'A': 89.09, 'C': 121.16, 'D': 133.10, 'E': 147.13, 'F': 165.19,
    'G': 75.07, 'H': 155.16, 'I': 131.17, 'K': 146.19, 'L': 131.17,
    'M': 149.21, 'N': 132.12, 'P': 115.13, 'Q': 146.15, 'R': 174.20,
    'S': 105.09, 'T': 119.12, 'V': 117.15, 'W': 204.23, 'Y': 181.19
}

# Count the occurrence of each amino acid in the insulin sequence
aaCountInsulin = {x: float(ainsulin.upper().count(x)) for x in aaWeights.keys()}

# Calculate the molecular weight of insulin
molecularWeightInsulin = sum(aaCountInsulin[x] * aaWeights[x] for x in aaWeights.keys())

# Print the rough molecular weight of insulin
print("The rough molecular weight of insulin: " + str(molecularWeightInsulin))
