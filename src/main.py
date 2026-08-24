from read import read_file
from input_data import input_parameters
from model_functions import summary, calculate_model
from output_data import output


def main():
    data_input=input_parameters()
    products=read_file()
    terms, product_vars=summary(products_data=products)
    model=calculate_model(terms=terms, data_parameter=data_input)
    output(product_vars=product_vars, model=model)
    

main()
