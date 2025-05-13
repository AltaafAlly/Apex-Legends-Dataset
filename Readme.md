# Apex Legends Dataset Project

This repository provides a comprehensive framework for collecting, processing, and analyzing player and legend statistics from Apex Legends. It is organized into several folders, each with a specific role in the data pipeline, from raw data acquisition to advanced analysis.

**This dataset features the top 500 players for overall career stats, as well as the top 500 players per legend category. For each legend, the dataset includes the top 500 players by damage, kills, matches played, and wins.**

**The data was captured in August 2024. Please note that Apex Legends is a live service game that is continuously updated and played by many players worldwide. As such, player rankings and statistics are subject to change over time.**

---

## Table of Contents

- [Folder Structure](#folder-structure)
- [Folder Descriptions](#folder-descriptions)
- [Data Flow Overview](#data-flow-overview)
- [Getting Started](#getting-started)
- [Usage](#usage)
- [Notes](#notes)
- [License](#license)
- [Contact](#contact)

---

## Folder Structure

```
Apex-Legends-Dataset/
│
├── Career_Stats_Dataset/
│   ├── Dataset_analysis.ipynb
│   ├── Total Player Career Stats.csv
│   ├── Career Stats/
│   ├── Non Imputed Career Datasets/
│   └── Player UIDs/
│
├── Legend Stats Dataset/
│   ├── Legend_Dataset_Analysis.ipynb
│   └── Processed_Legend_Stats/
│
└── Player UIDs/
    ├── usernames_with_uids_for_PC.csv
    ├── usernames_with_uids_for_PS4.csv
    ├── usernames_with_uids_for_Xbox.csv
    └── Player UIDs File/
```

---

## Folder Descriptions

### 1. `Career_Stats_Dataset/`

Contains datasets and analysis related to overall player career statistics.

- **Dataset_analysis.ipynb**  
  Jupyter notebook for cleaning, exploring, and visualizing the career stats data. Includes:
  - Data import and inspection
  - Handling missing values and duplicates
  - Exploratory Data Analysis (EDA) with summary statistics, histograms, boxplots, and correlation analysis
  - Leaderboard and top player analysis

- **Total Player Career Stats.csv**  
  Main CSV file with aggregated career stats for the top 500 players, including fields like `player_name`, `career_kills`, `career_wins`, and `career_revives`.

- **Career Stats/**  
  Contains platform-specific or batch-specific career stats CSVs (e.g., `Player Career Stats PC.csv`, `Player Career Stats PS4.csv`).

- **Non Imputed Career Datasets/**  
  Contains raw or partially processed datasets before imputation or cleaning.

- **Player UIDs/**  
  Contains scripts and files for mapping player usernames to unique IDs.

---

### 2. `Legend Stats Dataset/`

Contains datasets and analysis related to per-legend statistics.

- **Legend_Dataset_Analysis.ipynb**  
  Jupyter notebook for processing and analyzing legend-specific stats. Features:
  - Automated loading and validation of legend data files
  - Aggregation and visualization of legend performance metrics (damage, kills, matches played, wins)
  - Handling of missing or malformed data

- **Processed_Legend_Stats/**  
  Contains subfolders for each legend statistic, each featuring the top 500 players:
  - `Legend Damage/` — CSVs with per-legend damage data
  - `Legend Kills/` — CSVs with per-legend kills data
  - `Legend Matches Played/` — CSVs with per-legend matches played
  - `Legend Wins/` — CSVs with per-legend wins

---

### 3. `Player UIDs/`

Handles player identification and mapping.

- **usernames_with_uids_for_PC.csv**, **usernames_with_uids_for_PS4.csv**, **usernames_with_uids_for_Xbox.csv**  
  CSV files mapping player usernames to their unique IDs for each platform.

- **Player UIDs File/**  
  Contains scripts for converting and anonymizing player identifiers (e.g., replacing usernames with `User_n` labels).

---

## Data Flow Overview

1. **Player UIDs**  
   - Usernames are mapped to UIDs using the CSVs in `Player UIDs/`.
   - Stats for each UID are fetched and written to CSV using custom scripts (not included here for security reasons).

2. **Career Stats**  
   - Raw and processed career stats for the top 500 players are stored in `Career_Stats_Dataset/`.
   - `Dataset_analysis.ipynb` performs cleaning, EDA, and visualization.

3. **Legend Stats**  
   - Per-legend stats for the top 500 players in each category are stored in `Legend Stats Dataset/Processed_Legend_Stats/`.
   - `Legend_Dataset_Analysis.ipynb` aggregates and analyzes legend performance.

---

## Getting Started

### Requirements

- Python 3.7+
- Jupyter Notebook
- pandas, numpy, matplotlib, seaborn, requests

Install dependencies with:

```sh
pip install pandas numpy matplotlib seaborn requests
```

---

## Usage

### 1. Fetching Player Stats

- Place your username-UID mapping CSVs in `Player UIDs/`.
- Use your own scripts to fetch and save player stats from the API (not included in this repository).

### 2. Analyzing Career Stats

- Open `Career_Stats_Dataset/Dataset_analysis.ipynb` in Jupyter.
- Run the notebook to clean, explore, and visualize the career stats data.

### 3. Analyzing Legend Stats

- Place legend stat CSVs in the appropriate subfolders under `Legend Stats Dataset/Processed_Legend_Stats/`.
- Open `Legend Stats Dataset/Legend_Dataset_Analysis.ipynb` in Jupyter.
- Run the notebook to aggregate and analyze legend-specific performance.

---

## Notes

- **Data Privacy:**  
  Usernames can be anonymized using scripts in `Player UIDs/Player UIDs File/Conversion.py`.

- **API Usage:**  
  The [Mozambique API](https://apexlegendsapi.com/) has rate limits. Scripts for API access are not included here for security reasons.

- **Extensibility:**  
  The structure supports adding new platforms, legends, or additional stat categories as needed.

---

## License

This project is for research and educational purposes. Please respect the terms of service of any third-party APIs used.

---

## Contact

For questions or contributions, please open an issue or pull request on the repository.
