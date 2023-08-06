import string
from faker import Faker
from factory import fuzzy

faker = Faker()


class FuzzyEmail(fuzzy.FuzzyText):
    def __init__(self, domain: str = None, *args, **kwargs):
        self.domain = domain
        super().__init__(*args, **kwargs)

    def fuzz(self):
        domain = self.domain
        kwargs = {'domain': domain}
        kwargs = {k: v for k, v in kwargs.items() if v}
        return faker.email(**kwargs)


class FuzzyPhone(fuzzy.FuzzyText):
    def __init__(self, country_code: str = '', with_plus: bool = False, *args, **kwargs):
        self.country_code = country_code
        self.with_plus = with_plus
        super().__init__(*args, **kwargs)

    def fuzz(self):
        phone = fuzzy.FuzzyText(chars=string.digits, length=self.length).fuzz()
        if self.country_code:
            phone = self.country_code + phone
        if self.with_plus:
            phone = '+' + phone
        return phone


class FuzzyParagraph(fuzzy.FuzzyText):
    def __init__(self, nb_sentences=10, *args, **kwargs):
        self.nb_sentences = nb_sentences
        super().__init__(*args, **kwargs)

    def fuzz(self):
        nb_sentences = self.nb_sentences
        length = self.length
        result = ''
        while len(result) < length:
            paragraph = faker.paragraph(nb_sentences=nb_sentences)
            result += paragraph
        if len(result) > length:
            result = result[:length]
        return result


class FuzzyColor(fuzzy.FuzzyText):
    def __init__(self, with_hex=True, *args, **kwargs):
        self.with_hex = with_hex
        super().__init__(*args, **kwargs)

    def fuzz(self):
        color = faker.hex_color()
        color = color.upper()
        if not self.with_hex:
            color = color.replace('#', '')
        return color
