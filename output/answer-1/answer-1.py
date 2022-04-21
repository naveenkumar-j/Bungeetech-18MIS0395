import pandas as pd
grocery = pd.read_csv("D://Academics//Placement preparation//BungeeTech//internship-test2-master//internship-test2-master//input//question-1//main.csv")

grocery.head()

grocery.groupby('product_description')['price'].mean()

grocery["price_new"] = grocery['price'].fillna(
   grocery.groupby('product_description')['price'].transform("mean")
)

print(grocery)