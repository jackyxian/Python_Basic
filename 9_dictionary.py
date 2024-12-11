
# 结合input、字典、if判断，做一个查询流行语含义的电子词典程序
slang_dict = {"爱达未来":"杭州亚运会的主题口号“心心相融，@未来”（读作“爱达未来”），是诠释“更快、更高、更强——更团结”奥林匹克格言的中国实践。2023年6月，《爱达未来》作为杭州亚运会推广歌曲之一发布。",
            "烟火气":"指生机盎然、充满活力的生活气息。烟火气是温情，是祥和，需要珍惜和守护，也需要奉献和担当。烟火气是百姓心中最朴素、最踏实的幸福感。",
            "数智生活":"“数智”突显数据的价值和智慧的共享。伴随着大数据、人工智能等“数智”技术的快速发展，百姓的衣食住行等都发生了深刻的变化，日常生活更为便利。",
            "村BA":"2022年七八月份，贵州省黔东南州台盘乡台盘村举办贵州省“美丽乡村”篮球联赛。这场当地村民一年一度的篮球赛，经由短视频火爆全网，网友们仿照“NBA”“CBA”，称之为“村BA”。2023年“村BA”继续火爆，除贵州省外，北京、天津、河北、辽宁、吉林、黑龙江、江苏、山东等地也举办类似比赛。",
            "特种兵式旅游":"年轻人试图用最低的经济成本，挑战时间与体力的边界，以此换取最丰富的旅游文化体验。这种“时间短、景点多、花费少、效率高”的旅游方式被网友们称为“特种兵式旅游”，他们说：我来过，我看过，我感受，我打卡。",
            "显眼包":"原义指过于张扬、爱出风头的人，现在网络平台上以戏谑的方式指称那些个性鲜明、敢于展示自我、能营造欢乐氛围的人或事物。这个词语体现了互联网时代人们对个性化事物、多元化现象的包容。",
            "主打一个××":"一种流行的网络句式，强调某个人或某件事物在特定领域内的特色和优势。如“主打一个高性价比”、“主打一个便宜”、“主打一个方便”、“主打一个开心”。",
            "多巴胺穿搭":"一种通过服装搭配来营造愉悦感的穿搭风格，特点是缤纷、阳光、活力，对高饱和度的色彩进行搭配，在鲜亮色彩中寻求协调与平衡。“多巴胺穿搭”火爆之后，“多巴胺音乐” 、“多巴胺文学”等类似词条也陆续出现。",
            "命运的齿轮开始转动":"指改写命运的某个瞬间或影响人生轨迹的某个转折点。这个短语表面上说的是成功背后的运气、机遇等偶然因素，更多强调的是在压力和逆境中应尽快行动起来，才能把握自我命运曲线的走势、创造属于自己的辉煌。",
            "新职人":"指具有特定专业技能和经验背景、从事新兴职业的人。2019年以来，人力资源和社会保障部先后发布了5批共74个新职业，如商务数据分析师、农业数字化技术员、城市轨道交通检修工等。"}
# print(slang_dict)

query = input("请输入您想要查询的：")
if(query in slang_dict):
    print("您查询的 " + query + " 含义如下：")
    print(slang_dict[query])
else:
    print("您查询的流行语 " + query + " 暂未收录")
    print("当前本字典收录的字条数为：" +  str(len(slang_dict)) + "条")
