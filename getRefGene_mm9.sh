#!/bin/bash

curl -O http://hgdownload.cse.ucsc.edu/goldenPath/mm9/database/refGene.txt.gz
gunzip -c refGene.txt.gz > refGene_mm9
echo '{ "name" : "gencode_mm10", "type" : "genePredExt", "assembly" : "mm10", "url":"http://hgdownload.cse.ucsc.edu/goldenPath/mm9/database/refGene.txt.gz "}' > refGene_mm9.json
