import random
import  pandas as pd
#data = pd.read_csv('cache20.txt',header = None, sep='///')
#t#ext = data[0]
# text= "Markov chains are very interesting and its a tough algorithm to implement. This is a very interseting computer science problem. This is going to be implemented in web caches. "
# text="The Solar System formed 4.6 billion years ago from the gravitational collapse of a giant interstellar molecular cloud. The vast majority of the system's mass is in the Sun, with the majority of the remaining mass contained in Jupiter. The four smaller inner planets, Mercury, Venus, Earth and Mars, are terrestrial planets, being primarily composed of rock and metal. The four outer planets are giant planets, being substantially more massive than the terrestrials. The two largest, Jupiter and Saturn, are gas giants, being composed mainly of hydrogen and helium; the two outermost planets, Uranus and Neptune, are ice giants, being composed mostly of substances with relatively high melting points compared with hydrogen and helium, called volatiles, such as water, ammonia and methane. All eight planets have almost circular orbits that lie within a nearly flat disc called the ecliptic."
# text="Yo, Big Shaq, the one and only Man's not hot, never hot Skrrat (GottiOnEm), skidi-kat-kat Boom  Two plus two is four Minus one that's three, quick maths Everyday man's on the block Smoke trees (ah) See your girl in the park That girl is a uckers When the ting went quack-quack-quack You man were ducking (you man ducked) Hold tight, Asznee (my brudda) He's got the pumpy (big ting) Hold tight, my man (my guy)  He's got the frisbee (shew) I trap, trap, trap on the phone Movin' that cornflakes Rice Krispies Hold tight, my girl Whitney (my G) On, on, on, on, on the road doin' ten toes Like my toes (like my toes) You man thought I froze I see a peng girl, then I pose (chilin') If she ain't on it, I ghost Hah, look at your nose (check your nose, fam) You donut Nose long like garden hose"
order =4
ngram = dict()
beginnings = []
fobj = open("logfile.txt", "r")

listofinp = fobj.read().split("\n")
# text = " ".join(listofinp)
# print(listofinp)
for j in range(0, len(listofinp)):
    text = listofinp[j]
    for i in range(0, len(text) - order + 1):
        gram = text[i:i + order]
        if i == 0:
            beginnings.append(gram)
        if gram not in ngram:
            ngram[gram] = []
        if i < len(text) - order:
            ngram[gram].append(text[i + order])
print(beginnings)


# print(ngram)
def MarkovGen():
    curgram = random.choice(beginnings)
    result = curgram
    for i in range(0, 20):
        possibilities = ngram[curgram]
        next = random.choice(possibilities)
        result = result + next
        curgram = result[len(result) - order:len(result)]
    print(result)


MarkovGen()




