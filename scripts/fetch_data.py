import requests, zipfile, io, pandas as pd, pathlib
RAW = pathlib.Path("data/raw"); RAW.mkdir(parents=True, exist_ok=True)
# 1. PERI Greenhouse 100
peri = pd.read_html("https://peri.umass.edu/greenhouse-100-polluters-index")[0]
peri.to_csv(RAW/"peri_ghg100.csv", index=False)
# 2. EPA GHGRP facility-level data (latest)
url = "https://ghgdata.epa.gov/ghgp/download?download=GHD_FACILITY&year=2022"
resp = requests.get(url); zipfile.ZipFile(io.BytesIO(resp.content)).extractall(RAW)
print("Downloaded PERI & EPA datasets ? data/raw")
