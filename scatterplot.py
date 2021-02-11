import pandas as pd
import plotly.express as px
df = pd.read_csv("Covid Data.csv")
fig = px.scatter(df, x = "Date", y = "No of Cases", color = "Country")
fig.show()