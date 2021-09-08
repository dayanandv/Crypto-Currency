from matplotlib import legend
import pandas as pd
import matplotlib.pyplot as plt
import glob
import networkx as nx
from tqdm import tqdm
import os

cur_dir = os.getcwd()
path = cur_dir+'/dataset/dummy'
all_files = glob.glob(path + "/*.csv")
coins = []

merged = pd.read_csv(cur_dir+'/dataset/bitcoin.csv', usecols=['Date', 'Close**'], thousands=',')
merged['Date'] = pd.to_datetime(merged['Date'])
merged.sort_values(by=['Date'],inplace=True, ascending=True)

for iter, filename in enumerate(tqdm(all_files, desc='Reading files')):
    # print('Reading ', filename)
    df = pd.read_csv(filename, usecols=['Date', 'Close**'], thousands=',')
    df['Date'] = pd.to_datetime(df['Date'])
    # df['Volume'] = df['Volume'].astype('float')
    df.sort_values(by=['Date'],inplace=True, ascending=True)
    # merged = pd.merge_asof(merged, df, on='Date')
    merged = pd.merge(merged, df, on='Date', how='outer', suffixes=(None, '_' + str(filename).split('/')[-1].split('.')[0]))
    # coins.append(df) #Unused as of now

merged.to_csv(cur_dir+'/merged.csv', index=False)
merged.set_index('Date').plot(legend=False)
plt.show()

corrs = merged.corr()
#print(corrs)
corrs.to_csv(cur_dir+'/corrs.csv')

#***********************************************************************************************************************
# TODO: Reduce dimensions or filter and get rid of smaller values of corr.
#***********************************************************************************************************************

G = nx.from_numpy_matrix(corrs.values, parallel_edges=True, create_using=nx.Graph())
label_mapping = {idx: val for idx, val in enumerate(corrs.columns)}
G = nx.relabel_nodes(G, label_mapping)
degs = nx.degree(G)
pos=nx.spectral_layout(G)
nx.draw(G, pos, node_size=[i * 100 for (v,i) in degs], with_labels=True)
labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
nx.write_gexf(G, cur_dir+'/coins.gexf')
# nx.write_graphml(G, cur_dir+'/coins.graphml')
plt.show()