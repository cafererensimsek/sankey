import xlrd


Label = []
Source = []
Target = []
Value = []
Color2 = []

loc = input("location:")
wb = xlrd.open_workbook(loc + "/deneme.xlsx")
sheet = wb.sheet_by_index(0)

Title = sheet.cell_value(1, 4)
Font = sheet.cell_value(1, 5)
Color = sheet.cell_value(1, 6)
Thickness = sheet.cell_value(1, 7)
Pad = sheet.cell_value(1, 9)

for k in range(sheet.nrows): 
    Label.append((sheet.cell_value(k, 0)))

for i in range(sheet.nrows): 
    Source.append((sheet.cell_value(i, 1)))

for j in range(sheet.nrows): 
    Target.append((sheet.cell_value(j, 2)))

for k in range(sheet.nrows): 
    Value.append((sheet.cell_value(k, 3)))
    
for s in range(sheet.nrows): 
    Color2.append((sheet.cell_value(s, 8)))


import plotly.graph_objects

fig = plotly.graph_objects.Figure(data=[plotly.graph_objects.Sankey(
    node = dict(
      pad = Pad,
      thickness = Thickness,
      line = dict(color = "black", width = 0.5),
      label = Label[1:sheet.nrows],
      color = Color
    ),
    link = dict(
      source = Source[1:sheet.nrows],
      target = Target[1:sheet.nrows],
      value = Value[1:sheet.nrows],
      color = Color2[1:sheet.nrows]
  ))])

fig.update_layout(title_text=Title, font_size=Font)
fig.show()
plotly.io.write_image(fig, file=loc + "\diagram.pdf", format="pdf",
                      scale=None, width=None, height=None)


