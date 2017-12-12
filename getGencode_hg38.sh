#!/bin/bash

curl -O http://hgdownload.cse.ucsc.edu/goldenPath/hg38/database/wgEncodeGencodeBasicV27.txt.gz
gunzip -c wgEncodeGencodeBasicV27.txt.gz > wgEncodeGencodeBasic_hg38
echo '{ "name" : "gencode_hg38", "type" : "genePredExt", "assembly" : "hg38", "url":"http://hgdownload.cse.ucsc.edu/goldenPath/hg38/database/wgEncodeGencodeBasicV27.txt.gz "}' > wgEncodeGencodeBasic_hg38.json
