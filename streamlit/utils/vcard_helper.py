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

        # Name
        fullname = vcard.add('fn')
        fullname.value = self.name
        n = vcard.add('n')
        n.value = vobject.vcard.Name(family=self.name.split()[-1], given=' '.join(self.name.split()[:-1]))

        # Title
        if self.title:
            title = vcard.add('title')
            title.value = self.title

        # Organization
        if self.organization:
            org = vcard.add('org')
            org.value = self.organization

        # Email
        if self.email:
            email = vcard.add('email')
            email.value = self.email

        # Phone
        if self.phone:
            tel = vcard.add('tel')
            tel.value = self.phone

        # Website
        if self.website:
            url = vcard.add('url')
            url.value = self.website

        return vcard.serialize()