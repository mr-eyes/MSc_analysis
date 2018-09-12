from Bio import SeqIO
import plotly.plotly as py
import plotly.offline
import plotly.graph_objs as go

counts = {}
counts_percentage = {}
total = 0

fasta_sequences = SeqIO.parse(open("gencode.v28.transcripts.fa"), 'fasta')

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