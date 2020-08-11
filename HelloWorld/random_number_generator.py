import qsharp
from Qrng import SampleQuantumRandomNumberGenerator # import the quantum operation from the namespace defined in the file Qrng.qs


max = 50
output = max + 1
while output > max:
    bit_string = []  # We initialise a list to store the bits that
    # will define our random integer
    for i in range(0, max.bit_length()):  # We need to call the quantum
        # operation as many times as bits are needed to define the
        # maximum of our range. For example, if max=7 we need 3 bits
        # to generate all the numbers from 0 to 7.
        bit_string.append(SampleQuantumRandomNumberGenerator.simulate()) 
        # Here we call the quantum operation and store the random bit
        # in the list
    output = int("".join(str(x) for x in bit_string), 2)
# Transform bit string to integer

print("The random number generated is " + str(output))
