import ctypes

lib = ctypes.CDLL('./libPyList.so')
lib.print_python_list_info.argtypes = [ctypes.py_object]

list1 = ['hello', 'World']
lib.print_python_list_info(list1)

del list1[1]
lib.print_python_list_info(list1)

list2 = list1 + [4, 5, 6.0, (9, 8), [9, 8, 1024], "Holberton"]
lib.print_python_list_info(list2)

list3 = []
lib.print_python_list_info(list3)

list3.append(0)
lib.print_python_list_info(list3)

list3.append(1)
list3.append(2)
list3.append(3)
list3.append(4)
lib.print_python_list_info(list3)

list3.pop()
lib.print_python_list_info(list3)
