# default config
class BaseConfig(object):
    DEBUG = False
    SECRET_KEY = "+1,\xf9\x9e\\\x9c\x81\xa1B\xa5\x19r*\xee\xa1\xb6\xd1qox\xf2\x17\xbe\xad\xf3\xd8*\x82x"
    WTF_CSRF_ENABLED = True
    SALT = "SUMSALT"
    COOKIE_TIMEOUT = "1200"
    ENVNAME = "[Alpha]"
    DBHOST = "localhost"
    DBPORT = "28015"
    DATABASE = "crdb"
    DBAUTHKEY = "R3di5FTW"
    STATHAT_EZ_KEY = 'update_me'
    STATHAT_USE_GEVENT = True
    STATHAT_GEVENT_POOL_SIZE = 10
    STRIPE_PUBKEY = "update_me"
    ASSEMBLY_PRIVATE_KEY = "itisasecret"
    ASSEMBLY_PAYMENTS_URL = "https://payments-sandbox.assembly.com/products/cloudroutes"


class TestConfig(BaseConfig):
    DEBUG = True
    TESTING = True
    WTF_CSRF_ENABLED = False
    DATABASE = "crdb_test"


class DevelopmentConfig(BaseConfig):
    DEBUG = True


class ProductionConfig(BaseConfig):
    DBHOST = "update_me"
    DBPORT = "update_me"
    DATABASE = "crdb"
    DBAUTHKEY = "R3di5FTW"
    STATHAT_EZ_KEY = 'update_me'
    STATHAT_USE_GEVENT = True
    STATHAT_GEVENT_POOL_SIZE = 10
    STRIPE_PUBKEY = "update_me"
    ASSEMBLY_PRIVATE_KEY = "itisasecret"
