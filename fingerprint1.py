from PIL import Image
# Load the fingerprint image
fingerprint = Image.open("H://screen/fingerprint.PNG")

# Convert the image to grayscale
fingerprint1 = fingerprint.convert('L')

# Create a new blank image of the same size
mask = Image.new('L', fingerprint1.size, 0)

# Get the pixel data for the images
fingerprint_data = fingerprint1.load()
mask_data = mask.load()

# Iterate through each pixel and create the mask
for y in range(fingerprint1.size[1]):
    
    for x in range(fingerprint1.size[0]):
        # Apply a threshold to determine the mask value
        if fingerprint_data[x, y] >0:
            mask_data[x, y] = 0

# Apply the mask to the fingerprint image
masked_fingerprint = Image.new('L', fingerprint1.size, 0)
masked_fingerprint.paste(fingerprint1, mask=mask)

# Save the masked fingerprint image
masked_fingerprint.save('masked_fingerprint.PNG') 
fingerprint1.save('fingerprint1.PNG')
# combining two images
width1, height1 = fingerprint1.size
width2, height2 = masked_fingerprint.size
total_width = width1 + width2
max_height = max(height1, height2)
combined_image = Image.new("RGB", (total_width+50, max_height),(0,100,0))
combined_image.paste(fingerprint1, (0, 0))
combined_image.paste(masked_fingerprint, (width1+50, 0))
combined_image.save('combined_image.PNG')