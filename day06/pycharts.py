from pyecharts.charts import Line
line=Line()
line.add_xaxis(["CHN","GEM","USA"])
line.add_yaxis("ratio",[1.5,1.3,1.0])
line.render()
