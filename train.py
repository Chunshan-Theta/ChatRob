#coding:utf-8
# making chinese sentence to a set of words
import jieba

def Sentence2WordArray(T="安安你好今天的天氣真差"):
	
	seglist = jieba.cut(T, cut_all=False)
	result=[]
	for p in seglist: result.append(p)
	return result


def compare_Learn(a,b,alert=0):#len(a)>(b)
	print "^"*40
	ASentence = ""
	BSentence = ""
	for con in a:ASentence += con
	for con in b:BSentence += con
	print "原句：",ASentence,BSentence

	R1,R2,R3,R4 = compare(a,b,alert)
	global BestWeight
	CommonRate = (R1*BestWeight[0]+R2*BestWeight[1]+R3*BestWeight[2]+R4*BestWeight[3])/(BestWeight[0]+BestWeight[1]+BestWeight[2]+BestWeight[3])*100
	
	
	
	
	#print ExeNum*"->","相似度",CommonRate,"%"
	if CommonRate>70 :
		TrainedContent = open("data.txt","r").read()
		#print TrainedContent
		TrainDataFile=open("data.txt","w")
	
		NewText = TrainedContent
		
		for con_a in a:
			tooken = 0
			for con_b in b:
				if con_a==con_b:tooken=1
				if con_b in con_a or con_a in con_b:tooken=1
				if alert:
					print con_a,con_b,tooken
			if tooken==0 and len(con_a)<3:
				NewText+=","
				NewText+=con_a.encode("utf-8")
				print "delete: ",con_a.encode("utf-8")
		for con_b in b:
			tooken = 0
			for con_a in a:
				if con_a==con_b:tooken=1
				if con_b in con_a or con_a in con_b:tooken=1
				if alert:
					print con_a,con_b,tooken
			if tooken==0 and len(con_b)<3:
				NewText+=","
				NewText+=con_b.encode("utf-8")
				if alert:
					print "delete: ",con_b.encode("utf-8")
		TrainDataFile.write(NewText.strip("\n\r"))
		TrainDataFile.close()
	#print ASentence,BSentence

	return R1,R2,R3,R4

def compare_Sentence(a,b,alert=0,ExeNum=1):#len(a)>(b)
	
	ASentence = ""
	BSentence = ""
	for con in a:ASentence += con
	for con in b:BSentence += con
	if alert:
		print "原句：",ASentence,BSentence

	R1,R2,R3,R4 = compare(a,b,alert)
	global BestWeight
	CommonRate = (R1*BestWeight[0]+R2*BestWeight[1]+R3*BestWeight[2]+R4*BestWeight[3])/(BestWeight[0]+BestWeight[1]+BestWeight[2]+BestWeight[3])*100
	
	
	
	
	if ExeNum >4:
		if alert:
			print ASentence,BSentence,ExeNum*"->","相似度",CommonRate,"%"		
			print ASentence,BSentence
		return CommonRate
	#if len(ASentence)<5 or len(BSentence)<5:
	#	print ASentence,BSentence,ExeNum*"->","相似度",CommonRate,"%"
	#	return R1,R2,R3,R4
	if CommonRate < 70:
		
		TrainedContent = open("data.txt","r").read().split(",")
		if alert:
			print "TrainedContent: ",TrainedContent
		New_a=ASentence.encode("utf-8")
		New_b=BSentence.encode("utf-8")
		#print ASentence,BSentence
		for con in TrainedContent:
			con = unicode(con,"utf-8")
			if con in ASentence and len(New_a)>5:
				New_a =  ASentence.encode("utf-8").replace(con.encode("utf-8"),"")
			if con in BSentence and len(New_b)>5:
				New_b =  BSentence.encode("utf-8").replace(con.encode("utf-8"),"")
		#print ASentence,BSentence
		if alert:
			print ASentence,BSentence,ExeNum*"->","相似度",CommonRate,"%"
		#print ASentence,BSentence	
		return compare_Sentence(Sentence2WordArray(New_a),Sentence2WordArray(New_b),alert,ExeNum+1)
	if alert:
		print ASentence,BSentence,ExeNum*"->","相似度",CommonRate,"%"
	
	
	return CommonRate
def compare(a,b,alert=0):#len(a)>(b)
	
	if len(a)<len(b):
		c = a
		a = b
		b = c

	ASentence = ""
	BSentence = ""
	for con in a:ASentence += con
	for con in b:BSentence += con
	############################################	
	
	
	CommonTextNum=0
	for AContent in ASentence:
		if AContent in BSentence:
			CommonTextNum+=1
	
	CommonRate=1-float(CommonTextNum)/len(ASentence)
	R1 = 1-CommonRate #1
	if alert:
		print "#1 CommonTextRate(n) :",R1

	###
	CommonNum=0
	for bi in range(len(b)):
		for ai in range(len(a)):
			if a[ai]==b[bi]: CommonNum+=1
	
	CommonRate=float(CommonNum)/len(a)
	R2 = CommonRate #2
	if alert:
		print "#2 CommonWordRate% :",R2	
	###
	div_A = len(ASentence)/3+1
	div_B = len(BSentence)/3+1
	CommonTextNum_F=0
	for AContent in ASentence[0:div_A]:
		if AContent in BSentence[0:div_B]:
			CommonTextNum_F+=1
	R3 = CommonTextNum_F/len(ASentence[0:div_A]) 
	if alert:
		print "#R3 CommonTextRate_F(n) :",R3
	

	###
	div_B = len(BSentence)/3+1
	div_A = len(ASentence)-div_B
	
	CommonTextNum_B=0
	#print ASentence[div_A:len(ASentence)],BSentence[div_B:len(BSentence)]
	#print len(ASentence[div_A:len(ASentence)])
	for AContent in ASentence[div_A:len(ASentence)]:
		if AContent in BSentence[div_B:len(BSentence)]:
			CommonTextNum_B+=1
	#print ":",CommonTextNum_B
	#print ":",len(ASentence[div_A:len(ASentence)])
	R4 = CommonTextNum_B/len(ASentence[div_A:len(ASentence)])  #4
	#print "R4",R4
	if alert:
		print "#R4 CommonTextRate_B(n) :",R4
	###
	###
	
	return R1,R2,R3,R4
	#5 commontext
	#6 ***base on 字詞重要性
	#6-1 length
	#6-2 CommonWord
	#6-3 CommonPosition
	#6-4 commontext		
