import qrcode

# Website URL you want the QR code to lead to
website_url = "https://www.youtube.com"

# Generate QR code
qr = qrcode.QRCode(
    version=1,  # controls the size of the QR Code
    error_correction=qrcode.constants.ERROR_CORRECT_H,  # high error correction
    box_size=10,
    border=4,
)

qr.add_data(website_url)
qr.make(fit=True)

# Create an image of the QR code
img = qr.make_image(fill_color="black", back_color="white")

# Save the image
img.save("website_qr_code.png")

print("QR code generated and saved as 'website_qr_code.png'")
