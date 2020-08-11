import argparse

from HelloWorld.host import hello_world


OPERATIONS = {
    'hello_world': hello_world
}

if __name__ == "__main__":
    # add operation name command
    print(123)
    parser = argparse.ArgumentParser(description='Run various operations')
    parser.add_argument(
        'operation_name', metavar='Operation name', type=str,
        help='Available operations: \n{}'.format(', '.join(OPERATIONS.keys()))
    )
    args = parser.parse_args()
    operation_name = args.operation_name
    if operation_name in OPERATIONS.keys():
        print(f'Running {args.operation_name}')
        OPERATIONS[operation_name]()
    else:
        print('Operation not found')
