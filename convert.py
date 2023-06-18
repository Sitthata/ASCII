from PIL import Image

image = Image.open("output.png")

image.rotate(-90).save("output.png")
