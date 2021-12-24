from plotly import colors

for key in colors.PLOTLY_SCALES.keys():
    print(key)
    
# how colorscale 'Greens' is defined
print(colors.PLOTLY_SCALES['Greens'])