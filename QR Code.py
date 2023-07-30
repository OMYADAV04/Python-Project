import qrcode
from PIL import Image

# Create the QR code object
qr = qrcode.QRCode(
    version=15,
    box_size=5,
    border=5
)

data = "https://www.tpolymumbai.in/"
qr.add_data(data)
qr.make(fit=True)

# Generate the QR code image as a PIL Image object
qr_image = qr.make_image(fill_color="red", back_color="yellow")

# Convert the PIL Image to RGBA mode to support transparency
qr_image = qr_image.convert("RGBA")

# Create a blank image with the desired colors
colored_image = Image.new("RGBA", qr_image.size, (255, 0, 0, 0))  # Red background

# Composite the QR code image onto the colored image
final_image = Image.alpha_composite(colored_image, qr_image)

# Save the final image
final_image.save("QR.png")