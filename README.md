dokumentacia
Linked List, DFifo, TreeSort
Autor: Oliver Komka

1. Popis projektu
Projekt implementuje dynamicke datove struktury v jazyku Python. Nadväzuje na predchadzajuci projekt zamerany na vyhladavacie a triedenie algoritmy.
Ciele projektu:
-	Implementovat LinkedList s minimalne 10 metodami
-	Nahradit staticku Fifo(5000) dynamickou DFifo v simulacii Hypermarket
-	Naprogramovat TreeSort a zaradit ho do analyzy algoritmov

2. Teoria - Zretazene datove struktury
2.1 Linked List
Zretazeny zoznam je dynamicka linearna datova struktura. Prvky (uzly) su prepojene ukazovatelmi. Kazdy uzol obsahuje hodnotu a odkaz na nasledujuci uzol. Na rozdiel od pola prvky nemusia byt ulozene za sebou v pamati.

Vyhody:
-	Dynamicka velkost - moze rast a zmensovat sa za behu programu
-	Rychle vkladanie a mazanie na zaciatku: O(1)
-	Efektivne pre implementaciu zasobnikov a front
-	Nevyzaduje suvisly blok pamate

Nevyhody:
-	Pomaly pristup podla indexu: O(n)
-	Vyssia pamätova narocnost - kazdy uzol uklada aj ukazovatel
-	Slaba cache lokalita - prvky nie su v pamati za sebou

Zlozitost operacii:
-	Pristup podla indexu: Array O(1) vs LinkedList O(n)
-	Vkladanie na zaciatok: Array O(n) vs LinkedList O(1)
-	Vkladanie na koniec: Array O(1) vs LinkedList O(1)
-	Mazanie prvku: Array O(n) vs LinkedList O(1) ak pozname ukazovatel

2.2 Strom (Tree) a TreeSort
Strom je hierarchicka datova struktura. Binarny vyhladavaci strom (BST) ma vlastnost: lavy podstrom < koren < pravy podstrom. TreeSort vlozi vsetky prvky do BST a potom in-order prechodom (lavy-koren-pravy) ziska zotriedeny vystup.
-	Priemerna zlozitost: O(n log n)
-	Najhorsia zlozitost (utriedene data): O(n²)
-	Nestabilny algoritmus

3. Implementacia
3.1 LinkedList (linkedlist.py)
Jednosmerne zretazeny zoznam s triedou Node a LinkedList. Obsahuje 14 verejnych metod:
-	is_empty() - True ak je zoznam prazdny, O(1)
-	size() - pocet prvkov, O(1)
-	add_first(value) - vloz na zaciatok, O(1)
-	add_last(value) - vloz na koniec, O(1)
-	remove_first() - odober a vrat prvy prvok, O(1)
-	remove_last() - odober a vrat posledny prvok, O(n)
-	peek_first() - nahlad na prvy prvok bez odobratia, O(1)
-	peek_last() - nahlad na posledny prvok bez odobratia, O(1)
-	clear() - vymaz vsetky prvky, O(1)
-	index_of(value) - najdi index hodnoty, -1 ak nenajde, O(n)
-	insert_at(index, value) - vloz na dany index, O(n)
-	remove_at(index) - odober a vrat prvok na indexe, O(n)
-	to_list() - preved na Python list, O(n)
-	reverse() - obrat poradie zoznamu in-place, O(n)

3.2 DFifo (dfifo.py)
Dynamicka FIFO fronta postavena nad LinkedList. Nahradzuje povodnu staticku Fifo(5000) v simulacii Hypermarket.
-	put(item) - vlozi prvok na koniec fronty, O(1)
-	get() - vyberie a vrati prvok zo zaciatku fronty, O(1)
-	getLength() - vrati pocet prvkov, O(1)
Vyhoda oproti statickej verzii: fronta sa automaticky prisposobuje zatazi bez rizika preplnenia alebo mrhania pamatou.

3.3 TreeSort (treesort.py)
Implementovany pomocou binarneho vyhladavacieho stromu. Prebieha v dvoch fazach: budovanie BST (iterativne vkladanie) a in-order prechod (rekurzivny). Sleduje pocet porovnani a priradeni pre porovnanie s ostatnymi algoritmami.

3.4 Simulacia Hypermarket (simulacia.py)
Simuluje prevadzku hypermarketu pocas jednej zmeny (8 hodin). Zakaznici prichadzaju nahodne, nakupuju a potom cakaju v rade na pokladni. Staticka Fifo(5000) bola nahradena dynamickym DFifo - ziadne riziko pretecenia, efektivnejsia pametova sprava.

4. Vyhodnotenie TreeSort
4.1 Rovnomerne nahodne data
TreeSort dosahuje O(n log n) vykon porovnatelny s QuickSort a MergeSort. Pri N=10 000 trvalo triedenie priemerne ~11.5 ms, pri N=20 000 priemerne ~23 ms.

4.2 Kolisavo rastucie a klesajuce data
Vykon prudko klesol - cas narastol na ~820 ms (rastuce) a ~729 ms (klesajuce) pri N=10 000. Pricina: BST sa stava nevyvazenym a degeneruje smerom k linearnej strukture, co sposobuje blizke O(n²) spravanie.

4.3 Zaver k TreeSort
TreeSort je vhodny na nahodne data. Na semi-utriedene vstupy vsak bez vyvazenosti stromu (AVL, Red-Black) vyrazne klesaju vykony. Pocet priradeni je vzdy N pre obe velkosti, co reflektuje deterministicku fazu in-order extrakcie.

5. Zoznam suborov
-	linkedlist.py - LinkedList s 14 metodami
-	dfifo.py - Dynamicka FIFO fronta
-	simulacia.py - Hypermarket simulacia s DFifo
-	treesort.py - TreeSort algoritmus
-	sorty-rovnomerne.py - Analyza sort algoritmov, rovnomerne data
-	sorty-rastuce.py - Analyza sort algoritmov, kolisavo rastucie data
-	sorty-klesanie.py - Analyza sort algoritmov, kolisavo klesajuce data
-	search-a-sort-analyza_Oliver_Komka.xlsx - Kompletna analyza s Tree Sort datami

6. Zaver
Projekt splnil vsetky poziadavky zadania. LinkedList obsahuje 14 metod. DFifo uspesne nahradzuje staticku frontu. TreeSort je implementovany a zaradeny do analyzy pre vsetky tri typy vstupnych dat a obe velkosti N. Vsetky implementacie su v cistom Pythone bez externych kniiznic.
