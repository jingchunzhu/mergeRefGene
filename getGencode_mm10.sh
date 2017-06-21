#!/bin/bash

curl -O http://hgdownload.cse.ucsc.edu/goldenPath/mm10/database/wgEncodeGencodeBasicVM11.txt.gz
gunzip -c wgEncodeGencodeBasicVM11.txt.gz > wgEncodeGencodeBasic_mm10
echo '{ "name" : "gencode_mm10", "type" : "genePredExt", "assembly" : "mm10", "url":"http://hgdownload.cse.ucsc.edu/goldenPath/mm10/database/wgEncodeGencodeBasicVM11.txt.gz "}' > wgEncodeGencodeBasic_mm10.json
