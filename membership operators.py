number_list=[10,20,30,40,50]
search_number=int(input("enter the number to search:"))
present_result=search_number in number_list
absent_result=search_number not in number_list
print("number is present :",present_result)
print("number is absent:",absent_result)
