drawing = input()
left, right = drawing.split("()")
if left == right:
    print("correct")
else:
    print("fix")
