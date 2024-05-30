# This script will help you generate a vcf file containing your information. 

# imports
from vobject import vCard
from vobject.vcard import Name

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

# Print and write the vCard to a file
print(vcard.serialize())
with open('./files/contact.vcf', 'w') as f:
    f.write(vcard.serialize())