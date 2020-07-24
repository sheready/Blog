import os

class Config:
    '''
    General configuration parent class
    '''
    SQLALCHEMY_DATABASE_URI='postgresql+psycopg2://moringa:Access@localhost/myblogsite'
   
    SECRET_KEY = '! \x06i\x85\xb0xSo\nmbW\xb6\xefT \xd0Dp'
    WTF_CSRF_ENABLED = True

class ProdConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
    
class TestConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:Access@localhost/myblogsite'

class DevConfig(Config):

   DEBUG = True


config_options ={"production":ProdConfig,"default":DevConfig}
config_options = {
    'development':DevConfig,
    'production':ProdConfig,
    'test': TestConfig
}