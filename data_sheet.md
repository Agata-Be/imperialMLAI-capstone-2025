# Dataset Datasheet

## Motivation

**Purpose:**  
The dataset was created to support the development of predictive models that recommend the most suitable crops to grow based on soil and climate conditions. As it is not linked to any specific organization or farmer, its primary purpose is educational. On Kaggle, it is widely used for learning and experimentation.

**Data Creator:**  
The dataset was created by Atharva Ingle, a Data Scientist and Kaggle Competition Expert.

**Other Comments:**  
According to the author, the dataset was built by augmenting multiple sources of rainfall, climate, and fertilizer data from India.

--

## Composition

**Data Composition:**  
- Tabular dataset with 7 numerical features and 1 categorical target (crop label).
- Features: Nitrogen (N), Phosphorus (P), Potassium (K), Temperature (°C), Humidity (%), pH, Rainfall (mm).
- Target: Crop name (22 unique classes).
- Each row represents a set of environmental conditions and the corresponding suitable crop.
- No missing values, duplicates, or outliers identified.
- Dataset is clean, complete, and exhibits meaningful feature-label correlations.
- No predefined train/test splits.

**Confidentiality:**  
No personal, sensitive, or confidential information is included.

---

## Collection Process

Limited information is available. The dataset was compiled by aggregating data from various Indian sources related to rainfall, climate, and fertilizer usage. However, details such as data collection timeframe, specific regions, or institutions involved are not disclosed. This limits generalizability, especially for applications beyond the Indian context.

---

## Preprocessing / Cleaning / Labeling

- The dataset required minimal cleaning due to its quality.
- Preprocessing steps applied:
  1. **Feature scaling** (normalization or standardization).
  2. **Label encoding** (to convert categorical crop names into model-compatible values).
- These transformations were applied during modeling and were not saved as a separate dataset.

---

## Uses

**Other Potential Uses:**  
- Fertilizer recommendation  
- Irrigation planning  
- Agro-climatic zone clustering  
- Precision agriculture education and experimentation  

**Considerations and Risks:**  
- The data reflects *Indian agro-climatic conditions* and may not generalize to other geographies.
- It assumes access to *soil and weather sensors*, which may not be available to all farmers.
- It omits economic, cultural, and practical factors affecting real-world crop choices.
  
To avoid misuse:
- Validate models on local data before deployment elsewhere.
- Use model outputs to *support*, not replace, expert agronomic advice.
- Avoid integrating into policy or subsidy programs without fairness checks.

**Unsuitable Uses:**  
- Policy or subsidy decisions without broader context.  
- Market forecasting, land classification, or crop pricing tasks.  
- Health, safety, or toxicity assessments.

---

## Distribution

**Status:**  
The dataset is publicly available on [Kaggle](https://www.kaggle.com/datasets/atharvaingle/crop-recommendation-dataset/data) and is commonly used for research and educational purposes.

**License:**  
Released under the *Apache 2.0 License*, allowing use, modification, and distribution — including commercial use — with proper attribution.

---

## Maintenance

**Maintainer:**  
The dataset is maintained by its original contributor on Kaggle. There is no formal update schedule or versioning process. Project-specific adaptations are the responsibility of the individual user.
