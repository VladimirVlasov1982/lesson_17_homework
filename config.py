class BaseConfig:
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEBUG = False


class DevConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///test.db'
    RESTX_JSON = {'ensure_ascii': False, 'indent': 2}
    DEBUG = True


PER_PAGE = 5
