# Experiments

## CD-HIT

```bash
cd cd-hit/
bash run.sh <fasta_path> <similarity> <word_size> <output_folder>
```

## kCluster

1- Run `kmers_clustering/install_kCluster.sh`

2- Prepare data for indexing using `kCluster/scripts/kProcessor_prepare.py <fasta_file>`

```bash
bash run.sh <prepared_fasta> <kmer_size> <output_dir>
```