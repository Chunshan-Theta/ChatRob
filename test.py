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
	
		
#p = Sentence2WordArray("等等想要去吃點什麼嗎")安安你好今天的天氣真差
#for i in p: print i

#p1 = Sentence2WordArray()



p=["安安你好今天的天氣真差","安安你好今天的天氣真差","你好今天天氣真差","最近天氣真差阿","最近天氣真好阿","你好等等想要去吃點什麼嗎"]
for i in range(len(p)):
	p[i] =Sentence2WordArray(p[i])


a1 = compare(p[0],p[1])
a2 = compare(p[0],p[2]) 
b1 = compare(p[0],p[3])
F1 = compare(p[0],p[4])
F2 = compare(p[0],p[5])

target = [a1,a2,b1,F1,F2]

w=[1,2,1,1]
NewData=[]
for i in target:
	NewData.append((i[0]*w[0]+i[1]*w[1]+i[2]*w[2]+i[3]*w[3])/(w[0]+w[1]+w[2]+w[3]))
print (NewData[0]+NewData[1]-NewData[2]-NewData[3]-NewData[4])*100

