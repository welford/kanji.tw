import csv

#export all the thai characters as tiddlers
with open(".\\source\\thai.csv","r", encoding="utf-8-sig") as csv_file:
	data = csv.reader(csv_file)
	next(data) #skip header
	for r in data:
		f = open(".\\export\\tw-thai\\tiddlers\\"+r[0]+".tid", "w",encoding='utf8')
		f.write("created: 20150620130427249\n")
		f.write("modified: 20150620130427249\n")
		f.write("type: text/vnd.tiddlywiki\n")
		f.write("title: "+r[0]+"\n")
		f.write("thai-writing: "+r[1]+"\n")
		f.write("rtgs-writing: "+r[2]+"\n")
		f.write("meaning: "+r[3]+"\n")
		f.write("rtgs-initial: "+r[4]+"\n")
		f.write("rtgs-final: "+r[5]+"\n")
		f.write("ips-initial: "+r[6]+"\n")
		f.write("ips-final: "+r[7]+"\n")
		f.write("class: "+r[8]+"\n")
		f.write("tags: [[thai script]]\n")

		f.write("\n{{||thai-script-template}}\n")
		f.close()