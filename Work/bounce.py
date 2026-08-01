# bounce.py
#
# Exercise 1.5

height = 100
bounces = 10

while bounces > 0:
    height = height * 3/5
    print(round(height, 4))
    bounces = bounces - 1