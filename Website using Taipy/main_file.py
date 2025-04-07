from taipy import Gui
import pandas as pd

title = "Bar Graph by Mujtaba"
path = "logo.png"  
name_product = "Car"
max_price = '200'
min_price = '100'

def submit_display(state):
    # This function will be called when the button is clicked
    print("Your data has been saved!")
    print("Product Name:", state.name_product)
    print("Max Price:", state.max_price)
    print("Min Price:", state.min_price)

    with open("my_data.txt", "w") as file:
        file.write(f"Product Name: {state.name_product}")
        file.write(f", Max Price: {state.max_price}")
        file.write(f", Min Price: {state.min_price} ")

data = {
    "Date": pd.date_range("01-04-2025", periods=4, freq="D"),
    "Temp°C": [-15,-12.9,7.2,10.2],
    "Min": [-22,-19,2.7,6.5],
    "Max": [-8.6,12.1,2,13.5]
}

page = """
<|text-center|
<|{path}|image|>

<|{title}|hover_text=This is a simple bar graph example|>

What is the name of the product: <|{name_product}|input|>

Max. Price of the product: <|{max_price}|input|>

Min. Price of the product: <|{min_price}|input|>

<| Submit |button|on_action=submit_display|>

<|{title}|hover_text=This is a simple graph|>

<|{data}|chart|mode=lines|x=Date|y[1]=Temp°C|y[2]=Min|y[3]=Max|line[1]=dash|color[2]=blue|color[3]=red|>
""" 

if __name__ == '__main__':
    app = Gui(page)
    app.run(use_reloader=True)

