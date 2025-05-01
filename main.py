from vehicle import Bus, Passenger

def square(x):
    """ receives a number and return its square.
    If the input is not a number, return -1
    """
    if not isinstance(x, (int,float)):
        raise TypeError(f'The input is invalid: {x}, type={type(x)}')
    return x ** 2

def triple(x):
    """ receives a number and return its square.
    If the input is not a number, return 'input should be a number'
    """
    if not isinstance(x, (int,float)):
        return 'input should be a number'
    return x * 3

if __name__ == '__main__':
    a_number = input('enter a number to be squared:')
    print(a_number)
    squared_number = square(a_number)
    print(squared_number)
    try:
        odd_numbers = [1,3,5,7,9]
        # print(odd_numbers[3] + 'abc')
        print(odd_numbers[6])
    except TypeError as e:
        print('Type error happened.')
        print(e)
    except Exception as e:
        print('Something wrong happened.')
        print(e)
    print('Program continues.')

bus1 = Bus('272', 20, is_card_only=True)
yj = Passenger(is_cash_only=True)
yj.get_on(bus1)