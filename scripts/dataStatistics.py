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
#width=0.6
#p2 = pp.bar(12+n.arange(len(vals2_)), [i[0][1]+i[1][1] for i in zip(vals2_,vals_[12:])],   width,color="red")
#p1 = pp.bar(range(len(vals_)), [i[1] for i in vals_],   width)
#
#
#
#pp.xticks([i+width/2 for i in xrange(len(vals_))],
#          [i[0] for i in vals_] , rotation=70)
#pp.yticks(n.arange(0,5500,500))
#pp.xlim(-1,len(vals_))
#pp.ylim(0,max([i[1] for i in vals_])+200)
#pp.ylabel(u'messages count')
#pp.legend((p1[0], p2[0]), ('MySQL and MongoDB', 'IRC logs'))
#pp.title("AA messages registered each month")
#pp.show()

msgs_mes=[i[0][1]+i[1][1] for i in zip(vals2_,vals_[12:])]

####### ATIVIDADE
# horario de todas as msgs
shT=shs_+shsLL_
shT.sort()
shT_=shT[224:15369]
shT__=[datetime.datetime.strptime((i,i[:i.find(".")])["." in i],'%Y-%m-%dT%H:%M:%S') for i in shT_]
# filtrar mensagens de 2012 p frente. Sem a $$
shT2_=shT[15369:]
shT2__=[datetime.datetime.strptime((i,i[:i.find(".")])["." in i],'%Y-%m-%dT%H:%M:%S') for i in shT2_]

def cDiff(vetor,bins_):
    h1=n.histogram(vetor,bins=bins_)[0]
    return max(h1)/float(min(h1))
# segundos do minuto
#s1=[i.second for i in shT__]
#ms1=n.mean(s1)
#ds1=n.std(s1)
#Ms1=cDiff(s1,n.arange(61))
#p.subplot(611)
#p.hist(s1,bins=n.arange(61),normed=1)
#p.title("activity in each second (a)")
#s2=[i.second for i in shT2__]
#ms2=n.mean(s2)
#ds2= n.std(s2)
#p.subplot(612)
#p.hist(s2,bins=n.arange(61),normed=1)
#p.title("activity in each second (b)")
#Ms2=cDiff(s2,n.arange(61))
## minutos da hora
#m1=[i.minute for i in shT__]
#mm1=n.mean(m1)
#dm1=n.std(m1)
#Mm1=cDiff(m1,n.arange(61))
#p.subplot(613)
#p.hist(m1,bins=n.arange(61),normed=1)
#p.title("activity in each minute (a)")
#m2=[i.minute for i in shT2__]
#mm2=n.mean(m2)
#dm2= n.std(m2)
#Mm2=cDiff(m2,n.arange(61))
#p.subplot(614)
#p.hist(m2,bins=n.arange(61),normed=1)
#p.title("activity in each minute (b)")
#
## distribuicao uniforme
#u1=n.random.random_integers(0,59,len(s1))
#mu1=n.mean(u1)
#du1= n.std(u1)
#Mu1= cDiff(u1,n.arange(61))
#p.subplot(615)
#p.hist(u1,bins=n.arange(61),normed=1)
#p.title("Uniform distribution simulation (a)")
#u2=n.random.random_integers(0,59,len(s2))
#mu2=n.mean(u2)
#du2= n.std(u2)
#Mu2= cDiff(u2,n.arange(61))
#p.subplot(616)
#p.hist(u2,bins=n.arange(61),normed=1)
#p.title("Uniform distribution simulation (b)")
#p.show()
#
## horas do dia
#h1=[i.hour for i in shT__]
#mh1=n.mean(h1)
#def GG(nn):
#    if abs(nn-mh1)>12:
#        return 24-abs(nn-mh1) 
#    else:
#        return abs(nn-mh1)
#dh1__=n.array([GG(i) for i in h1])
#dh1=((dh1__**2.)/len(dh1__))**0.5
#Mh1=cDiff(h1,n.arange(25))
#h2=[i.hour for i in shT2__]
#mh2=n.mean(h2)
#def GG(nn):
#    if abs(nn-mh2)>12:
#        return 24-abs(nn-mh2) 
#    else:
#        return abs(nn-mh2)
#dh2__=n.array([GG(i) for i in h2])
#dh2=((dh2__**2.)/len(dh2__))**0.5
#Mh2=cDiff(h2,n.arange(25))
#
#p.subplot(411)
#p.hist(h1,bins=n.arange(25),normed=1)
#p.title("activity in each hour (a)")
#Mh1=cDiff(h1,n.arange(25))
#p.subplot(412)
#p.hist(h2,bins=n.arange(25),normed=1)
#p.title("activity in each hour (b)")
#Mh2=cDiff(h2,n.arange(25))
## distribuicao uniforme
#u1=n.random.random_integers(0,23,len(h1))
#mu1=n.mean(u1)
#du1= n.std(u1)
#Mu1= cDiff(u1,n.arange(25))
#p.subplot(413)
#p.hist(u1,bins=n.arange(25),normed=1)
#p.title("Uniform distribution simulation (a)")
#u2=n.random.random_integers(0,23,len(h2))
#mu2=n.mean(u2)
#du2= n.std(u2)
#Mu2= cDiff(u2,n.arange(25))
#p.subplot(414)
#p.hist(u2,bins=n.arange(25),normed=1)
#p.title("Uniform distribution simulation (b)")
#p.show()

