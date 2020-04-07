# NTIN060 | Homework 05/5

Milan Wikarski (milan@wikarski.sk)

## Zadanie

**6. Revoluce u Bobří řeky.** Chcete zavést KaraNET i ve své domovské vesnici Kravařích. Síť možných spojení je bohužel trochu řidší a spojení odpovídá rovinnému grafu. Jak dlouho bude trvat nalézt páteřní síť v tomto rozložení?

## Riešenie a dôkaz správnosti

Majme súvislý rovinný graf <code>G = (V, E)</code>, zobrazenie <code>E -> w</code>, ktoré každej hrane priradí nejakú váhu. Hľadáme minimálnu kostru grafu <code>G</code>.

Pre nájdenie minimálnej kostry grafu <code>G</code> použijeme Jarníkův algoritmus. Vyberieme si nejaký vrchol <code>v<sub>0</sub></code> (náhodne) a začneme so stromom <code>T = ({v<sub>0</sub>}, {})</code>, ktorý obsahuje iba vrchol <code>v<sub>0</sub></code> a žiadne hrany.

### Stav vrcholov

Každý vrchol <code>v ∊ V</code> sa bude nachádzať v jednom z troch stavov:

1. **IN** - ak <code>v</code> patrí do T.
2. **NEIGHBOR** - ak <code>v</code> nepatrí do T a zároveň existuje hrana <code>e={u, v} ∊ G</code> medzi <code>T</code> a zvyškom grafu <code>G</code> (tzn. <code>u ∊ V(T), v ∊ V(G) \ V(T)</code>).
3. **OUT** - v ostatných prípadoch.

Tieto stavy budú uložené v poli <code>state</code>.

### Ohodnotenie vrcholov

Každý vrchol <code>v ∊ V</code> budú mať ohodnotenie <code>eval[v]</code> - to odpovedá:

- <code>+∞</code>, ak <code>state[v] = OUT</code>.
- najnižšej váhe z hrán, ktoré vedú z vrchola <code>v</code> do nejakého vrchola <code>u ∊ V(T)</code>, ak <code>state[v] = NEIGHBOR</code>.
- ak <code>state[v] = IN</code>, hodnota <code>eval[v]</code> nás nezaújíma a nebude uložená

Ohodnotenie hrán si uložíme do minimálnej haldy, ktorá bude mať operácie ExtractMin a Decrease.

### Predchodcovia

Ďalej si budeme držať pole predchodcov <code>pred[v]</code>. Bude platiť, že ak <code>eval[v] < +∞</code>, potom hrana <code>e = {v, pred[v]}</code> je hrana s najnižším ohodnotením, ktorá vedie z vrchola <code>v</code> do nejakého vrchola <code>u ∊ V(T)</code>.

### Beh algoritmu

V každom kroku algoritmu si vyberieme vrchol <code>v ∊ V</code> s najnižším ohodnotením <code>eval[v]</code> z haldy a pripojíme ho ku grafu <code>T</code> hranou <code>e = {v, pred[v]}</code>. Ďalej prepočítame hodnotu <code>eval[u]</code> pre všetkých susedov <code>u</code> vrchola <code>v</code>, ktorí nepatria do <code>T</code> (konkrétne ju znížime, ak hrana medzi vrcholmi <code>u</code> a <code>v</code> má nižšiu váhu, ako je hodnota <code>eval[u]</code>).

### Správnosť

Tu je dôležité, že ani hrana <code>e</code>, ani vrchol <code>v</code> nepatria do grafu <code>T</code>, a teda ku <code>T</code> pripájame listy. Z toho dostávame, že graf <code>T</code> bude počas celého behu algoritmu strom.

Algoritmus sa po najviac <code>n</code> krokoch zastaví, keďže v každom kroku sme ku grafu <code>T</code> pridali jeden vrchol.

V každom kroku vyberáme najľahšiu hranu elementárneho rezu medzi stromom <code>T</code> a zvyškom grafu. Všetky vybrané hrany teda ležia v minimálnej kostre, a teda strom <code>T</code> je minimálnou kostrou grafu <code>G</code>.

## Algoritmus

```C
ALGORITMUS: PravdepodobnostUspechuPrenosu
---------------------------------------------------------------
 INPUT: graf G = (V, E), zobrazenie E -> w
OUTPUT: Strom T, ktorý je minimálnou kostrou grafu G

 1. for ∀ v ∊ V:
 2.   eval[v] <- +∞
 3.   pred[v] <- null
 4.   state[v] <- OUT
 5. v0 <- random vertex from V
 6. eval[v0] <- 0
 7. state[v0] <- NEIGHBOR
 8. while (exists v ∊ V such that state[v] = NEIGHBOR):
 9.   v <- ExtractMin(pred)                                 ⊲ Vyberieme vrchol s najnižšou hodnotou eval z haldy
10.   state[v] <- IN
11.   if (pred[v] is not null):                             ⊲ Nutná kontrola, pretože pred[v0] is null
12.     V(T) <- V(T) ∪ {v}
13.     E(T) <- E(T) ∪ {v, pred[v]}                         ⊲ Pridáme list ku stromu T
14.   for (∀ u; u is neighbour of v):                       ⊲ Každý vrchol u spojený hranou s vrcholom v
15.     if (state[u] != IN and eval[u] > w({u, v})):
16.       state[u] <- NEIGHBOR
17.       eval[u] <- w({u, v})
18.       pred[u] <- v
19. return T
```

## Časová a priestorová zložitosť

Označme si <code>n = |V|</code> počet vrcholov a <code>m = |E|</code> počet hrán.

### Časová zložitosť

Jarníkův algoritmus nájde minimálnu kostru pri použití halde v čase <code>O(m \* log(n))</code>. Pre rovinné grafy platí <code>m ≤ 3n - 6</code>, z čoho dostávame <code>O(m \* log(n)) = O((3n - 6) \* log(n)) = O(n \* log(n))</code>

### Priestorová zložitosť

Algoritmus pracuje s pomocnými poľami <code>pred</code> a <code>state</code> a haldou <code>eval</code> ktoré majú dĺžku <code>n</code>. Ďalej potrebujeme pamäť na ukladanie kostry <code>T</code>, čo je najvaic <code>O(n + m)</code>. Z hore spomenutého odhadu ale máme <code>O(n + m) = O(n + 3n - 6)</code>. Dokopy to všetko je <code>O(3n + n + 3n - 6) = O(n)</code>.
