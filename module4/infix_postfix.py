from StackADT import Stack


def infix_to_postfix(infix):
    prec = {}
    prec["^"] = 4
    prec["*"] = 3
    prec["/"] = 3
    prec["+"] = 2
    prec["-"] = 2
    prec["("] = 1
    op_stack = Stack()
    postfix_list = []
    token_list = infix.split()

    for token in token_list:
        if token.isdigit():
            postfix_list.append(token)
        elif token == "(":
            op_stack.push(token)
        elif token == ")":
            top = op_stack.pop()
            while top != "(":
                postfix_list.append(top)
                top = op_stack.pop()
        else:
            while (not op_stack.is_empty() and
                   (prec[op_stack.peek()] > prec[token] or
                    (prec[op_stack.peek()] == prec[token] and token != "^"))):
                postfix_list.append(op_stack.pop())
            op_stack.push(token)

    while not op_stack.is_empty():
        postfix_list.append(op_stack.pop())

    return " ".join(postfix_list)


def postfix_eval(postfix):
    op_stack = Stack()
    token_list = postfix.split()

    for token in token_list:
        if token.isdigit():
            op_stack.push(int(token))
        else:
            op2 = op_stack.pop()
            op1 = op_stack.pop()
            result = do_math(token, op1, op2)
            op_stack.push(result)

    return op_stack.pop()


def do_math(op, op1, op2):
    if op == "*":
        return op1 * op2
    elif op == "/":
        return op1 / op2
    elif op == "+":
        return op1 + op2
    elif op == "-":
        return op1 - op2
    elif op == "^":
        return op1 ** op2


def simple_calculator(infix_expression):
    postfix_expression = infix_to_postfix(infix_expression)
    return postfix_eval(postfix_expression)


def main():
    test_cases = [
        "5 * 3 ^ ( 4 - 2 )",
        "12 + 34 * 56",
        "( 100 / 20 ) + 30",
        "2 ^ 10 * 4",
        "90 + ( 21 - 11 ) * 5"
    ]

    for infix_expression in test_cases:
        result = simple_calculator(infix_expression)
        print(f"Infix: {infix_expression}")
        print(f"Result: {result}\n")


if __name__ == "__main__":
    main()
