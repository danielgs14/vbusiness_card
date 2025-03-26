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

        name_parts = self.name.split()
        if len(name_parts) >= 2:
            given_name = " ".join(name_parts[:-1])
            family_name = name_parts[-1]
        else:
            given_name = ""
            family_name = self.name

        n = vcard.add('n')
        n.value = vobject.vcard.Name(family=family_name, given=given_name)

        fn = vcard.add('fn')
        fn.value = self.name

        tel = vcard.add('tel')
        tel.value = self.phone

        email = vcard.add('email')
        email.value = self.email

        url = vcard.add('url')
        url.value = self.website

        if self.organization:
            org = vcard.add('org')
            org.value = [self.organization]

        if self.title:
            title = vcard.add('title')
            title.value = self.title

        return vcard.serialize()