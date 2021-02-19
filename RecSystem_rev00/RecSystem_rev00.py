# -*- coding: utf-8 -*-
"""
RECSYSTEM v1.0
"""

import nltk

import time


"""BASE DE DADOS COM TEXTO"""

base = [('estou sentindo raiva de voce ','raiva'),
	('nao sei o que fazer','tristeza'),
	('estou desapontado com tudo','tristeza'),
	('a vida nao vale a pena','tristeza'),
	('estou sentindo dores','tristeza'),
	('voce me enlouquece ','raiva'),
	('estou esperando a muito tempo','raiva'),
	('nao quero esperar mais','raiva'),
	('esqueca de mim','raiva'),
	('vou destruir voce','raiva'),
	('quero quebrar sua cara','raiva'),
	('voce e irritante','raiva'),
	('estou me sentindo perturbado','raiva'),
	('vou explodir de odio','raiva'),
	('sinto que vou cair','medo'),
	('viver e tudo de bom','alegria'),
	('estou me sentindo otimo','alegria'),
	('estou me sentindo leve','alegria'),
	('acho que estou apaixonado','afeto'),
	('voce mexe comigo','afeto'),
	('meu coracao e seu','afeto'),
	('quero me casar com voce','afeto'),
	('voce quer namorar comigo','afeto'),
	('estou transbordando de amor','afeto'),
	('e melhor viver bem','alegria'),
	('a vida tem altos e baixos','medo'),
	('estou muito satisfeito ','alegria'),
	('nao conheco o necessario','medo'),
	('estou esperando resposta','medo'),
	('a resposta nao foi satisfatoria','medo'),
	('existem coisas que nao conheco','medo'),
	('quero bem a todos','afeto'),
	('espero que todos sejam felizes','afeto'),
	('a felicidade pode ser universal','afeto'),
	('a felicidade e um dom','alegria'),
	('a tristeza e ruim','tristeza'),
	('a alegria e boa demais','alegria'),
	('o afeto e um bom sentimento','afeto'),
	('o medo nos afasta a todos','medo'),
	('a raiva destroi tudo que toca','raiva')]
                
"""REMOÇÃO DAS STOPWORDS"""

lista_padrao_stopwords = nltk.corpus.stopwords.words('portuguese')

def aplicaStemmerStopwords(texto):
    stemmer = nltk.stem.RSLPStemmer()
    frasesStemming = []
    for (palavras, emocao) in texto:
        comStemming = [str(stemmer.stem(p)) for p in palavras.split() if p not in nltk.corpus.stopwords.words('portuguese')]
        frasesStemming.append((comStemming, emocao))
    return frasesStemming

base_1 = aplicaStemmerStopwords(base)

def buscapalavras(frases):
    todaspalavras = []
    for (palavras, emocao) in frases:
        todaspalavras.extend(palavras)
    return todaspalavras
    
palavras = buscapalavras(base_1)

def buscafrequencia(palavras):
    palavras = nltk.FreqDist(palavras)
    return palavras

frequencia = buscafrequencia(palavras)

def buscapalavrasunicas(frequencia):
    freq = frequencia.keys()
    return freq
    
palavras_unicas = buscapalavrasunicas(frequencia)

def extratorpalavras(documento):
    doc = set(documento)
    caracteristicas = {}
    for palavras in palavras_unicas:
        caracteristicas['%s' % palavras] = (palavras in doc)
    return caracteristicas

basecompletatreinamento = nltk.classify.apply_features(extratorpalavras, base_1)
classificador = nltk.NaiveBayesClassifier.train(basecompletatreinamento)



while True:
    entrada = raw_input("Digite o texto: ")
    testestemming = []
    stemmer = nltk.stem.RSLPStemmer()
    for (palavrastreinamento) in entrada.split():
        comstem = [p for p in palavrastreinamento.split()]
        testestemming.append(str(stemmer.stem(comstem[0])))
    novo = extratorpalavras(testestemming)
    distribuicao = classificador.prob_classify(novo)
    for classe in distribuicao.samples():
        print("%s: %f" % (classe, distribuicao.prob(classe)))
    entrada = ""
    print "Aguardando entrada"
    time.sleep(0.5)

        