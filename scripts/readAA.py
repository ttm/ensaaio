#!/usr/bin/python                                                      
#-*- coding: utf-8 -*-                                                 
import rdflib as r
from SPARQLWrapper import SPARQLWrapper, JSON
import sys, time, cPickle as pickle
T=time.time()
#g=r.Graph()
#g.parse("/disco/aa01/rdf/aaStoreMongo.rdf")

sparql3 = SPARQLWrapper("http://localhost:82/aaNEW/query")

q1="SELECT ?s ?p ?o WHERE {?s ?p ?o}"
PREFIX="""PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX ops: <http://purl.org/socialparticipation/ops#>
PREFIX opa: <http://purl.org/socialparticipation/opa#>
PREFIX foaf: <http://xmlns.com/foaf/0.1/>
PREFIX aa: <http://purl.org/socialparticipation/aa/>
PREFIX dc: <http://purl.org/dc/terms/>"""

PREFIX2="PREFIX aa: <http://purl.org/socialparticipation/aa/>"

#sparql3.setQuery(PREFIX+q1)
#q2="SELECT ?s ?o (group_concat(?s2) as ?ss) WHERE {?s a aa:User . ?s aa:nick ?o . ?s2 aa:user ?s . OPTIONAL { ?s2 a aa:Shout } } GROUP BY ?s ?o"
q2="""
SELECT ?shID ?seID
       ?nick ?msg ?created ?valid
       ?screated ?smsg ?sscreencast ?sscore ?cnick 
       WHERE {
           ?shID a aa:Shout . 
           OPTIONAL { ?shID aa:user ?s . 
                     ?s aa:nick ?nick 
           } .
           OPTIONAL { ?shID aa:shoutMessage ?msg } . 
           OPTIONAL { ?shID aa:created ?created } .
           OPTIONAL { ?shID aa:valid ?valid } .
           OPTIONAL { ?shID aa:session ?seID .
                     OPTIONAL { ?seID aa:created ?screated } .
                     OPTIONAL { ?seID aa:checkMessage ?smsg } .
                     OPTIONAL { ?seID aa:screencast ?sscreencast } .
                     OPTIONAL { ?seID aa:score ?sscore } .
                     OPTIONAL { ?seID aa:checker ?cid .
                                ?cid aa:nick ?cnick } .
           } .
       }
"""
#q2="SELECT ?nick ?msg ?created ?sessionID ?checker ?screated ?smsg ?score ?screencast WHERE {?s a aa:User . ?s aa:nick ?nick .  OPTIONAL { ?sht aa:user ?s . ?sht a aa:Shout . ?sht aa:shoutMessage ?msg . ?sht aa:created ?created . ?sht aa:valid ?valid. } OPTIONAL { ?sht aa:session ?sessionID . ?sessionID aa:checker ?user2 . ?user2 aa:nick ?checker . ?sessionID aa:created ?screated . ?sessionID aa:checkMessage ?smsg . ?sessionID aa:score ?score . ?sessionID aa:screenscast ?screenscast } }"

