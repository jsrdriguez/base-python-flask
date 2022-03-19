from .dev import DevConfig
from .prod import ProdConfig
from .local import LocalConfig
from .test import TestConfig

config = {
  'prod': ProdConfig,
  'dev': DevConfig,
  'local': LocalConfig,
  'test': TestConfig
}