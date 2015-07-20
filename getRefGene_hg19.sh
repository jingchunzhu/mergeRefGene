#!/bin/bash

curl -O http://hgdownload.cse.ucsc.edu/goldenPath/hg19/database/refGene.txt.gz
gunzip -c refGene.txt.gz > refGene_hg19
echo '{ "cgdata" : {"name" : "refGene_hg19", "type" : "genePredExt", "assembly" : "hg19"} }' > refGene_hg19.json
