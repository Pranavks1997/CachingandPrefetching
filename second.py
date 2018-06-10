from sklearn.cluster import Birch
import  pandas as pd
from matplotlib import pyplot as py
#import third.py
global dicc
dicc = dict()
def generalization(list,list2):
    dic = dict()
    print((list2))
    for i in range(len(list)):
        #print(list[i][0:3])
        if str(list[i][0:3]) not in dic:
            dic[str(list[i][0:3])]=list2[i]
        else:
            dic[str(list[i][0:3])]+=list2[i]
    dicc = dic.copy()
    return dic
    #
    # print(dic)

def compute( df):
    thirdcol = df[3]
    fifthcol = df[5]
    list1 = []
    list2=[]
    for i in range(len(df)):
        urlstr = str(thirdcol[i])
        timecal=float(fifthcol[i])
        url = urlstr[10:].split("/")
        list1.append(url)
        list2.append(timecal)
    dic = generalization(list1,list2)
    global dicc
    dicc = dic.copy()

#def asdf():
#    return dicc
    for i in dic.keys():
        pass
        #print(url)
        #st = df[[3][i]]
        #s = st[10:]
    #print(df[3])

def generalizationLater(list):#,list2):
    dic = dict()

    for i in range(len(list)):
        #print(list[i][0:3])
        if str(list[i][0:3]) not in dic:
            dic[str(list[i][0:3])]=0
        else:
            dic[str(list[i][0:3])]+=1
    diccc = dic.copy()
    return dic
    #
    # print(dic)

def computeLater( df):
    thirdcol = df[3]
    fifthcol = df[5]
    list1 = []
    list2=[]
    for i in range(len(df)):
        urlstr = str(thirdcol[i])
        timecal=float(fifthcol[i])
        url = urlstr[10:].split("/")
        list1.append(url)
        #list2.append(timecal)
    dic = generalizationLater(list1)#,list2)
    global diccc
    diccc = dic.copy()
    #for k,v in sorted(diccc.iteritems(), key=lambda(k,v):(v,k)):
    l =[]
    sred = list(sorted(diccc.items(), key=lambda value: value[1]))
    #for k,v in diccc.values():
     #   pass
    #l= diccc.values().sort()
    print(sred[-5:],"asdfasdfdsfsdfddddddddddddddddddd")
    return (sred[-5:]) #TODO: CHANGE THE NUMBER OF LINKS RETRIEVEDD IF NEEDED TO

    #templist=sred[-5:]
    #print(diccc)
    #return diccc


#def asdf():
#    return dicc
    #for i in dic.keys():
     #   pass
        #print(url)
        #st = df[[3][i]]
        #s = st[10:]
    #print(df[3])


data = pd.read_csv('dataset.txt',header = None, sep=' ')
#while(True):
compute(data[[3,5]])

x= []
x1 = data[2]
#print(x1)
y = data[3]
z = data[5]
#print(len(data))
for i in range(len(data)):#len(data)):
    try:
        x11 = ("%.2f" % (x1[i]/1000000) )#data[2][i]
        #print(type(x11))
        a = data[3][i]
        ab=a[10:].split("/")
        abc=ab[0:3]
        '''print(abc)#,"abcabcabc\n")
        print(dicc[str(abc)])#,"dsafdsf")#dicc[abc],"dicdicididic\n")'''
        y1 = dicc[str(abc)]
        #y1 = y[i]#data[3][i]
        #z1 =
        z1= ("%.2f" % (z[i]/1000000) )#z[i]#data[5][i]
        #print(x11,z1)
        listt = [float(x11),y1]#,float(z1)]
        py.scatter(x11,y1,color='g')
        #py.plot(x11,y1,z1)
        #print(listt)
        x.append(listt)
        #print(x,"vvvvvvvvvvvvvvvvvvvv")
    except ValueError:
        break
    except AttributeError:
        pass
#py.show()
# x = [[0,1,111],[0.3,1,0.7],[-0.3,1,0.9]]


#print(x)
brc = Birch(branching_factor=50, n_clusters = None, threshold= 0.5, compute_labels= True)

brc.fit(x)
#Birch(branching_factor= 50, compute_labels= True , copy= True, n_clusters= None, threshold= 0.5)
#for i in brc.predict(x):
print(brc.predict(x))
hosalist=brc.predict(x)
nanlist=list()
vijay=[]
doddlist=list()
for nanclustnum in range(0,max(hosalist)+1,1):
    cnt=0
    for ll in hosalist:
        if ll==nanclustnum:
            vijay.append(cnt)

        cnt+=1
    doddlist.append(vijay)
    vijay = []
print("vijay",vijay)
print("doddlist",doddlist)
print("nanclustnum",nanclustnum)
global numbOfTextFilesGenerated
numbOfTextFilesGenerated = 0
for j in range(0,max(hosalist)+1,1):
#    for i in doddlist[j]:
 #       l=i
  #      innondcnt=0
    filename = str(str(j) + ".txt")
    #print(filename)
    filehandler = open(filename,"w+")
    numbOfTextFilesGenerated
    numbOfTextFilesGenerated += 1
    hosafile=open('dataset.txt',"r")
    for k,line in enumerate(hosafile):

        if k in doddlist[j]:
            print(k,line)
            filehandler.write(line)
    filehandler.close()
    hosafile.close()

        #l=l+1
        #innondcnt+=1
    #print("jjjjjjjjjjjjjj")



# frequency count for the cluster files generated helper methods: genralizationLater

for x in range(numbOfTextFilesGenerated):
    st = str(str(x)+".txt")
    data = pd.read_csv(st, header=None, sep=' ')
    # while(True):
    dictReturned = computeLater(data[[3, 5]])
    st = "cache2" + str(x) + ".txt"
    fh = open(str(st), 'w+')
    for i in dictReturned:
        r,t = i
        fh.write(str(r))
        fh.write("///")
        fh.write(str(t))
        fh.write("\n")
        #print(str(r)+"sadfadsfadsf"+str(t))
    #print(st)
    #fh.write(str(dictReturned))
    #fh.write("\n")
    fh.close()
    #print(diccc)
    '''for i in range(numbOfTextFilesGenerated):
        st = "cache1"+str(i)+".txt"
        fh = open(str(st),'w')
        for k in dicc.keys():
            fh.write(str(k))
            fh.write("\n")
        fh.close()'''


