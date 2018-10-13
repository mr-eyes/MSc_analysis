# Experiments

## CD-HIT

```bash
cd cd-hit/
bash run.sh <fasta_path> <similarity> <word_size> <output_folder>
```

## Kallisto

```bash
cd kmers_clustering/
bash run.sh <fasta_path> <kmer_size> <output_folder>
```

## KProcessor

```bash
cd cd-hit/
./Kprocessor index -i <fasta_path> -o <output_file> -k <kmer_size> --names <names_file>
```