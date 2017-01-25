#-*-coding:utf-8-*-
import json
import random
class ChatRob:
	def __init__(self,JsonDataURL="JsonData.json"):
		self.DataURL = JsonDataURL;
		
		self.MainData = self.LoadJson(JsonDataURL)

	def LoadJson(self,JsonDataUrl):
		#read json file 
		f = open(JsonDataUrl, 'r')
		b_str = f.read()
		f.close()
		return json.loads(b_str)
		
	def All(self):
		# print all key and data
		for key, value in self.MainData.iteritems():
		    print key+": ",self.MainData[key]
		    
		print "len: ",str(len(self.MainData))
	def Learn(self,JsonData):
		NewData = json.loads(JsonData)
		tooken = 1
		# alert common key
		for Nkey, value in NewData.iteritems():
		    # if found fail,would break
		    if tooken == 0:
			print "error"
			break
		    target = Nkey
		    for Okey in self.MainData.iteritems():
			# if found common Key ,would break
			if target == Okey:
				print "error"
				tooken = 0
			
		if tooken == 1:
			# conbine two array
			self.MainData = dict(NewData.items() + self.MainData.items())

			#updata json data
			NewData = "{"
			for key, value in self.MainData.iteritems():
				# if type of data is list ,would run this
				if type(self.MainData[key])==list:
					NewData+='"'+key+'":'
					NewData+='["'
					for i in range(len(self.MainData[key])):
						if i != 0: 
							NewData+='","'
						NewData+=self.MainData[key][i]
					NewData+='"]'
					NewData+=','
				else:
					NewData+= '"'+key+'":"'+self.MainData[key]+'",'
			# delete extra ","
			NewData =NewData[0:len(NewData)-1]+'}'

			text_file = open("JsonData.json", "w")
			text_file.write(NewData.encode('utf8'))
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

		
	


#create ChatRob
T = ChatRob()
#T.All()
#T.Learn('{"你好":"你好"}')
#T.All()
T.Learn('{"北七13":"吃屎"}')
T.All()
#T.Learn('{"乖乖":"閉嘴"}')
#T.All()
T.listen()


 
