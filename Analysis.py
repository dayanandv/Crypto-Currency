from matplotlib import legend
import pandas as pd
import matplotlib.pyplot as plt
import glob
import networkx as nx
from tqdm import tqdm

path = '/home/dayanand/Projects/Crypto Currency/dataset/data'
all_files = glob.glob(path + "/*.csv")
coins = []

merged = pd.read_csv('/home/dayanand/Projects/Crypto Currency/2/bitcoin.csv', usecols=['Date', 'Volume'], thousands=',')
merged['Date'] = pd.to_datetime(merged['Date'])
merged.sort_values(by=['Date'],inplace=True, ascending=True)

for iter, filename in enumerate(tqdm(all_files, desc='Reading files')):
    # print('Reading ', filename)
    df = pd.read_csv(filename, usecols=['Date', 'Volume'], thousands=',')
    df['Date'] = pd.to_datetime(df['Date'])
    # df['Volume'] = df['Volume'].astype('float')
    df.sort_values(by=['Date'],inplace=True, ascending=True)
    # merged = pd.merge_asof(merged, df, on='Date')
    merged = pd.merge(merged, df, on='Date', how='outer', suffixes=(None, '_' + str(filename).split('/')[-1].split('.')[0]))
    # coins.append(df) #Unused as of now

# print(merged)

merged.set_index('Date').plot(legend=False)
plt.show()

corrs = merged.corr()
print(corrs)
corrs.to_csv('/home/dayanand/Projects/Crypto Currency/corrs.csv')

#***********************************************************************************************************************
# TODO: Reduce dimensions or filter and get rid of smaller values of corr.
#***********************************************************************************************************************

G = nx.from_numpy_matrix(corrs.values, parallel_edges=True, create_using=nx.Graph())
label_mapping = {idx: val for idx, val in enumerate(corrs.columns)}
G = nx.relabel_nodes(G, label_mapping)
degs = nx.degree(G)
#nx.draw(G, node_size=[v * 100 for v in degs.values()], with_labels=True)
nx.write_gexf(G, '/home/dayanand/Projects/Crypto Currency/coins.gexf')
plt.show()