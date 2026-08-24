

def input_parameters():
    parameter=["budget", "kkal", "protein", "fat", "carbs"]
    data_parameter={}

    for i in parameter:
        data_parameter[i]=int(input(f"Enter a {i}: "))

    return data_parameter