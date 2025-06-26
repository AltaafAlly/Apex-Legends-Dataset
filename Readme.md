# Apex Legends Dataset Project

This repository provides a comprehensive framework for collecting, processing, and analyzing player and legend statistics from Apex Legends. It is organized into several folders, each with a specific role in the data pipeline, from raw data acquisition to advanced analysis.

**This dataset features the top 500 players for overall career stats which include career kills, career wins and career revives across Playstation, PC and Xbox, as well as the top 500 players per legend category. For each legend, the dataset includes the top 500 players by damage, kills, matches played, and wins.**

**The data was captured in August 2024. Please note that Apex Legends is a live service game that is continuously updated and played by many players worldwide. As such, player rankings and statistics are subject to change over time.**

---

## 📁 Repository Structure

```
Apex-Legends-Dataset/
│
├── Career_Stats_Dataset/
│   ├── Dataset_analysis.ipynb
│   ├── Dataset_Individual.ipynb
│   ├── Total Player Career Stats.csv
│   ├── Imputated Datasets/
│   │   ├── MICE_Imputed_PC.csv
│   │   ├── MICE_Imputed_PS4.csv
│   │   └── MICE_Imputed_Xbox.csv
│   ├── Non Imputed Career Datasets/
│   │   ├── Career_Stats_PC.csv
│   │   ├── Career_Stats_PS4.csv
│   │   ├── Career_Stats_Xbox.csv
│   │   └── ...
│   └── Player UIDs/
│
└── Legend Stats Dataset/
    ├── Clustering_Analysis.ipynb
    ├── Legend_Dataset_Analysis_Model.ipynb
    ├── Legend_Dataset_Analysis_of_Stats.ipynb
    └── Processed_Legend_Stats/
        ├── all_legends_combined.csv
        ├── Legend Damage/
        │   ├── <Legend>_damage.csv
        │   └── ...
        ├── Legend Kills/
        │   ├── <Legend>_kills.csv
        │   └── ...
        ├── Legend Matches Played/
        │   ├── <Legend>_games_played.csv
        │   └── ...
        └── Legend Wins/
            ├── <Legend>_wins.csv
            └── ...
```

---

## 📊 Main Notebooks

### Career_Stats_Dataset

- **Dataset_analysis.ipynb**  
  Exploratory data analysis and visualization of player career stats (kills, wins, revives). Includes data cleaning, summary statistics, and platform comparison.

- **Dataset_Individual.ipynb**  
  Platform comparison, imputation, and regression/classification models for player stats. Includes visualizations and summary statistics for PC, Xbox, and PS4.

### Legend Stats Dataset

- **Legend_Dataset_Analysis_of_Stats.ipynb**  
  In-depth analysis of legend-specific stats, including damage, kills, matches played, and wins. Includes data cleaning, aggregation, and visualization.

- **Legend_Dataset_Analysis_Model.ipynb**  
  Machine learning model to predict a legend's role (Assault, Support, etc.) based on game performance (kills, damage).

- **Clustering_Analysis.ipynb**  
  Clustering analysis of legends based on performance metrics (kills per match, kills per win, damage per match). Includes K-Means, GMM, and Hierarchical clustering, with visualizations and cluster composition analysis.

---

## 🏷️ Data Sources

- **Career Stats:**  
  CSVs with player career stats (kills, wins, revives) for PC, Xbox, and PS4, both imputed and non-imputed.

- **Legend Stats:**  
  CSVs for each legend and stat (damage, kills, matches played, wins), processed and stored in subfolders.

---

## ⚙️ How to Use

1. **Clone the repository** and open in VS Code or Jupyter.
2. **Install dependencies:**  
   - pandas, numpy, matplotlib, seaborn, scikit-learn, xgboost (for regression), scipy
3. **Run the notebooks** in order for data cleaning, analysis, and modeling.
4. **Modify file paths** if your directory structure differs.

---

## 🧠 Example Analyses

- **Predicting Legend Role:**  
  Given a game's performance (e.g., `Kills=X`, `Damage=Y`), the model predicts which role (Assault, Support, etc.) the player was likely playing.

- **Clustering Legends:**  
  Legends are clustered based on performance metrics to find groups with similar playstyles or effectiveness.

- **Platform Comparison:**  
  Compare stats across PC, Xbox, and PS4 to analyze differences in player performance.

---

## 📈 Features

- Data cleaning and imputation for missing values
- Exploratory data analysis and visualization
- Platform comparison (PC, Xbox, PS4)
- Machine learning models for:
  - Predicting wins from kills (regression)
  - Predicting legend role from game stats (classification)
- Clustering analysis of legends
- Legend-specific performance analysis

---

## 📄 License

This project is for educational and research purposes only. Apex Legends is a trademark of Electronic Arts Inc. Please respect the terms of service of any third-party APIs used.

---

## 🙏 Acknowledgements

- Apex Legends community for data inspiration
- scikit-learn, pandas, matplotlib, seaborn for open-source tools

---
## Notes

- **API Usage:**  
  The [Mozambique API](https://apexlegendsapi.com/) has rate limits. Scripts for API access are not included here for security reasons.

- **Extensibility:**  
  The structure supports adding new platforms, legends, or additional stat categories as needed.

## Contact

For questions or contributions, please open an issue or pull request on the repository.
