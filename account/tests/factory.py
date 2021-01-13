from core import fields
import factory
from ..models import Account

"""

Mock Account

"""


class AccountFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Account

    name = factory.Sequence(lambda n: "Name {}".format(n))
    legalname = factory.Sequence(lambda n: "Legalname {}".format(n))
    vat = factory.Sequence(lambda n: "Vat {}".format(n))
    address = factory.Sequence(lambda n: "address {}".format(n))
    city = factory.Sequence(lambda n: "city {}".format(n))
    zipcode = factory.Sequence(lambda n: "zipcode {}".format(n))
    country = factory.Sequence(lambda n: "Country {}".format(n))
    province = factory.Sequence(lambda n: "Province {}".format(n))
    geo = factory.Sequence(lambda n: "Geo {}".format(n))
    phone = factory.Sequence(lambda n: "Phone {}".format(n))
    email = factory.Sequence(lambda n: "Email {}".format(n))
    pec = factory.Sequence(lambda n: "Pec {}".format(n))
    sdi = factory.Sequence(lambda n: "Sdi {}".format(n))
    type = 0
