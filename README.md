# The Finisher's Signature: A Data-Driven Analysis of Messi vs. Mbappé  
### *An Application of an Expected Goals (xG) Model to Profile Elite Goal-Scorers*

![Python](https://img.shields.io/badge/Python-3.9-blue?logo=python)
![Pandas](https://img.shields.io/badge/Pandas-1.3+-lightgrey?logo=pandas)
![Scikit-learn](https://img.shields.io/badge/Scikit--learn-0.24+-orange?logo=scikit-learn)

---

## 📌 Project Overview

Are all goals created equal?

In football analytics, raw goal counts can deceive. A player’s finishing skill is not simply a product of how many goals they score — but *how difficult* those goals were. This project tackles the challenge of disentangling finishing ability from chance and context by building a custom Expected Goals (xG) model. The aim: to quantitatively evaluate and compare the shot quality, overperformance, and stylistic tendencies of two generational forwards — Lionel Messi and Kylian Mbappé — over four full seasons.

---

## 🔍 Key Findings

- **Elite Overperformance Uncovered**: Confirmed both players as elite, long-term overperformers using 4 seasons of FBRef shot data  
  - *Mbappé: +18.0 Goals vs xG*  
  - *Messi: +5.4 Goals vs xG*
- **Robust Model Performance**: Developed a logistic regression-based xG model with **ROC AUC = 0.83** on hold-out test data — a strong signal of predictive accuracy.
- **Distinct Finishing Archetypes Identified**:  
  - **Mbappé** emerged as a *Dynamic Finisher* — thriving in high-speed, open-play scenarios, often from wider angles.  
  - **Messi** revealed the profile of a *Technical Maestro* — converting more from tight, central positions with clinical precision and footwork.

---

## 📊 Key Visual: Player Finishing Profiles

A side-by-side breakdown of predicted xG vs actual goal outcomes for each player:

![Mbappé xG Scatter Plot](https://github.com/Clarkey33/xG-model/blob/main/images/player_finishing_profile/mbappe_shot_xG_predicted_xG.png?raw=true)
![Messi xG Scatter Plot](https://github.com/Clarkey33/xG-model/blob/main/images/player_finishing_profile/messi_shot_xG_predicted_xG.png?raw=true)

---

## 🧭 Project Components & Links

- 🔗 **[Portfolio Walkthrough](https://clarkey33.github.io/xG-model/)** — High-level, interactive write-up  
- 🎥 **[Video Presentation](https://www.youtube.com/watch?v=4pMvgw1hn94)** — 6-minute walkthrough with visuals  
- 📄 **[Full Technical Report (PDF)](https://github.com/Clarkey33/xG-model/blob/main/report/player_finishing_profile_report.pdf)** — In-depth model, EDA, and evaluation  
- 📓 **[Jupyter Notebooks](https://github.com/Clarkey33/xG-model/tree/main/notebooks)** — Reproducible analysis, model training, and visualizations

---

## 🛠 Tech Stack

- Python  
- Pandas  
- NumPy  
- Scikit-learn  
- Matplotlib  
- Seaborn  
- SHAP  

---

## 📁 Repository Structure

xG-model/
│
├── data/ # Cleaned FBRef shot data
├── images/ # Visualizations for presentation & report
│ └── player_finishing_profile/
├── notebooks/ # Jupyter notebooks (EDA, modeling, evaluation)
├── report/ # Technical PDF report
├── src/ # Core functions and custom modules
├── README.md # This file


## Acknowledgments
*   Shot and match data sourced from FBRef and powered by StatsBomb.

*   Inspired by industry leaders like Opta, and StatsBomb in their efforts to bring advanced metrics to football analysis.