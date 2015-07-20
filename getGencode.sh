#!/bin/bash

curl -O http://hgdownload.cse.ucsc.edu/goldenPath/hg19/database/wgEncodeGencodeBasicV19.txt.gz
gunzip -c wgEncodeGencodeBasicV19.txt.gz > wgEncodeGencodeBasic_hg19
echo '{ "cgdata" : {"name" : "gencode_hg19", "type" : "genePredExt", "assembly" : "hg19"} }' > wgEncodeGencodeBasic_hg19.json
