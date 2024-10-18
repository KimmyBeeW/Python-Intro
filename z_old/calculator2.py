from pair import *
from operator import add, sub, mul, truediv, pow, floordiv
from math import sqrt


def tokenize(expression):
    """ Takes a string and returns a list where each item
    in the list is a parenthesis, one of the four operators (/, *, -, +),
    or a number literal. """
    return expression.strip().replace('(', '( ').replace(')', ' )').split()


def parse_tokens(tokens, index):
    """ Takes a list of tokens and an index and converts the tokens to a Pair list
    """
    token = tokens[index]
    if token == '(':
        operator = tokens[index + 1]
        if index != 0:
            pair_list, new_index = parse_tokens(tokens, index + 2)
            operator = Pair(operator, pair_list)
            index = new_index
        elif index == 0:
            index += 2
        pair_list, new_index = parse_tokens(tokens, index)
        return Pair(operator, pair_list), new_index
    elif token == ')':
        return nil, index + 1
    else:
        try:
            if '.' in token:
                operand = float(token)
            else:
                operand = int(token)
            pair_list, index = parse_tokens(tokens, index + 1)
            return Pair(operand, pair_list), index
        except (ValueError, TypeError):
            raise TypeError  # "Operand must be an integer or a float"


def parse(tokens):
    paired, index = parse_tokens(tokens, 0)
    return paired


def main_loop():
    """
    The main loop of your program should do the following:
    1. Print a prompt. The cursor should remain on the line with the prompt after printing.
        For this project your prompt should be calc >> .
    2. Read input from the user. The program should read the entire line as a single string to be parsed.
    3. If the supplied string is the word exit, the program should stop.
    4. Parse the supplied string and validate that it is a valid expression.
    5. If not, print an error and return to step 1.
    6. Evaluate the valid expression to get the result
    7. Print the result
    8. Return to step 1
    """
    # print('Enter valid expression or "exit" to exit.')
    while True:
        exp = input("calc >> ")
        if exp == 'exit':
            break
        else:
            tokens1 = tokenize(exp)
            try:
                pair_obj = parse(tokens1)
                result = eval(pair_obj)
                print(result)
            except TypeError:
                print("Error: invalid expression.")


def reduce(func, operands, initial):
    """
    traverse the pair list, applying the function to all the values in the pair list
    starting with the initial value. For the first value in the operands list, call
    the function with the initial value and the list value and capture the return value.
    For all later list elements, apply the function to the current list element and the
    result from the previous step. Once all elements have been processed, return the final result.
    >>> reduce(add, Pair(3, Pair(4, Pair(5, nil))), 0)
    12
    >>> reduce(truediv, Pair(12, Pair(4, nil)), 144)
    3.0
    >>> reduce(sub, Pair(12, Pair(4, nil)), 2*12)
    8
    >>> reduce(mul, Pair(12, Pair(4, nil)), 1)
    48
    """
    if operands != nil:
        result = func(initial, operands.first)
        if operands.rest is not nil:
            result = reduce(func, operands.rest, result)
        return result
    else:
        return initial


def apply(operator, operands):
    """
    adding functionality:
        // - integer division
        % - the modulus operator
        sqrt - the square root operator
        pow - the exponent operator
    >>> apply("+", Pair(3, Pair(4, Pair(5, nil))))
    12
    >>> apply("-", Pair(12, Pair(4, nil)))
    8
    >>> apply("*", Pair(12, Pair(4, nil)))
    48
    >>> apply("/", Pair(12, Pair(4, nil)))
    3.0
    >>> apply("//", Pair(12, Pair(4, nil)))
    3
    >>> apply("%", Pair(13, Pair(4, nil)))
    1
    >>> apply("sqrt", Pair(16, Pair(4, nil)))
    6.0
    >>> apply("pow", Pair(12, Pair(4, nil)))
    20736
    """
    if operator == "+":
        return reduce(add, operands, 0)
    elif operator == "-":
        return reduce(sub, operands.rest, operands.first)
    elif operator == "*":
        return reduce(mul, operands, 1)
    elif operator == "/":
        return reduce(truediv, operands.rest, operands.first)
    elif operator == "//":
        return reduce(floordiv, operands.rest, operands.first)
    elif operator == "%":
        modulo = lambda a, b: a % b
        return reduce(modulo, operands.rest, operands.first)
    elif operator == "sqrt":
        sq_rt = lambda a, b: sqrt(a) + sqrt(b)
        return reduce(sq_rt, operands.rest, operands.first)
    elif operator == "pow":
        return reduce(pow, operands.rest, operands.first)
    else:
        raise TypeError


def eval(syntax_tree):
    """calculates a paired list of expressions
    >>> eval(Pair('*', Pair(Pair('-', Pair(8, Pair(4, nil))), Pair(4, nil))))
    16
    """
    if isinstance(syntax_tree, float) or isinstance(syntax_tree, int):
        return syntax_tree
    elif isinstance(syntax_tree, Pair):
        if isinstance(syntax_tree.first, Pair):
            frst = eval(syntax_tree.first)
            rst = eval(syntax_tree.rest.map(eval))
            return Pair(frst, rst)
        elif syntax_tree.first in ["+", "-", "/", "*"]:
            operands = syntax_tree.rest.map(eval)
            return apply(syntax_tree.first, operands)
    else:
        raise TypeError


if __name__ == "__main__":
    print("Welcome to the CS 111 Calculator Interpreter: Going Further.")
    main_loop()
    print("Goodbye!")
