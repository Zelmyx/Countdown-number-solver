
def solve(numbers, target):
    recursive_permutations(numbers, target, [])
    correct_expressions(valid_expression_list)
    print(valid_expression_list[6])


def recursive_permutations(numbers, target, expression):
    for i in range(len(numbers)):
        expression.append(numbers.pop(i))

        if calculate(expression) == target:
            valid_expression_list.append(expression[:])

        if len(numbers) == 0:
            break

        for i in range(4):
            if i == 0:
                expression.append("*")
            elif i == 1:
                expression.append("+")
            elif i == 2:
                expression.append("/")
            elif i == 3:
                expression.append("-")
            recursive_permutations(numbers, target, expression)

        numbers.insert(0, expression.pop())
    if len(expression) % 2 == 1:
        numbers.insert(0, expression.pop())
    if len(expression) != 0:
        expression.pop()
    return


def operators(operator, total, char):
    if operator == "*":
        return total * char
    elif operator == "+":
        return total + char
    elif operator == "/":
        return total / char
    elif operator == "-":
        return total - char


def calculate(expression):
    total = 0
    operator = "+"
    for char in expression:
        if type(char) == int:
            total = operators(operator, total, char)
            if type(total) != int:
                # total is a fraction
                return 0
        else:
            operator = char

    return total


def correct_expressions(valid_expression_list):
    for expression in valid_expression_list:
        num_numbers = int((len(expression) + 1) / 2)
        pairs_of_parenthesis = num_numbers - 2

        for i in range(len(expression) - 2, 1, -2):
            if expression[i] == "+" or expression[i] == "-":
                pairs_of_parenthesis -= 1
            elif expression[i] == "*" or expression[i] == "/":
                if expression[i - 2] == "*" or expression[i - 2] == "/":
                    pairs_of_parenthesis -= 1
                else:
                    expression.insert(i, ")")
            else:
                expression.insert(i, ")")

        for _ in range(pairs_of_parenthesis):
            expression.insert(0, "(")


valid_expression_list = []

solve([1, 2, 3, 4], 24)
