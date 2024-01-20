import turtle 

rgb_colors = []
colors = colorgram.extract('spongebob.jpeg', 30)
for color in colors:
    r = colors.rbg.r
    g = colors.rbg.g 
    b = colors.rgb.b
    new_color = (r,g,b)
    rgb_colors.append(new_color)

print(rgb_colors)
