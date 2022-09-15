import pandas as pd
import numpy as np
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import MinMaxScaler
from sklearn.ensemble import RandomForestClassifier
import pickle

def data_cleaning(df):
    df = df.copy()
    df = df.drop_duplicates()
    df = df.replace({"P":"Healthy","N":"Diseased"})
    df.columns = list(map(lambda x: x.lower(), df.columns))
    df.columns = df.columns.str.replace(" ", "_")
    df = df.drop(["t3_measured","tsh_measured","tt4_measured","t4u_measured","fti_measured",
           "referral_source", "query_on_thyroxine","query_hypothyroid",
           "query_hyperthyroid", "psych", "tbg_measured", "tbg"],axis=1)
    df = df.replace("?", np.nan)
    cols = ["age", "tsh", "t3", "tt4", "t4u", "fti"]
    for col in cols:
        df[col] = pd.to_numeric(df[col])
    df = df.dropna(subset = ["age"])
    imputer_median = SimpleImputer(strategy="median")
    imputer_mode = SimpleImputer(strategy="most_frequent")
    cols = ["tsh", "t3", "tt4", "t4u", "fti"]
    for col in cols:
        df[col] = imputer_median.fit_transform(df[[col]])
    df["sex"] = imputer_mode.fit_transform(df[["sex"]])
    df = df[df["age"] < 120]
    return df

def feature_selection(df):
    df = df.copy()
    df = df.drop(["t4u", "age", "tt4", "thyroid_surgery", "tumor", "i131_treatment", "hypopituitary",
            "sick", "lithium"], axis = 1)
    return df


def load(filename = "filename.pickle"): 
    try: 
        with open(filename, "rb") as file: 
            return pickle.load(file) 
    except FileNotFoundError: 
        print("File not found!")
