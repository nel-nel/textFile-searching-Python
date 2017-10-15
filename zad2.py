def reading(fName):
    f=open(fName,'r')
    counter=0
    lstOfObj=[]
    for line in f:
        counter+=1
        variant = Anotation(line)
        lstOfObj.append(variant)
    return lstOfObj


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

        for i in atr:
            nameVal=i.split('=')
            name=str(nameVal[0])
            setattr(self,nameVal[0],nameVal[1])


def getChr(lstOfObj):
    allChr=[]
    for i in lstOfObj:
        if i.seqid not in allChr:
            allChr.append(i.seqid)
    print(allChr)
    dictChr= {x:0 for x in allChr}
    print(dictChr)
    return dictChr
        

    
def prove(arrOfObj,dictChr):
    allMistakes={};
    mistakes=[]
    for i in arrOfObj:
        if i.type=="deletion":
            if i.Variant_seq!='-':
                allMistakes+=1
                if i.seqid in dictChr:
                    dictChr[i.seqid]+=1     
    return dictChr


lstOfObj=reading(r'C:\Users\user\Downloads\exam\exam\a.gvf')
dictChr=getChr(lstOfObj)
prove(lstOfObj,dictChr)
