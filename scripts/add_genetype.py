#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
mapped = {"Gene" = ["tr_id_1","tr2,"tr3",...]}
"""

from Bio import SeqIO
import argparse
import os


def Main():
    mapped = {}

    with open(gtf_file_path, 'r') as gtf:
        for line in gtf:
            if line[0] == '#':
                continue
            fields = line.strip().split('\t')
            feature_type = fields[2]
            info = fields[-1].split('; ')

            if feature_type == 'transcript':
                gene_type = info[2].replace('"', '').split()[1]
                transcript_id = info[1].replace('"', '').split()[1]

                mapped[transcript_id] = gene_type

    with open(output_fasta, 'w') as output_handle:
        sequences = SeqIO.parse(open(original_fasta_file), 'fasta')
        for seq in sequences:
            transcript_id = seq.id.split('|')[0]
            gene_type = mapped[transcript_id]
            seq.id = seq.description = seq.name + gene_type + '|'
            SeqIO.write(seq, output_handle, 'fasta')


if __name__ == '__main__':
    original_fasta_file = ''
    gtf_file_path = ''
    output_fasta = ''

    parser = argparse.ArgumentParser()

    parser.add_argument(
        '-i', action='store', dest='original_fasta_file', help='The Original fasta file')

    parser.add_argument('-g', action='store', dest='gtf_file',
                        help='Set GTF File path')

    parser.add_argument('-o', action='store', dest='output_fasta_file',
                        help='New fasta file name')

    args = parser.parse_args()

    if args.gtf_file:
        if os.path.isfile(args.gtf_file):
            gtf_file_path = args.gtf_file
        else:
            exit('File: ' + args.gtf_file + 'Does not exist!')

        if args.original_fasta_file:
            if os.path.isfile(args.original_fasta_file):
                original_fasta_file = args.original_fasta_file
            else:
                exit('File: ' + args.original_fasta_file
                     + 'Does not exist!')

        if args.output_fasta_file:
            output_fasta = args.output_fasta_file
        else:
            output_fasta = 'new_' + original_fasta_file
    else:

        parser.print_help()
        exit(0)

    Main()
