import string, os, sys

fin =open("stats_multiple_structure",'r')
fout = open ("multiple_multipleIsland_good",'w')

dic={}
for line in fin.readlines():
    line =string.strip(line)
    data = string.split(line)
    gene =data[2]
    num =data[4]
    exons= data[5]
    if not dic.has_key(gene):
        dic[gene]=[]
    dic[gene].append(data)
fin.close()

badgenes=[]
for gene in dic.keys():
    islands = dic[gene]
    if len(islands) ==1:
        continue
    for i in range(1, len(islands)):
        same =1
        if islands[0][5] == islands[i][5]:
            continue
        one = string.split(islands[0][5],',')
        two= string.split(islands[i][5],',')
        two.reverse()
        if one  == two:
            continue
        same=0
    if not same:
        print gene
        badgenes.append(gene)

os.system ("grep -v chr[1-9]*_ multiple_multipleIsland > tmp")
frefgene= open("tmp",'r')
for line in frefgene.readlines():
    data = string.split(line)
    gene =data[2]
    if gene in badgenes:
        continue
    fout.write(line)
fout.close()
frefgene.close()
