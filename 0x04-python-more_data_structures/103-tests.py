import ctypes

lib = ctypes.CDLL('./libPython.so')
lib.print_python_list.argtypes = [ctypes.py_object]
lib.print_python_bytes.argtypes = [ctypes.py_object]

s = b"Hello"
lib.print_python_bytes(s)

b1 = b'\xff\xf8\x00\x00\x00\x00\x00\x00'
lib.print_python_bytes(b1)

b2 = b'What does the \'b\' character do in front of a string literal?'
lib.print_python_bytes(b2)

lst1 = [b'Hello', b'World']
lib.print_python_list(lst1)

del lst1[1]
lib.print_python_list(lst1)

lst2 = lst1 + [4, 5, 6.0, (9, 8), [9, 8, 1024], b"Holberton", "Betty"]
lib.print_python_list(lst2)

lst3 = []
lib.print_python_list(lst3)

lst3.append(0)
lib.print_python_list(lst3)

lst3.append(1)
lst3.append(2)
lst3.append(3)
lst3.append(4)
lib.print_python_list(lst3)

lst3.pop()
lib.print_python_list(lst3)

lst4 = ["Holberton"]
lib.print_python_list(lst4)

lib.print_python_bytes(lst4)
