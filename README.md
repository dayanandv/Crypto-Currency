# Crypto-Currency

## An attempt at modeling relationship between crypto currencies using Network Science

Considering bitcoin as a base (since it has the longest timeline), the timeseries of 200 cryptocurrencies (coins) are parsed and merged (on the 'Volume' column as of now, may change to 'Close**') to a single dataframe. The correlation between columns are computed and dumped into the file corrs.csv. This correlation value is used to build a network with the coins as nodes and correlation valeus as edges.

## Ideas TODO:
1. The network has to be filtered out to remove low-significance edges (based on |corr value|) so that it is no longer a fully connected dense network.
2. Timeseries ('Date' column) has to be windowed and discretized to see how correlation values changes across the timeline
3. Graph embedding methods to be explored to apply GNN algos which can potentially help in prediction
4. Direct application of algorithms like Graph Attention Network (GAT) for tasks like link prediction are to be explored

## Potential applications:
1. Predicting the price of a dependent coin from the prices of 'market driving' coins by aggregation (weighted sum of neighbors?).
2. Study the price dynamics of coins newly introduced into the market (new nodes in the dynamic network) at it's initial (high dependence) stages
3. Optimizing the profit/loss value vs investment risk to tackle dynamics of external events and aid in portfolio diversification