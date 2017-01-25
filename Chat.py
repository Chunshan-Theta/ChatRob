#-*-coding:utf-8-*-
import json
import random
class ChatRob:
	def __init__(self,JsonData):
		self.MainData = json.loads(JsonData)
	def All(self):
		# print all key and data
		for key, value in self.MainData.iteritems():
		    print key+": ",self.MainData[key]
		    
		print str(len(self.MainData))
        def Learn(self,JsonData):
		# conbine two array

		NewData = json.loads(JsonData)
		self.MainData = dict(NewData.items() + self.MainData.items())

		#updata json data
		NewData = "{"
		for key, value in self.MainData.iteritems():
		    NewData+= '"'+key+'":"'+self.MainData[key]+'",'
		NewData += '"coder":"theta"}'
		text_file = open("JsonData.json", "w")
		text_file.write(NewData.encode('utf8'))

		text_file.close()
	def listen(self):
		ask = "ask"
		while ask != "close":
			ask = raw_input("安安,你想對我說什麼嗎? >> ")
			#call data using chinese key
			u = unicode(ask, "utf-8")
			try:
				if type(self.MainData[u])==list:
					print self.MainData[u][random.randint(0, len(self.MainData[u])-1)]
				else:
					print self.MainData[u]
			except:
				if ask != "close":
					print "人家聽不懂你說的話耶"

		
	
#read json file 
f = open("JsonData.json", 'r')
b_str = f.read()
f.close()

#create ChatRob
T = ChatRob(b_str)
T.All()
#T.Learn('{"安安":"哈摟"}')
#T.All()
#T.Learn('{"北七":"吃屎"}')
#T.All()
#T.Learn('{"乖乖":"閉嘴"}')
#T.All()
T.listen()


 
