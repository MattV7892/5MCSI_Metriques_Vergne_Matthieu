import requests
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

# 1. Appel API GitHub
url = "https://api.github.com/repos/OpenRSI/5MCSI_Metriques/commits"
response = requests.get(url)
data = response.json()

# 2. Extraction des timestamps
timestamps = []
for commit in data:
    date_str = commit["commit"]["author"]["date"]  # clé indiquée dans l'énoncé
    dt = datetime.fromisoformat(date_str.replace("Z", "+00:00"))
    timestamps.append(dt)

# 3. Convertir en DataFrame
df = pd.DataFrame({"datetime": timestamps})

# 4. Arrondir à la minute
df["minute"] = df["datetime"].dt.floor("T")

# 5. Regrouper minute par minute
counts = df.groupby("minute").size()

# 6. Tracer graphique
plt.figure(figsize=(12, 5))
plt.plot(counts.index, counts.values, marker="o")
plt.xlabel("Minute")
plt.ylabel("Nombre de commits")
plt.title("Activité des commits (minute par minute)")
plt.grid(True)
plt.tight_layout()
plt.show()
