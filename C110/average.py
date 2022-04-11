import pandas as pd
import statistics as st
import plotly.figure_factory as ff
import random
df = pd.read_csv('newdata.csv')
avg = df['average'].tolist()
finaldata = []
def sampling():
    data = []
    for a in range(0,100):
        rp = random.randint(0,len(avg)-1)
        data.append(avg[rp])
    mean = st.mean(data)
    finaldata.append(mean)
for a in range(0,1000):
    sampling()

graph = ff.create_distplot([finaldata],['average'],show_hist=False)
graph.show()