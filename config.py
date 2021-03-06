import os

class Config:


    NEWS_API_KEY = 'e2213e59a10643e1a9bfd7cdf3ee86b9'
    NEWS_API_BASE_URL = 'https://newsapi.org/v1/source'

class ProdConfig(Config):
    pass

class DevConfig(Config):
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}
