# Crop Recommendation Model
*Capstone Project – AI & ML, Imperial College London (2025)*

## Non-Technical Explanation
This project helps farmers decide which crops are most suitable to grow based on their local soil and climate conditions. By analyzing factors like rainfall, temperature, humidity, soil pH, and nutrient levels (N, P, K), the model suggests the best crop option. The goal is to support smarter agricultural planning, improve yields, and demonstrate how machine learning can assist in sustainable farming. While primarily designed for educational and research purposes, the project highlights how data-driven approaches can complement traditional farming knowledge and help optimize decision-making in agriculture.

## Data
We used the [Crop Recommendation Dataset](https://www.kaggle.com/datasets/atharvaingle/crop-recommendation-dataset/data) (Atharva Ingle, 2020).  
- ~2200 records, each describing soil and climate conditions for a crop.  
- **Features:** Nitrogen (N), Phosphorus (P), Potassium (K), Temperature (°C), Humidity (%), pH, Rainfall (mm).  
- **Target:** 22 crop classes.  
- The dataset is clean, with no missing values or duplicates, and is licensed under the **Apache 2.0 License**.


## Model
We evaluated multiple algorithms: Decision Tree, Gradient Boosting, XGBoost, Logistic Regression, and AdaBoost. **Random Forest** was selected as the primary model due to its superior accuracy (*99.5%*) and stability across folds.  **Logistic Regression** was considered as a simpler, more interpretable alternative, while AdaBoost underperformed.

## Hyperparameter Optimisation
We tuned the models using *cross-validated search*:  
- **Logistic Regression** → GridSearchCV (tuning `C`, `class_weight`, `penalty`)  
- **Decision Tree** → GridSearchCV (tuning `criterion`, `max_depth`, `min_samples_split`, `min_samples_leaf`)  
- **Random Forest** → GridSearchCV (tuning `n_estimators`, `max_depth`, `min_samples_split`, `min_samples_leaf`, `max_features`, `class_weight`)  
- **Gradient Boosting** → GridSearchCV (tuning `n_estimators`, `learning_rate`, `max_depth`, `subsample`, `max_features`)  
- **XGBoost** → RandomizedSearchCV (tuning `n_estimators`, `learning_rate`, `max_depth`, `subsample`, `colsample_bytree`, `min_child_weight`, `reg_lambda`, `gamma`)  
AdaBoost was not tuned further due to weak baseline results. We used *StratifiedKFold cross-validation* with accuracy and F1-score as evaluation metrics.

## Results
- **Random Forest**: 99.5% accuracy (±0.002) – best performance, highly stable  
- **Logistic Regression**: 96.1% accuracy (±0.003), more interpretable  
- **AdaBoost**: 79.1% accuracy, not suitable for deployment  
The results indicate that the model can recommend crops with very high reliability within the dataset’s scope.

**Permutation Importance analysis** shows that *humidity and rainfall* are the strongest predictors, followed by *potassium* and *nitrogen*.**Temperature and pH* contribute very little, likely due to limited variability in the dataset. This indicates that *water management and soil nutrients* are the most critical factors when choosing crops.