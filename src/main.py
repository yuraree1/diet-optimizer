import pandas as pd
from pulp import LpProblem, LpMinimize, LpVariable, lpSum, value, LpStatus, PULP_CBC_CMD

products_data=pd.read_csv("../data/products.csv")


model=LpProblem(name="Minimize_diet_cost", sense=LpMinimize)

product_vars={x: LpVariable(name=f"{x}", lowBound=0) for x in products_data["name"]}



calories_terms=[]
protein_terms=[]
fat_terms=[]
carbs_terms=[]
price_terms=[]


for index, row in products_data.iterrows():
    calories_terms.append(row["calories"] * product_vars[row["name"]])
    protein_terms.append(row["protein"] * product_vars[row["name"]])
    fat_terms.append(row["fat"] * product_vars[row["name"]])
    carbs_terms.append(row["carbs"] * product_vars[row["name"]])
    price_terms.append(row["price"] * product_vars[row["name"]])


model+=lpSum(price_terms)

model+=(lpSum(price_terms)<=700, "budget")
model+=(lpSum(calories_terms)<=2400, "kkal")
model+=(lpSum(protein_terms)>=120, "protein")
model+=(lpSum(fat_terms)<=50, "fat")
model+=(lpSum(carbs_terms)<=200, "carbs")



max_per_product=2
for k, v in product_vars.items():
    model += (v<= max_per_product, f"max_{k}")

model.solve(PULP_CBC_CMD(msg=False))

if LpStatus[model.status]=="Infeasible":
    print("The constraints contradict each other")

else:

    for k, v in product_vars.items():
        if v.varValue>0.0000001:
            print(f"{k}: {v.varValue:.2f}")

    print(f"Total cost: {value(model.objective):.2f}")






