from LinkedStack import LinkedStack
from PositionalList import PositionalList

L = LinkedStack
P = PositionalList

def precedence(op):
    """Return the precedence of the operator."""
    if op in ('+', '-'):
        return 1
    if op in ('*', '/'):
        return 2
    if op == '^':
        return 3
    return 0

def preprocess_expression(expression):
    """Prepare the expression for tokenization, adding spaces around operators."""
    operators = set('+-*/^()')
    result = []
    for char in expression:
        if char in operators:
            result.append(f' {char} ')
        else:
            result.append(char)
    return ''.join(result).split()

def infix_to_postfix(expression):
    """Convert infix expression to postfix notation using LinkedStack."""
    stack = L()
    output = P()

    for char in expression:
        if char.isdigit():  # Operand
            output.add_last(char)
        elif char == '(':
            stack.push(char)
        elif char == ')':
            while not stack.is_empty() and stack.top() != '(':
                output.add_last(stack.pop())
            stack.pop()
        else:
            while (not stack.is_empty() and
                   precedence(stack.top()) >= precedence(char)):
                output.add_last(stack.pop())
            stack.push(char)

    while not stack.is_empty():
        output.add_last(stack.pop())

    return " ".join([item for item in output])

def insertion_sort_ascending(pos_list):
    if pos_list.first() is None:
        return

    cursor = pos_list.first()
    while cursor is not None:
        next_cursor = pos_list.after(cursor)
        key = cursor.element()

        walk = cursor
        while walk != pos_list.first() and pos_list.before(walk).element() > key:
            pos_list.replace(walk, pos_list.before(walk).element())
            walk = pos_list.before(walk)

        pos_list.replace(walk, key)
        cursor = next_cursor

def insertion_sort_descending(pos_list):
    if pos_list.first() is None:
        return

    cursor = pos_list.first()
    while cursor is not None:
        next_cursor = pos_list.after(cursor)
        key = cursor.element()

        walk = cursor
        while walk != pos_list.first() and pos_list.before(walk).element() < key:
            pos_list.replace(walk, pos_list.before(walk).element())
            walk = pos_list.before(walk)

        pos_list.replace(walk, key)
        cursor = next_cursor

def main():
    print("Infix to Postfix")
    expression = input("Enter an infix expression: ").strip()
    try:
        tokens = preprocess_expression(expression)
        postfix = infix_to_postfix(tokens)
        print("Postfix expression:", postfix)
    except Exception as e:
        print(f"Error during postfix conversion: {e}")

    print("\nNumbers:")
    numbers = [1, 72, 81, 25, 65, 91, 11]
    print("Numbers:", numbers)


    pos_list = P()
    for num in numbers:
        pos_list.add_last(num)

    insertion_sort_ascending(pos_list)
    print("ASCENDING ORDER:", [item for item in pos_list])

    pos_list = P()
    for num in numbers:
        pos_list.add_last(num)

    insertion_sort_descending(pos_list)
    print("DESCENDING ORDER:", [item for item in pos_list])

if __name__ == "__main__":
    main()
