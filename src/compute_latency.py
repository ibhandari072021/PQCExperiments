import pandas as pd

# Load synthetic PQC benchmark data
df = pd.read_csv("../data/sample_pqc_latency.csv")

# Compute mean latency by algorithm
latency_stats = df.groupby('algorithm')['latency_ms'].mean()

# Compute minimum attack success rate by sector
attack_stats = df.groupby('sector')['attack_success_rate'].min()

# Save summary results
latency_stats.to_csv("../docs/mean_latency_by_algorithm.txt", sep='\t')
attack_stats.to_csv("../docs/min_attack_rate_by_sector.txt", sep='\t')

print("Analysis complete: docs/mean_latency_by_algorithm.txt and docs/min_attack_rate_by_sector.txt")
