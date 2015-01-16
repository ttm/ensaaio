#!/usr/bin/python                                                      
#-*- coding: utf-8 -*-                                                 
import rdflib as r
from SPARQLWrapper import SPARQLWrapper, JSON
import sys, time, cPickle as pickle
T=time.time()
##############################
f=open("./pickle/dicts.pickle", 'rb')
um,ss=pickle.load(f)
print(time.time()-T)
 
print(u"there are %i AA sessions \n\
to which are associated %i messages\n\
of all %i AA registered messages"%(len(ss),
                    sum([len(ss[i]) for i in ss.keys()]),
                    sum([len(um[i]) for i in um.keys()])))
sss=ss.keys()
ums=um.keys()

f=open("./pickle/arbitraryAlias.pickle", 'rb')
AA=pickle.load(f)
print(time.time()-T)
 

# remover "shout " do comeco das msgs
# remover "alert " do comeco das msgs
# remover "notify"

# fazer histograma de atividade no tempo

# ver de quando a quando temos shouts e sessions validadas
# ateh quando tem screencast registrado

# fazer medidas com a resolucao dos alias arbitrarios e sem, e ver
# se os alias nao sao tambem uma forma de deixar mais natural o processo
# apontar tb q n se sabe dos alias dos perifericos, pois sao de fora
# o que pode tb causar distorcoes

# agrupar usuarios em comum
# Alias Abitrarios sao resolvidos com o conhecimento
# dos autores e apresentacao para a comunidade

for aa in AA:
    for nick in aa:
        print('%s & %i'%(nick, len(um[nick]),))

nicks=um.keys()
count=0
for nick in nicks:
    checkers=[i for i in um[nick] if i[-1]]
    count+=len(checkers)
