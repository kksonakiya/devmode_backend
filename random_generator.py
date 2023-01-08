import string
import random

def id_generator(N):

    uid=''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(N))
    return uid




