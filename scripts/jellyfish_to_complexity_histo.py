from Bio import SeqIO
import sys
import os
import plotly.plotly as py
import plotly.offline
import plotly.graph_objs as go
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


df = {}

if len(sys.argv) < 3:
    exit("run: python [jellyFish file_name] [kmer_size]")

file_name = sys.argv[1]
kmer_size = int(sys.argv[2])

with open(file_name, "r") as kmers:
    for line in tqdm(kmers, total=130328323):
        line = line.split(" ")
        kmer = line[0]
        count = int(line[1])
        score = calculateDustScore(kmer)
        
        if score in df:
            df[score] += count
        else:
            df[score] = count

data = [go.Bar(
    x=df.keys(),
    y=df.values(),
)]

layout = go.Layout(
    title='<b>Complexity distribution of kmer: '+ str(kmer_size) +'</b>',
    xaxis=dict(title='<b>Complexity Score (bp)</b>',),
    yaxis=dict(title='<b>Number of occurence</b>',)
)

print ("Generating histogram.html ...")
fig = go.Figure(data=data, layout=layout)
plotly.offline.plot(fig, filename='k'+str(kmer_size)+'_jelly_histogram.html', auto_open=False)
