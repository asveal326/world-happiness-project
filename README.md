# World Happiness Project

## Overview
This project explores global well-being using the World Happiness Report dataset from 2015 to 2022. The analysis investigates how GDP per capita, social support, healthy life expectancy, freedom, generosity, and corruption relate to national happiness scores.

## Authors
- Aysia Veal
- Jalen Jackson
- Mian Pan

## Objectives
- Examine global happiness patterns over time
- Identify the factors most associated with happiness
- Compare the happiest and least happy countries
- Build clear visualizations to communicate insights

## Dataset
Source: World Happiness Report dataset from Kaggle  
Link: https://www.kaggle.com/datasets/mathurinache/world-happiness-report

Supporting reference:  
World Happiness Report 2024  
https://files.worldhappiness.report/WHR24.pdf

## Project Structure
- \`data/raw/\` – original yearly CSV files
- \`data/processed/\` – cleaned and merged datasets
- \`notebooks/\` – Jupyter notebook and exported figures
- \`s/figures/\` – saved charts
- \`outputs/tables/\` – saved tables
- \`src/\` – helper Python scripts

## Key Visualizations
- Choropleth map of global happiness over time
- Correlation heatmap of happiness factors
- GDP per capita vs Happiness Score scatter plot
- Average global happiness over time
- Top 10 countries with greatest improvement and decline
- Normalized comparison of top 5 vs bottom 5 happiest countries

## Key Findings
- GDP per capita had the strongest positive correlation with happiness
- Social support and freedom also showed meaningful relationships
- Global happiness inc gradually from 2015 to 2022
- Happiest countries consistently performed better across multiple factors

## Tools Used
- Python
- pandas
- plotly
- matplotlib
- seaborn
- scikit-learn
- Jupyter Notebook
