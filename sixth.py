import random
import fifth
import pandas as pd
def check():
    pass
a = {}
data = pd.read_csv('dataset2.txt',header = None, sep=' ')
list = (data[3])
#print(list)
list2 =( data[2])
#print(list2)
itr = 0
try:
    for i in list2:
        a[i] = str(list[itr])
        #print(i,"asdffffffff")
        #a[i] = list2[itr]
        #print(i)

        itr+=1
except KeyError:
    pass
global hitratiocnt
hitratiocnt = 0
for tend in range(2):

    userId = random.choice(list2)
#userId = 917504
    flag = False
    curCluster = None
    for clusterCount in range(0,fifth.numbOfTextFilesGenerated):
        st = str(clusterCount)+".txt"
        f = pd.read_csv(st,header = None, sep=' ')
        print(f[2])
        for i in f[2]:

            if i == userId:

                curCluster = clusterCount
                flag= True
        if(flag):

            break

    if curCluster is None:

        print("Retrieved from server")
    s = str(a[userId])
    #forwardSlash = s.find("//")

    #url = s[forwardSlash:].split("/")
    url = s[10:].split("/")
    url = (url[:3])
    #print(url)
    st = "cache2"+str(clusterCount)+".txt"
    df = pd.read_csv(st, header=None, sep='///')

    for i in df[0]:
        #print(str(url)+"    "+str(i))
        if str(url) == str(i):
            #print("Fetched from cache! ")
            hitratiocnt+=1
            break
    #print(df)
    #fcac=open(str,"r")
    #fcac.read()

    print(clusterCount)
    #print(list2)
    #print(random.choice(list2))
    #fh = open("dataset.txt",'r')
    print(str(tend)+"random value generated")
print(hitratiocnt)