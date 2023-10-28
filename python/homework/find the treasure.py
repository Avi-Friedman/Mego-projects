list_1 = ['_','_','_']
list_2 = ['_','_','_']
list_3 = ['_','_','_']
print(f"{list_1}\n{list_2}\n{list_3}")
user_row = (int(input("In which row is the cache?:"))-1)
user_column = (int(input("In which column is the cache?:"))-1)
matrix = [list_1,list_2,list_3]
(matrix[user_row][user_column]) = "x"
print(f"{list_1}\n{list_2}\n{list_3}")








