#coding:utf-8
# making chinese sentence to a set of words
import jieba

def Sentence2WordArray(T="安安你好今天的天氣真差"):
	
	seglist = jieba.cut(T, cut_all=False)
	result=[]
	for p in seglist: result.append(p)
	return result


def compare(a,b,alert=0):#len(a)>(b)
	
	if len(a)<len(b):
		c = a
		a = b
		b = c
	############################################	
	
	lendef=abs(len(a)-len(b))
	R1= 1-float(lendef)/len(a) #1
	if alert:
		print "#1 lendef(n) :",R1

	###
	CommonNum=0
	for p1w in a:
		for p2w in b:
			if p1w==p2w: CommonNum+=1
	
	CommonRate=1-float(CommonNum)/len(a)
	R2 = 1-CommonRate #2	
	if alert:
		print "#2 CommonRate% :",R2	
	###

	CommonTextCommonPosition = 1
	for i in range(len(b)-1):
		try:
			if abs(int(a.index(b[i+1]))-int(a.index(b[i])))<=1:
				CommonTextCommonPosition+=1
		except:
			CommonTextCommonPosition = CommonTextCommonPosition
	R3 = float(CommonTextCommonPosition)/len(b) #3	
	if alert:
		print "#3 diff:",R3

	###
	CommonTextCommonPosition2 = 1
	for i in range(len(b)-1):
		try:
			if abs(int(a.index(b[i+1]))-int(a.index(b[i])))<=2:
				CommonTextCommonPosition2+=1
		except:
			CommonTextCommonPosition2 = CommonTextCommonPosition2
	R4 = float(CommonTextCommonPosition2)/len(b) #4	
	if alert:
		print "#4 diff:",R4
	###
	###
	print "相似度",(R1+R2+R3+R4)/4*100,"%"
	return R1,R2,R3,R4
	
		

def AdjestWeight(t,w):
	
	NewData=[]
	for i in t:
		NewData.append((i[0]*w[0]+i[1]*w[1]+i[2]*w[2]+i[3]*w[3])/(w[0]+w[1]+w[2]+w[3]))
	#print NewData[0],NewData[1],NewData[2],NewData[3],NewData[4]
	print (NewData[0]+NewData[1]-NewData[2]-NewData[3]-NewData[4])*100/2
	return (NewData[0]+NewData[1]-NewData[2]-NewData[3]-NewData[4])*100/2




def CompareComputer(CommonArray,WeightArray=[1,1,1,1],i=0):
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

	print Best[0],"score: ",Best[1]
	print WeightArray[0],WeightArray[1],WeightArray[2],WeightArray[3]
	print i 
	if i<10:
		CompareComputer(CommonArray,WeightArray,i+1)
	else:
		global BestWeight
		BestWeight = WeightArray


#p = Sentence2WordArray("等等想要去吃點什麼嗎")安安你好今天的天氣真差
#for i in p: print i

#p1 = Sentence2WordArray()

global BestWeight
BestWeight = [1,1,1,1]


def training(SentenceList):
	for i in range(len(SentenceList)):
		SentenceList[i] =Sentence2WordArray(SentenceList[i])


	Common_1 = compare(SentenceList[0],SentenceList[1])
	Common_2 = compare(SentenceList[0],SentenceList[2]) 
	Common_3 = compare(SentenceList[0],SentenceList[3])
	Common_4 = compare(SentenceList[0],SentenceList[4])
	Common_5 = compare(SentenceList[0],SentenceList[5])

	CommonArray = [Common_1,Common_2,Common_3,Common_4,Common_5]
	global BestWeight
	CompareComputer(CommonArray,BestWeight)

	print BestWeight
##################train 1
SentenceList=["安安你好今天的天氣真差","安安你好今天的天氣真差","你好今天天氣真差","最近天氣真差阿","最近天氣真好阿","你好等等想要去吃點什麼嗎"]
training(SentenceList)
##################train 2
SentenceList=["最近心情不太好","最近心情不太好","最近心情不是太好","最近天氣真差阿","最近天氣真好阿","你好等等想要去吃點什麼嗎"]
training(SentenceList)
##################train 3
SentenceList=["最近心情不太好","心情不太好耶","最近心情感覺到不是太好","安安你好今天的天氣真差","你好今天天氣真差","最近天氣真差阿"]
training(SentenceList)



















