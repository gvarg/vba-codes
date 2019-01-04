# This Python file uses the following encoding: utf-8
import os, sys

v_text = 'Az EP-választásokra hívja fel a figyelmet Orbán Viktor levélben. Mindenki megkapja a levelet január közepéig, aki korábban jóváhagyta azt. A levél a Fidesz EP-kampányát készíti elő, amelynek most nagyobb a tétje, mint korábban bármikor. Ennek oka, hogy az idei választás tétje, hogy Európa bevándorlókontinenssé válik-e. Már kézbesítik Orbán Viktor levelét – írja a Magyar Idők. A lap úgy tudja, hogy január 3-án megkezdődött levelek kiküldése, amelyben a közelgő, májusi európai parlamenti (EP-) választás tétjére hívja fel a figyelmet a miniszterelnök. Ez a levél Fidesz EP-kampányát készíti elő. A leveleket január közepéig mindenki megkapja, de csak azok kapnak ilyet, akik erre korábban felhatalmazást kaptak. Orbán Viktor a 2019 májusában következő európai parlamenti választásról ír majd, amelynek tétje nagyobb lesz, mint a korábbi években bármikor. Brüsszel a sorozatos terrortámadásokból mit sem tanulva továbbra is bevándorlókontinenssé akarja tenni Európát, és ezt rá akarja erőltetni a nemzetállamokra. Mi, magyarok ezt nem fogadhatjuk el. Az ellenzék már bebizonyította, hogy rájuk nem számíthatunk ebben a küzdelemben, mert ők Brüsszelt képviselik Magyarországon. Nekünk pedig olyan képviselőkre van szükségünk, akik Magyarországot képviselik Brüsszelben. A Fidesz–KDNP jelöltjei a magyar érdekeket mindig megalkuvás nélkül fogják képviselni az Európai Parlamentben – olvasható a levéllel kapcsolatos, néhány napja kiadott közleményben. Orbán Viktor miniszterelnök felszólal az Európai Parlament vitáján. Az EP-választási kampány ugyan hivatalosan később kezdődik, de a februári parlamenti idénykezdetre és a hagyományos miniszterelnöki évértékelőre gyakorlatilag már az uniós voksolás hangolásaként tekintenek a kormányzó pártban. Orbán Viktor legutóbb egy éve, tavaly januárban fordult levélben támogatóihoz, a miniszterelnök Soros György tevékenysége elleni kampányhoz kért pénzt. A levél címzettjei a csatolt csekk segítségével járulhatnak hozzá ahhoz. Tavaly január végén lapunknak úgy nyilatkozott, hogy négy hét alatt több mint 36 ezren válaszoltak a kiküldött levélre, és mintegy 186 millió forint érkezett a megadott számlaszámra. Átlagosan ötezer forinttal támogatták az Orbán Viktor által meghirdetett célt. A befolyt pénzből felvilágosító anyagokat és plakátokat készítettek. A Fidesz régóta él a közösségi finanszírozás adta lehetőségekkel. A mikroadományok küldése egyben fontos visszajelzés is a pártot támogatók részéről. Ez Nyugat-Európában, de főként az Amerikai Egyesült Államokban bevett gyakorlat.'
#hányszor szerepelnek?
#Orbán
#Soros
#Brüsszel
v_orban=0
v_soros=0
v_brusszel=0

v_list=v_text.split(" ")

for item in v_list:
    if item[:5].lower()=='orbán':
        v_orban += 1
    if item[:6].lower()=='soros':
        v_soros += 1
    if item[:8].lower()=='brüsszel':
        v_brusszel += 1

print('Szavak száma:')
print('Orbán: {num}'.format(num=v_orban))
print('Soros: {num}'.format(num=v_soros))
print('Brüsszel: {num}'.format(num=v_brusszel))
