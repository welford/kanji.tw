import json

#export all the joyo data ad tiddlers
# 1. to create the structure:
# 	tiddlywiki .\kanjidb\export\tw-jouyou --init server 
# 2. run this script
# 3. run the server
# 	tiddlywiki .\kanjidb\export\tw-jouyou --listen  
# you can then import the data from the server
with open(".\\source\\kanji-jouyou.json","rb") as json_file:
	data = json.load(json_file)
	count = {
		1 :"一",2:"二",3:"三",4:"四",5:"五",6:"六",7:"七",8:"八",9:"九",10:"十",11:"十一",12:"十二",13:"十三",14:"十四",15:"十五",16:"十六",17:"十七",18:"十八",19:"十九",20:"二十",21:"二十一",22:"二十二",23:"二十三",24:"二十四",25:"二十五",26:"二十六",27:"二十七",28:"二十八",29:"二十九",30:"三十",31:"三十一",32:"三十二",33:"三十三",34:"三十四",35:"三十五",36:"三十六",37:"三十七",38:"三十八",39:"三十九",
	}
	for d in data:
		f = open(".\\export\\tw-jouyou\\tiddlers\\"+d+".tid", "w",encoding='utf8')
		f.write("created: 20150620130427249\n")
		f.write("modified: 20150620130427249\n")
		f.write("type: text/vnd.tiddlywiki\n")
		f.write("title: "+d+"\n")
		f.write("訓読み:")
		for r in data[d]["readings_kun"]:
			f.write(" " + r)
		f.write("\n")
		f.write("音読み:")
		for r in data[d]["readings_on"]:
			f.write(" " + r)
		f.write("\n")
		f.write("画数: "+str(data[d]["strokes"])+"\n")
		f.write("jplt: "+str(data[d]["jlpt_new"])+"\n")
		f.write("グレード: "+str(data[d]["grade"])+"\n")
		f.write("意味:")
		for r in data[d]["meanings"]:
			f.write(" [[" + r + "]]")
		f.write("\n")

		grade = "教育漢字" if data[d]["grade"] < 7 else ""
		grade = "人名用" if data[d]["grade"] > 7 and data[d]["grade"] < 10 else ""

		f.write("tags: 常用 類：字 "+grade+" "+count[data[d]["strokes"]]+"画\n")

		f.write("\n{{||漢字テンプレート}}\n")
		f.close()