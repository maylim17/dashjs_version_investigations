import pandas as pd
import matplotlib.pyplot as plt
import sys

results_folder = input("Enter results folder: ")
csv_allmetrics = results_folder + "/allmetrics.csv"
csv_tputpushed = results_folder + "/tputpushed.csv"

plt.rcParams["figure.figsize"] = [7.50, 3.50]
plt.rcParams["figure.autolayout"] = True

# allmetric_header1 = ['timestamp', 'last_tc_value', 'throughput']
# allmetric_header2 = ['timestamp', ]

# tputpushed_header = ['timestamp', 'tc_value', 'dash_value']

# df = pd.read_csv(csv_allmetrics, names=allmetric_header1)

# df.set_index('timestamp').plot()


f_tputpushed = open(csv_tputpushed, 'r')
lines_tputpushed = f_tputpushed.readlines()
data_tputpushed = {}
for line in lines_tputpushed:
    line = line.strip().replace('\n', '')
    if 'dashjs' in line:
        values = line.split(', ')
        tput_tc = values[1]
        tput_dash = values[2]
        client_id = values[3]

plt.show()