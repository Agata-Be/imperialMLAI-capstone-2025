# Model Card – Crop Recommendation Model

---


## Model Description

**Inputs:**  
The model uses seven environmental and soil features to predict the optimal crop:
- **Nitrogen (N):** ratio of nitrogen in soil  
- **Phosphorus (P):** ratio of phosphorus in soil  
- **Potassium (K):** ratio of potassium in soil  
- **Temperature (°C)**  
- **Humidity (%)**  
- **pH value** of the soil  
- **Rainfall (mm)**  

**Output:**  
- A categorical prediction of the most suitable crop to grow under the given conditions (22 possible crop types).

**Model Architecture:**  
- **Primary model:** **Random Forest Classifier**  
  - Selected for its strong performance (accuracy ~99%) and stability across cross-validation folds.  
- **Alternative model:** **Logistic Regression**  
  - Offers interpretability and low computational cost, with slightly lower accuracy (~97%).  
- **Other models evaluated:**  
  - **Decision Tree Classifier**  
  - **Gradient Boosting Classifier**  
  - **XGBoost Classifier**  
  These performed well but did not outperform Random Forest.  
- **AdaBoost Classifier**  
  - Significantly underperformed and was excluded from further tuning.

---


## Performance

Models were evaluated using **stratified 5-fold cross-validation** on the training set. The final selected model was tested on a hold-out test set. Metrics reported include accuracy, F1-score, precision, and recall.

### Cross-validated Results (baseline)

| Model               | Accuracy (mean) | Std Dev | Notes                                |
|--------------------|-----------------|---------|--------------------------------------|
| **Random Forest**       | **0.9955**        | 0.001   | Highest accuracy, most stable        |
| Logistic Regression | 0.9614          | 0.012   | Interpretable and lightweight        |
| AdaBoost            | 0.2403         | 0.084   | Poor fit; not tuned further          |

### Tuned Results (after hyperparameter optimization)

- **Random Forest** achieved **99.6% accuracy** and strong F1-macro on the test set.  
- **Logistic Regression**, post-tuning, reached **97.6% accuracy**.  
- **Other tree-based models** (Gradient Boosting, XGBoost) performed similarly to Random Forest but were more computationally intensive.

> **Note:** The dataset appears highly separable, and results may overestimate real-world performance. Additional evaluation on noisier, real-world data is recommended before deployment.

---


## Feature Importance (Permuation Importance interpretation summary)

Permutation Importance shows how much model performance degrades when a feature’s values are randomly shuffled. If shuffling a feature significantly reduces accuracy, that feature is considered important.

From the permutation importance charts, we conclude:
- The relative importance of features is consistent across train and test sets, indicating **stability** and **low risk of overfitting**.

- **Humidity** has the **strongest impact** on model performance (>30%) in both sets. Its low standard deviation across runs suggests a stable and dominant contribution.

- **Rainfall, Nitrogen, Potassium, and Phosphorus** all show **moderate importance** (~10–20% range).

- **Temperature and pH** have **minimal impact** on predictions (~1%), suggesting they play a limited role in discriminating between crop types.

---


## Limitations

- Dataset is **specific to Indian agro-climatic zones** and may not generalize to other regions without retraining.  

- Only **22 crop types** are supported — new crops are not covered.  

- No **temporal, spatial, or geolocation features** included — seasonal dynamics and regional soil variations are unaccounted for.  

- No **market, economic, or logistical factors** are included — recommendations are purely agro-environmental.  

- The model assumes **accurate soil and weather measurements** — which may be unavailable or unaffordable for some farmers.  

- **Model performance is likely optimistic** due to dataset simplicity.

---

## Trade-offs

- **Performance vs. Interpretability:**  
  Random Forest provides near-perfect accuracy but is less transparent. Logistic Regression offers interpretability and efficiency, but with slightly lower accuracy.  

- **Generality vs. Specificity:**  
  Model performs exceptionally well on Indian data but may need retraining or validation for use in other climates or soil types.  

- **Practical Deployment vs. Data Availability:**  
  While the model highlights key agronomic drivers (rainfall, humidity, soil nutrients), its usefulness in practice depends on farmers' access to reliable soil and weather data.  

---


## Ethical Considerations

- **Fairness:** Without local validation, applying the model to other regions may disadvantage farmers in different climatic or soil conditions.  

- **Accessibility:** Assumes availability of digital soil and weather sensors, which may not be equitable.  

- **Misuse Risk:** Should not be used for regulatory, financial, or policy decisions (e.g., subsidies or land access) without human oversight.  

- **Data Bias:** Training labels may reflect historical agronomic decisions, not necessarily optimal ones.

---


## Recommendations

- **Use cases:** Educational tools, research, prototyping, and farmer advisory systems (with caution).  

- **Before deployment:**  
  - Validate on **local field data** from the target region  
  - Involve **agronomists** in decision refinement  
  - Combine with **real-time sensor feeds** and **weather forecasts**  
  - Consider expansion to include **economic, geographic, and temporal dimensions**

---