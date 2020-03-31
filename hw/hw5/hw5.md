# NTIN060 | Homework 05/5

Milan Wikarski (milan@wikarski.sk)

## Zadanie

5.Pravděpodobnost.Každé spojení má pravděpodobnost úspěchu přenosu <code>0 ≤ p<sub>i</sub> ≤ 1</code>. Pravděpodobnost úspěchu pro cestu <code>v<sub>1</sub>, ..., v<sub>k</sub></code> je <code>p<sub>(v1, v2)</sub> \* ... \* p<sub>(vk-1, vk)</sub></code>. Chcete najít cestu, po které je nejvíce pravděpodobné, že uspějete. Jak ji najdete?

## Riešenie a dôkaz správnosti

Majme graf <code>G = (V, E)</code>, zobrazenie <code>E -> p</code>, ktoré každej hrane priradí nejakú pravdepodobnosť <code>0 ≤ p<sub>i</sub> ≤ 1</code> a nejaké vrcholy <code>v<sub>0</sub>,u<sub>0</sub> ∊ V</code> Chcem zistiť cestu s najväčšou pravdepodobnosťou úspechu z <code>v<sub>0</sub></code> do <code>u<sub>0</sub></code>.

Vytvoríme si pole <code>S[v]</code>, kde budeme uchovávať pravdepodobnosť úspechu spojenia z vrcholu <code>v<sub>0</sub></code> do vrcholu <code>v</code>. Začneme vo vrchole <code>v<sub>0</sub></code>, pre ktorý bude platiť <code>S[v<sub>0</sub>] = 1</code>. Pre všetky ostatné vrcholy nastavíme túto hodnotu na 0.

Vytvoríme si frontu, do ktorej budeme ukladať otvorené vrcholy. Na začiatku cyklu z fronty vyberieme jeden vrchol, preskúmame jeho susedov, prepočítame pravdepodobnosti prenosu a otvoríme 0 alebo viac vrcholov, ktoré pridáme na koniec fronty. Toto sa bude opakovať, dokým sa fronta úplne nevyprázdni. Po skončení výpočtu budú v poli <code>S</code> správne hodnoty pravdepodobnosti úspechu prenosu pre každý vrchol.

### Výpočet pravdepodobnosti spojenia

