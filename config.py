class Config:
    DEBUG = True
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024  # Max request size 16 MB


class DevelopmentConfig(Config):
    ENV = 'development'


class ProductionConfig(Config):
    DEBUG = False
    ENV = 'production'


config_by_name = {
    'dev': DevelopmentConfig,
    'prod': ProductionConfig
}
