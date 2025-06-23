import argparse

parser = argparse.ArgumentParser(description="meow like a cat")
parser.add_argument("-n",default=1,type=int, help="Number of time to meow")
args = parser.parse_args()

for _ in range(args.n):
    print("meow")



