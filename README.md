# 📊 Electrification of Swedish Cars

## Project Overview

This project investigates the relationship between income trends and car registration patterns in Sweden, with a special focus on electric vehicle adoption over time.

The project includes:
- 🚘 Advanced data analysis of car registrations by fuel type
- 💰 Income distribution trends across Swedish regions and age groups
- 📉 Combined insights showing how economic factors may be influencing EV adoption
- 📈 Visual Power BI dashboard for storytelling and insight delivery

## 🧠 Key Insights

- ✅ Average Disposable Income in Sweden declined starting 2022, possibly due to inflation and economic slowdown.
- ✅ Total new car registrations have been declining since 2017 — indicating a shift in consumer behavior or purchasing power.
- ⚠️ Electric car registrations began declining from 2023, despite years of upward trend — raising questions about affordability or incentives.
- 🔋 Electricity was once the fastest-growing fuel type but has now plateaued or declined in several regions.

These insights were derived by combining two datasets from official Swedish source — SCB (Statistiska centralbyrån) and visualizing the story through a dashboard.

## 🔍 Exploratory Data Analysis

The EDA was conducted using Python (Pandas, Matplotlib, Seaborn):

📁 `exploratory_analysis/income_data_exploratory_analysis.ipynb`
- Data cleaning (missing values, column renaming)
- Income trends by year and region
- Breakdown by age groups
- Trend identification: Income growth until 2021, decline post-2022

📁 `exploratory_analysis/car_data_exploratory_analysis.ipynb`
- Monthly and yearly registration trends
- Fuel type transition: petrol → electric → decline
- Seasonal patterns in car purchases
- Region-wise electric vehicle adoption

## 📊 Power BI Dashboard

The final dashboard (📁 `dashboard/electrification_dashboard.pbix`) includes:
- Trend Charts for new car registrations and income levels
- Stacked Area Charts showing fuel type transitions
- Top Regions for EV adoption
- Year-over-Year DAX Measures
- Slicers for time period and fuel type exploration

You can explore:
- How income levels and EV adoption vary over time
- Whether economic pressure is reducing electric car purchases
- Regional leadership in electric vehicle transitions

## 🛠️ Tools Used

- Python (Pandas, Seaborn, Matplotlib)
- Jupyter Notebooks
- Power BI (DAX, Power Query, Data Modeling)
- Data Cleaning and EDA
- Dashboard Design