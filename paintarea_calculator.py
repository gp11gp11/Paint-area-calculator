'''
Instructions
You are painting a wall. The instructions on the paint can says that 1 can of paint can cover 5 square meters of wall. Given a random height and width of wall, calculate how many cans of paint you'll need to buy.

number of cans = (wall height ✖️ wall width) ÷ coverage per can.

e.g. Height = 2, Width = 4, Coverage = 5

number of cans = (2 ✖️ 4) ÷ 5

                     = 1.6

But because you can't buy 0.6 of a can of paint, the result should be rounded up to 2 cans.


'''



import math
def paint_calc(height,width,cover):
    no_of_can = math.ceil((height*width)/cover)#ceil is used to round off to heigher whole number,eg:2.3 get converted to 3
    print(f"you'll need {no_of_can} cans of paint")

#Write your code above this line 👆
# Define a function called paint_calc() so that the code below works.   

# 🚨 Don't change the code below 👇
test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)
