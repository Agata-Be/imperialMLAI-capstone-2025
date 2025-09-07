# Model Card - Crop Recommendation Model

---

## Model Description

**Input:**  
The model takes seven environmental and soil features as input:  
- Nitrogen (N) – ratio of nitrogen content in soil  
- Phosphorus (P) – ratio of phosphorus content in soil  
- Potassium (K) – ratio of potassium content in soil  
- Temperature (°C)  
- Humidity (%)  
- pH value of the soil  
- Rainfall (mm)  

**Output:**  
- A categorical prediction of the most suitable crop to grow under the given conditions (22 possible crop labels).

**Model Architecture:**  
- **Primary Model:** Random Forest Classifier (ensemble of decision trees; selected for its high accuracy and stability)  
- **Alternative Model:** Logistic Regression (simpler, more interpretable, slightly lower accuracy)  
- **Additional Models Tested:**  
  - **Decision Tree Classifier**  
  - **Gradient Boosting Classifier**  
  - **XGBoost Classifier**  
  (these models achieved strong performance but still underperformed compared to Random Forest, so they were not selected for deployment)  
- **AdaBoost Classifier:** Tested but showed lower performance and was not pursued further  


---

## Performance

The models were evaluated using *stratified 5-fold cross-validation*. Accuracy, precision, recall, and F1-score were used as evaluation metrics.  

| Model               | Mean Accuracy | Std Dev | Notes                          |
|---------------------|---------------|---------|--------------------------------|
| Random Forest       | *0.9948*    | 0.002   | Best performing, very stable   |
| Logistic Regression | 0.9613        | 0.003   | Interpretable, lightweight     |
| AdaBoost            | 0.7911        | 0.014   | Underperformed, not pursued    |

- Random Forest was the strongest from all tree-based models, it achieved the highest and most stable performance.  
- Logistic Regression also performed strongly, with the advantage of interpretability.  
- AdaBoost lagged significantly and was excluded from further tuning.  

---

## Limitations

- The dataset is *specific to Indian agro-climatic conditions* and may not generalize globally without retraining.  
- The dataset includes only *22 crop types*; new crops are not supported.  
- *No spatial, geolocation, or temporal variation* is captured (e.g., seasonal effects).  
- *Socioeconomic and market factors* influencing crop choice are not included.  
- The model assumes *accurate soil and weather measurements*, which may not be accessible to all farmers.

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

- **Fairness:** Using the dataset without local validation could disadvantage farmers in regions with different climates, soils, or crops.  
- **Access:** Assumes availability of soil and climate sensors, which may not be equitable across farming communities.  
- **Risk of misuse:** Should not be directly applied for high-stakes decisions (e.g., subsidies, loans, or land allocation) without additional contextual data and expert oversight.  

---

## Recommendations

- Use this model for **educational, research, and prototyping purposes** in agriculture.  
- For real-world deployment:  
  - Validate on **local datasets** before use.  
  - Combine predictions with **expert agronomic advice**.  
  - Integrate **real-time weather and soil sensor data** for improved accuracy.  
  - Expand the dataset to cover **more regions, seasons, and crop types**.  

---