import plotly.offline as py
from plotly.graph_objs import Scatter, Layout
import plotly.graph_objs as go

import plotly.offline as of
import plotly.graph_objs as go

of.offline.init_notebook_mode(connected=True)
trace0 = go.Scatter(
    x=[1, 2, 3, 4],
    y=[10, 15, 13, 17],
    #散点图
    mode='markers'
)
trace1 = go.Scatter(
    x=[1, 2, 3, 4],
    y=[16, 5, 11, 9]
)
data = go.Data([trace0, trace1])
of.plot(data)