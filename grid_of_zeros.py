'''for row_loop_var in range(1,4):
    for col_loop_var in range(1,4):
        print(0,end=" ")
    print()'''
rows=int(input("enter the number of rows:"))
cols=int(input("enter the number of cols:"))
for row_loop_var in  range(1,rows+1):
    for col_loop_var in range(1,cols+1):
        print("*",end=" ")
        print() 
