# def intersect(f,v):
#     list_common = []
#     # for i in f:
#     #     for j in v:
#     #         if i==j:
#     #             list_common.append(i)
#     # return list_common

#     # list_common = [i for i in f if i in v]
#     # return list_common
#     # for i in f:
#     #     if i in v:
#     #         #print(i)
#     #         list_common.append(i)
#     # return list_common
#     list_common =list(set(list(f)).intersection(v))
#     return list_common

# fruits=['Grapes',"Apples",'Oranges','Mango','Pear','Lemon','Tomato','Avacado']
# vegetables=['Tomato','Onion','Okra','Tindora','Raddish','Asparagus','Avacado']
# common_list = intersect(fruits,vegetables)
# print(common_list)
# def pair(a,b):
#     c= []
#     for (x,y) in zip(a,b):
#         #c= list(set(list(c).append(x,y)))
#         print("{0},{1}".format(x,y))

       
#     #return c
def pair(a,b):
    for (x,y) in enumerate(a):
        for (i,j) in enumerate(b):
            if x is i:
                print("{0},{1}".format(y,j))
                continue

a=['d','f','g','h']
b=[1,2,3,4]
pair(a,b)
#print(paired)

