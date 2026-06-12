"""
Future of Data: Quantum Analytics
CODTECH Data Analyst Internship - Task 1
Author: Data Analyst Intern
Description: Exploratory Data Analysis on the future of Quantum Computing in Data Analytics
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import warnings
warnings.filterwarnings('ignore')

# ─── 1. Simulated Quantum Analytics Dataset ───────────────────────────────────

np.random.seed(42)
years = list(range(2020, 2036))

quantum_data = {
    "Year": years,
    "Quantum_Computing_Market_USD_Billion": [
        0.47, 0.61, 0.78, 1.02, 1.30, 1.76, 2.35, 3.18,
        4.50, 6.10, 8.40, 11.50, 15.80, 21.20, 28.70, 38.90
    ],
    "Classical_Computing_Market_USD_Billion": [
        412, 430, 448, 467, 490, 512, 535, 558,
        580, 602, 622, 640, 656, 670, 682, 693
    ],
    "Quantum_Speedup_Factor": [
        1.2, 1.5, 1.9, 2.4, 3.1, 4.0, 5.3, 7.1,
        9.5, 12.8, 17.2, 23.1, 31.0, 41.5, 55.8, 74.9
    ],
    "Qubit_Count": [
        50, 66, 127, 156, 433, 1121, 2000, 4158,
        8000, 15000, 30000, 60000, 120000, 250000, 500000, 1000000
    ],
    "Error_Rate_Percent": [
        3.5, 3.1, 2.8, 2.4, 2.0, 1.7, 1.4, 1.1,
        0.9, 0.7, 0.55, 0.42, 0.32, 0.24, 0.18, 0.13
    ],
    "Quantum_AI_Applications": [
        5, 8, 13, 20, 31, 48, 73, 110,
        166, 249, 373, 559, 838, 1256, 1883, 2824
    ],
    "Industry_Adoption_Percent": [
        2, 3, 5, 7, 10, 14, 19, 26,
        34, 44, 55, 66, 75, 82, 88, 92
    ],
    "Data_Processing_Speed_PB_per_sec": [
        0.01, 0.02, 0.04, 0.08, 0.17, 0.35, 0.72, 1.50,
        3.10, 6.40, 13.20, 27.30, 56.50, 116.90, 241.80, 500.00
    ],
    "Investment_USD_Billion": [
        0.93, 1.10, 1.40, 1.75, 2.20, 2.85, 3.70, 4.90,
        6.50, 8.60, 11.40, 15.10, 20.00, 26.50, 35.10, 46.50
    ]
}

df = pd.DataFrame(quantum_data)

# ─── 2. Summary Statistics ─────────────────────────────────────────────────────
print("=" * 65)
print("   FUTURE OF DATA: QUANTUM ANALYTICS - CODTECH INTERNSHIP TASK 1")
print("=" * 65)
print("\n📊 Dataset Overview:")
print(f"   Rows: {df.shape[0]}  |  Columns: {df.shape[1]}")
print(f"   Year Range: {df['Year'].min()} – {df['Year'].max()}")

print("\n📈 Key Statistics:\n")
summary_cols = [
    "Quantum_Computing_Market_USD_Billion",
    "Qubit_Count",
    "Industry_Adoption_Percent",
    "Error_Rate_Percent"
]
print(df[summary_cols].describe().round(2).to_string())

print("\n📌 Projected Highlights by 2035:")
row_2035 = df[df["Year"] == 2035].iloc[0]
print(f"   • Market Size        : ${row_2035['Quantum_Computing_Market_USD_Billion']:.1f}B")
print(f"   • Qubit Count        : {int(row_2035['Qubit_Count']):,}")
print(f"   • Industry Adoption  : {row_2035['Industry_Adoption_Percent']}%")
print(f"   • Error Rate         : {row_2035['Error_Rate_Percent']}%")
print(f"   • Speedup Factor     : {row_2035['Quantum_Speedup_Factor']}x")

# ─── 3. Visualizations ────────────────────────────────────────────────────────
colors = {
    "quantum": "#6C63FF",
    "classical": "#00C9A7",
    "error": "#FF6B6B",
    "qubit": "#FFC75F",
    "investment": "#845EC2",
    "adoption": "#00B0A0",
    "speed": "#F9A825"
}

fig, axes = plt.subplots(3, 2, figsize=(16, 18))
fig.suptitle(
    "Future of Data: Quantum Analytics\nCODTECH Data Analyst Internship – Task 1",
    fontsize=18, fontweight='bold', y=0.98, color="#2C3E50"
)
fig.patch.set_facecolor('#F0F4F8')

# ── Plot 1: Market Growth ──
ax1 = axes[0, 0]
ax1.fill_between(df["Year"], df["Quantum_Computing_Market_USD_Billion"],
                  alpha=0.3, color=colors["quantum"])
ax1.plot(df["Year"], df["Quantum_Computing_Market_USD_Billion"],
         marker='o', color=colors["quantum"], linewidth=2.5, markersize=5)
ax1.set_title("Quantum Computing Market Growth (USD Billion)", fontweight='bold')
ax1.set_xlabel("Year")
ax1.set_ylabel("Market Size (USD Billion)")
ax1.set_facecolor('#FAFAFA')
ax1.grid(True, alpha=0.3)

# ── Plot 2: Qubit Count ──
ax2 = axes[0, 1]
ax2.bar(df["Year"], df["Qubit_Count"], color=colors["qubit"], edgecolor='white', linewidth=0.5)
ax2.set_title("Qubit Count Progression", fontweight='bold')
ax2.set_xlabel("Year")
ax2.set_ylabel("Qubit Count")
ax2.set_facecolor('#FAFAFA')
ax2.grid(True, alpha=0.3, axis='y')
ax2.set_yscale('log')
plt.setp(ax2.get_xticklabels(), rotation=45)

# ── Plot 3: Error Rate Reduction ──
ax3 = axes[1, 0]
ax3.fill_between(df["Year"], df["Error_Rate_Percent"],
                  alpha=0.3, color=colors["error"])
ax3.plot(df["Year"], df["Error_Rate_Percent"],
         marker='s', color=colors["error"], linewidth=2.5, markersize=5)
ax3.set_title("Error Rate Reduction Over Time (%)", fontweight='bold')
ax3.set_xlabel("Year")
ax3.set_ylabel("Error Rate (%)")
ax3.set_facecolor('#FAFAFA')
ax3.grid(True, alpha=0.3)

# ── Plot 4: Industry Adoption ──
ax4 = axes[1, 1]
bars = ax4.barh(df["Year"].astype(str), df["Industry_Adoption_Percent"],
                color=colors["adoption"], edgecolor='white')
for bar, val in zip(bars, df["Industry_Adoption_Percent"]):
    ax4.text(bar.get_width() + 0.5, bar.get_y() + bar.get_height() / 2,
             f'{val}%', va='center', fontsize=7.5, color='#2C3E50')
ax4.set_title("Industry Adoption Rate (%)", fontweight='bold')
ax4.set_xlabel("Adoption (%)")
ax4.set_ylabel("Year")
ax4.set_facecolor('#FAFAFA')
ax4.grid(True, alpha=0.3, axis='x')

# ── Plot 5: Investment Trend ──
ax5 = axes[2, 0]
ax5.fill_between(df["Year"], df["Investment_USD_Billion"],
                  alpha=0.3, color=colors["investment"])
ax5.plot(df["Year"], df["Investment_USD_Billion"],
         marker='^', color=colors["investment"], linewidth=2.5, markersize=6)
ax5.set_title("Global Investment in Quantum Analytics (USD Billion)", fontweight='bold')
ax5.set_xlabel("Year")
ax5.set_ylabel("Investment (USD Billion)")
ax5.set_facecolor('#FAFAFA')
ax5.grid(True, alpha=0.3)

# ── Plot 6: Data Processing Speed ──
ax6 = axes[2, 1]
ax6.plot(df["Year"], df["Data_Processing_Speed_PB_per_sec"],
         color=colors["speed"], linewidth=2.5, marker='D', markersize=5)
ax6.fill_between(df["Year"], df["Data_Processing_Speed_PB_per_sec"],
                  alpha=0.2, color=colors["speed"])
ax6.set_title("Quantum Data Processing Speed (PB/sec)", fontweight='bold')
ax6.set_xlabel("Year")
ax6.set_ylabel("Speed (PB/sec)")
ax6.set_facecolor('#FAFAFA')
ax6.grid(True, alpha=0.3)
ax6.set_yscale('log')

plt.tight_layout(rect=[0, 0, 1, 0.96])
plt.savefig("quantum_analytics_charts.png",
            dpi=150, bbox_inches='tight', facecolor='#F0F4F8')
print("\n✅ Charts saved: quantum_analytics_charts.png")

# ─── 4. Correlation Analysis ──────────────────────────────────────────────────
print("\n🔗 Correlation Matrix (Key Variables):\n")
corr_cols = [
    "Quantum_Computing_Market_USD_Billion",
    "Qubit_Count",
    "Error_Rate_Percent",
    "Industry_Adoption_Percent",
    "Investment_USD_Billion"
]
corr = df[corr_cols].corr().round(3)
print(corr.to_string())

# ─── 5. Save Dataset as CSV ───────────────────────────────────────────────────
df.to_csv("quantum_analytics_data.csv", index=False)
print("\n✅ Dataset saved: quantum_analytics_data.csv")
print("\n🎯 Analysis Complete! Ready for GitHub submission.")
