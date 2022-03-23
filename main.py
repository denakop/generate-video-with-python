from modules.Request import Request
from modules.GenerateVideo import GenerateVideo
from services.ElasticSearch import ElasticSearch
from services.MariaDb import MariaDb



mariadb = MariaDb()
database_host_names = mariadb.get_host_names()

# elasticsearch = ElasticSearch()
# document = elasticsearch.get_document() # get document from elasticsearch
#


# urlArrays = [
#     "https://portalcretinos.ig.com.br/todos-falam-que-essa-mulher-tem-20-anos-mas-ninguem-acredita-quando-ela-revela-sua-verdadeira-idade/",
#     "https://portalcretinos.ig.com.br/equipe-de-linn-lamenta-falecimento-e-sister-continua-sem-saber-nada-dentro-do-bbb22/",
#     "https://portalcretinos.ig.com.br/bbb22-eliminados-voltarao-ao-programa-entenda/",
#     "https://portalcretinos.ig.com.br/bbb22-arthur-aguiar-faz-desabafo-aos-prantos-em-raio-x-e-convocou-seus-fas/"
# ]
#
# request = Request()
# for url in urlArrays:
#     request.getImages(url)
#
# generateVideo = GenerateVideo()
