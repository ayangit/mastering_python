# we use the eval keyword to evaluate an expression
# A expression is something that returns a value

#Evalueating user input
# user_input : int = input(" Enter an Integer: ")
# result : float = eval(user_input)
# print(result)

# Evaluating multiline string

# text : str = """
# 10 * '\\nHello'
# """
# print(eval(text))

# Things that can't be evaluated  like above
#It won't recognise the assignment operator as it does not evaluate to anything
# text : str = """
# x = 10
# y = x *8
# """
# print(eval(text))

# The following returns "Hello" and None as print returns "None" as response
text : str = """
print('Hello')
"""
print(eval(text))