# dias da semana
w1=[i.weekday() for i in shT__]
mw1=n.mean(w1)
def GG(nn):
    if abs(nn-mw1)>3:
        return 7-abs(nn-mw1) 
    else:
        return abs(nn-mw1)
dw1__=n.array([GG(i) for i in w1])
dw1=((dw1__**2.)/len(dw1__))**0.5
Mw1=cDiff(w1,n.arange(8))
w2=[i.weekday() for i in shT2__]
mw2=n.mean(w2)
def GG(nn):
    if abs(nn-mw2)>12:
        return 24-abs(nn-mw2) 
    else:
        return abs(nn-mw2)
dw2__=n.array([GG(i) for i in w2])
dw2=((dw2__**2.)/len(dw2__))**0.5
Mw2=cDiff(w2,n.arange(8))

p.subplot(411)
p.hist(w1,bins=n.arange(8),normed=1)
p.title("activity in each weekday (a)")
Mw1=cDiff(w1,n.arange(8))
p.xticks([])
p.subplot(412)
p.hist(w2,bins=n.arange(8),normed=1)
p.title("activity in each weekday (b)")
Mw2=cDiff(w2,n.arange(8))
# distribuicao uniforme
u1=n.random.random_integers(0,6,len(w1))
mu1=n.mean(u1)
du1= n.std(u1)
Mu1= cDiff(u1,n.arange(8))
p.xticks([])
p.subplot(413)
p.hist(u1,bins=n.arange(8),normed=1)
p.title("Uniform distribution simulation (a)")
u2=n.random.random_integers(0,6,len(w2))
mu2=n.mean(u2)
du2= n.std(u2)
Mu2= cDiff(u2,n.arange(8))
p.xticks([])
p.subplot(414)
p.hist(u2,bins=n.arange(8),normed=1)
p.title("Uniform distribution simulation (b)")
p.xticks(n.arange(7)+0.5,["mon","tue","wed","thu","fri","sat","sun"])
p.subplots_adjust(left=0.07,bottom=0.05,right=0.97,top=0.92,hspace=0.34)
p.show()

# dias do mes
d1=[i.day for i in shT__]
md1=n.mean(d1)
def GG(nn):
    if abs(nn-md1)>15:
        return 30-abs(nn-md1) 
    else:
        return abs(nn-md1)
dd1__=n.array([GG(i) for i in d1])
dd1=((dd1__**2.)/len(dd1__))**0.5
Md1=cDiff(d1,n.arange(33))
d2=[i.day for i in shT2__]
md2=n.mean(d2)
def GG(nn):
    if abs(nn-md2)>15:
        return 30-abs(nn-md2) 
    else:
        return abs(nn-md2)
dd2__=n.array([GG(i) for i in d2])
dd2=((dd2__**2.)/len(dd2__))**0.5
Md2=cDiff(d2,n.arange(33))

p.subplot(411)
p.hist(d1,bins=n.arange(33),normed=1)
p.title("activity in days along the month (a)")
Md1=cDiff(d1,n.arange(1,31))
#p.xticks([])
p.subplot(412)
p.hist(d2,bins=n.arange(33),normed=1)
p.title("activity in days along the month (b)")
Md2=cDiff(d2,n.arange(1,31))
# distribuicao uniforme
u1=n.random.random_integers(0,29,len(d1))+1
mu1=n.mean(u1)
du1= n.std(u1)
Mu1= cDiff(u1,n.arange(30)+1)
#p.xticks([])
p.subplot(413)
p.hist(u1,bins=n.arange(33),normed=1)
p.title("Uniform distribution simulation (a)")
u2=n.random.random_integers(0,29,len(d2))+1
mu2=n.mean(u2)
du2= n.std(u2)
Mu2= cDiff(u2,n.arange(30)+1)
#p.xticks([])
p.subplot(414)
p.hist(u2,bins=n.arange(33),normed=1)
p.title("Uniform distribution simulation (b)")
#p.xticks(n.arange(7)+0.5,["mon","tue","wed","thu","fri","sat","sun"])
p.subplots_adjust(left=0.07,bottom=0.05,right=0.97,top=0.94,hspace=0.46)
p.show()




# meses do ano

