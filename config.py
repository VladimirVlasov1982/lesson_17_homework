class BaseConfig:
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///test.db'
    RESTX_JSON = {'ensure_ascii': False, 'indent': 2}


PER_PAGE = 5
