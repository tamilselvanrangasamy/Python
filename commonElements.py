def Common_elements(list1,list2):
    common=[]
    for i in list1:
        for j in list2:
            if i==j:
                common.append(i)
    return common


list1=[1,2,3,4,5]
list2=[3,2,7,5,6]
print(Common_elements(list1,list2))
