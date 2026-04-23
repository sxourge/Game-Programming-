Total = 0

# End was increased by one to produce the exact number 32482 
End = 32483
Value1 = 7.1
Value2 = 9.1

# loop combines all numbers. Displays / produces the summary of 437 to 32482. (NOT 437 x 32482)
for i in range(437, End):
    Total = Total + i
    # print produces the number summary via the console 
    # removing space in front of "print" will remove string of numbers in the console and only show the final number 
    print(Total)

# if = determines if Value1 is greater than Value2 
if Value1 > Value2:
    result = Value1 / Value2
    # print shows the result
    print (result)

# elif = will be used in case "if" does not apply / is "false". determines if Value2 is smaller than Value1 
elif Value1 < Value2:
    result = Value1 / Value2 
    print (result)

# else = variable is set to 1
else:
    result = 1
    print (result)