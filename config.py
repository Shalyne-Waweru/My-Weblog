import os

class Config:

    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://shalyne:12345@localhost/blogs'
    UPLOADED_PHOTOS_DEST ='app/static/photos'
    UPLOADED_BLOGPHOTOS_DEST ='app/static/blogPhotos'

class ProdConfig(Config):
    pass


class DevConfig(Config):
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}