import pandas as pd
from pulp import LpProblem, LpMinimize, LpVariable, lpSum

products_data=pd.read_csv("../data/products.csv")


model=LpProblem(name="small-price", sense=LpMinimize)

product_vars={x: LpVariable(name=f"{x}", lowBound=0) for x in products_data["name"]}

name_price=dict(zip(products_data["name"], products_data["price"]))


terms=[name_price[name] * product_vars[name] for name in name_price]

model+=lpSum(terms)

print(model)