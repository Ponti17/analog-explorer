import pandas as pd

filename = "nmos_rf.csv"
df = pd.read_csv(filename)
df.to_pickle("nmos_rf_sim.pkl")
