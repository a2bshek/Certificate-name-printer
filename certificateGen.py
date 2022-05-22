from PIL import Image, ImageFont, ImageDraw
import pandas

font_ttf = ImageFont.truetype(r'font.ttf', 70)
font_color = "#AE8126"
w,h = 1350, 865

def make_cert(name):
    image_source = Image.open(r'template.png')
    draw = ImageDraw.Draw(image_source)
    name_width, name_height = draw.textsize(name, font=font_ttf)
    draw.text((w-name_width/2, h-name_height/2), name, fill=font_color, font=font_ttf)
    image_source.save("./Cert/" + name+".png")
    print(name ' - Successfully printed')

data = pandas.read_excel("./names.xlsx")
names = list(data.Name)
for i in names:
    make_cert(i)
