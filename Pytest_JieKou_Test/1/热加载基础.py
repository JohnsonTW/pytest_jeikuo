# split函数
# args1 = "345,678"
# result = args1.split(",")
# print(result)

# data = "12,24"
# # map函数
# min_digits, max_digits = map(int, data.split(','))
# print(max_digits)
# print(type(max_digits))


# data = {"name": "Lisa", "age": "35"}
# # data.items() 返回所有键值对
# print(data.items())
# print(data.values())
# print(data.keys())


data2 = "${max(222)}"
if data2.startswith('${') and data2.endswith('}'):
    func_name, args = data2[2:-1].split('(', 1)
    # 从args的开头到倒数第2个字符的所有内容 :  max(222)
    args = args[:-1]
    print(func_name)
    print(args)
