import pandas as pd
import matplotlib.pyplot as plt

filename = "nch_full_sim.csv"
model = pd.read_csv(filename)

# vds = "vds=1.00e+00"
vds = 0.1
vds = "{:.2e}".format(vds)
L = "length=1.00e-06"
param = "gmoverid"

search_params = [vds, L, param]
data = [title for title in model.columns if all(param in title for param in search_params)]

fix, ax = plt.subplots()
for title in data:
    ax.plot(model[data[0]], model[data[1]], label=title)
plt.show()