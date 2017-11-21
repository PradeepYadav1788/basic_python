import operations as op
x1 = op.X()
# calling insert
x1.insert(20, 30)
myVals = x1.display()
print(myVals)
# calling modify
myVals1 = x1.modify(100, 200)

print(myVals1)