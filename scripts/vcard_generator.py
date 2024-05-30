# This script will help you generate a vcf file containing your information and then produce a png with it 

# imports
# imports for vCard
from vobject import vCard
from vobject.vcard import Name

# imports for QR
import qrcode

# create contact info
# you can add more attributes. check this link: https://en.wikipedia.org/wiki/VCard
# remember to remove <>

contact_me = {
    'N': Name(family='<your_last_name> - <your_country>', given='<your_first_name>') # I'm going to a conference so I'm also adding my country for easy recalling
    , 'FN': '<your_first_name> <your_last_name> - <your_country>' 
    , 'TEL': '<+123456789>' #Remember to include the plus sign and country code
    , 'EMAIL': '<your_email@email.com>'
    , 'URL': '<your_website.com>'
    , 'NOTE': 'Affiliated to <your_org>' # Using the ORG attribute returned semicolons so I'm using this instead
}

# create and being vCard
vcard = vCard()
vcard.name = 'vCard'
vcard.useBegin = True

# loop to use dictionary values
for key, value in contact_me.items():
    vcard.add(key).value = value

# store vCard in object
qr_vcard = vcard.serialize()

# write the vCard to a vcf file
with open('./files/contact.vcf', 'w') as f:
    f.write(vcard.serialize())

#### QR for vCard
# let's create a qr with the vCard!

qr = qrcode.QRCode(
    version = 1
    , error_correction = qrcode.constants.ERROR_CORRECT_L # this is a simple QR so error correction doesn't need to be high
    , box_size = 14 
    , border = 2,
)

# it may be more tidy to specify here the colors to be used later
bg = (0, 0, 0)
fill = (255, 255, 255)

# add your vCard here
qr.add_data(qr_vcard)

# make it!
img = qr.make_image(
    back_color = bg
    , fill_color = fill)

# save it!
img.save("./files/qr_vCard.png")