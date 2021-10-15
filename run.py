## Run tests

from main import *

tests = [(500,0.1), (500, 0.01), (500, 0.001), (1000, 0.0001),(2500, 0.25), (2500, 0.1), (2500, 0.01), (10000, 0.01),(10000,0.001)]

for n, test in enumerate(tests):
    print("_"*50)
    print(f"Test {n+1} of {len(tests)}\n")
    print(f"Number of points: {test[0]}")
    print(f"Collision radius: {test[1]}")
    print("\n")
    
    if (test[0] > 2500) : print("WARNING: This test will take a long time to run. Please be patient\n")

    try:
        result, extraData = runTest(*test)
        print(f"Success! Speed-up: {result:.2f}x")
        print(extraData)
    
    except RadiusTooBig as e:
        print(e)
    except RadiusTooSmall as e:
        print(e)
    except LogicError as e:
        print(e)

    print("_"*50)
    print("\n")
