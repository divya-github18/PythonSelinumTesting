import pytest


# A simple addition function that adds/concatenates two input values
def add_operation(input_1, input_2):
    return input_1 + input_2


# We make use of the parametrize decorator to supply input arguments
# to the test function

@pytest.mark.parametrize('inp_1, inp_2,result',
                         [
                             (9, 6, 15),
                             ('Cross browser testing on ', 'LambdaTest', 'Cross browser testing on LambdaTest'),
                             ('pytest', 'framework', 'pytest framework1')
                         ]
                         )
def test_add_integers_strings(inp_1, inp_2, result):
    result_1 = add_operation(inp_1, inp_2)
    assert result_1 == result


# Enable the stack trace for debugging the issue
@pytest.mark.parametrize('inp_1, inp_2,result',
                         [
                             (9, 6, 15),
                             ('Cross browser testing on ', 'LambdaTest', 'Cross browser testing on LambdaTest1')
                         ]
                         )
def test_add_integers_strings_fail_case(inp_1, inp_2, result):
    result_1 = add_operation(inp_1, inp_2)
    if result_1 != result:
        pytest.fail("Test failed", True)