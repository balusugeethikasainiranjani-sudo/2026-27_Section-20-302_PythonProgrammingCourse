rows=int(input("enter the number of rows:"))
for row_loop_var in range (1,row+1):
    for col_loop_var_spaces in range(1,rows-row_loop_var+1):
        print(" ",end=" ")
    for col_loop_var_num in range(1,2*row_loop_var+1):
        print("*",end=" ")
    