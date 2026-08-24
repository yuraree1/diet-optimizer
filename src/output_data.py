from pulp import LpProblem, LpMinimize, LpVariable, lpSum, value, LpStatus, PULP_CBC_CMD

def output(product_vars, model):
    max_per_product=2
    for k, v in product_vars.items():
        model += (v<= max_per_product, f"max_{k}")

    model.solve(PULP_CBC_CMD(msg=False))

    if LpStatus[model.status]=="Infeasible":
        print("The constraints contradict each other")

    else:
        print("\n")

        for k, v in product_vars.items():
            if v.varValue>0.0000001:
                print(f"{k}: {v.varValue:.2f}")
        
        print("\n")
        print(f"Total cost: {value(model.objective):.2f}")
