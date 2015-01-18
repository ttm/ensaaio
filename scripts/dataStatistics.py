#!/usr/bin/python                                                      
#-*- coding: utf-8 -*-                                                 
import rdflib as r
from SPARQLWrapper import SPARQLWrapper, JSON
import sys, time, cPickle as pickle, numpy as n, datetime
import pylab as p
import matplotlib.pyplot as pp
T=time.time()
##############################
f=open("./pickle/dicts.pickle", 'rb')
um,ss,shd=pickle.load(f)
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
# remover "push"
# remover "start"
# remover "stop"

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

#for aa in AA:
#    total=0
#    for nick in aa:
#        print('%s & %i'%(nick, len(um[nick]),))
#        total+=len(um[nick])
#    print total
#
#nicks=um.keys()
#count=0
#for nick in nicks:
#    checkers=[i for i in um[nick] if i[-1]]
#    count+=len(checkers)
#
f=open("./pickle/um_ss_.pickle", 'rb')
um_,ss_,shd_,shLL_=pickle.load(f)
print(time.time()-T)
### users in sessions
# pega cada session, a ID do shout, vai no dict, pega o user.
def S(nick):
    for aa in AA:
        if nick in aa:
            return aa[0]
    return nick
users=[]
#for seID in ss_.keys():
#    if len(ss_[seID])>1:
#        shouts=ss_[seID]
#        for shout in shouts:
#            shID=shout[-1]
#            users+=[S(shd_[shID][1])]
#nusers=len(set(users))
## ve o len(set(users))
#smsgs=[j for i in ss_.keys() for j in ss_[i]]
#smsgs_=[j[0] for j in smsgs if j[0]]
#smsgs_.sort()
#
#sessions=[
#("number of sessions",len(ss_)),
#("number of shouts in sessions",sum([len(ss_[i]) for i in ss_.keys()])),
#("number sessions with more than 1 shout",sum([len(ss_[i])>1 for i in ss_.keys()])),
#("number of shouts in sessions with more than 1 shout",sum([len(ss_[i]) for i in ss_.keys() if len(ss_[i])>1])),
#("number of users in sessions",nusers),
#("number of checkers in sessions",len(set([S(ss_[i][0][-2]) for i in ss_.keys() if len(ss_[i])>1]))),
#("number of screencasts in sessions",len(set([i[2] for i in smsgs]))),
#("number of scored sessions",sum([(ss_[i][0][3] not in ("","0")) for i in ss_.keys() if (len(ss_[i])>1)])),
#("average session score",n.mean([int(ss_[i][0][3]) for i in ss_.keys() if (ss_[i][0][3] not in ("","0")) and (len(ss_[i])>1)])),
#("standard deviation of score",n.std([int(ss_[i][0][3]) for i in ss_.keys() if (ss_[i][0][3] not in ("","0")) and (len(ss_[i])>1)])),
#("average number of shouts",n.mean([len(ss_[i]) for i in ss_.keys() if len(ss_[i])>1])),
#("standard deviation of number of shouts",n.std([len(ss_[i]) for i in ss_.keys() if len(ss_[i])>1])),
##("first session from",min(smsgs_)),
#("first session from",u'2011-07-06T03:23:05'), # smsgs_[211]
##("last session from",max(smsgs_)),
#("last session from",u'2014-04-01T09:11:36'),
#]
#i=0
#for c in sessions:
#    if i<8:
#        print("%s & %i \\\\ \\hline"%(c[0],c[1]))
#    elif i<12:
#        print("%s & %.2f \\\\ \\hline"%(c[0],c[1]))
#    else:
#        print("%s & %s \\\\ \\hline"%(c[0],c[1]))
#    i+=1
#
# t = datetime.datetime.strptime(date, '%Y-%m-%dT%H:%M:%S')
shs=[list(shd_[i])+[i] for i in shd_.keys()]
shs_=[i[2] for i in shs]
shs_.sort()
shsLL_=[i[0] for i in shLL_]
shsLL_.sort()

shs__=[datetime.datetime.strptime((i,i[:i.find(".")])["." in i],'%Y-%m-%dT%H:%M:%S') for i in shs_[224:]]
miny=shs__[0].year
maxy=shs__[-1].year
vals=[]
for y in xrange(miny,maxy+1):
    SH=[i for i in shs__ if i.year==y]
    for m in xrange(1,12+1):
        mc=sum([i.month==m for i in SH])
        if m==1:
            vals+=[(u"%i-%i"%(y,m),mc)]
        else:
            vals+=[(u"%i"%(m,),mc)]
vals_=vals[6:-11]
#fig = p.figure()
#ax = fig.add_subplot(111)

### IRC
shsLL__=[datetime.datetime.strptime((i,i[:i.find(".")])["." in i],'%Y-%m-%dT%H:%M:%S') for i in shsLL_]
miny=shsLL__[0].year
maxy=shsLL__[-1].year
vals2=[]
for y in xrange(miny,maxy+1):
    SH=[i for i in shsLL__ if i.year==y]
    for m in xrange(1,12+1):
        mc=sum([i.month==m for i in SH])
        if m==1:
            vals2+=[(u"%i-%i"%(y,m),mc)]
        else:
            vals2+=[(u"%i"%(m,),mc)]
#vals2_=vals2[6:-11]
vals2_=vals2[6:-11]
width=0.6
p2 = pp.bar(12+n.arange(len(vals2_)), [i[0][1]+i[1][1] for i in zip(vals2_,vals_[12:])],   width,color="red")
p1 = pp.bar(range(len(vals_)), [i[1] for i in vals_],   width)



pp.xticks([i+width/2 for i in xrange(len(vals_))],
          [i[0] for i in vals_] , rotation=70)
pp.yticks(n.arange(0,5500,500))
pp.xlim(-1,len(vals_))
pp.ylim(0,max([i[1] for i in vals_])+200)
pp.ylabel(u'messages count')
pp.legend((p1[0], p2[0]), ('MySQL and MongoDB', 'IRC logs'))
pp.title("AA messages registered each month")
pp.show()

msgs_mes=[i[0][1]+i[1][1] for i in zip(vals2_,vals_[12:])]
