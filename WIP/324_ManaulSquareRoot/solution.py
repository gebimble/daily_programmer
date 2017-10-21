#! /usr/bin/env python


import os


def massage(number):
    '''Takes a number given in the main program, and does a little this-n-that
    in order to get the total number of digits equal to an even number.

    Arguments:
        number - a number (in any format?)

    Returns:
        number - the original value provided, but with a trailing or leading 0
                 if required

    Excepts:
        None'''

    number = str(float(number))

    number_parts = []

    if len(number.replace('.', '')) % 2:

        for i, value in enumerate(number.split('.')):

            if len(value) % 2:
                if i:
                    value = value + '0'
                else:
                    value = '0' + value

            number_parts.append(value)

            if '.' not in number_parts:
                number_parts.append('.')

        number = number_parts

        number = ''.join(number)

    return number


def slicer(number, operating_number, a, b):
    '''Takes the supplied number, turns it into something to operate on, and
    whatever is left.

    Arguments:
        number - the number string to slice up
        a - the current value of the solution

    Returns:
        operating_number - the leading 2 digits (the stuff that the square
                           rooting is going to work on
        number - the bits of the number that are left
        decimal_flag - something that tells us if we've ran up against a
                       decimal yet

    Excepts:
        None'''

    if a:
        if b:
            operating_number = str(float(operating_number)
                                   - (((20 * a) + b) * b)) + number[:2]
        else:
            operating_number = str(float(operating_number) - ((a ** 2)))
                                                           + number[:2]
    else:
        operating_number = number[:2]

    if '.' in number[2:4]:
        decimal_flag = True
        number = number.replace('.', '')
    else:
        decimal_flag = False
        
    number = number[2:] + '00'

    return operating_number, number, decimal_flag


def manual_sqrt(precision, number):
    '''Take the provided number, and returns the square root of it to the given
    number of decimal places.

    Arguments:
        precision - the number of decimal places that the answer should return.
        number - the number to find the square root of

    Returns:
        solution - the answer!

    Excepts:
        None'''

    # massage the number into the right format

    massaged_number = massage(number)

    # do the maths

    a = 0
    b = 0

    operating_number = 0

    decimal_flag = False

    operating_number, massaged_number, decimal_flag = slicer(massaged_number,
                                                             operating_number,
                                                             a, b)

    if not a:
        for a in range(9, -1, -1):
            if (a ** 2) > float(operating_number):
                pass
            else:
                break

    solution = str(a)

    while True:

        if (a ** 2) == float(number):
            return solution + '.' + (int(precision) * '0')

        if decimal_flag and '.' not in solution:
            solution = solution + '.'

        if '.' in solution:

            if solution.split('.')[1] == '' and int(precision) == 0:
                solution = solution.replace('.', '')
                return solution
                break

            elif len(solution.split('.')[1]) == int(precision):
                return solution
                break

        operating_number, massaged_number, decimal_flag = slicer(massaged_number,
                                                                 operating_number,
                                                                 a, b)

        a = int(solution.replace('.',''))

        for b in range(9, -1, -1):

            if (((20 * a) + b) * b) > float(operating_number):
                pass
            else:
                break

        solution = solution + str(b)

_, precision, number = os.sys.argv

solution = manual_sqrt(precision, number)

print(solution)
