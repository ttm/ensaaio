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

#sparql3.setQuery(PREFIX+q1)
#q2="SELECT ?s ?o (group_concat(?s2) as ?ss) WHERE {?s a aa:User . ?s aa:nick ?o . ?s2 aa:user ?s . OPTIONAL { ?s2 a aa:Shout } } GROUP BY ?s ?o"
q2="""
SELECT ?nick ?msg ?created ?valid WHERE {
           ?sht a aa:Shout . 
           OPTIONAL { ?sht aa:user ?s . 
                     OPTIONAL {?s aa:nick ?nick }.
           } .
           OPTIONAL { ?sht aa:shoutMessage ?msg } . 
           OPTIONAL { ?sht aa:created ?created } .
           OPTIONAL { ?sht aa:valid ?valid } .
           OPTIONAL { ?sht aa:session ?sessionID .
                     OPTIONAL { ?sessionID aa:checkMessage ?smsg } .
                     OPTIONAL { ?sessionID aa:score ?sscore } .
                     OPTIONAL { ?sessionID aa:created ?screated } .
                     OPTIONAL { ?sessionID aa:screencast ?sscreencast } .
                     OPTIONAL { ?sessionID aa:checker ?cid .
                                ?cid aa:nick ?cnick } .
                     OPTIONAL { ?sessionID aa:checker ?cid .
                                ?cid aa:nick ?cnick } .
           } .
}
"""
#q2="SELECT ?nick ?msg ?created ?sessionID ?checker ?screated ?smsg ?score ?screencast WHERE {?s a aa:User . ?s aa:nick ?nick .  OPTIONAL { ?sht aa:user ?s . ?sht a aa:Shout . ?sht aa:shoutMessage ?msg . ?sht aa:created ?created . ?sht aa:valid ?valid. } OPTIONAL { ?sht aa:session ?sessionID . ?sessionID aa:checker ?user2 . ?user2 aa:nick ?checker . ?sessionID aa:created ?screated . ?sessionID aa:checkMessage ?smsg . ?sessionID aa:score ?score . ?sessionID aa:screenscast ?screenscast } }"
sparql3.setQuery(PREFIX+q2)
sparql3.setReturnFormat(JSON)

results3 = sparql3.query().convert()

print time.time()-T


res=results3["results"]["bindings"]

f=open("./pickle/query2.pickle", 'wb')
pickle.dump(res,f)
f.close()
#f=open("./pickle/query2.pickle", 'rb')
#res=pickle.load(f)
#print(time.time()-T)
 

#users=[i["s"]["value"] for i in res]
nicks=[i["nick"]["value"] for i in res]

user_msgs=um={}
for sht in res:
    nick=sht["nick"]["value"]
    try:
        msg=sht["msg"]["value"]
    except:
        msg=""
    try:
        created=sht["created"]["value"]
    except:
        created=""
    try:
        valid=sht["valid"]["value"]
        print "TEM SIM"
    except:
        valid=False

    if msg:
        if nick not in um.keys():
            um[nick]=[] # lista de tuplas (msg, data)
        if msg != u"TIMESLOT PERDIDO":
            um[nick]+=[(msg,created,valid)] # lista de tuplas (msg, data)
    #print("%s\n%s\n%s\n%s\n\n"%(nick, msg, created, valid))
    #time.sleep(0.3)

print(time.time()-T)

# para cada session, verificar quais os dados vinculados e shoutIDs vinculados

nicks=um.keys()
count=0
for nick in nicks:
    checkers=[i for i in um[nick] if i[-1]]
    count+=len(checkers)
    

"""
    try:
        checker=sht["checker"]["value"]
    except:
        checker=""
    try:
        screated=sht["screated"]["value"]
    except:
        screated=""
    try:
        smsg=sht["smsg"]["value"]
    except:
        smsg=""
    try:
        score=sht["score"]["value"]
    except:
        score=""
    try:
        screencast=sht["screencast"]["value"]
    except:
        screencast=""
    try:
        sid=sht["sessionID"]["value"]
    except:
        sid=""
"""
