from modules.Request import Request
from modules.GenerateVideo import GenerateVideo

urlArrays = [
    "https://portalcretinos.ig.com.br/todos-falam-que-essa-mulher-tem-20-anos-mas-ninguem-acredita-quando-ela-revela-sua-verdadeira-idade/",
    "https://portalcretinos.ig.com.br/equipe-de-linn-lamenta-falecimento-e-sister-continua-sem-saber-nada-dentro-do-bbb22/",
    "https://portalcretinos.ig.com.br/bbb22-eliminados-voltarao-ao-programa-entenda/",
    "https://portalcretinos.ig.com.br/bbb22-arthur-aguiar-faz-desabafo-aos-prantos-em-raio-x-e-convocou-seus-fas/"
]

request = Request()
for url in urlArrays:
    request.getImages(url)

generateVideo = GenerateVideo()
