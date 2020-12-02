from collections import namedtuple

Color = namedtuple('color', ['red', 'green', 'bllue'])

color = Color(55, 155, 255)

print color.red
