from modules.Request import Request
from modules.GenerateVideo import GenerateVideo
from services.ElasticSearch import ElasticSearch
from services.MariaDb import MariaDb
from modules.FormatUrls import FormatUrls
from urllib.parse import urlparse

import time

start_time = time.time()


def init():
    # init and get hostnames with slider in console database
    mariadb = MariaDb()
    database_host_names = mariadb.get_host_names()

    # init and get urls from elasticsearch
    elasticsearch = ElasticSearch()
    # document = elasticsearch.get_document() # get document from elasticsearch
    document = elasticsearch.get_urls()  # test to get urls from elasticsearch without request

    # format urls to get hostnames equal to database hostnames
    format_urls = FormatUrls(document, database_host_names)
    urls = format_urls.format_urls()





# urls = {
#     '1000': [
#     "https://portalcretinos.ig.com.br/todos-falam-que-essa-mulher-tem-20-anos-mas-ninguem-acredita-quando-ela-revela-sua-verdadeira-idade/",
#     "https://portalcretinos.ig.com.br/equipe-de-linn-lamenta-falecimento-e-sister-continua-sem-saber-nada-dentro-do-bbb22/",
#     "https://portalcretinos.ig.com.br/bbb22-eliminados-voltarao-ao-programa-entenda/",
#     "https://portalcretinos.ig.com.br/bbb22-arthur-aguiar-faz-desabafo-aos-prantos-em-raio-x-e-convocou-seus-fas/",
#     "https://portalcretinos.ig.com.br/familia-se-descuida-e-silvio-santos-e-fotografado-sem-os-dentes-em-momento-intimo-internautas-comentam-a-foto/"
#     ],
#     '2000': [
#     "https://48rsonline.com/inscricoes-para-programa-de-estagio-da-caixa-sao-prorrogadas-veja-nova-data/",
#     "https://48rsonline.com/fenix-realiza-contratacao-com-ugencia-para-preencher-diversas-vagas-que-foram-abertas-setor-de-estoque-producao-e-construcao-civil/",
#     "https://48rsonline.com/empresa-abre-vagas-para-6-funcoes-do-setor-comercial-de-nivel-medio-e-superior-com-salario-de-ate-r-4-00000-comissao/",
#     "https://48rsonline.com/se-voce-tem-disponibilidade-de-trabalhar-no-amazon-jungle-palace-hotel-envie-seu-curriculo-e-concorra-uma-vaga/",
#     "https://48rsonline.com/nube-tem-mais-de-8-mil-vagas-de-estagio-em-todo-o-brasil/"
#     ]
# }

def mount_video(urls):
    request = Request()
    video_name = None
    for account in urls:
        request_time = time.time()
        for url in urls[account]:
            request.getImages(url)
            video_name = urlparse(url).netloc
        print("Request Time %s seconds ---" % (time.time() - request_time))
        GenerateVideo(video_name)


init()
print("Total Time %s seconds ---" % (time.time() - start_time))
