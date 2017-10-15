
def reading(fName):
    f=open(fName,'r')
    counter=0
    arrOfObj=[]
    for line in f:
        counter+=1
        variant = Anotation(line)
        #print(variant.Variant_seq)
        arrOfObj.append(variant)
        break
    return arrOfObj
        

class Anotation:
    def    __init__(self,line):
        #cols are separated with tab
        ar = line.split('\t')
        #every col becomes an atribute for the object 
        self.seqid=ar[0]
        self.source=ar[1]
        self.type=ar[2]
        self.start=ar[3]
        self.end=ar[4]
        self.score=ar[5]
        self.strand=ar[6]
        self.phase=ar[7]
        self.atributes=ar[8]
        atr=self.atributes.split(';')
        #print(atr)
        for i in atr:
            #print(i)
            nameVal=i.split('=')
            #print(nameVal)
            name=str(nameVal[0])
            setattr(self,nameVal[0],nameVal[1])

def prove(arrOfObj):
    mistakes=0
    for i in arrOfObj:
        if i.type=="deletion":
            if i.Variant_seq=="-":
                mistakes+=1
    print(mistakes)    
    return mistakes
            


prove(reading(r'D:\My Documents\IT\BMI\Linux\exam\a.gvf'))







        
