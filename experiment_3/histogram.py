"""
Plotting histogram of sequences lengths and their transcript types.
"""


from Bio import SeqIO
import plotly.plotly as py
import plotly.offline
import plotly.graph_objs as go
import sys

file_name = ""

if len(sys.argv) < 2:
    exit("Please pass the fasta file path.")
else:
    file_name = sys.argv[1]    

counts = {}
counts_percentage = {}
total = 0

fasta_sequences = SeqIO.parse(file_name, 'fasta')

for seq in fasta_sequences:
    transcript_type = str(seq.id).split("|")[-2]
    if transcript_type in counts:
        length = len(seq)
        counts[transcript_type] += length
        total += length
    else:
        length = len(seq)
        counts[transcript_type] = len(seq)
        total += length


for key, value in counts.iteritems():
    counts_percentage[key] = (float(value) / total) * 100


types = counts.keys()
frequency = counts.values()

data = [go.Bar(
    x= types,
    y= frequency
)]

fig = go.Figure(data=data)
plotly.offline.plot(fig, filename='histogram.html', auto_open=False)
