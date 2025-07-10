from hashids import Hashids
from django.conf import settings

hashids = Hashids(settings.HASHIDS_SALT, min_length=8)

def h_encode(id):
    return hashids.encode(id)

def h_decode(h):
    if z := hashids.decode(h):
        return z[0]


class HashIdConverter:
    regex = '[a-zA-Z0-9]{8,}'

    def to_python(self, value):
        return h_decode(value)

    def to_url(self, value):
        return h_encode(value)
