# Trade-Off Analysis of Statistical and Machine Learning Models in Energy Load Forecasting

**Author:** Sidnei José de Castro Ribeiro Junior  
**Institution:** Technological Federal University of Paraná (UTFPR)  
**Advisor:** Adolfo Neto

![Status](https://img.shields.io/badge/Status-In%20Progress-yellow)

## Overview

This project performs a trade-off analysis between statistical and machine learning (ML) models for short-term energy load forecasting in the Southeast region of Brazil. The two fronts of comparison are **accuracy** and **computational cost**.

The hypothesis is that statistical models will be faster but less accurate than ML models, due to their relative simplicity and lower degree of flexibility.

---

## Models

| Model | Paradigm |
|---|---|
| Linear Regression (LR) | Statistical (baseline) |
| SARIMAX | Statistical |
| XGBoost | Machine Learning |
| LSTM | Machine Learning |

---

## Dataset

- **Energy demand data:** National Electric System Operator ([ONS](https://dados.ons.org.br/dataset/curva-carga)) — hourly data from 2023 to 2024, Southeast region only.
- **Meteorological data:** National Institute of Meteorology ([INMET](https://bdmep.inmet.gov.br/)) — hourly data from January 2023 to December 2024, all stations in the Southeast region.

---

## Evaluation Metrics

**Accuracy:**
- RMSE — Root Mean Squared Error
- MAE — Mean Absolute Error
- MAPE — Mean Absolute Percentage Error

**Computational Cost:**
- Training time
- Inference time

---

## Feature Engineering

- Lag features: 1h, 2h, 3h, 6h, 12h, 24h, and 48h prior
- Perceived temperature (Wind Chill / Heat Index)
- Meteorological season (meteorological calendar, Southern Hemisphere)
- Weekend boolean indicator
- Dummy encoding for categorical variables

---

## Environment & Setup

| Component | Version |
|---|---|
| Python | 3.13.7 |
| Jupyter Lab | 4.4.6 |
| Docker | 28.5.1 |
| OS | EndeavourOS 2025.03.19 |

**Hardware:**
- CPU: Intel i5-14400F
- RAM: 32 GB DDR4
- GPU: NVIDIA RTX 5060

### Installation

#### Using Docker Compose (Recommended)
```bash
# Clone the repository
git clone https://github.com/SiddiJr/energy-load-forecast
cd energy-load-forecast

# Build and start the container
docker-compose up -d

# Access Jupyter Lab at http://localhost:8888
```

#### Manual Installation
```bash
# Clone the repository
git clone https://github.com/SiddiJr/energy-load-forecast
cd energy-load-forecast

# Install dependencies
pip install -r requirements.txt

# Launch Jupyter Lab
jupyter lab
```
---

## Methodology Summary

1. **Data collection** — ONS load demand + INMET meteorological data
2. **Pre-processing** — imputation, feature selection via correlation analysis, column renaming
3. **Feature engineering** — lag features, perceived temperature, seasonal dummies
4. **Cross-validation** — scikit-learn `TimeSeriesSplit` to prevent data leakage
5. **Hyperparameter tuning** — Random Search for XGBoost and LSTM; autocorrelation/partial autocorrelation analysis for SARIMAX
6. **Evaluation** — RMSE, MAE, MAPE, training time, inference time
7. **Interpretability** — statsmodels summaries (LR, SARIMAX), XGBoost Feature Importance, SHAP values (LSTM)

## Sobre
Sidnei Junior - https://www.linkedin.com/in/sidjr/
