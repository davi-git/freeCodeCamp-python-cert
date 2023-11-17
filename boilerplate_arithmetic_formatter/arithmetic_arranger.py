'''
INSTRUCTIONS:

Students in primary school often arrange arithmetic problems vertically to make them easier to solve. For example, "235 + 52" becomes:

  235
+  52
-----

Create a function that receives a list of strings that are arithmetic problems and returns the problems arranged vertically and side-by-side.
The function should optionally take a second argument. When the second argument is set to True, the answers should be displayed.

Example

Function Call:
arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])

Output:
   32      3801      45      123
+ 698    -    2    + 43    +  49
-----    ------    ----    -----

Function Call:
arithmetic_arranger(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"], True)

Output:
  32         1      9999      523
+  8    - 3801    + 9999    -  49
----    ------    ------    -----
  40     -3800     19998      474

Rules
The function will return the correct conversion if the supplied problems are properly formatted, otherwise, it will return a string that describes
an error that is meaningful to the user.

Situations that will return an error:
    - If there are too many problems supplied to the function. The limit is five, anything more will return: "Error: Too many problems."
    - The appropriate operators the function will accept are addition and subtraction. Multiplication and division will return an error.
      Other operators not mentioned in this bullet point will not need to be tested. The error returned will be: "Error: Operator must be '+' or '-'."
    - Each number (operand) should only contain digits. Otherwise, the function will return: "Error: Numbers must only contain digits."
    - Each operand (aka number on each side of the operator) has a max of four digits in width. Otherwise, the error string returned will be:
      "Error: Numbers cannot be more than four digits."

If the user supplied the correct format of problems, the conversion you return will follow these rules:
    - There should be a single space between the operator and the longest of the two operands, the operator will be on the same line as the second operand,
      both operands will be in the same order as provided (the first will be the top one and the second will be the bottom).
    - Numbers should be right-aligned.
    - There should be four spaces between each problem.
    - There should be dashes at the bottom of each problem. The dashes should run along the entire length of each problem individually.
      (The example above shows what this should look like.)
'''


def arithmetic_arranger(problems, show_results=False):
    '''
    Description:
        This function receives a list of strings that are arithmetic problems and returns the problems arranged vertically and side-by-side.
    
    Args:
        - problems: a list of strings that are arithmetic problems
        - show_results [optional]: a boolean variable that indicates whether to show the result of arithmetic problems (Default: False)
    
    Returns:
        Returns the problems arranged vertically and side-by-side
    '''

    # Error handler: too many problems when more than 5
    if len(problems) > 5:
        return "Error: Too many problems."

    # There will be 4 rows for each problem
    first_line = ""
    second_line = ""
    third_line = ""
    fourth_line = ""

    # Initialize boolean variable to handle the first problem differently from others
    is_first_problem = True

    # Arrange vertically each problem
    for problem in problems:
        # Split terms from string
        terms = problem.split()
        number1_str = terms[0]
        number2_str = terms[2]
        operator = terms[1]

        # Error handler: only addition and subtraction accepted
        if operator != '+' and operator != '-':
            return "Error: Operator must be '+' or '-'."

        # Error handler: operands should only contain digits
        try:
            number1 = int(number1_str)
            number2 = int(number2_str)
        except:
            return "Error: Numbers must only contain digits."

        # Calculate the max length of the operands
        number1_len = len(number1_str)
        number2_len = len(number2_str)
        max_length = max(number1_len, number2_len)

        # Error handler: operands overcome limit of 4 digits
        if max_length > 4:
            return "Error: Numbers cannot be more than four digits."

        # Create a string of blanks to write in the first row considering the max length of the operands and the first operand length
        spaces_to_add_1st_line = max_length - number1_len + 2
        first_line_spaces = ''
        for i in range(spaces_to_add_1st_line):
            first_line_spaces = first_line_spaces + ' '

        # Write first row depending on whether it is the first problem or not:
        # - for the first problem append the first operand to the string of blanks
        if is_first_problem:
            first_line = first_line_spaces + number1_str
        # - for the subsequent problems add 4 more blank spaces before the first operand to distance problems from each other
        else:
            first_line = first_line + "    " + first_line_spaces + number1_str

        # Create a string of blanks to write in the second row considering the max length of the operands and the second operand length
        spaces_to_add_2nd_line = max_length - number2_len
        second_line_spaces = ''
        for i in range(spaces_to_add_2nd_line):
            second_line_spaces = second_line_spaces + ' '

        # Write second row depending on whether it is the first problem or not:
        # - for the first problem write the operator and add a blank space to the string of blanks and then append the second operand
        if is_first_problem:
            second_line = operator + " " + second_line_spaces + number2_str
        # - for the subsequent problems add 4 more blank spaces (to distance problems from each other) and the operator before the string of blanks,
        #   then append the second operand
        else:
            second_line = second_line + "    " + operator + " " + second_line_spaces + number2_str

        # Write third row depending on whether it is the first problem or not:
        # - for problems subsequent to the first, write 4 blank spaces to distance problems from each other
        if not is_first_problem:
            third_line = third_line + "    "
        # - for every problem, draw a line (-----) considering the max length of the operands
        for i in range(max_length + 2):
            third_line = third_line + "-"

        # If 'show_results' argument is True, calculate and return operation result (fourth row)
        if show_results:
            # Calculate result and convert it to string
            if operator == '+':
                result = number1 + number2
            else:
                result = number1 - number2
            result_str = str(result)
            result_len = len(result_str)

            # Create a string of blanks to write in the fourth row considering the max length of the operands and the result length
            spaces_to_add_4th_line = max_length + 2 - result_len
            fourth_line_spaces = ''
            for i in range(spaces_to_add_4th_line):
                fourth_line_spaces = fourth_line_spaces + ' '

            # Write fourth row depending on whether it is the first problem or not:
            # - for the first problem append the result to the string of blanks
            if is_first_problem:
                fourth_line = fourth_line_spaces + result_str
            # - for the subsequent problems add 4 more blank spaces before the result to distance problems from each other
            else:
                fourth_line = fourth_line + "    " + fourth_line_spaces + result_str

        is_first_problem = False

    # Set the final string:
    # - with results
    if show_results:
        arranged_problems = first_line + "\n" + second_line + "\n" + third_line + "\n" + fourth_line
    # - without results
    else:
        arranged_problems = first_line + "\n" + second_line + "\n" + third_line
    
    # Return final string
    return arranged_problems
