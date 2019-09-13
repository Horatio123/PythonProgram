import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='my math script'
    )
    parser.add_argument('-n', '--num1', help="number 1", type=float)
    parser.add_argument('-m', '--num2', help="number 2", type=float)
    parser.add_argument('-o', '--operation', help='operator', default='+')

    args = parser.parse_args()
    print(args)
    result = None
    if args.operation == '-':
        result = args.num1 - args.num2
    elif args.operation == '+':
        result = args.num1 + args.num2
    elif args.operation == '/':
        result = args.num1 / args.num2
    elif args.operation == '*':
        result = args.num1 * args.num2
    elif args.operation == 'pow':
        result = pow(args.num1, args.num2)

    print(result)

# python3 argparseExp.py -n=66 -m=666 -o=+
# python3 argparseExp.py --num1 66 --num2 666 --operation +
# python3 argparseExp.py --num1 66 --num2 666
# python3 argparseExp.py --num1 66 --num2 6 --operation *
