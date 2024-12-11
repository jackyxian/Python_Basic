# BMI (身体质量指数 = 体重（kg）÷ 身高²（m）)
user_weight = float(input("请输入您的体重(单位：kg)："))
user_height = float(input("请输入您的体重(单位：m)："))
user_BMI = user_weight / (user_height ** 2)
print("您的 BMI 值为：" + str(user_BMI))

# 偏瘦 user_BMI <= 18.5
# 正常 18.5 < user_BMI <= 25
# 偏胖 25 < user_BMI <= 30
# 肥胖 user_BMI > 30

if user_BMI <= 18.5:
    print("此 BMI 值属于偏瘦范围。")
elif 18.5 < user_BMI <= 25:
    print("此 BMI 值属于正常范围。")
elif 25 < user_BMI <= 30:
    print("此 BMI 值属于偏胖范围。")
else:
    print("此 BMI 值属于肥胖范围。")