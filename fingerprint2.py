from PIL import Image

# Create a red image (255 intensity for red, 0 for green and blue)
red_image = Image.new("RGB", (500,500),(50,100,255))

# Save the image
red_image.save("red_image.jpg")
from PIL import Image, ImageDraw

# Create a new image with a white background
width, height = 300, 200
new_image = Image.new("RGB", (width, height), "white")

# Create a drawing object
draw = ImageDraw.Draw(new_image)

# Draw a red rectangle on the image
rectangle_color = "red"
rectangle_coordinates = [(50, 50), (250, 150)]
draw.rectangle(rectangle_coordinates, fill=rectangle_color)

# Save the created image
new_image.save("created_image.jpg")

