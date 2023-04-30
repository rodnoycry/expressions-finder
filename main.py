import itertools


def get_expressions(expected_result: int, is_single_result: bool = False):
    """
    Function for finding all expression from '0123456789' string with
    pluses, minuses and/or empty strings within, that after evaluating will
    return expected number

    expected_result: int - number that will be result of evaluating of
        expression
    is_single_result: bool - return only first success expression

    Returns list of possible results
    """
    # Get initial data
    number_range = range(0, 10)
    initial_string = ''.join(str(x) for x in number_range)
    initial_string_length = len(initial_string)

    # Generate all possible combinations of plus and minus signs or empty string
    options = list(itertools.product(['+', '-', ''], repeat=initial_string_length - 1))

    # Iterate through all possible expressions and evaluate them
    success_result_list = []
    for option in options:
        expression = ''
        for i, digit in enumerate(initial_string):
            expression += digit
            if i < initial_string_length - 1:
                expression += option[i]
        # Exclude integers started with zero as it will throw Python syntax error
        # and also will not affect results
        if not expression.startswith('01'):
            # Calculate result and if success add expression to the result list
            result = eval(expression)
            if result == expected_result:
                success_result_list.append(expression)
            if is_single_result:
                return success_result_list
    return success_result_list


if __name__ == '__main__':
    result_list = get_expressions(expected_result=200)
    # Check results and print them
    for result_expression in result_list:
        calculated_result = eval(result_expression)
        print(f"{result_expression} = {calculated_result}")
