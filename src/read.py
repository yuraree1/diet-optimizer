import pandas as pd


def read_file():
    products_data=pd.read_csv("../data/products.csv")
    return products_data