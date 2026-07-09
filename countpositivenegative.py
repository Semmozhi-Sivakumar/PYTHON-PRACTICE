#Count positive and negative numbers.
numbers = [10,-5,20,-1,-8,6]
positive = 0
negative = 0
for i in numbers:
    if(i>0):
        positive=positive+1
    else:
        negative=negative+1
print(positive)
print(negative)        