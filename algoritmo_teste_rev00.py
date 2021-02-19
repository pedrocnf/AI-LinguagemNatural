# -*- coding: utf-8 -*-
"""ALGORITMO TESTE DE MINERAÇÃO DE EMOÇÕES EM TEXTOS USANDO NLTK
"""

import nltk

"""BASE DE DADOS COM TEXTO"""
base = [('eu sou admirada por muitos','alegria'),
        ('me sinto completamente amado','alegria'),
        ('amar e maravilhoso','alegria'),
        ('estou me sentindo muito animado novamente','alegria'),
        ('eu estou muito bem hoje','alegria'),
        ('que belo dia para dirigir um carro novo','alegria'),
        ('o dia está muito bonito','alegria'),
        ('estou contente com o resultado do teste que fiz no dia de ontem','alegria'),
        ('o amor e lindo','alegria'),
        ('nossa amizade e amor vai durar para sempre', 'alegria'),
        ('estou amedrontado', 'medo'),
        ('ele esta me ameacando a dias', 'medo'),
        ('isso me deixa apavorada', 'medo'),
        ('este lugar e apavorante', 'medo'),
        ('se perdermos outro jogo seremos eliminados e isso me deixa com pavor', 'medo'),
        ('tome cuidado com o lobisomem', 'medo'),
        ('se eles descobrirem estamos encrencados', 'medo'),
        ('estou tremendo de medo', 'medo'),
        ('eu tenho muito medo dele', 'medo'),
        ('estou com medo do resultado dos meus testes', 'medo'),
        ('eles querem me bater', 'medo')]
        
"""REMOÇÃO DAS STOPWORDS"""

lista_padrao_stopwords = nltk.corpus.stopwords.words('portuguese')

"""
def removerStopwords(texto,lista_padrao_stopwords):
    frases = []
    for (palavras, emocao) in texto:
        semstop = [p for p in palavras.split() if p not in lista_padrao_stopwords]
        frases.append((semstop, emocao))
    return frases
"""
"""EXTRAÇÃO DOS RADICAIS COM REMOÇÃO DE STOPWORDS"""

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

def resultado():
    entrada = raw_input("Digite o texto a avaliar: ")
    testestemming = []
    stemmer = nltk.stem.RSLPStemmer()
    for (palavrastreinamento) in entrada.split():
        comstem = [p for p in palavrastreinamento.split()]
        testestemming.append(str(stemmer.stem(comstem[0])))
    novo = extratorpalavras(testestemming)
    distribuicao = classificador.prob_classify(novo)
    for classe in distribuicao.samples():
        print("%s: %f" % (classe, distribuicao.prob(classe)))