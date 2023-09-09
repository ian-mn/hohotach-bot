from apscheduler.schedulers.twisted import TwistedScheduler
from odnoklassniki_parser import settings
from odnoklassniki_parser.spiders.spider import OdnoklassnikiSpider
from scrapy.crawler import CrawlerProcess
from scrapy.settings import Settings

crawler_settings = Settings()
crawler_settings.setmodule(settings)
process = CrawlerProcess(settings=crawler_settings)

process.crawl(OdnoklassnikiSpider)

sched = TwistedScheduler()
sched.add_job(
    process.crawl,
    "interval",
    args=[OdnoklassnikiSpider],
    seconds=60 * 60,
)
sched.start()
process.start(False)
