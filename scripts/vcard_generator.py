# This script will help you generate a png file containing a QR Code. 
# The QR Code can be scanned to obtain a vCard.

#imports
import qrcode 
import vobject

qr = qrcode.QRCode(
    version = none,
    error_correction = qrcode.constants.ERROR_CORRECT_L,
    box_size = 10,
    border = 4,
)
qr.add_data('Some data')
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")

img = qr.make_image(back_color=(6, 107, 167), fill_color=(250, 186, 118))