#!/bin/bash

curl -O http://hgdownload.cse.ucsc.edu/goldenPath/hg38/database/wgEncodeGencodeCompV23.txt.gz
gunzip -c wgEncodeGencodeCompV23.txt.gz > wgEncodeGencodeCompV23
echo '{ "type" : "genePredExt", "assembly" : "hg38", "url":"http://hgdownload.cse.ucsc.edu/goldenPath/hg38/database/wgEncodeGencodeCompV23.txt.gz"}' > wgEncodeGencodeCompV23.json
