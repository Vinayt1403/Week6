Interactive Sales Dashboard 
Week 6 – Data Visualization Mastery with Seaborn & Plotly 
 
1. Project Overview 
1.1 Project Title 
Interactive Sales Dashboard Using Seaborn and Plotly 
1.2 Project Objective 
The objective of this project is to design and implement an interactive sales dashboard that 
provides meaningful insights into sales performance using advanced data visualization 
techniques. The dashboard helps stakeholders understand: 
• Sales trends over time 
• Product-wise sales performance 
• Regional sales distribution 
• Statistical distribution of price and quantity 
• Correlation between key numerical variables 
The project emphasizes visual storytelling, statistical analysis, and interactive exploration 
using Python visualization libraries. 
 
2. Dataset Description 
The dataset represents transactional sales data with the following attributes: 
Column Name Description 
Date Date of transaction 
Product Product sold (Phone, Laptop, Tablet, etc.) 
Quantity Number of units sold 
Price Price per unit 
Customer_ID Unique customer identifier 
Region Sales region (North, South, East, West) 
Column Name Description 
Total_Sales Quantity × Price 
 
3. Setup Instructions 
3.1 System Requirements 
• Python 3.9 or higher 
• Windows / macOS / Linux 
• Internet connection for library installation 
Python Pre defined Modules 
• pandas as pd – For loading, cleaning, and manipulating sales data. 
• seaborn as sns – For creating statistical plots like bar, box, violin, and heatmaps. 
• matplotlib.pyplot as plt – For figure control, layouts, and saving static plots. 
• plotly.express as px – For quick, interactive charts with hover info and color coding. 
• plotly.graph_objects as go – For detailed interactive charts and multiple traces. 
• from plotly.subplots import make_subplots – To arrange multiple Plotly charts in a 
grid. 
• os – For creating folders and managing files. 
 
3.2 Installation Steps 
1. Clone or download the project repository 
2. Navigate to the project directory 
3. (Optional) Create a virtual environment 
4. Install required dependencies 
pip install -r requirements.txt 
 
 
 
 
3.3 Run the Project 
python dashboard.py 
 
4. Code Structure 
4.1 File Hierarchy 
Interactive-Sales-Dashboard/ 
 │ 
├── sales_data.csv 
├── dashboard.py 
├── requirements.txt 
├── interactive_dashboard.png 
 │ 
├── visualizations/ 
│   ├── day1_basic_barplot.png 
│   ├── day2_boxplot.png 
│   ├── day2_violinplot.png 
│   ├── day3_heatmap.png 
│   ├── day4_subplot_dashboard.png 
│   ├── day7_final_report_chart.png 
│ 
└── README.md 
4.2 Code Organization 
• Data Loading Module – Reads and prepares dataset 
• Visualization Layer – Seaborn & Plotly charts 
• Dashboard Layer – Integrated multi-chart layout 
• Export Layer – Saves charts for documentation 
 
5. Dashboard Guide & Visualization Interpretation 
5.1 Day 1 – Basic Seaborn Plot 
Bar Plot: Total Sales by Product 
Purpose: 
Shows overall product performance. 
Insight: 
Identifies top-performing and low-performing products. 
 
 
5.2 Day 2 – Statistical Visualizations 
Box Plot – Price Distribution by Product 
Purpose: 
Analyzes price variability and detects outliers. 
 
 
 
Violin Plot – Sales Distribution by Region 
Purpose: 
Shows distribution shape and density of sales across regions. 
 
 
 
5.3 Day 3 – Heatmap & Correlation 
Correlation Heatmap 
Purpose: 
Displays relationships between Quantity, Price, and Total Sales. 
Insight: 
Helps understand how pricing and quantity impact revenue. 
 
 
 
5.4 Day 4 – Multi-Plot Dashboard (2×2 Grid) 
Included Visuals: 
• Sales by Product 
• Price by Region 
• Quantity Distribution 
• Sales Trend 
Purpose: 
Provides a high-level analytical overview in a single dashboard. 
 
 
 
5.5 Day 5 – Interactive Visualizations (Plotly) 
Interactive Line Chart 
• Hover tooltips 
• Zoom & pan 
• Region-based color coding 
 
 
5.6 Day 6 – Dashboard Integration 
Integrated Interactive Dashboard 
Combines multiple charts into a unified interactive layout using Plotly subplots. 
Business Value: 
Allows decision-makers to analyze multiple KPIs simultaneously. 
 
 
 
 
6. Technical Details 
6.1 Algorithms Used 
• Aggregation (groupby, sum) 
• Correlation analysis (.corr()) 
• Statistical visualization methods (box, violin plots) 
6.2 Data Structures 
• Pandas DataFrame 
• NumPy arrays (indirect usage) 
• Plotly Graph Objects 
6.3 Architecture Overview 
Raw Data → Data Processing → Visualization Layer → Dashboard Layer → Export & 
Reporting 
 
7. Testing Evidence & Validation 
7.1 Data Validation 
• Verified no missing values 
• Confirmed correct data types 
• Checked consistency of Total_Sales calculations 
7.2 Visualization Testing 
• Verified plot rendering 
• Checked axis labels and legends 
• Confirmed interactive elements function correctly 
         Insert Screenshot: 
 
 
8. Quality Standards Checklist 
Requirement Status 
Project Overview      
Clear Objectives      
Setup Instructions      
Organized Code Structure      
Multiple Chart Types      
Interactive Visuals      
Visual Documentation      
Technical Explanation      
Testing Evidence      
 
9. Conclusion 
This project successfully demonstrates data visualization mastery using Seaborn and Plotly. 
The interactive dashboard delivers actionable insights through well-designed visuals, 
statistical analysis, and professional presentation, making it suitable for real-world business 
decision-making.
