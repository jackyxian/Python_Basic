contacts = ["老余", "老林", "老陳", "老曾", "老李", "老張"]
for name in contacts:
    message_content = name + "：岁始之乐，点翠画柳喜开颜。云开雾散,良辰美景共团圆。祝福：" + name + "及家人新年快乐，平安顺遂，虎年大吉！🧨"
    print(message_content)

year = "龙"
for name in contacts:
    message_content = """
    律回春渐，新元肇启。
    新岁甫至，福气东来。
    金{0}贺岁，欢乐祥瑞。
    金{0}敲门，五福临门。
    给{1}及家人拜年啦！
    新春快乐，{0}年大吉！
    """.format(year,name)
    print(message_content)