Rozoberme hlavný cyklus. Na jeho začiatku z fronty vyberieme vrchol <code>v</code>. Pozrieme sa na všetky jeho susedné vrcholy. Uvažujme susedný vrchol <code>u</code>. Chceme zistiť, či pravdepodobnosť úspechu prenosu po ceste <code>(v<sub>0</sub>, ..., v, u)</code> (označíme ju <code>p'</code>) je väčšia, ako hodnota <code>S[u]</code>. Ak platí <code>p' > S[u]</code>, potom sme objavili cestu z <code>v<sub>0</sub></code> do <code>u</code>, ktorá má väčšiu pravdepodobnosť úspechu, než sme si doteraz mysleli. V takom prípade nastavíme <code>S[u] = p'</code> a vrchol <code>u</code> otvoríme (dáme ho na koniec fronty).

### Predchodcovia vrcholov

Vytvoríme si pole <code>P[v]</code>, kde budeme uchovávať predchodcov vrcholu <code>v</code>. Takto budeme vedieť spätne zistiť cestu z <code>v<sub>0</sub></code> do <code>u<sub>0</sub></code>. Vždy, keď budeme nastavovať <code>S[u] = p'</code>, nastavíme aj <code>P[u] = v</code>.

### Fázy výpočtu

Výpočet bude prebiehať vo fázach. Vo fáze <code>F<sub>0</sub></code> otvoríme vrchol <code>v<sub>0</sub></code>. Vo fáze <code>F<sub>i+1</sub></code> zatvárame vrcholy otvorené vo fáze <code>F<sub>i</sub></code>. Vo fáze <code>F<sub>i</sub></code> budeme už definitívne poznať hodnoty <code>S[u]</code> a <code>P[u]</code> pre všetky vrcholy <code>u ∊ V</code>, pre ktoré platí <code>d(v<sub>0</sub>, u) ≤ i</code>, kde <code>d(v<sub>0</sub>, u)</code> je počet hrán medzi vrcholmi <code>v<sub>0</sub></code> a <code>u</code> (analogicky z Bellman-Fordova algoritmu; dá sa dokázať indukciou). Tým pádom po najviac <code>O(n)</code> fázach budeme poznať definitívne hodnoty <code>S[v]</code> a <code>P[v]</code> pre všetky <code>v ∊ V</code>.

## Algoritmus

```C
ALGORITMUS: PravdepodobnostUspechuPrenosu
---------------------------------------------------------------
 INPUT: graf G = (V, E), zobrazenie E -> p a vrcholy v0, u0
OUTPUT: Cesta z v0 do u0 s najväčšou pravdepodobnosťou úspechu

 1. queue <- new Queue()                 ⊲ vytvoríme si prázdnu frontu
 2. for ∀ v ∊ V:
 3.   S[v] <- 0                          ⊲ Pravdepodobnosť úspechu cesty (v0, ..., v)
 4.   P[v] <- null                       ⊲ Predchodca vrcholu v
 5. S[v0] <- 1
 6. queue.enqueue(v0)                    ⊲ Začneme vo v0
 7. while (queue is not empty):
 8.   v <- queue.dequeue()               ⊲ Vyberieme v z fronty
 9.   for (∀ u; u is neighbour of v):    ⊲ Každý vrchol u spojený hranou s vrcholom v
10.      if (S[u] < S[v] * p[(v, u)]):   ⊲ Ak sme našli lepšiu cestu
11.        S[u] <- S[v] * p[(v, u)]
12.        P[u] <- v
13.        queue.enqueue(u)
14. path <- new List()
15. while (u0 != null):
16.   path.append(u0)
17.   u0 <- P[u0]
18. return path.reverse()
Poznámka: p[(v, u)] je pravdepodobnosť spojenia po hrane (v, u)
```

## Časová a priestorová zložitosť

Označme si `n = |V|` počet vrcholov a `m = |E|` počet hrán.

### Časová zložitosť

Rozdelme si algoritmus na 3 časti:

#### 1. Inicializácia

Inicializácia prebehne v čase `O(n)`, pretože inicializujeme hodnoty `P[v]` a `S[v]` pre všetky `v ∊ V`.

#### 2. Výpočet

Vieme, že výpočet skončí po najviac <code>O(n)</code> fázach. Behom jedej fázy algoritmnus relaxuje každý vrchol najviac raz, takže celá fáza trvá <code>O(m)</code>. Dokopy to je <code>O(nm)</code>.

#### 3. Budovanie cesty

Výsledná cesta môže byť poskladaná z najviac <code>n</code> vrcholov, takže jej poskladanie bude trvať najviac <code>O(n)</code>.

Všetky tri časti spolu budú trvať <code>O(n + nm + n) = O(nm)</code>.

### Priestorová zložitosť

Algoritmus pracuje s pomocnými poľami `P` a `D`, ktoré majú dĺžku `n`. Okrem toho potrebuje pamäť pre frontu, kde v jeden moment nemôže byť viac, ako `n` prvkov. Výslednú cestu vytvorí pomocou spojového zoznamu, ktorý bude mať najviac `n` prvkov. Spolu teda vyžaduje `O(4n) = O(n)` pamäte.

## Alternatívny pohľad na problém

Alternatívne by sme sa na problém mohli dívať takto. Našou úlohou je násť cestu poskladanú z hrán <code>e<sub>1</sub>, e<sub>2</sub>, ..., e<sub>k</sub></code>, kde platí, že <code>e<sub>1</sub> = (v<sub>0</sub>, w)</code>, <code>e<sub>k</sub> = (w', u<sub>0</sub>)</code>. Označme si <code>p<sub>i</sub></code> pravdepodobnosť úspechu prenosu po hrane <code>e<sub>i</sub></code>. Potom našou úlohou je nájsť:

```
argmax {e1, e2, ..., ek} (p1 * p2 * ... * pk)
```

Čo je ekvivalentné s

```
argmax {e1, e2, ..., ek} (log(p1) + log(p2) + ... + log(pk))
```

Hľadáme minimum súčtu logaritmov. Vynásobme celý súčet hodnoutou (-1) a budeme hľadať

```
argmin {e1, e2, ..., ek} (-log(p1) - log(p2) - ... - log(pk))
```

Vieme, že platí <code>0 ≤ p<sub>i</sub> ≤ 1</code> pre všetky <code>i</code>. To znamená, že určite platí aj <code>0 ≤ -log(p<sub>i</sub>)</code> pre všetky <code>i</code>. Spravme si substitúciu <code>W[i] = -log(p<sub>i</sub>)</code>. Dostávame alternatívne ohodnotenie hrán <code>W</code>, kde každá váha je nezáporná a my chcem nájsť najkratšiu cestu vzhľadom na toto ohodnotenie. Na to nám ale postačí ľubovoľný relaxačný algoritmus (ja som použil modifikovaný Bellmanov-Fordov).
