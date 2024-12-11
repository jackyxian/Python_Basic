# list1 = [1, 3, 5, 7, 9, 11]
# dict1 = {"小明":1.78, "小花":1.65}
# str1 = "Hello, world"
# for num in list1:
#     print(num)
# for item in dict1.items():
#     print(item)
# for str in str1:
#     print(str)
#
# temperautre_list = [36.4, 36.6, 36.2, 37.0, 36.5, 36.8, 38.3, 38.1]
# for temperature in temperautre_list:
#     if(temperature >= 38):
#         print(temperature)
#         print("完球了")

temperautre_dict = {"张三":36.4, "李四":36.6, "王五":36.2, "小明":37.0, "小华":36.5, "小丽":36.8, "小田":38.3, "小天":38.1}
for temperature_name, temperature_value in temperautre_dict.items():
    if temperature_value >= 38:
        print(temperature_name + "发烧了：" + str(temperature_value) + " 度")
        print("完球了")


# 算出 1至100的和
total = 0
for i in range(1, 101):
    total += i
    print(total)


