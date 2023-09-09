from odnoklassniki_parser.database import Meme, insert


class OdnoklassnikiParserPipeline:
    def process_item(self, item, spider):
        insert(Meme(**item))
        return item
