import pandas as pd
import numpy as np

footbal = pd.read_csv('D://Academics//Placement preparation//BungeeTech//internship-test2-master//internship-test2-master//input//question-3//main.csv')



discipline = footbal[['Team', 'Yellow Cards', 'Red Cards']]

discipline.sort_values(by=['Red Cards', 'Yellow Cards'], ascending = False)

print(discipline)