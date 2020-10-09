## Approach
## The idea is to convert the given infix expression
## into postfix expression and then calculate the postfix expression
## because it's easy to calculate postfix expression.


## Input formatting
## Whitespace character is used to format the input
## i.e. each operator and operand is seperated by a whitespace.
## Example input format: ( 20 * ( 30 + 10 ) / ( 10 * 2 ) )



def precedence(s):
    if s =='*' or s=='/':
        return 2
    elif s =='+' or s=='-':
        return 1
    else:
        return -1


def evaluate(a, b, op):
    if op=='+':
        return a+b
    if op=='-':
        return b-a
    if op=='*':
        return a*b
    if op=='/':
        return b/a


def infixToPostfix(exp):
	stack = []
	post = []
	for i in exp:
		if i == '(':
			stack.append(i)
		elif i == ')':
			while stack[-1] != '(':
				post.append(stack.pop())
			stack.pop()
		elif precedence(i) == -1:
			post.append(i)
		else:
			if not stack
			or  precedence(i) > precedence(stack[-1]):
				stack.append(i)
			else:
				while stack
				and precedence(i) <= precedence(stack[-1])
				and precedence(stack[-1]) != -1:
					post.append(stack.pop())
				stack.append(i)
	while stack:
		post.append(stack.pop())
	return post



def calculate(post):
    stack = []
    for i in post:
        if i.isnumeric():
            stack.append(int(i))
        else:
            a = stack.pop()
            b = stack.pop()
            stack.append(evaluate(a,b,i))
    return stack[-1]

exp = input().split()
print(calculate(infixToPostfix(exp)))
