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



# para cada session, verificar quais os dados vinculados e shoutIDs vinculados

nicks=um.keys()
count=0
for nick in nicks:
    checkers=[i for i in um[nick] if i[-1]]
    count+=len(checkers)
