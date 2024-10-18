from ArrayStack import ArrayStack as Stack
S = Stack
def is_matched(expression):
    stack = Stack()
    opening = "([{"
    closing = ")]}"
    pairs = {')': '(', ']': '[', '}': '{'}

    for char in expression:
        if char in opening:
            stack.push(char)
        elif char in closing:
            if stack.is_empty():
                return False
            if stack.pop() != pairs[char]:
                return False

    return stack.is_empty()

expressions = [
    "( )(( )){([( )])}",
    "((( )(( )){([( )])})))",
    ")(( )){([( )])}",
    "({[]})",
    "("
]

for expr in expressions:
    print(f"Expression: {expr}")
    print('')
    print(f"Is balanced: {is_matched(expr)}\n")
    print('===========================================================')




    def reverse_file_lines(file_name):
        stack = Stack()


        with open(file_name, 'r') as file:
            for line in file:
                stack.push(line.rstrip('\n'))


        with open(file_name, 'w') as file:
            while not stack.is_empty():
                file.write(stack.pop() + '\n')


    file_name = 'myfile.txt'
    reverse_file_lines(file_name)

    print(f"Lines in '{file_name}' have been reversed.")


    def reverseFileName(file_name):
        stack = Stack