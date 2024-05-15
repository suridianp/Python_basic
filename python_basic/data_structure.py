my_list = [1,2,3,4,5,'string',[1,2,4],100]
print(my_list[-3])
my_list.append(5000)
print(my_list)
my_map = {
    "key_1": 1,
    "key_2": 2
}
my_map ["key_1"] = 5
print(my_map)
print(my_map["key_1"])
my_map2 = {
    "key_3":3,
    "key_4":4
}
my_map.update(my_map2)
print(my_map)
dic_1 = {
    1:10,
    2:20
}
dic_2 = {
    3:30,
    4:40
}
dic_1.update(dic_2)
print(dic_1)