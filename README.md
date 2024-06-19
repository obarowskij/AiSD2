
# Zespół nr: 1
### Skład zespołu wraz z funkcjami:<br />

Jakub Obarowski - przywódca<br />
Dorota Harasimiuk - sekretarz<br />
Marcel Tutak - zastępca<br /><br />
### Role:
kierownik - Jakub Obarowski<br />
koordynator - Dorota Harasimiuk<br />
programista - cały zespół<br />
strona graficzna - Dorota Harasimiuk<br />
tester - cały zespół<br />
autor dokumentacji - Dorota Harasimiuk<br />
### Spis treści
- [Ogólny opis](#1)
- [Wystartowanie projektu](#2)
- [Testy](#3)
- [Harmonogram](#4)
- [Dokumentacja](#5)
- [Opis algorytmów](#6)
- [Technologie](#7)

  
<a id='1'></a>
# Ogólny opis
Nasz projekt Flatworld to historia - zasiadasz, odpalasz aplikację webową i stopniowo tworzysz świat, w którym żyją płaszczaki.
# FlatWorld
![kraina](https://github.com/obarowskij/AiSD/assets/146991219/70d9dfba-e964-468b-bb6d-59a82b36d572)
<a id='2'></a>
# Wystartowanie projektu
### Krok 1.
Stworzenie środowiska wirtualnego
```bash
  python -m venv venv
  venv\Script\activate
```
### Krok 2.
pobranie paczki requirements
```bash
  pip install -r requirements.txt
```

### Krok 3.
Migracje
```bash
  python manage.py migrate
```

### Krok 4.
Uruchomienie aplikacji
```bash
  python manage.py runserver
```
Serwer uruchomi się domyślnie pod adresem http://127.0.0.1:8000
<a id='3'></a>
### Uruchomienie Testów
```bash
pytest
```
<a id='4'></a>
# Harmonogram realizacji
![obraz](https://github.com/obarowskij/AiSD2/assets/146991219/fd599c54-ca0b-496d-9471-f48bb7a9612b)

<a id='5'></a>
# Dokumentacja
| L.p | Specyfikacja problemu (dane i wyniki) | Do jakich treści w zadaniu odnosi się algorytm | Zastosowane struktury danych | Informacje o zastosowanym algorytmie | Osoba realizująca |
| --- | -------------------------------------- | --------------------------------------------- | ---------------------------- | ----------------------------------- | ------------------ |
| 1.  | Dane: zbiór punktów orientacyjnych tworzących obszar Krainy <br /> Wynik: bliczenie otoczki wypukłej Krainy | Zdefiniowanie obszaru w którym żyją płaszczaki na Stronie | stos, listy | Algorytm Grahama | Harasimiuk |
| 2.  | Dane: lista tragarzy i lista punktów świata<br /> Wynik: Lista tragarzy, którzy mogą współpracować ze sobą przy transporcie odcinków z fabryki oraz punkt, gdzie znajduje się fabryka | Wybudowanie fabryki i dobranie tragarzy do transportu odcinków z fabryki | słowniki | Proste dopasowanie i obliczenia | Harasimiuk |
| 3.  | Dane: Otoczka wypukła Krainy oraz lista tragarzy gotowych do współpracy<br /> Wynik: Minimalny koszt zbudowania płotu wokół Krainy | Zbudowanie płotu wokół Krainy | kolejka | Djikstra + prosty wzór na koszt | Obarowski |
| 4.  | Dane: Ciąg znaków (opowieść-melodia) i słowo które zostało w niej zmienione <br /> Wynik: Indeksy podmienionego słowa w piosence | Znalezienie oryginalnej melodii | Lista | Algorytm Rabina-Karpa | Obarowski |
| 5.  | Dane: Ciąg znaków a1a2...an reprezentujący opowieść-melodię<br /> Wynik: kodowanie dla ciągu znaków, umożliwiające kompresję danych | Problem niewystarczającej ilości pamięci na komputerze informatyka płaszczaka | słowniki, 'drzewo' | Huffman | Obarowski |
| 6.  | Dane: Lista strażników i lista punktów obserwacyjnych <br /> Wynik: Harmonogram pracy strażników ustawiany według minimalnej liczby odsłuchań melodii w trakcie pracy | Potrzeba ochrony płotu | drzewo przedziałowe + słownik | Algorytm własny + RMQ | Tutak |
<a id='6'></a>
# Algorytm Grahama
### 1.Kroki algorytmu:
1. Znajdowanie punktu początkowego: Wybierany jest punkt o najmniejszej współrzędnej y (a w przypadku remisu, punkt o najmniejszej współrzędnej x).</br>
2. Sortowanie: Wszystkie punkty są sortowane według kąta polarniego względem punktu początkowego.</br>
3. Budowanie otoczki wypukłej: Punkt początkowy i dwa pierwsze punkty posortowanej listy dodaje się do stosu. Następnie przechodzi się przez pozostałe punkty, dodając je do stosu i usuwając punkty z wierzchołka stosu, jeśli nie tworzą zakrętu w lewo.</br>
### 2.Złożoność obliczeniowa
Złożoność czasowa algorytmu Grahama wynosi O(nlogn), gdzie n to liczba punktów. Jest to spowodowane przede wszystkim koniecznością sortowania punktów według kąta polarniego. Kroki związane z przeglądaniem i budowaniem otoczki wypukłej mają złożoność liniową O(n).
### 3.Niezmiennik
Niezmiennikiem w algorytmie Grahama jest fakt, że w każdej iteracji stos zawiera sekwencję punktów tworzących część otoczki wypukłej. Innymi słowy, każdy punkt na stosie jest częścią otoczki wypukłej dla punktów przetworzonych do tej pory. Dzięki temu możemy być pewni, że po przetworzeniu wszystkich punktów stos będzie zawierał pełną otoczkę wypukłą.

# Algorytm Rabin-Karp
### 1.Kroki algorytmu:
1. Pierwszym krokiem algorytmu jest obliczenie hasha wzorca.</br>
2. Główny krok algorytmu polega na przesuwaniu wzorca względem tekstu (text) i porównywaniu go z tekstem, aż do znalezienia dopasowania lub zakończenia przeszukiwania. W przypadku zgodności hashy wzorca oraz wycinka tekstu, wykorzystujemy algorytm naiwny w celu ich porównania.
### 2.Złożoność obliczeniowa
Złożoność czasowa algorytmu KMP wynosiO(n+m), gdzie nn to długość tekstu, a m to długość wzorca. Jest to spowodowane przede wszystkim faktem, że preprocessing wzorca wymaga czasu liniowego, a samo wyszukiwanie wymaga tylko jednego przejścia przez cały tekst.
### 3.Niezmiennik
Niezmiennikiem algorytmu KMP jest fakt, że w każdej iteracji wyszukiwania pozycja wzorca w tekście zawsze znajduje się na takiej pozycji, gdzie możliwe jest dopasowanie. To oznacza, że nie ma potrzeby cofania się w tekście podczas procesu wyszukiwania, ponieważ algorytm korzysta z informacji zawartych w tablicy częściowych dopasowań, aby przesuwać wzorzec na przód, jeśli wystąpi niezgodność.

# Algorytm Huffmana
### 1.Kroki algorytmu:
1. Budowa drzewa Huffmana: Pierwszym krokiem algorytmu jest budowa drzewa Huffmana na podstawie częstotliwości występowania symboli w tekście (lub innych danych), gdzie symbole o niższej częstotliwości występowania mają dłuższe kody, a te o wyższej częstotliwości mają krótsze kody. Drzewo to jest binarne, z węzłami reprezentującymi symbole oraz ich częstotliwości, a liśćmi reprezentującymi same symbole.</br>
2. Przypisanie kodów: Następnie koduje się symbole na podstawie drzewa Huffmana, przypisując im kody binarne. Kody te są tworzone poprzez przypisanie 0 do każdej krawędzi wychodzącej w lewo z węzła i 1 do krawędzi wychodzącej w prawo. Kody są budowane poprzez przechodzenie od korzenia do liścia i zapisywanie sekwencji bitów na podstawie kierunków w drzewie.
### 2.Złożoność obliczeniowa
Złożoność czasowa budowy drzewa Huffmana wynosi O(nlogn), gdzie n to liczba symboli. Jest to spowodowane przede wszystkim sortowaniem symboli według ich częstości oraz konstrukcją drzewa binarnego. Złożoność pamięciowa algorytmu jest również O(n)O(n).
### 3.Niezmiennik
Niezmiennikiem algorytmu Huffmana jest fakt, że drzewo Huffmana zawsze zachowuje własność optymalnej kodowania, czyli sumaryczna długość kodów dla wszystkich symboli jest minimalna. Ta własność jest zachowywana podczas budowy drzewa oraz przypisywania kodów, co zapewnia optymalność uzyskanego kodu Huffmana.

# Algorytm Dijkstra
### 1.Kroki algorytmu:
1. Stworzenie grafu na podstawie macierzy
2. Dodanie krawędzi do grafu
3. Zainicjalizowanie kolejki priorytetowej i dodanie do niej wierzchołka startowego z odległościa równa 0.
4. Pobranie wierzchołka z kolejki, który ma najmniejszą dotychczasową odległość, jeśli jest to wierzchołek docelowy, progam kończy działanie.
5. Oblicznie nowej odległości jako suma dotychczasowej odległości do bieżącego wierzchołka i wagi krawędzi prowadzącej do sąsiada. Jeśli nowa odległość jest mniejsza niż dotychczasowa odległość do sąsiada, zaktualizowanie odległości oraz dodanie sąsiada do kolejki priorytetowej.
### 2.Złożoność obliczeniowa
Główna pętla algorytmu ma złożoność O(V), gdzie V to liczba węzłów. Dla każdego węzła sprawdzane są wszystkie jego krawędzie, co w najgorszym przypadku zajm,uje O(E), gdzie E to liczba krawędzi w grafie. Operacje na kolejce priorytetowej zajmują O(log V) czasu co daje łączną złożoność O((V+E)logV)
### 3.Niezmiennik
Niezmiennikami algorytmu Dijkstry sa fakty, że kolejka priorytetowa zawsze zawiera węzły, które zostały odkryte, ale jeszcze nie odwiedzone, wszystkie węzły w zbiorze visited mają swoje najkrótsze odległości od węzła start oraz to że słownik previous_nodes zawiera poprzedni węzeł dla każdego odwiedzonego węzła na najkrótszej ścieżce od węzła start.
# Algorytm RMQ
### 1.Kroki algorytmu:
1. Ustalenie 7 strażników według ich poziomu energii na każdy dzień tygodnia.
2. Losowanie energii w danym dniu na każdym punkcie płotu oraz tworzenie i uzupelnianie drzewa przedziałowego nimi.
3. Ustalanie na jakich punktach ma się zatrzymać strażnik tak, aby jak najmniej musiał odsłuchiwać melodii.
### 2.Złożoność obliczeniowa
Złożoność czasowa wyboru strażników to O(n log n), ponieważ mieszkańcy są posortowani względem energii i wybranych zostaje tylko 7. Każdy dzień jest inny, zatem energia w każdym punkcie też jest inna czyli O(n). Budowa drzewa przedziałowego z tych wylosowanych energii O(n). Ustalanie gdzie ma się zatrzymywać strażnik jest O(n log n).
### 3.Niezmiennik
Algorytm utrzymuje poprawność pozycji strażnika i, list stop_points i songs, gdzie i wskazuje ostatnią pozycję zatrzymania, a listy zawierają odpowiednie punkty zatrzymania i miejsca do grania melodii. Minimalna energia w przeszukiwanych przedziałach jest kluczowa dla decyzji o zatrzymaniu się strażnika. Lista strażników jest początkowo posortowana według energii, a wybrani strażnicy tworzą harmonogram zgodnie z oczekiwaniami algorytmu.
<a id='7'></a>
# Wykorzystane technologie
Python, Django, JS




