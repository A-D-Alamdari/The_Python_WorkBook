"""
Exercise 124: Evaluate Postfix

    Evaluating a postfix expression is easier than evaluating an infix expression because it
    does not contain any brackets and there are no operator precedence rules to consider.
    A postfix expression can be evaluated using the following algorithm:

        Create a new empty list, values

        For each token in the postfix expression
            If the token is a number then
                Convert it to an integer and add it to the end of values
            Else
                Remove an item from the end of values and call it right
                Remove an item from the end of values and call it left
                Apply the operator to left and right
                Append the result to the end of values
        Return the first item in values as the value of the expression

    Write a program that reads a mathematical expression in infix form from the user,
    evaluates it, and displays its value. Uses your solutions to Exercises 122 and 123
    along with the algorithm shown above to solve this problem.
"""


def tokenize(expression):
    tokens = []
    current_token = ''

    for char in expression:
        if char.isspace():
            continue

        if char.isdigit() or (char == '-' and not current_token) or (char == '+' and not current_token):
            current_token += char
        else:
            if current_token:
                tokens.append(current_token)
                current_token = ''

            if char != ' ':
                tokens.append(char)

    if current_token:
        tokens.append(current_token)

    return tokens


def infix_to_postfix(infix_tokens):
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
    operators = []
    postfix = []

    for token in infix_tokens:
        if token.isdigit():
            postfix.append(token)
        elif token in precedence:
            while operators and operators[-1] != '(' and precedence[token] <= precedence[operators[-1]]:
                postfix.append(operators.pop())
            operators.append(token)
        elif token == '(':
            operators.append(token)
        elif token == ')':
            while operators and operators[-1] != '(':
                postfix.append(operators.pop())
            if operators and operators[-1] == '(':
                operators.pop()

    while operators:
        postfix.append(operators.pop())

    return postfix


def evaluate_postfix(postfix_tokens):
    values = []

    for token in postfix_tokens:
        if token.isdigit():
            values.append(int(token))
        else:
            right = values.pop()
            left = values.pop()

            if token == '+':
                result = left + right
            elif token == '-':
                result = left - right
            elif token == '*':
                result = left * right
            elif token == '/':
                result = left / right
            elif token == '^':
                result = left ** right

            values.append(result)

    return values[0]


def main():
    expression = input("Enter a mathematical expression in infix form: ")

    infix_tokens = tokenize(expression)
    postfix_tokens = infix_to_postfix(infix_tokens)

    value = evaluate_postfix(postfix_tokens)

    print("Value:", value)


if __name__ == '__main__':
    main()
