import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import os

# Load Data
df = pd.read_csv("sales_data.csv", parse_dates=["Date"])
os.makedirs("visualizations", exist_ok=True)

# Basic plots + colors + styles
sns.set_style("whitegrid")
sns.set_palette("Set2")

plt.figure(figsize=(8, 5))
sns.barplot(x="Product", y="Total_Sales", data=df, estimator=sum)
plt.title("Total Sales by Product")
plt.savefig("visualizations/day1_basic_barplot.png")
plt.close()

# Box plots, violin plots, annotations
plt.figure(figsize=(8, 5))
sns.boxplot(x="Product", y="Price", data=df)
plt.title("Price Distribution by Product")
plt.savefig("visualizations/day2_boxplot.png")
plt.close()

plt.figure(figsize=(8, 5))
sns.violinplot(x="Region", y="Total_Sales", data=df)
plt.title("Sales Distribution by Region")
plt.savefig("visualizations/day2_violinplot.png")
plt.close()

# HEATMAPS & CORRELATION
plt.figure(figsize=(8, 6))
corr = df[["Quantity", "Price", "Total_Sales"]].corr()
sns.heatmap(corr, annot=True, cmap="coolwarm", linewidths=0.5)
plt.title("Correlation Heatmap")
plt.savefig("visualizations/day3_heatmap.png")
plt.close()

# MULTI-PLOT DASHBOARD (2×2 GRID)
fig, axes = plt.subplots(2, 2, figsize=(14, 10))
fig.suptitle("Sales Dashboard Overview", fontsize=16)

sns.barplot(ax=axes[0, 0], x="Product", y="Total_Sales", data=df, estimator=sum)
axes[0, 0].set_title("Sales by Product")

sns.boxplot(ax=axes[0, 1], x="Region", y="Price", data=df)
axes[0, 1].set_title("Price by Region")

sns.violinplot(ax=axes[1, 0], x="Product", y="Quantity", data=df)
axes[1, 0].set_title("Quantity Distribution")

sns.lineplot(
    ax=axes[1, 1],
    data=df.groupby("Date")["Total_Sales"].sum().reset_index(),
    x="Date",
    y="Total_Sales"
)
axes[1, 1].set_title("Sales Trend")

plt.tight_layout()
plt.savefig("visualizations/day4_subplot_dashboard.png")
plt.close()

# Hover + Dropdown
fig_interactive = px.line(
    df.groupby(["Date", "Region"])["Total_Sales"].sum().reset_index(),
    x="Date",
    y="Total_Sales",
    color="Region",
    title="Interactive Sales Trend by Region",
    markers=True
)
fig_interactive.show()

# Dashboard multiple interactive charts
dashboard = make_subplots(
    rows=2, cols=2,
    subplot_titles=[
        "Sales Trend",
        "Sales by Product",
        "Sales by Region",
        "Quantity by Product"
    ]
)

# Sales Trend
trend = df.groupby("Date")["Total_Sales"].sum().reset_index()
dashboard.add_trace(
    go.Scatter(x=trend["Date"], y=trend["Total_Sales"], mode="lines+markers"),
    row=1, col=1
)

# Product Sales
prod = df.groupby("Product")["Total_Sales"].sum().reset_index()
dashboard.add_trace(
    go.Bar(x=prod["Product"], y=prod["Total_Sales"]),
    row=1, col=2
)

# Region Sales
reg = df.groupby("Region")["Total_Sales"].sum().reset_index()
dashboard.add_trace(
    go.Bar(x=reg["Region"], y=reg["Total_Sales"]),
    row=2, col=1
)

# Quantity
qty = df.groupby("Product")["Quantity"].sum().reset_index()
dashboard.add_trace(
    go.Bar(x=qty["Product"], y=qty["Quantity"]),
    row=2, col=2
)

dashboard.update_layout(
    height=800,
    title_text="Integrated Interactive Sales Dashboard",
    showlegend=False
)

dashboard.show()

# Branding + Export-ready visuals
sns.set_theme(style="white", palette="deep")

plt.figure(figsize=(10, 5))
sns.lineplot(
    data=trend,
    x="Date",
    y="Total_Sales",
    linewidth=2.5
)
plt.title("Company XYZ | Sales Performance Report")
plt.xlabel("Date")
plt.ylabel("Total Sales")
plt.savefig("visualizations/day7_final_report_chart.png")
plt.close()

print("Dashboard Completed Successfully")
