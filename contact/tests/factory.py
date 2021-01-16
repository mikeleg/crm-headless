from account.tests.factory import AccountFactory
from core import fields

import factory

from ..models import Contact

"""

Mock Contact

"""



class ContactFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Contact

    name = factory.Sequence(lambda n: "name {}".format(n))
    surname = factory.Sequence(lambda n: "surname {}".format(n))
    email = factory.Sequence(lambda n: "test1{}@mail.com".format(n))
    default = True
    account = factory.SubFactory(AccountFactory)
