import random

# MFT memory management technique
def mft():
    mem = ['0'] * 200 + ['1'] * 200 + ['2'] * 200 + ['3'] * 200 + ['4'] * 200
    for i in range(0, 1000, 200):
        print(f'{i}-{i+199}\t' + ''.join(mem[i:i+200]))

# MVT memory management technique
def mvt():
    mem = ['0'] * 1000
    for task in range(5):
        size = random.randint(50, 200)
        start = random.randint(0, 1000 - size)
        for i in range(start, start+size):
            mem[i] = str(task)
    for i in range(0, 1000, 100):
        print(f'{i}-{i+99}\t' + ''.join(mem[i:i+100]))

# Test case
print("MFT Memory Management")
mft()
print("\nMVT Memory Management")
mvt()
