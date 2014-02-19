import string, os, sys

if len(sys.argv[:])!=4:
    print "python mergeRefGene.py refGeneGB refgene_good(merged good model, see notes) multiple_multipleIsland (see notes)"
    print "****multiple island output to file=multiple_multipleIsland\n"
    sys.exit()
    
fin=open(sys.argv[1],'r')
fout=open(sys.argv[2],'w')
fmulti =open(sys.argv[3],'w')

refdic={}
for line in fin.readlines():
    line =string.strip(line)
    data= string.split(line,'\t')
    gene= data[12]
    if refdic.has_key(gene):
        refdic[gene].append(data)
    else:
        refdic[gene]=[data]
fin.close()

genes = refdic.keys()
print len(genes)

islandDic={}
c=0
for gene in genes:
    allData = refdic[gene]
    #only one entry for this gene
    if len(allData) ==1:
        fout.write(string.join(allData[0],'\t')+'\n')
        continue

    #more then one entry, build islands for each gene 
    if not islandDic.has_key(gene):
        islandDic[gene]=[]
    for data in allData:
        overlap=0
        for i in range (0, len(islandDic[gene])):
            island=islandDic[gene][i]
            start = int(island[4])
            end =int(island[5])
            proStart =int(island[6])
            proEnd =int(island[7])
            chr =island[2]
            strand =island[3]
            if data[3] != strand or data[2] != chr:
                continue
            if end < int(data[4]) or int(data[5]) < start:
                continue
            #same island
            overlap =1
            if int(data[4]) < start:
                islandDic[gene][i][4] =int(data[4])
            if int(data[5]) > end:
                islandDic[gene][i][5] = int(data[5])
            if int(data[6]) < proStart:
                islandDic[gene][i][6] =int(data[6])
            if int(data[7]) > proEnd:
                islandDic[gene][i][7] = int(data[7])
            break
        if not overlap:
            islandDic[gene].append(data)

    #merge island if needed
    allIslands = islandDic[gene]
    allGoodIslands =[]
    for i in range (0, len(allIslands)):
        good =1
        for j in range (i+1, len(allIslands)):
            if allIslands[i][3] != allIslands[j][3] or allIslands[i][2] != allIslands[j][2]:
                continue
            if int(allIslands[i][5]) < int(allIslands[j][4]) or int(allIslands[j][5]) < int(allIslands[i][4]):
            #if end < int(data[4]) or int(data[5]) < start:
                continue
            good =0
            if int(allIslands[i][4]) < int(allIslands[j][4]):
                allIslands[j][4] = int(allIslands[i][4])
            if int(allIslands[i][5]) > int(allIslands[j][5]):
                allIslands[j][5] = int(allIslands[i][5])
            if int(allIslands[i][6]) < int(allIslands[j][6]):
                allIslands[j][6] =int(allIslands[i][6])
            if int(allIslands[i][7]) < int(allIslands[j][7]):
                allIslands[j][7] =int(allIslands[i][7])
            break
        if good:
            allGoodIslands.append(allIslands[i])
    islandDic[gene]= allGoodIslands[:]
    
    # for each island, build the maximum gene model.
    allIslands = islandDic[gene]
    for island in allIslands:
        #collect myData for each island
        myData=[]
        start = int(island[4])
        end =int(island[5])
        chr =island[2]
        strand =island[3]
        for data in allData:
            if data[3] != strand or data[2] != chr:
                continue
            if end < int(data[4]) or int(data[5]) < start:
                continue
            myData.append(data)
        segments=[]
        for data in myData:
            n= int(data[8])
            starts = string.split(data[9],',')
            ends = string.split(data[10],',')
            for i in range (0,n):
                overlap=0
                for j in range (0, len(segments)):
                    #not overlap
                    if int(ends[i]) < int(segments[j][0]) or int(segments[j][1]) < int(starts[i]):
                        continue
                    overlap=1
                    if int(starts[i]) < int(segments[j][0]):
                        segments[j][0] =str(int(starts[i]))
                    if int(ends[i]) > int(segments[j][1]):
                        segments[j][1] = str(int(ends[i]))
                    #break
                if not overlap:
                    segments.append([starts[i],ends[i]])
            segments.sort()

        # uniq set of segments
        u_segments=[]
        for seg in segments:
            if seg not in u_segments:
                u_segments.append(seg)
        segments=u_segments

        #ouptut for each island
        output = island
        if len(islandDic[gene])!=1:
            for i in range (0,8):
                fmulti.write(str(output[i])+'\t')
            fmulti.write(str(len(segments))+'\t')
            for i in range (0,len(segments)):
                fmulti.write(str(segments[i][0])+',')
            fmulti.write('\t')
            for i in range (0,len(segments)):
                fmulti.write(str(segments[i][1])+',')
            fmulti.write('\t')
            fmulti.write(string.join(output[11:],'\t')+'\n')
        else:
            for i in range (0,8):
                fout.write(str(output[i])+'\t')
            fout.write(str(len(segments))+'\t')
            for i in range (0,len(segments)):
                fout.write(str(segments[i][0])+',')
            fout.write('\t')
            for i in range (0,len(segments)):
                fout.write(str(segments[i][1])+',')
            fout.write('\t')
            fout.write(string.join(output[11:],'\t')+'\n')

    if len(islandDic[gene])!=1:
        c= c+1
print c
fout.close()
fmulti.close()

# total 24847
# one transcript 15346
# multiple transcript, one island 8187
# multiple islands 1314

# python refgene_to_bed.py multiple_multipleIsland > output
# cut -f 1,4,6,10,11 output|grep -v "_" |sort |uniq -c > stats_multiple_structure
