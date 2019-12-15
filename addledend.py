from PIL import Image, ImageDraw, ImageFont
import os

filename = 'homelab.png'

legend = """\
Out of service
Not built
"""

diag = Image.open(filename)

width, height = diag.size

# Setting rectangle position
start_x = width - 210
end_x = width - 230
start_y = 5
end_y = 15

# Setting font
RictyFont = ImageFont.truetype(os.path.abspath('C:\Windows\Fonts\RictyDiminished-Regular.ttf'), 18)

draw = ImageDraw.Draw(diag)

# Add legend in top right
# end x, end y, start x, start y
draw.rectangle((end_x, end_y, start_x, start_y), fill='lightgray')
draw.rectangle((end_x, end_y + 20 , start_x, start_y + 20), fill='lightblue')

draw.text((width - 200 ,0), legend, fill='black', font=RictyFont)

diag.save('_'.join(['legend', filename]))
