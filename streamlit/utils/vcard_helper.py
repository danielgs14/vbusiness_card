import vobject

class cardgenerator:
    def __init__(self, name, title=None, organization=None, email=None, phone=None, website=None):
        self.name = name
        self.title = title
        self.organization = organization
        self.email = email
        self.phone = phone
        self.website = website

    def generate_vcard(self):
        vcard = vobject.vCard()

        vcard.add('n')
        vcard.n.given = self.name.split()[0]
        vcard.n.family = self.name.split()[-1]

        vcard.add('fn')
        vcard.fn.value = self.name

        vcard.add('email')
        vcard.email.value = self.email

        vcard.add('tel')
        vcard.tel.value = self.phone

        vcard.add('title')
        vcard.title.value = self.title

        vcard.add('url')
        vcard.url.value = self.website

        if self.organization:
            vcard.add('org')
            vcard.org.value = self.organization
            vcard.org.encoding = 'UTF-8'

        return vcard.serialize()