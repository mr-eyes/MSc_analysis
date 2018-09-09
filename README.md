# cdhit-clstr-simplifier

Simplify CD-HIT output ".clstr" file for better inspection.

## Clone (Recursively)
```sh
git clone --recursive https://github.com/mr-eyes/master-analysis.git 
```

## CD-HIT

  ## Handy Scripts (./handy_scripts)
``` 
handy_scripts
	└── cdhit_clstr_to_tsv.py  
```
1- cdhit_clstr_to_tsv.py : Convert the *.clstr output file of cd-hit to tabular file.

## Experiment_3 



 - **Data**: [Transcript sequences (ALL)](ftp://ftp.ebi.ac.uk/pub/databases/gencode/Gencode_human/release_28/gencode.v28.transcripts.fa.gz)
- **Word Size:** 6
- **Similarity threshold:** 0.85 
- **MAX_RAM:** 20 GB
- **No. Threads:** 32
- **Data Download:** ``` bash download.sh```
- **Run :** ``` cd expirement_3; bash run.sh ```

> Alter the run.sh parameters to change previous config.
