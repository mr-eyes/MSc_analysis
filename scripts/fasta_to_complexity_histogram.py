from Bio import SeqIO
import sys
import os
import plotly.plotly as py
import plotly.offline
import plotly.graph_objs as go
from collections import Counter
from tqdm import tqdm

def calculateDustScore(read):
    dec = {}
    if(len(read) < 3):
        return 0.0
    for i in range(0, len(read)-2):
        s = read[i:i+3]
        if s not in dec:
            dec[s] = 1
        else:
            dec[s] = dec[s]+1
    sum_val = 0.0
    for i in range(0, len(dec)):
        tc = float(dec.values()[i])
        score = (tc*(tc-1))/2.0
        sum_val = sum_val+score

    return sum_val/(len(read)-2)

df = []

if len(sys.argv) < 3:
    exit("run: python [file_name] [kmer_size]")

file_name = sys.argv[1]
kmer_size = int(sys.argv[2])

file_type = "fasta"


if file_name.split(".")[-1] == "fastq":
    file_type = "fastq"

sequences = SeqIO.parse(open(file_name), file_type)
for seq in tqdm(sequences, total=203835): # Replace the number of sequences to view the progress bar
    seq = str(seq.seq)
    for i in range(len(seq) - kmer_size + 1):
        kmer = str(seq)[i:i+kmer_size]
        score = calculateDustScore(kmer)
        df.append(score)  

scores = Counter(df)

data = [go.Bar(
    x=scores.keys(),
    y=scores.values(),
)]

layout = go.Layout(
    title='<b>Complexity distribution of kmer: '+ str(kmer_size) +'</b>',
    xaxis=dict(title='<b>Complexity Score (bp)</b>',),
    yaxis=dict(title='<b>Number of occurence</b>',)
)

print ("Generating histogram.html ...")
fig = go.Figure(data=data, layout=layout)
plotly.offline.plot(fig, filename='k'+ str(kmer_size) + '_histogram.html', auto_open=False)
