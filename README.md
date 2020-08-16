Disclaimer: This repository is incomplete and being worked on.

# BLAST alignments

## Background

From Wikipedia on August 16th 2020:

> In bioinformatics, BLAST (basic local alignment search tool) is an algorithm and program for comparing primary biological sequence information, such as the amino-acid sequences of proteins or the nucleotides of DNA and/or RNA sequences. A BLAST search enables a researcher to compare a subject protein or nucleotide sequence (called a query) with a library or database of sequences, and identify library sequences that resemble the query sequence above a certain threshold. 

For more information on BLAST, please refer to:
https://en.wikipedia.org/wiki/BLAST_(biotechnology)
https://blast.ncbi.nlm.nih.gov/Blast.cgi

## Code

This repository contains a colleciton basic tools neeeded to execute BLAST searches. A useful method to avoid cumbersome installations of dependecies is to launch a docker container and run the code inside of it. To install docker, please follow the instructions in their website:

https://www.docker.com/

After the installation is complete, go to terminal and type the following code:

```
docker run -it -v ~/local/folder/to/map:/biopython biopython/biopython /bin/bash
```

This will cause a laundry list of installations that you don't have to worry about. Once it is complete, you'll be at the command line of a docker container that has all the tools that you need to continue with these instructions.
