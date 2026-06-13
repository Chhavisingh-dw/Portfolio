import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

# Load the data
df = pd.read_excel("India_Energy_Dashboard_Data.xlsx", 
                    sheet_name="Yearly_RE_Capacity")

# Chart - RE Growth Line Chart
fig, ax = plt.subplots(figsize=(12, 7))

# Background colour
fig.patch.set_facecolor('#0D1B2A')
ax.set_facecolor('#1C2E42')

# Plot the line
ax.plot(df['Year'], df['Total_RE_GW'], 
        color='#3DAA6E', linewidth=3, 
        marker='o', markersize=8,
        markerfacecolor='#C4974A')

# Add data labels
for x, y in zip(df['Year'], df['Total_RE_GW']):
    ax.annotate(f'{y}', (x, y), 
                textcoords="offset points",
                xytext=(0, 12), 
                ha='center', 
                color='white', 
                fontsize=9)

# Styling
ax.set_title('India Renewable Energy Growth (2015-2024)', 
             color='white', fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Year', color='#C4974A', fontsize=12)
ax.set_ylabel('Total RE Capacity (GW)', color='#C4974A', fontsize=12)
ax.tick_params(colors='white')
ax.grid(True, alpha=0.2, color='white')

plt.tight_layout()
plt.savefig('india_re_growth.png', dpi=150, bbox_inches='tight')
plt.show()
print("Chart saved!")

# Chart 2 - State wise Bar Chart
df2 = pd.read_excel("India_Energy_Dashboard_Data.xlsx", 
                     sheet_name="State_Performance")

fig2, ax2 = plt.subplots(figsize=(12, 7))
fig2.patch.set_facecolor('#0D1B2A')
ax2.set_facecolor('#1C2E42')

bars = ax2.bar(df2['State'], df2['Total_RE_GW'], 
               color='#3DAA6E', edgecolor='#C4974A')

ax2.set_title('State-wise RE Capacity 2024', 
              color='white', fontsize=16, fontweight='bold')
ax2.set_xlabel('State', color='#C4974A', fontsize=12)
ax2.set_ylabel('Total RE Capacity (GW)', color='#C4974A', fontsize=12)
ax2.tick_params(colors='white', axis='both')
plt.xticks(rotation=45, ha='right')
ax2.grid(True, alpha=0.2, color='white', axis='y')

plt.tight_layout()
plt.savefig('state_performance.png', dpi=150, bbox_inches='tight')
plt.show()
print("Chart 2 saved!")




# Chart 3 - NDC Progress Pie Chart
df3 = pd.read_excel("India_Energy_Dashboard_Data.xlsx", 
                     sheet_name="NDC_Progress")

fig3, ax3 = plt.subplots(figsize=(10, 7))
fig3.patch.set_facecolor('#0D1B2A')
ax3.set_facecolor('#0D1B2A')

colors = ['#3DAA6E', '#C4974A', '#2E4A63', '#5B8DB8']

wedges, texts, autotexts = ax3.pie(
    df3['Progress_Pct'],
    labels=df3['Target'],
    colors=colors,
    autopct='%1.1f%%',
    startangle=90,
    wedgeprops={'edgecolor': '#0D1B2A', 'linewidth': 2}
)

for text in texts:
    text.set_color('white')
    text.set_fontsize(9)

for autotext in autotexts:
    autotext.set_color('white')
    autotext.set_fontweight('bold')

ax3.set_title('India NDC Progress — 2025', 
              color='white', fontsize=16, fontweight='bold')

plt.tight_layout()
plt.savefig('ndc_progress.png', dpi=150, bbox_inches='tight')
plt.show()
print("Chart 3 saved!")