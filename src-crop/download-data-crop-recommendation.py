# %%
import kagglehub
import os

# Download to current directory
try: 
    download_location = "../data"
    path = kagglehub.dataset_download("atharvaingle/crop-recommendation-dataset", path=download_location)
except Exception as e:
    print("Visit this URL to manually download the dataset:", "https://www.kaggle.com/datasets/atharvaingle/crop-recommendation-dataset/data")
# %%
