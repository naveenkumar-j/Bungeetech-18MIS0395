import pandas as pd
grocery = pd.read_csv("D://Academics//Placement preparation//BungeeTech//internship-test2-master//internship-test2-master//input//question-2//main.csv")


grocery["sales_amount"]=grocery["sales_quantity"].where(
  grocery["unit"]!="pcs",
  grocery["product_description"].str.split("-",expand=True)[1].astype("float")*\
  grocery["sales_quantity"]
)

print(grocery)