#sparql3.setQuery(PREFIX2+q2)
#sparql3.setReturnFormat(JSON)
#
#results3 = sparql3.query().convert()
#
#print time.time()-T
#
#
#res=results3["results"]["bindings"]
#
#f=open("./pickle/query2.pickle", 'wb')
#pickle.dump(res,f)
#f.close()
#####################################################
#f=open("./pickle/query2.pickle", 'rb')
#res=pickle.load(f)
#print(time.time()-T)
# 
#
##users=[i["s"]["value"] for i in res]
#nicks=[i["nick"]["value"] for i in res]
#
#user_msgs=um={}
#sessions=ss={}
#def getVal(tcoisa="coisa"):
#    if tcoisa in sht.keys():
#        tval=sht[tcoisa]["value"]
#    else:
#        tval=""
#    return tval
#G=getVal
#
#for sht in res:
#    shID=sht["shID"]["value"]
#    if "msg" in sht.keys():
#        msg=sht["msg"]["value"]
#    else:
#        msg=""
#    nick=sht["nick"]["value"]
#    if "msg" in sht.keys():
#        msg=sht["msg"]["value"]
#    else:
#        msg=""
#    if "created" in sht.keys():
#        created=sht["created"]["value"]
#    else:
#        created=""
#    try:
#        valid=sht["valid"]["value"]
#    except:
#        valid=False
#
#    if G("msg"):
#        if G("nick") not in um.keys():
#            um[G("nick")]=[] # lista de tuplas (msg, data)
#        if G("msg") != u"TIMESLOT PERDIDO":
#            um[G("nick")]+=[(G("msg"),G("created"),G("valid"),G("shID"))] # lista de tuplas (msg, data)
#            if G("seID"):
#                if G("seID") not in ss.keys():
#                    ss[G("seID")]=[]
#                ss[G("seID")]+=[(G("screated"), G("smsg"), G("screenscast"), G("sscore"),G("cnick"),G("shID"))]
#    #print("%s\n%s\n%s\n%s\n\n"%(nick, msg, created, valid))
#    #time.sleep(0.3)
#
#print(time.time()-T)
#
#f=open("./pickle/dicts.pickle", 'wb')
#pickle.dump((um,ss),f)
#f.close()
###############################
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
#AA=[('o0o0o','hybrid','greenkobold','blober','escritor','hercules'),
#    ('humannoise','ims0iniA'),
#    ('automata','aut0mata'),
#    ('v1z',),
#    ('adr',),
#    ('angelina',),
#    ('angelina',),
#   ]
#U=ums
#AA=[
#    (1,3,6,19,24,32,33,60,61,86,92,96,97,103,114,127,129,145,146,160,172), # hybrid
#    (0,5,9,30,37,49,55,80,89,112,115,124,157,169,175), # humannoise
#    (7,76,118,128,134,136), # angelina
#    (4,13,16,45,93,178), # presto
#    (10,47,87,99,142,153,173), # cravelho
#    (21,111,117,119,154,159), # v1z
#    (56,71,94,148,156), #audiohack
#    (20,53,85,120), # Pjr (plinio)
#    (48,77,108,125), # automata_
#    (31,35,113), # anonymous, Guest
#    (27,64), # ggdo
#    (43,65), # witness
#    (74,91), #sescBelenzinho
#    (41,105), # tonussi
#    (101,155), #gabithume
#    (158,176), #liviaascava
#    (54,162), #mancha
#    (51,107), #glerm
#    (58,130), #hiato(br1)
#    (2,150), # adr
#    (8,131), # yupana bot
#    (122,), #DaneoShiga
#    (78,), #jow
#    (69,), #gonzo
#    (11,), # cadinot
#    (12,), # bzum
#    (14,), # PedroBarata
#    (57,), #flecha
#    (15,), # joepie91
#    (17,), # dj_brip
#    (18,), # hick (nivaldinho)
#    (22,), # doceafagonanuca
#    (23,), # paulordbm
#    (25,), # Aderbal
#    (26,), # slucky
#    (28,), # capo
#    (29,), # teste
#    (34,), # libotte
#    (36,), # JPM
#    (38,), # Manjaro
#    (39,), # gilsonbeck 
#    (40,), # monod
#    (42,), # 'id found as shout creator but not as id for user with nick'
#    (44,), # crash_daemons
#    (46,), # SrKaioh
#    (50,), #uriguilherme 
#    (52,), #felipe machado
#    (59,), #Rafaman
#    (62,), #quirinobahr
#    (63,), #tibiriba
#    (66,), #leib999
#    (67,), #bjonnh
#    (68,), #kbsa
#    (70,), #caioc
#    (72,), #ricardo brazileiro
#    (73,), #lari (larissa arruda?)
#    (75,), #mquasar
#    (79,), #atmt
#    (81,), #queen
#    (82,), #aurium
#    (83,), #malacabado
#    (84,), #leosimoes
#    (88,), #eah
#    (90,), #cibeleborg
#    (95,), #kraven
#    (98,), #rebecchi
#    (100,), #lacRavoLenia
#    (102,), #Mateus
#    (104,), #coletivo
#    (106,), #pliskin
#    (109,), #hmbr
#    (110,), #rck
#    (116,), #sephioff8
#    (121,), #fdeSanca
#    (123,), #fran_paizao
#    (126,), #ongueiro
#    (132,), #yaso
#    (133,), #casanova
#    (135,), #gama
#    (137,), #tarrafa
#    (138,), #rfabbri bot
#    (139,), #celularkobold
#    (140,), #ananse
#    (141,), #karmiac
#    (143,), #fefo
#    (144,), #gosma
#    (147,), #lap01
#    (149,), #paloma
#    (151,), #barraponto
#    (152,), #thibo
#    (161,), #orlando o2
#    (163,), #lmatos
#    (164,), #isaura / fer
#    (165,), #mari
#    (166,), #lalenia
#    (167,), #daniel teia
#    (168,), #lucas
#    (170,), #identi.ca
#    (171,), #b0ttt
#    (174,), #warlock
#    (177,), #aleij
#    (179,), #ispMarin
#]

#AA=[tuple([U[ii] for ii in i]) for i in AA]
#f=open("./pickle/arbitraryAlias.pickle", 'wb')
#pickle.dump(AA,f)
#f.close()
###############################


for aa in AA:
    for nick in aa:
        print('%s & %i'%(nick, len(um[nick]),))

# tabela com numero total de mensagens por nick
# e agrupado por alias
#AA=[(U[0],U[5],U[9]), # humannoise
#    (U[1],U[3],U[6],U[19]), # hybrid
#    (U[2],), # adr
#    (U[4],U[13],U[16]), # presto
#    (U[7],), # angelina
#    (U[8],), # yupana bot
#    (U[10],), # cravelho
#    (U[11],), # cadinot
#    (U[12],), # bzum
#    (U[14],), # PedroBarata
#    (U[15],), # joepie91
#    (U[17],), # dj_brip
#    (U[18],), # hick (nivaldinho)
#]

nicks=um.keys()
count=0
for nick in nicks:
    checkers=[i for i in um[nick] if i[-1]]
    count+=len(checkers)
