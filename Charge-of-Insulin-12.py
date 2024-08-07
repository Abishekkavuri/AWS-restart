# Python3.6
# Coding: utf-8

# Store the human preproinsulin sequence in a variable called preproinsulin:
preproInsulin = "malwmrllpllallalwgpdpaaafvnqhlcgshlvealylvcgergffytpktrreaedlqvgqvelgggpgagslqplalegslqkrgiveqcctsicslyqlenycn"

# Store the remaining sequence elements of human insulin in variables:
lsInsulin = "malwmrllpllallalwgpdpaaa"
bInsulin = "fvnqhlcgshlvealylvcgergffytpkt"
aInsulin = "giveqcctsicslyqlenycn"
cInsulin = "rreaedlqvgqvelgggpgagslqplalegslqkr"
insulin = bInsulin + aInsulin

# Define the pKR values for specific amino acids
pKR = {'y': 10.07, 'c': 8.18, 'k': 10.53, 'h': 6.00, 'r': 12.48, 'd': 3.65, 'e': 4.25}

# Print the preproinsulin sequence
print("Preproinsulin sequence: " + preproInsulin)

# Print the sequence of human insulin chain A
print("The sequence of human insulin, chain A: " + aInsulin)

# Function to calculate the net charge of the insulin sequence at a given pH
def calculate_net_charge(sequence, pH):
    # Count the occurrence of each amino acid that affects charge
    seqCount = {x: sequence.count(x) for x in pKR.keys()}

    # Calculate the positive charge contribution
    positive_charge = sum((seqCount[x] * (10 ** pKR[x]) / ((10 ** pH) + (10 ** pKR[x]))) for x in ['k', 'h', 'r'])

    # Calculate the negative charge contribution
    negative_charge = sum((seqCount[x] * (10 ** pH) / ((10 ** pH) + (10 ** pKR[x]))) for x in ['y', 'c', 'd', 'e'])

    # Calculate the net charge
    netCharge = positive_charge - negative_charge
    return netCharge

# Define the pH value for calculation
pH = 7.4

# Calculate the net charge of the insulin sequence at the specified pH
netCharge = calculate_net_charge(insulin, pH)

# Print the net charge
print("The net charge of insulin at pH {:.1f}: {:.2f}".format(pH, netCharge))
