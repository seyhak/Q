import qsharp
from Qrng import SampleQuantumRandomNumberGenerator


def hello_world():
    print(SampleQuantumRandomNumberGenerator.simulate())


for i in range(100):
    hello_world()
