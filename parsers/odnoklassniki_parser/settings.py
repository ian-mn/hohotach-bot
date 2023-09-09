from pydantic import Field, SecretStr
from pydantic_settings import BaseSettings

BOT_NAME = "odnoklassniki_parser"

SPIDER_MODULES = ["odnoklassniki_parser.spiders"]
NEWSPIDER_MODULE = "odnoklassniki_parser.spiders"

ROBOTSTXT_OBEY = False
CONCURRENT_REQUESTS_PER_DOMAIN = 5

#REQUEST_FINGERPRINTER_IMPLEMENTATION = "2.7"
#TWISTED_REACTOR = "twisted.internet.asyncioreactor.AsyncioSelectorReactor"
FEED_EXPORT_ENCODING = "utf-8"

ITEM_PIPELINES = {
    "odnoklassniki_parser.pipelines.OdnoklassnikiParserPipeline": 300,
}


class DBSettings(BaseSettings):
    user: str = Field("parser", env="DB_USER")
    password: SecretStr = Field("123qwe", env="DB_PASS")
    host: str = Field("db", env="DB_HOST")
    port: int = Field(5432, env="DB_PORT")
    name: str = Field("memes", env="DB_NAME")
