import argparse

def sum_numbers(a: int , b: int) -> int:
    return a + b

### Command-line positional arguments. ###
# '''
def main():
    parser = argparse.ArgumentParser(description='Description: Sum two numbers')
    parser.add_argument('num1', type=int, help='First number')

    # `nargs='?'` argument allows the 'num2' argument to be optional.
    parser.add_argument('num2', type=int, nargs='?', default=0, help='Second number (default: 0)')
    args = parser.parse_args()

    result = sum_numbers(args.num1, args.num2)
    print(f"The sum of {args.num1} and {args.num2} is {result}")
# '''
## In Terminal: $ python sum.py 5
##              $ python sum.py 5 4

### Command-line options ###
'''
def main():
    parser = argparse.ArgumentParser(description='Description: Sum two numbers')
    parser.add_argument('--num1', type=int, required=True, help='First number')
    parser.add_argument('--num2', type=int, default=0, help='Second number (default: 0)')
    args = parser.parse_args()

    result = args.num1 + args.num2
    print(f"The sum of {args.num1} and {args.num2} is {result}")
'''

## In terminal: $ python sum.py --num1 5 --num2 10
##              $ python sum.py --num1 3

### Another option ###


'''
def main():
    parser = argparse.ArgumentParser(description='Sum two numbers')
    parser.add_argument('-n', '--num1', type=int, required=True, help='First number')
    parser.add_argument('-m', '--num2', type=int, default=0, help='Second number (default: 0)')
    args = parser.parse_args()

    result = args.num1 + args.num2
    print(f"The sum of {args.num1} and {args.num2} is {result}")
'''

### Usage
#   $ python sum.py -n 5 -m 3
#   $ python sum.py -n 3


###### Others
#      $ python sum.py --help
#      $ python sum.py -h

if __name__ == "__main__":
    main()
