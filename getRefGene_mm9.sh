#!/bin/bash

curl -O http://hgdownload.cse.ucsc.edu/goldenPath/mm9/database/refGene.txt.gz
gunzip -c refGene.txt.gz > refGene_mm9
echo '{ "name" : "refGene_mm9", "type" : "genePredExt", "assembly" : "mm9", "url":"http://hgdownload.cse.ucsc.edu/goldenPath/mm9/database/refGene.txt.gz "}' > refGene_mm9.json
