# BLAST alignments

## Background

From Wikipedia on August 16th 2020:

> In bioinformatics, BLAST (basic local alignment search tool) is an algorithm and program for comparing primary biological sequence information, such as the amino-acid sequences of proteins or the nucleotides of DNA and/or RNA sequences. A BLAST search enables a researcher to compare a subject protein or nucleotide sequence (called a query) with a library or database of sequences, and identify library sequences that resemble the query sequence above a certain threshold. 


# Code

This repository contains a colleciton basic tools neeeded to execute BLAST searches. A useful method to avoid cumbersome installations of dependecies is to launch a docker container and run the code inside of it:
```
docker run -it -v ~/local/folder/to/map:/biopython biopython/biopython /bin/bash
```
