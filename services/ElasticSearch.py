from datetime import datetime, timedelta
from elasticsearch import Elasticsearch
from dotenv import load_dotenv

import os


class ElasticSearch:
    def __init__(self):
        self.es = None
        load_dotenv()
        self.host = os.getenv('ELASTICSEARCH_HOSTS')
        self.id = os.getenv('ELASTICSEARCH_API_ID')
        self.key = os.getenv('ELASTICSEARCH_API_KEY')
        self.max_documents = '1000'
        self.connect() # connect to elasticsearch

    def connect(self):
        self.es = Elasticsearch(self.host, verify_certs=False, request_timeout=600, api_key=(self.id, self.key))

    def get_urls(self):
        return {
            '1': [{'key': 'https://sample.denakop.com/examples/xandr-psp-amp.html', 'doc_count': 319},
                      {'key': 'https://sample.denakop.com/examples/implementacao-ad-manager.html', 'doc_count': 102},
                      {'key': 'https://sample.denakop.com/examples/xandr-psp-amp-2.html', 'doc_count': 47},
                      {'key': 'https://sample.denakop.com/examples/denakop-tag.html?denakop_debug=true&pbjs_debug=true',
                       'doc_count': 19}, {
                          'key': 'https://sample.denakop.com/examples/implementacao-ad-manager.html?google_preview=cStYcvHd6scY4fuZkQYw4ZfPmAaIAYCAgODoxcfcrAE&iu=21715141650&gdfp_req=1&lineItemId=5941741827&creativeId=138383705684',
                          'doc_count': 12}], '10000': [{
            'key': 'https://olhardigital.com.br/2022/03/16/carros-e-tecnologia/caloi-traz-de-volta-sua-mobylette-com-motor-eletrico-e-custando-menos-de-r-10-mil/amp/',
            'doc_count': 3128560}, {
            'key': 'https://olhardigital.com.br/2022/03/12/colunistas/asteroide-atingiu-a-terra-nesta-sexta-2-horas-depois-de-ser-descoberto/amp/',
            'doc_count': 2607168}, {
            'key': 'https://olhardigital.com.br/2022/03/13/medicina-e-saude/estudo-aponta-dois-sintomas-que-podem-ser-primeiros-sinais-de-parkinson/amp/',
            'doc_count': 1692634}, {
            'key': 'https://olhardigital.com.br/2022/03/10/ciencia-e-espaco/por-favor-de-a-uma-mae-russa-cujo-filho-morreu-nesta-guerra-injusta-diz-ex-astronauta-da-nasa-ao-devolver-medalha-a-russia/amp/',
            'doc_count': 1386762}, {
            'key': 'https://olhardigital.com.br/2022/03/15/ciencia-e-espaco/cientistas-analisam-duas-bolhas-gigantes-localizadas-no-manto-da-terra/amp/',
            'doc_count': 1112458}],
                '10006': [{'key': 'http://naoentreaki.com.br/boa-noite/', 'doc_count': 2},
                          {'key': 'http://naoentreaki.com.br/geek/', 'doc_count': 2},
                          {'key': 'http://naoentreaki.com.br/wtf/', 'doc_count': 2},
                          {'key': 'http://naoentreaki.com.br/amizade/', 'doc_count': 1},
                          {'key': 'http://naoentreaki.com.br/animais/', 'doc_count': 1}],
                '10010': [{'key': 'https://joaobidu.com.br/horoscopo', 'doc_count': 1044073},
                          {'key': 'https://joaobidu.com.br/horoscopo/signos/previsao-gemeos', 'doc_count': 234060},
                          {'key': 'https://joaobidu.com.br/horoscopo/signos/previsao-virgem', 'doc_count': 230187},
                          {'key': 'https://joaobidu.com.br/horoscopo/signos/previsao-touro', 'doc_count': 228235},
                          {'key': 'https://joaobidu.com.br/horoscopo/signos/previsao-cancer', 'doc_count': 228167}],
                '10016': [{
                    'key': 'https://criticalhits.com.br/cinema-e-tv/usuario-twitter-explica-em-20-segundos-porque-the-big-bang-theory-nao-tem-graca-nenhuma/',
                    'doc_count': 6},
                    {'key': 'http://criticalhits.com.br/fallout-4-melhores-perks/', 'doc_count': 3}, {
                        'key': 'https://criticalhits.com.br/masashi-kishimoto-faz-revelacoes-surpreendentes-sobre-o-triangulo-amoroso-entre-naruto-hinata-e-sakura/',
                        'doc_count': 3}, {
                        'key': 'https://criticalhits.com.br/mod-para-the-sims-4-te-deixa-encher-seu-filho-de-porrada-dentro-do-jogo/',
                        'doc_count': 3}, {
                        'key': 'https://criticalhits.com.br/motor-rock-e-removido-permanentemente-do-steam-e-disponibilizado-de-graca-no-site-do-desenvolvedor/',
                        'doc_count': 1}], '10027': [{
                'key': 'http://famosidades.com.br/famosos/bruna-marquezine-vira-piada-por-erro-ortografico-em-tatuagem/',
                'doc_count': 9}, {
                'key': 'http://famosidades.com.br/famosos/neymar-estaria-investindo-em-atriz-desafeto-de-marquezine/',
                'doc_count': 6}, {
                'key': 'http://famosidades.com.br/famosos/rafa-brites-faz-desabafo-apos-irma-ser-agredida-durante-eleicoes/',
                'doc_count': 6}, {
                'key': 'http://famosidades.com.br/blog-a-fazenda/ana-paula-renault-tem-o-cache-mais-alto-de-a-fazenda/',
                'doc_count': 3}, {
                'key': 'http://famosidades.com.br/famosos/fatima-se-emociona-ao-ler-textao-sobre-separacao-de-bonner/',
                'doc_count': 3}], '10050': [{
                'key': 'http://ciclovivo.com.br/inovacao/tecnologia/ar-condicionado-de-tubos-de-argila-tem-custo-zero-de-energia/',
                'doc_count': 2}],
                '10052': [{'key': 'https://paladar.estadao.com.br/noticias/receita,brownie-de-chocolate,10000067293',
                           'doc_count': 33551}, {
                              'key': 'https://paladar.estadao.com.br/noticias/receita,como-fazer-a-caipirinha-perfeita,70002417070',
                              'doc_count': 20429}, {
                              'key': 'https://paladar.estadao.com.br/noticias/receita,mousse-de-chocolate-perfeita,70003730503',
                              'doc_count': 19902}, {
                              'key': 'https://paladar.estadao.com.br/noticias/receita,como-fazer-o-pao-de-queijo-perfeito,10000007904',
                              'doc_count': 18073},
                          {'key': 'https://esportes.estadao.com.br/programacao/natv', 'doc_count': 17720}],
                '10055': [{'key': 'https://semprefamilia.com.br/virtudes-e-valores/', 'doc_count': 3},
                          {'key': 'https://semprefamilia.com.br/educacao-dos-filhos/', 'doc_count': 2},
                          {'key': 'https://semprefamilia.com.br/assista-6-maneiras-de-ser-um-otimo-tio-ou-tia/',
                           'doc_count': 1}, {
                              'key': 'https://semprefamilia.com.br/assista-como-a-familia-pode-estimular-o-cerebro-dos-avos/',
                              'doc_count': 1}, {
                              'key': 'https://semprefamilia.com.br/grafiteiro-responde-a-mensagens-depressivas-em-banheiro-feminino-de-escola-publica/',
                              'doc_count': 1}],
            '10550': [{'key': 'https://portalcretinos.ig.com.br/todos-falam-que-essa-mulher-tem-20-anos-mas-ninguem-acredita-quando-ela-revela-sua-verdadeira-idade/', 'doc_count': 3},
                      {'key': 'https://portalcretinos.ig.com.br/equipe-de-linn-lamenta-falecimento-e-sister-continua-sem-saber-nada-dentro-do-bbb22/', 'doc_count': 2},
                      {'key': 'https://portalcretinos.ig.com.br/bbb22-eliminados-voltarao-ao-programa-entenda/',
                       'doc_count': 1}, {
                          'key': 'https://portalcretinos.ig.com.br/bbb22-arthur-aguiar-faz-desabafo-aos-prantos-em-raio-x-e-convocou-seus-fas/',
                          'doc_count': 1}, {
                          'key': 'https://portalcretinos.ig.com.br/familia-se-descuida-e-silvio-santos-e-fotografado-sem-os-dentes-em-momento-intimo-internautas-comentam-a-foto/',
                          'doc_count': 1}],
                '10056': [{'key': 'https://www.bnews.com.br/ultimasnoticias.html', 'doc_count': 15193},
                          {'key': 'https://www.bnews.com.br/policia/', 'doc_count': 11400}, {
                              'key': 'https://www.bnews.com.br/noticias/policia/jovem-que-pegou-uber-para-ir-shopping-e-desapareceu-e-encontrado.html',
                              'doc_count': 6776}, {
                              'key': 'https://www.bnews.com.br/noticias/bbb22/bbb-22-sister-sem-correndo-apos-flagrar-movimentacao-suspeita-embaixo-do-edredom.html',
                              'doc_count': 3700}, {
                              'key': 'https://www.bnews.com.br/noticias/policia/mulher-e-estuprada-e-enterrada-viva-proximo-divisa-entre-mg-e-ba.html',
                              'doc_count': 3577}], '10057': [{
                'key': 'https://www.metropoles.com/distrito-federal/na-mira/video-personal-espanca-morador-de-rua-apos-flagrar-traicao-de-mulher',
                'doc_count': 700708}, {
                'key': 'https://www.metropoles.com/colunas/leo-dias/mae-de-marilia-revela-audio-da-cantora-deus-sera-que-vou-morrer',
                'doc_count': 630313}, {
                'key': 'https://www.metropoles.com/entretenimento/bbb/bbb22-para-movimentar-jogo-jade-picon-sugere-beijao-em-arthur-aguiar?amp',
                'doc_count': 339724}, {
                'key': 'https://www.metropoles.com/entretenimento/bbb/bbb22-para-movimentar-jogo-jade-picon-sugere-beijao-em-arthur-aguiar?amp=',
                'doc_count': 312716}, {
                'key': 'https://www.metropoles.com/colunas/leo-dias/exclusivo-mae-de-marilia-abre-quarto-e-mostra-celular-da-cantora',
                'doc_count': 312682}],
                '10059': [{'key': 'https://fatosdesconhecidos.ig.com.br/fale-conosco/', 'doc_count': 7},
                          {'key': 'https://fatosdesconhecidos.ig.com.br/copa2018/', 'doc_count': 4},
                          {'key': 'https://fatosdesconhecidos.ig.com.br/creppypasta/', 'doc_count': 4},
                          {'key': 'https://fatosdesconhecidos.ig.com.br/curiosidades/', 'doc_count': 4},
                          {'key': 'https://fatosdesconhecidos.ig.com.br/fatosnerd/', 'doc_count': 4}], '10060': [
                {'key': 'https://acontecenabahia.com.br/piauiense-de-25-anos-e-o-juiz-federal-mais-jovem-do-brasil/',
                 'doc_count': 2}],
                '10064': [{'key': 'http://tnh1.com.br/tnh1-tv/canal/pajucara-noite/', 'doc_count': 6}, {
                    'key': 'https://tnh1.com.br/noticia/nid/soco-no-rosto-mulher-denuncia-agressao-de-eleitores-de-bolsonaro/',
                    'doc_count': 2}, {'key': 'http://tnh1.com.br/tnh1-tv/canal/pajucara-noite', 'doc_count': 1},
                          {'key': 'http://tnh1.com.brnull', 'doc_count': 1}],
                '10065': [{'key': 'https://testosterona.blog.br/mulheres/lingerie-day-2017', 'doc_count': 1}],
                '10066': [{'key': 'https://www.correiobraziliense.com.br/cidades-df', 'doc_count': 442832}, {
                    'key': 'https://www.correiobraziliense.com.br/mundo/2022/02/4988992-analise-pode-ser-o-comeco-do-fim-de-putin.html',
                    'doc_count': 270596}, {
                              'key': 'https://www.correiobraziliense.com.br/politica/2022/03/4990525-pm-acusado-de-matar-marielle-revela-que-foi-ajudado-por-bolsonaro-em-2009.html',
                              'doc_count': 222060}, {
                              'key': 'https://www.correiobraziliense.com.br/brasil/2022/03/4994378-covid-agrava-o-drama-de-mineira-presa-com-cocaina-na-tailandia.html',
                              'doc_count': 205312}, {
                              'key': 'https://www.correiobraziliense.com.br/politica/2022/03/4993464-mourao-nao-vamos-mais-pagar-rs-4-por-litro-de-gasolina.html',
                              'doc_count': 191601}],
                '10070': [{'key': 'https://clickbebe.net/voce-sabe-o-que-e-parto-humanizado/', 'doc_count': 5}],
                '10072': [{
                    'key': 'https://portalpopline.com.br/christina-aguilera-lanca-video-conceitual-para-nova-musica-twice/',
                    'doc_count': 2}, {
                    'key': 'http://portalpopline.com.br/brasil-da-primeiro-certificado-de-platina-para-crying-club-de-camila-cabello/',
                    'doc_count': 1},
                    {'key': 'http://portalpopline.com.br/leonardo-torres-10-anos-sem-sandy-junior/',
                     'doc_count': 1}, {
                        'key': 'https://portalpopline.com.br/que-performances-bts-canta-e-danca-fake-love-e-idol-no-seoul-music-awards/',
                        'doc_count': 1}], '10075': [{
                'key': 'https://apontador.com.br/local/pr/ponta_grossa/emissoras_de_radio/2U32PKR2/radio_nilson_de_oliveira.html',
                'doc_count': 1}, {
                'key': 'https://apontador.com.br/local/sp/santana_de_parnaiba/enderecos_empresariais/C402376F04445Q445F/creaplan.html',
                'doc_count': 1}, {
                'key': 'https://apontador.com.br/local/sp/santana_de_parnaiba/transporte_geral_/693N8B73/gt_transdore_cargas_jd_professor_benoa.html',
                'doc_count': 1}, {
                'key': 'https://apontador.com.br/local/sp/sao_paulo/hospedagem_e_turismo/C40819842D315Z315E/comfort_vila_mariana.html',
                'doc_count': 1}], '10076': [{
                'key': 'https://istoe.com.br/df-esposa-de-personal-que-agrediu-morador-de-rua-afirma-vi-a-imagem-de-deus/',
                'doc_count': 3698183}, {
                'key': 'https://istoe.com.br/rs-menina-morre-apos-passar-mal-em-sala-de-aula-e-pai-afirma-ela-era-saudavel/',
                'doc_count': 3583431}, {
                'key': 'https://istoe.com.br/mansao-mais-cara-do-mundo-e-vendida-pela-metade-do-preco/',
                'doc_count': 3543104}, {
                'key': 'https://istoe.com.br/dona-do-maior-bumbum-do-brasil-e-assediada-na-rua/',
                'doc_count': 3514251}, {
                'key': 'https://istoe.com.br/juliette-faz-exigencias-absurdas-ao-ser-internada-em-hospital-diz-colunista/',
                'doc_count': 3092399}],
                '10078': [{'key': 'https://odia.ig.com.br/esporte/flamengo', 'doc_count': 88670},
                          {'key': 'https://odia.ig.com.br/esporte', 'doc_count': 62191}, {
                              'key': 'https://odia.ig.com.br/diversao/bbb/2022/03/6350239-video-eliezer-cerca-jessilane-na-piscina-producao-precisa-intervir.html',
                              'doc_count': 29278}, {'key': 'https://odia.ig.com.br/diversao', 'doc_count': 28744}, {
                              'key': 'https://odia.ig.com.br/diversao/televisao/2022/03/6350977-comentaristas-brigam-ao-vivo-em-debate-sobre-guerra-entre-russia-e-ucrania.html',
                              'doc_count': 26795}],
                '10080': [{'key': 'https://blogdoenem.com.br/notas-de-corte-do-sisu/', 'doc_count': 6},
                          {'key': 'https://blogdoenem.com.br/redacao_enem_nota_1000/', 'doc_count': 2},
                          {'key': 'https://blogdoenem.com.br/design/', 'doc_count': 1}], '10083': [{
                'key': 'https://dci.com.br/financas/bradesco-incorpora-empresa-de-seguros-e-emite-363-mil-ac-es-1.49437',
                'doc_count': 8},
                {
                    'key': 'https://dci.com.br/servicos/novos-vazamentos-de-dados-pessoais-evidenciam-buraco-na-fiscalizac-o-1.737545',
                    'doc_count': 3}],
                '10090': [{'key': 'https://womenshealthbrasil.com.br/motivos-de-fazer-muito-coco/', 'doc_count': 1841},
                          {'key': 'https://womenshealthbrasil.com.br/fumar-maconha-durante-a-amamentacao/',
                           'doc_count': 1510},
                          {'key': 'https://runnersworld.com.br/recuperacao-de-lesoes/', 'doc_count': 1416},
                          {'key': 'https://womenshealthbrasil.com.br/o-que-e-capuz-do-clitoris/', 'doc_count': 1048},
                          {'key': 'https://womenshealthbrasil.com.br/fatos-sobre-sexo-anal/', 'doc_count': 1025}],
                '10093': [{
                    'key': 'https://www.superlutas.com.br/noticias/182236/video-assista-o-nocaute-do-ano-sofrido-pela-brasileira-luana-dread-no-ufc-londres/amp/',
                    'doc_count': 43868}, {
                    'key': 'https://www.superlutas.com.br/noticias/180840/dos-anjos-diz-que-tirou-o-pe-do-acelerador-e-critica-treinadores-de-renato-moicano-no-ufc-272/amp/',
                    'doc_count': 35311}, {
                    'key': 'https://www.superlutas.com.br/noticias/182236/video-assista-o-nocaute-do-ano-sofrido-pela-brasileira-luana-dread-no-ufc-londres/',
                    'doc_count': 26853}, {
                    'key': 'https://www.superlutas.com.br/noticias/181005/video-lutador-mexicano-erra-golpe-e-nocauteia-arbitro-em-evento-de-mma-no-bahrein/amp/',
                    'doc_count': 23288}, {
                    'key': 'https://www.superlutas.com.br/noticias/182485/masvidal-e-covington-esquecem-luvas-e-protagonizam-briga-em-restaurante-nos-estados-unidos/amp/',
                    'doc_count': 23255}],
                '10096': [{'key': 'https://www.jornalopcao.com.br/categoria/ultimas-noticias/', 'doc_count': 26553}, {
                    'key': 'https://www.jornalopcao.com.br/opcao-cultural/15-grandes-poemas-para-homenagear-o-dia-da-mulher-88907/',
                    'doc_count': 16777}, {
                              'key': 'https://www.jornalopcao.com.br/ultimas-noticias/cobra-ataca-homem-enquanto-ele-cuidava-de-criancas-na-piscina-veja-video-385694/',
                              'doc_count': 16380},
                          {'key': 'https://www.jornalopcao.com.br/categoria/bastidores/', 'doc_count': 15263}, {
                              'key': 'https://www.jornalopcao.com.br/ultimas-noticias/morte-de-marielle-ronnie-lessa-explica-origem-de-seu-patrimonio-milionario-384522/',
                              'doc_count': 10675}], '10097': [{
                'key': 'https://correio24horas.com.br/noticia/nid/caso-marielle-testemunhas-afirmam-que-pms-mandaram-sair-do-local/',
                'doc_count': 2}], '10098': [{
                'key': 'https://www.revistabula.com/49097-o-filme-da-netflix-que-vai-te-conquistar-desde-a-primeira-cena-e-lavar-sua-alma/',
                'doc_count': 604159},
                {
                    'key': 'https://www.revistabula.com/49133-selvagem-poderoso-e-perturbador-o-filme-da-netflix-que-vai-grudar-na-sua-cabeca/',
                    'doc_count': 597890},
                {
                    'key': 'https://www.revistabula.com/49264-melhor-filme-da-netflix-em-2022-ira-deixa-lo-sem-piscar-ate-a-ultima-cena/',
                    'doc_count': 470694},
                {
                    'key': 'https://www.revistabula.com/48741-balalaica-do-fim-do-mundo/',
                    'doc_count': 436162},
                {
                    'key': 'https://www.revistabula.com/48736-o-filme-delirante-da-netflix-que-te-mantera-imovel-no-sofa-olhos-grudados-na-tv-e-coracao-saindo-pela-boca/',
                    'doc_count': 410506}],
                '10102': [{'key': 'https://www.correiodopovo.com.br/%C3%BAltimas', 'doc_count': 346144}, {
                    'key': 'https://www.correiodopovo.com.br/not%C3%ADcias/pol%C3%ADtica/ministro-onyx-lorenzoni-confirma-antecipa%C3%A7%C3%A3o-do-13%C2%BA-para-aposentados-1.787030',
                    'doc_count': 126147},
                          {'key': 'https://www.correiodopovo.com.br/blogs/hiltormombach', 'doc_count': 78762}, {
                              'key': 'https://www.correiodopovo.com.br/not%C3%ADcias/geral/temporal-provoca-estragos-em-porto-alegre-1.783734',
                              'doc_count': 67361}, {
                              'key': 'https://www.correiodopovo.com.br/not%C3%ADcias/geral/duas-apostas-acertam-mega-sena-e-levam-r-94-6-milh%C3%B5es-cada-1.791574?amp=1',
                              'doc_count': 60939}], '10103': [{
                'key': 'https://jb.com.br/pais/2019/08/1014911-mpf-pede-acao-urgente-da-policia-federal-para-evitar-ataque-de-pistoleiros-aos-indigenas-xikrin-em-altamira--pa.html',
                'doc_count': 35},
                {'key': 'https://jb.com.br/busca/', 'doc_count': 6}, {
                    'key': 'https://jb.com.br/bem_viver/saude/2020/03/1022740-cuba-anuncia-que-produz-vacina-contra-o-coronavirus-que-esta-sendo-usado-na-china-e-ja-curou-1-500-pessoas.html',
                    'doc_count': 4},
                {'key': 'https://jb.com.br/index.php', 'doc_count': 4},
                {'key': 'https://jb.com.br/bem_viver', 'doc_count': 3}],
                '10104': [{'key': 'https://frasesparawhats.com.br/status-para-whatsapp', 'doc_count': 1}],
                '10105': [{'key': 'https://www.nsctotal.com.br/home', 'doc_count': 153947},
                          {'key': 'https://www.nsctotal.com.br/dc', 'doc_count': 47599},
                          {'key': 'https://www.nsctotal.com.br/an', 'doc_count': 25220}, {
                              'key': 'https://www.nsctotal.com.br/noticias/quem-era-o-trabalhador-morto-em-acidente-com-elevador-em-balneario-camboriu',
                              'doc_count': 23377}, {
                              'key': 'https://www.nsctotal.com.br/noticias/entenda-os-motivos-da-guerra-entre-russia-e-ucrania',
                              'doc_count': 19466}], '10106': [
                {'key': 'https://www.daninoce.com.br/receitas/brigadeirao-supercremoso-e-facil/', 'doc_count': 16908}, {
                    'key': 'https://www.daninoce.com.br/receitas/bolo-gelado-com-recheio-de-leite-ninho-e-supermolhadinho/',
                    'doc_count': 9927},
                {'key': 'https://www.daninoce.com.br/ideias/como-limpar-e-energizar-os-cristais/', 'doc_count': 9202},
                {'key': 'https://www.daninoce.com.br/receitas/pudim-de-leite-ninho/', 'doc_count': 7381}, {
                    'key': 'https://www.daninoce.com.br/receitas/pastel-de-nata-ou-pastel-de-belem-receita-familiar-portuguesa/',
                    'doc_count': 7184}], '10108': [{
                'key': 'https://cadaminuto.com.br/noticia/307660/2017/08/01/as-raizes-da-inseguranca-publica-brasileira-e-a-licao-de-joacaba',
                'doc_count': 1}, {
                'key': 'https://cadaminuto.com.br/noticia/320909/2018/05/18/o-ataque-no-texas-todos-viram-mas-e-o-ataque-impedido-em-illinois-por-alguem-armado',
                'doc_count': 1}, {
                'key': 'https://cadaminuto.com.br/noticia/320993/2018/05/21/a-inglaterra-e-pacifica-por-conta-do-desarmamento-nem-uma-coisa-nem-outra',
                'doc_count': 1}], '10111': [{
                'key': 'https://diaonline.ig.com.br/2022/01/05/programa-maes-de-goias-confira-a-lista-de-beneficiarias/?utm_source=Dinake+Nubia&utm_campaign=diaonline-author',
                'doc_count': 8303}, {
                'key': 'https://diaonline.ig.com.br/cameras-ao-vivo/',
                'doc_count': 3555}, {
                'key': 'https://diaonline.ig.com.br/2022/01/05/programa-maes-de-goias-confira-a-lista-de-beneficiarias/',
                'doc_count': 2853}, {
                'key': 'https://diaonline.ig.com.br/2019/05/31/clubes-em-brasilia-melhores-opcoes-para-voce-se-divertir/?utm_source=Isabela+Gon%C3%A7alves&utm_campaign=diaonline-author',
                'doc_count': 1303}, {
                'key': 'https://diaonline.ig.com.br/2020/03/20/dicionario-goiano-conheca-algumas-de-nossas-girias-e-expressoes/?utm_source=Isabela+Gon%C3%A7alves&utm_campaign=diaonline-author',
                'doc_count': 1247}], '10113': [{
                'key': 'https://jornaldotocantins.com.br/editorias/esporte/atacante-indígena-aru-ex-palmas-morre-em-acidente-de-carro-1.1492767',
                'doc_count': 1},
                {
                    'key': 'https://jornaldotocantins.com.br/editorias/esporte/dupla-do-paraná-conquista-1º-lugar-no-circuito-bb-sub-19-1.907936',
                    'doc_count': 1},
                {
                    'key': 'https://jornaldotocantins.com.br/editorias/esporte/eliésio-vence-corrida-sesi-de-rua-do-trabalhador-1.841192',
                    'doc_count': 1},
                {
                    'key': 'https://jornaldotocantins.com.br/editorias/esporte/governo-anuncia-reformas-de-r-1-8-mi-em-complexos-esportivos-de-araguaína-1.1542036',
                    'doc_count': 1}],
                '10117': [{
                    'key': 'https://estrelando.com.br/celebridades/nota/2019/11/30/will-smith-compartilha-video-hilario-de-peru-atravessando-a-rua-no-dia-de-acao-de-gracas-assista-243927/foto-1',
                    'doc_count': 2}, {
                    'key': 'https://estrelando.com.br/foto/2015/03/09/confira-os-famosos-que-ja-ganharam-estatuas-de-si-mesmos-133916/foto-1',
                    'doc_count': 2}, {
                    'key': 'https://estrelando.com.br/foto/2014/12/01/os-diretores-que-ja-fizeram-pontas-em-suas-producoes-183552/foto-1',
                    'doc_count': 1}, {
                    'key': 'https://estrelando.com.br/foto/2019/07/10/como-nao-amar-veja-os-momentos-mais-fofos-da-familia-beckham-203471/foto-1',
                    'doc_count': 1}, {
                    'key': 'https://estrelando.com.br/foto/2019/07/10/veja-os-famosos-que-tambem-amam-pizza-206393/foto-1',
                    'doc_count': 1}],
                '10118': [{'key': 'https://bancodeseries.com.br/index.php?action=mygrade', 'doc_count': 37678},
                          {'key': 'https://bancodeseries.com.br/index.php', 'doc_count': 37149},
                          {'key': 'https://bancodeseries.com.br/index.php?action=se&serieid=22428&episode=1',
                           'doc_count': 13884},
                          {'key': 'https://www.bancodeseries.com.br/index.php', 'doc_count': 6662},
                          {'key': 'https://bancodeseries.com.br/index.php?action=correio&ajax=1&showthread=1000571053',
                           'doc_count': 4899}], '10120': [{
                'key': 'https://portalovertube.com/noticias-da-tv/veja-a-grade-de-programacao-da-globo-de-05-a-11-de-marco-de-2022/',
                'doc_count': 128}, {
                'key': 'https://portalovertube.com/bbb-22/resultado-de-enquete-uol-bbb-2022-mostra-que-participante-sai-com-59/',
                'doc_count': 124}, {
                'key': 'https://portalovertube.com/noticias-da-tv/quem-saiu-do-the-masked-singer-brasil-saiba-quem-foi-o-setimo-desmascarado-13-03-2022/',
                'doc_count': 112}, {
                'key': 'https://portalovertube.com/noticias-da-tv/veja-a-grade-de-programacao-da-globo-de-12-a-18-de-marco-de-2022/',
                'doc_count': 111}, {
                'key': 'https://portalovertube.com/bbb-22/votacao-gshow-com-saiba-como-votar-para-eliminar-jessilane-arthur-aguiar-ou-jade-picon-no-bbb-2022/',
                'doc_count': 85}], '10123': [
                {'key': 'https://www.diariooficialdf.com.br/ranking-dos-melhores-cursos-online-para-concursos/',
                 'doc_count': 5145},
                {'key': 'https://www.diariooficialdf.com.br/concursos-para-tecnico-em-enfermagem-para-passar-rapido/',
                 'doc_count': 1317},
                {'key': 'https://www.diariooficialdf.com.br/qual-melhor-gran-cursos-ou-estrategia-concursos/',
                 'doc_count': 1141},
                {'key': 'https://www.diariooficialdf.com.br/concurso-para-enfermeiro-como-se-preparar-corretamente/',
                 'doc_count': 381}, {
                    'key': 'https://www.diariooficialdf.com.br/6-melhores-concursos-para-nivel-medio-que-voce-precisa-conhecer/',
                    'doc_count': 344}]}

    def get_document(self):
        year = str(datetime.now().year)
        month = datetime.now().month
        month = str(month).zfill(2)
        query = self.get_query()
        after_key = None
        urls = {}
        account_id = os.getenv('ACCOUNT_ID') or None

        if  account_id is None:
            while True:
                if after_key is not None:
                    query['aggs']['account']['composite']['after'] = {'accountId': after_key}

                response = self.es.search(index='console-' + year + '.' + month, body=query, size=self.max_documents)
                for buckets in response['aggregations']['account']['buckets']:
                    urls_array = []
                    account_id = buckets['key']['accountId']
                    for hostname in buckets['hostname']['buckets']:
                        url_hostname = hostname['key']
                        for path_name in hostname['pathname']['buckets']:
                            url = 'https://' + url_hostname + path_name['key']
                            urls_array.append(url)
                    urls[account_id] = urls_array
                if 'after_key' in response['aggregations']['account']:
                    after_key = response['aggregations']['account']['after_key']['accountId']
                else:
                    break
        else:
            query['query']['bool']['filter'].append({'term': {'accountId': account_id}})
            response = self.es.search(index='console-' + year + '.' + month, body=query, size=self.max_documents)
            for buckets in response['aggregations']['account']['buckets']:
                urls_array = []
                account_id = buckets['key']['accountId']
                for hostname in buckets['hostname']['buckets']:
                    url_hostname = hostname['key']
                    for path_name in hostname['pathname']['buckets']:
                        url = 'https://' + url_hostname + path_name['key']
                        urls_array.append(url)
                urls[account_id] = urls_array

        return urls

    def get_query(self):
        date = datetime.now()
        date = date.replace(microsecond=00, second=59, minute=59, hour=23)
        date = date.isoformat()
        date = date + '-03:00'

        date_less_three_days = datetime.now() - timedelta(days=3)
        date_less_three_days = date_less_three_days.replace(microsecond=00, second=00, minute=00, hour=00)
        date_less_three_days = date_less_three_days.isoformat()
        date_less_three_days = date_less_three_days + '-03:00'

        query = {
            "track_total_hits": False,
            "query": {
                "bool": {
                    "filter": [
                        {
                            "range": {
                                "date": {
                                    "gte": date_less_three_days,
                                    "lte": date,
                                }
                            }
                        },
                        {
                            "term": {
                                "action": {
                                    "value": "authorized"
                                }
                            }
                        }
                    ],
                    "must_not": [
                        {
                            "term": {
                                "pageUrl.pathname": {
                                    "value": "/"
                                }
                            }
                        }
                    ]
                }
            },
            "aggs": {
                "account": {
                    "composite": {
                        "size": self.max_documents,
                        "sources": [
                            {
                                "accountId": {
                                    "terms": {
                                        "field": "accountId"
                                    }
                                }
                            }
                        ]
                    },
                    "aggs": {
                        "hostname": {
                            "terms": {
                                "field": "pageUrl.hostname",
                                "size": 1
                            },
                            "aggs": {
                                "pathname": {
                                    "terms": {
                                        "field": "pageUrl.pathname",
                                        "size": 5
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }

        return query