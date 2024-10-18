from pair import Pair, nil


def tokenize(expression):
    """ Takes a string and returns a list where each item
    in the list is a parenthesis, one of the four operators (/, *, -, +),
    or a number literal. """
    return expression.strip().replace('(', '( ').replace(')', ' )').split()


def parse_tokens(tokens, index):
    """ Takes a list of tokens and an index and converts the tokens to a Pair list

    >>> parse_tokens(['(', '+', '1', '1', ')'], 0)
    (Pair('+', Pair(1, Pair(1, nil))), 5)
    >>> parse_tokens(['(', '*', '(', '-', '8', '4', ')', '4', ')'], 0)
    (Pair('*', Pair(Pair('-', Pair(8, Pair(4, nil))), Pair(4, nil))), 9)
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
            raise TypeError("Operand must be an integer or a float")


if __name__ == "__main__":
    expr = "(* (- 6 8) (/ 18 3) (+ 10 1 2))"
    parsed1, index1 = parse_tokens(tokenize(expr), 0)
    print(parsed1)
