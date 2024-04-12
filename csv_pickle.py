import pandas as pd

filename = "nch_full_sim.csv"
df = pd.read_csv(filename)
df.to_pickle("nch_full_sim.pkl")
