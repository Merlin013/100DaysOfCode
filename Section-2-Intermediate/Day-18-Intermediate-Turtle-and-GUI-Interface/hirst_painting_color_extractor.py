import colorgram

rgb_colors = []
colors = colorgram.extract("image.jpg", 30)
# print(colors)
"""This part of the code is used to extract rgb color values from a given image"""
for color in colors:
    # rgb_colors.append(color.rgb)
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r, g, b)
    rgb_colors.append(new_color)

print(rgb_colors)

color_list = [(237, 245, 240), (212, 149, 95), (215, 80, 62), (47, 94, 142), (231, 218, 92), (148, 66, 91),
              (22, 27, 40), (155, 73, 60), (122, 167, 195), (40, 22, 29), (39, 19, 15), (209, 70, 89),
              (192, 140, 159), (39, 131, 91), (125, 179, 141), (75, 164, 96), (229, 169, 183), (15, 31, 22),
              (51, 55, 102), (233, 220, 12), (159, 177, 54), (99, 44, 63), (35, 164, 196), (234, 171, 162),
              (105, 44, 39), (164, 209, 187), (151, 206, 220)]
