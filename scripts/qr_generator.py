# This script will help you generate a png file containing a QR Code. 
# The QR Code can be scanned to obtain a vCard.

# imports
import qrcode

# Create the QR Code to be scanned
qr = qrcode.QRCode(
    version = 1
    , error_correction = qrcode.constants.ERROR_CORRECT_L # this is a simple QR so should be able to be scanned easily
    , box_size = 14 
    , border = 2,
)

# perhaps it may be more tidy to specify here the colors to be used later
bg = (0, 0, 0)
fill = (255, 255, 255)

# add your website here
qr.add_data('https://<your_website.com>')

# make it!
img = qr.make_image(
    back_color = bg
    , fill_color = fill)

# save it!
img.save("./files/qr_code_website.png")