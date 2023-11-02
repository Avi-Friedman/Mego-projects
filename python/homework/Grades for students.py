students_dic = {"yosef israeli" : 75, "elisha shechter" : 67, "beni shachar" : 98, "yoel mizrachi" : 83, "dani tal" : 55,}
students_dic_new ={}
for item in students_dic:
    if students_dic[item] >= 90:
        students_dic_new [item] = "Amazing"
    elif students_dic[item]  >= 80:
        students_dic_new [item] = "beyond expectations"
    elif students_dic[item]  >= 70:
        students_dic_new [item] = "You can do more"
    else:
        students_dic_new [item] = "you failed"
print(students_dic_new)

