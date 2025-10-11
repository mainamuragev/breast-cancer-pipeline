import pandas as pd
import matplotlib.pyplot as plt

# Load CSV
df = pd.read_csv("recurrence_delay.csv")

# Group and average
avg_delay = df.groupby("recurrence_type")["delay_days"].mean()

# Plot
avg_delay.plot(kind="bar", color="skyblue", edgecolor="black")
plt.title("Average Delay by Recurrence Type")
plt.xlabel("Recurrence Type")
plt.ylabel("Average Delay (days)")
plt.tight_layout()
plt.savefig("delay_bar_chart.png")
plt.show()
