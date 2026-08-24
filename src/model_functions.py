from pulp import LpProblem, LpMinimize, LpVariable, lpSum, value, LpStatus, PULP_CBC_CMD

def summary(products_data):

    terms={
        "calories_terms":[],
        "protein_terms":[],
        "fat_terms":[],
        "carbs_terms":[],
        "price_terms":[]
        }
    
    

    product_vars={x: LpVariable(name=f"{x}", lowBound=0) for x in products_data["name"]}

    for index, row in products_data.iterrows():
        terms["calories_terms"].append(row["calories"] * product_vars[row["name"]])
        terms["protein_terms"].append(row["protein"] * product_vars[row["name"]])
        terms["fat_terms"].append(row["fat"] * product_vars[row["name"]])
        terms["carbs_terms"].append(row["carbs"] * product_vars[row["name"]])
        terms["price_terms"].append(row["price"] * product_vars[row["name"]]) 

    return terms, product_vars

def calculate_model(terms, data_parameter):
    model=LpProblem(name="Minimize_diet_cost", sense=LpMinimize)

    model+=lpSum(terms["price_terms"])


    model+=(lpSum(terms["price_terms"])<=data_parameter["budget"], "budget")
    model+=(lpSum(terms["calories_terms"])<=data_parameter["kkal"], "kkal")
    model+=(lpSum(terms["protein_terms"])>=data_parameter["protein"], "protein")
    model+=(lpSum(terms["fat_terms"])<=data_parameter["fat"], "fat")
    model+=(lpSum(terms["carbs_terms"])<=data_parameter["carbs"], "carbs")

    return model