from Bio import SeqIO
import sys
import os

if len(sys.argv) < 4:
    exit("Please pass required parameters\nhelp: python filter_by_length.py <fasta_file> <output_fasta_file> <length_threshold>")

original_fasta_file = sys.argv[1]
output_fasta = sys.argv[2] + "_" + os.path.basename(original_fasta_file)
threshold = int(sys.argv[3])

with open(output_fasta, 'w') as output_handle:
        sequences = SeqIO.parse(open(original_fasta_file), 'fasta')
        for seq in sequences:
            if len(seq) >= threshold:
                SeqIO.write(seq, output_handle, 'fasta')
