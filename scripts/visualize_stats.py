import json
import plotly.plotly as py
import plotly.graph_objs as go
import plotly.offline

complete_clean = {"complete_genes": {"max": [], "min": [], "mean": [], "median": [], "std": []},
                  "complete_loci": {"max": [], "min": [], "mean": [], "median": [], "std": []}}

complete_mixed = {"complete_loci": {"max": [], "min": [], "mean": [], "median": [], "std": []},
                  "no_genes": {"max": [], "min": [], "mean": [], "median": [], "std": []},
                  "no_loci": {"max": [], "min": [], "mean": [], "median": [], "std": []}}

incomplete_mixed = {"complete_genes": {"max": [], "min": [], "mean": [], "median": [], "std": []},
                    "complete_loci": {"max": [], "min": [], "mean": [], "median": [], "std": []},
                    "no_genes": {"max": [], "min": [], "mean": [], "median": [], "std": []},
                    "no_loci": {"max": [], "min": [], "mean": [], "median": [], "std": []}}

kmers = [str(k) for k in range(21, 101, 2)]

for kmer_size in range(21, 101, 2):
    file_name = "json/res" + str(kmer_size) + "_stats.json"
    with open(file_name, 'r') as f:
        data = json.load(f)
        cc = data["_complete_clean"]
        cm = data["_complete_mixed"]
        im = data["_incomplete_mixed"]

        ## Complete Clean -------------------------
        for feature in ["complete_genes", "complete_loci"]:
            for stat in ["max", "min", "mean", "median", "std"]:
                complete_clean[feature][stat].append(cc[stat][feature])

        ## Complete Mixed -------------------------
        for feature in ["complete_loci", "no_genes", "no_loci"]:
            for stat in ["max", "min", "mean", "median", "std"]:
                complete_mixed[feature][stat].append(cm[stat][feature])

        ## inComplete Mixed -------------------------
        for feature in ["complete_genes", "complete_loci", "no_genes", "no_loci"]:
            for stat in ["max", "min", "mean", "median", "std"]:
                incomplete_mixed[feature][stat].append(im[stat][feature])

vis_complete_clean = []
vis_complete_mixed = []
vis_incomplete_mixed = []


## Complete Clean -------------------------
for feature in ["complete_genes", "complete_loci"]:
    for stat in ["max", "min", "mean", "median", "std"]:
        plot = go.Scatter(
            x=kmers,
            y=complete_clean[feature][stat],
            mode='lines+markers',
            name=feature + " " + stat
        )
        vis_complete_clean.append(plot)


## Complete Mixed -------------------------
for feature in ["complete_loci", "no_genes", "no_loci"]:
    for stat in ["max", "min", "mean", "median", "std"]:
        plot = go.Scatter(
            x=kmers,
            y=complete_mixed[feature][stat],
            mode='lines+markers',
            name=feature + " " + stat
        )
        vis_complete_mixed.append(plot)


## inComplete Mixed -------------------------
for feature in ["complete_genes", "complete_loci", "no_genes", "no_loci"]:
    for stat in ["max", "min", "mean", "median", "std"]:
        plot = go.Scatter(
            x=kmers,
            y=incomplete_mixed[feature][stat],
            mode='lines+markers',
            name=feature + " " + stat
        )
        vis_incomplete_mixed.append(plot)

layout = dict(title='<b>Kmers Clustering Assessment</b>',
              xaxis=dict(title='<b>Kmer Size</b>'),
              yaxis=dict(title='<b>Value</b>', type="log"),
              )

fig_complete_clean = dict(data=vis_complete_clean, layout=layout)
fig_complete_mixed = dict(data=vis_complete_mixed, layout=layout)
fig_incomplete_mixed = dict(data=vis_incomplete_mixed, layout=layout)

plotly.offline.plot(fig_complete_clean,
                    filename="complete_clean.html", auto_open=False)

plotly.offline.plot(fig_complete_mixed,
                    filename="complete_mixed.html", auto_open=False)

plotly.offline.plot(fig_incomplete_mixed,
                    filename="incomplete_mixed.html", auto_open=False)