import qrcode

# Create QR code with custom text/URL
text = "Hello, this is my QR code!"  # Replace with your desired content
qr = qrcode.make(text)

# Save the QR code as an image
qr.save("my_qrcode.png")

print("QR code has been generated successfully!")