def AdjestWeight(t,w):
	
	NewData=[]
	for i in t:
		NewData.append((i[0]*w[0]+i[1]*w[1]+i[2]*w[2]+i[3]*w[3])/(w[0]+w[1]+w[2]+w[3]))
	#print NewData[0],NewData[1],NewData[2],NewData[3],NewData[4]
	#print (NewData[0]+NewData[1]-NewData[2]-NewData[3]-NewData[4])*100/2
	sorce = 0
	for SorceOfCompution in NewData:sorce+=SorceOfCompution
	sorce = sorce/len(NewData)*100
	return sorce




def CompareComputer(CommonArray,WeightArray,alert=0):
	s = AdjestWeight(CommonArray,WeightArray)

	NewWeightArray_1=[WeightArray[0]+1,WeightArray[1],WeightArray[2],WeightArray[3]]
	a1 = AdjestWeight(CommonArray,NewWeightArray_1)

	NewWeightArray_2=[WeightArray[0],WeightArray[1]+1,WeightArray[2],WeightArray[3]]
	a2 = AdjestWeight(CommonArray,NewWeightArray_2)

	NewWeightArray_3=[WeightArray[0],WeightArray[1],WeightArray[2]+1,WeightArray[3]]
	a3 = AdjestWeight(CommonArray,NewWeightArray_3)

	NewWeightArray_4=[WeightArray[0],WeightArray[1],WeightArray[2],WeightArray[3]+1]
	a4 = AdjestWeight(CommonArray,NewWeightArray_4)

	Best = ["s",s]

	if a1>s and a1>s :
		Best = ["a1",a1]
		WeightArray = NewWeightArray_1
	if a2>a1 and a2>s :
		Best = ["a2",a2]
		WeightArray = NewWeightArray_2
	if a3>a2 and a3>s:
		Best = ["a3",a3]
		WeightArray = NewWeightArray_3
	if a4>a3 and a4>s:
		Best = ["a4",a4]
		WeightArray = NewWeightArray_4
	if alert:
		print Best[0],"score: ",Best[1]
		print WeightArray[0],WeightArray[1],WeightArray[2],WeightArray[3]
		print i 
	
	global BestWeight
	BestWeight = WeightArray
	TrainDataFile=open("BestWeight.txt","w")
	BestWeightText=""
	for weight in BestWeight:
		BestWeightText+=str(weight)+"\n"
	TrainDataFile.write(BestWeightText)






def training(SentenceList):
	for i in range(len(SentenceList)):
		SentenceList[i] =Sentence2WordArray(SentenceList[i])
	CommonArray=[]
	for Common in SentenceList:
		for i in range(len(SentenceList)):	
			CommonArray.append(compare_Learn(SentenceList[i],Common))
			

	global BestWeight
	CompareComputer(CommonArray,BestWeight)

	print BestWeight



BestWeightContent = open("BestWeight.txt","r").readlines()


global BestWeight
BestWeight = []
for Weight in BestWeightContent:
	BestWeight.append(int(Weight))
##################train 1

#SentenceList=["今天的天氣真差","天氣真差","天氣超級差的","最近的天氣真差"]
#training(SentenceList)



##################train 2


#SentenceList=["最近心情不太好","最近心情不太好"]
#training(SentenceList)


##################train 3
#SentenceList=["最近的心情不太好","心情不太好耶","最近心情不太好"]
#training(SentenceList)



##################train 4
#SentenceList=["肚子餓","現在肚子餓","肚子餓了","肚子有點餓了"]
#training(SentenceList)

##################train 5
#SentenceList=["開心","真開心","超級開心的","今天超開心"]
#training(SentenceList)

##test two sentence

print compare_Sentence(Sentence2WordArray("你好今天天氣真差"),Sentence2WordArray("你好今天天氣真差"))
print compare_Sentence(Sentence2WordArray("安安你好今天的天氣真差"),Sentence2WordArray("你好今天天氣真差"))
print compare_Sentence(Sentence2WordArray("今天的天氣真差"),Sentence2WordArray("天氣真差"))
print compare_Sentence(Sentence2WordArray("你好今天的天氣真差"),Sentence2WordArray("天氣差"))
print compare_Sentence(Sentence2WordArray("超級開心的"),Sentence2WordArray("真開心"))
print compare_Sentence(Sentence2WordArray("今天的天氣真差"),Sentence2WordArray("今天的天氣真好"))
print compare_Sentence(Sentence2WordArray("現在肚子餓"),Sentence2WordArray("今天的天氣真差"))













