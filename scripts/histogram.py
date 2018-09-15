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
filtered_counts = {}

fasta_sequences = SeqIO.parse(file_name, 'fasta')

for seq in fasta_sequences:
    length = len(seq)

    if length in counts:
        counts[length] += 1
    else:
        counts[length] = 1


for key, value in counts.iteritems():
    if value > 15:
        filtered_counts[key] = value

lengths = filtered_counts.keys()
no_seqs = filtered_counts.values()

data = [go.Bar(
    #histfunc = "count",
    x=lengths,
    y=no_seqs,

)]

layout = go.Layout(
    title='Seqs Lengths Vs. Occurence',
    xaxis=dict(
        title='Lengths (bp)'
    ),
    yaxis=dict(
        title='No. Of Seqs'
    )
)

fig = go.Figure(data=data, layout=layout)
plotly.offline.plot(fig, filename='histogram.html', auto_open=False)
