from nltk import Text
from corpus_generator import corpus
from item2 import media, LDS
from item3 import hapaxes, collocations, maisFrequentes

sites_governamentais = corpus.words('sites_governametais.txt')
comentario_de_produtos = corpus.words('comentario_de_produtos.txt')
resumos_artigos = corpus.words('resumos_artigos.txt')
portais_de_noticias = corpus.words('portais_de_noticias.txt')

sites_governamentais = Text(sites_governamentais)
comentario_de_produtos = Text(comentario_de_produtos)
resumos_artigos = Text(resumos_artigos)
portais_de_noticias = Text(portais_de_noticias)

categorias = [sites_governamentais, comentario_de_produtos, resumos_artigos, portais_de_noticias]

for cat in categorias:
    print("----------------Resultados para a categoria de", cat.name, "---------------")
    print("média de caracteres por palavra: ", media(cat))
    print("LDS: ", LDS(cat))
    print("Hapaxes: ", hapaxes(cat))
    print("Collocations: ", collocations(cat))
    print("10 palavras mais frequentes: ", maisFrequentes(cat, 10))

