import pandas as pd

records = (('Protokol č.:', 'tup', 'asdsad'),('ghg','df'))


b=('Koagulační faktor V', 'F5; G1691A (Leiden)', 'F5; NM_000130.4; c.1601G>A', 'G/G(WT)', 'Methyltetrahydrofolát reduktáza', 'MTHFR; C677T', 'MTHFR; NM_005957.4; c.665C>T', 'C/T(HET)', 'Methyltetrahydrofolát reduktáza', 'MTHFR; A1298C', 'MTHFR; NM_005957.4; c.1286A>C', 'A/C(HET)')
print(b)
for i in range(0, len(b),4):
	for j in range(i,i+4):
		print(b[j])
		print (i, j)
	print ("\n")

leiden=["Koagulační faktor V", "F5; G1691A (Leiden)", "F5; NM_000130.4; c.1601G>A"]
leiden.append("ahoj")
a = leiden
#print (leiden, a)
#data = {'mut':  ['leiden', 'protrombin', 'MT1', 'MT2'],
        #'>0.8': ['G/G(WT)', 'A/A(HOM)','T/T(HOM)','C/C(HOM)'],
         #'0.2-0.8' :['G/A(HET)','G/A(HET)','C/T(HET)','A/C(HET)'],
         #'<0.2' : ['A/A(HOM)', 'G/G(WT)','C/C(WT)', 'A/A(WT)']
        #}
#df = pd.DataFrame(data,columns=['mut', '>0.8', '0.2-0.8', '<0.2'])
#print df
#file = open('Data/003_19_Dvorakova.out.csv','r')

#f = pd.read_csv("Data/003_19_Dvorakova.out.csv", sep=',')
#b=pd.DataFrame(f)
#print f['report']
#print (b.loc[(b['Start'] == 169519049)])

#print (b.loc[((b['analysis'] == 'TROMBO_basic') | (b['analysis'] == 'TROMBO_full')) & (b['Start'] == 169519049) & (b['End'] == 169519049) & (b['Ref'] == 'T') & (b['Alt'] == 'C') & (b['report'] == True)])

##if not b.loc[((b['analysis'] == 'TROMBO_basic') | (b['analysis'] == 'TROMBO_full')) & (b['Start'] == 169519049) & (b['End'] == 169519049) & (b['Ref'] == 'T') & (b['Alt'] == 'C') & (b['report'] == True)].empty:
	#print ("YES")

#print (b)
#a=f.values.tolist()
##for row in range(0, len(client_list)):
	
#print (a)
#print f.loc[f['Chr' == 'chr1']]
#a = f.loc[:,['Chr']]
#print a[]
#for i in f.columns.tolist():
	#print f[i]
#print (f.loc[f['Chr' == 'chr1']])
#a=[]
#for line in file:
	#a.append(line.split(','))

#print a

#boxes = {'Color': ['Green','Green','Green','Blue','Blue','Red','Red','Red'],
         #'Shape': ['Rectangle','Rectangle','Square','Rectangle','Square','Square','Square','Rectangle'],
         #'Price': [10,15,5,5,10,15,15,5]
        #}

#df = pd.DataFrame(boxes, columns= ['Color','Shape','Price'])
#print df
#print df.loc[df['Color'] == 'Green']
#print (select_color)