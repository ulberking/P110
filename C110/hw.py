import pandas as pd
import statistics as st
import plotly.figure_factory as ff
import random
df = pd.read_csv('medium_data.csv')
list = df['reading_time'].tolist()
finaldata = []
def sampling():
    data = []
    for a in range(0,100):
        rd = random.randint(0,len(list)-1)
        data.append(list[rd])
    mean = st.mean(data)
    finaldata.append(mean)

for a in range(0,1000):
    sampling()
graph = ff.create_distplot([finaldata],['list'],show_hist=False)
graph.show()