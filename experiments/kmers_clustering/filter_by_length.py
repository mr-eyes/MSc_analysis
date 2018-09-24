from Bio import SeqIO
import sys

original_fasta_file = sys.argv[1]
output_fasta = sys.argv[2]
threshold = int(sys.argv[3])

with open(output_fasta, 'w') as output_handle:
        sequences = SeqIO.parse(open(original_fasta_file), 'fasta')
        for seq in sequences:
            if len(seq) >= threshold:
                SeqIO.write(seq, output_handle, 'fasta')
