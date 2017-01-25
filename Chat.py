#-*-coding:utf-8-*-
import json
class ChatRob:
	def __init__(self,JsonData):
		self.MainData = json.loads(JsonData)
	def All(self):
		# print all key and data
		for key, value in self.MainData.iteritems():
		    print key+": "+self.MainData[key]
		    
		print str(len(self.MainData))
        def Learn(self,JsonData):
		# conbine two array

		NewData = json.loads(JsonData)
		self.MainData = dict(NewData.items() + self.MainData.items())

		
	
#read json file 
f = open("JsonData.json", 'r')
b_str = f.read()
f.close()

#create ChatRob
T = ChatRob(b_str)
T.All()
T.Learn('{"安安":"哈摟"}')
T.All()
T.Learn('{"北七":"吃屎"}')
T.All()
T.Learn('{"乖乖":"閉嘴"}')
T.All()



 
