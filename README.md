
# Zespół nr: 1
### Skład zespołu wraz z funkcjami:<br />

Jakub Obarowski - przywódca<br />
Dorota Harasimiuk - sekretarz<br />
Marcel Tutak - zastępca<br /><br />
### Role:
koordynator - Jakub Obarowski, Dorota Harasimiuk<br />
programista - cały zespół<br />
strona graficzna - Dorota Harasimiuk<br />
tester - cały zespół<br />
autor dokumentacji - Dorota Harasimiuk<br />

# Ogólny opis
Nasz projekt Flatworld to historia - zasiadasz, odpalasz aplikację webową i stopniowo tworzysz świat, w którym żyją płaszczaki.
# FlatWorld
![kraina](https://github.com/obarowskij/AiSD/assets/146991219/70d9dfba-e964-468b-bb6d-59a82b36d572)

# Wystartowanie projektu

### Krok 1.
pobranie paczki requirements
```bash
pip install -r requirements.txt
```

### Krok 2.
Migracje
```bash
python manage.py migrate
```

### Krok 3.
Uruchomienie aplikacji
```bash
python manage.py runserver
```
Serwer uruchomi się domyślnie pod adresem http://127.0.0.1:8000

### Uruchomienie Testów
```bash
pytest
```
# Harmonogram realizacji
![obraz](https://github.com/obarowskij/AiSD2/assets/146991219/fd599c54-ca0b-496d-9471-f48bb7a9612b)


# Dokumentacja
| L.p | Specyfikacja problemu (dane i wyniki) | Do jakich treści w zadaniu odnosi się algorytm | Zastosowane struktury danych | Informacje o zastosowanym algorytmie | Osoba realizująca |
| --- | -------------------------------------- | --------------------------------------------- | ---------------------------- | ----------------------------------- | ------------------ |
| 1.  | Dane: zbiór punktów orientacyjnych tworzących obszar Krainy <br /> Wynik: bliczenie otoczki wypukłej Krainy | Zdefiniowanie obszaru w którym żyją płaszczaki na Stronie | stos, listy | Algorytm Grahama | Harasimiuk |
| 2.  | Dane: lista tragarzy i lista punktów świata<br /> Wynik: Lista tragarzy, którzy mogą współpracować ze sobą przy transporcie odcinków z fabryki oraz punkt, gdzie znajduje się fabryka | Wybudowanie fabryki i dobranie tragarzy do transportu odcinków z fabryki | słowniki | Proste dopasowanie i obliczenia | Harasimiuk |
| 3.  | Dane: Otoczka wypukła Krainy oraz lista tragarzy gotowych do współpracy<br /> Wynik: Minimalny koszt zbudowania płotu wokół Krainy | Zbudowanie płotu wokół Krainy | kolejka | Djikstra + prosty wzór na koszt | Obarowski |
| 4.  | Dane: Ciąg znaków (opowieść-melodia) i słowo które zostało w niej zmienione <br /> Wynik: Indeksy podmienionego słowa w piosence | Znalezienie oryginalnej melodii | Lista | Algorytm Rabina-Karpa | Obarowski |
| 5.  | Dane: Ciąg znaków a1a2...an reprezentujący opowieść-melodię<br /> Wynik: kodowanie dla ciągu znaków, umożliwiające kompresję danych | Problem niewystarczającej ilości pamięci na komputerze informatyka płaszczaka | słowniki, 'drzewo' | Huffman | Obarowski |
| 6.  | Dane: Lista strażników i lista punktów obserwacyjnych <br /> Wynik: Harmonogram pracy strażników ustawiany według minimalnej liczby odsłuchań melodii w trakcie pracy | Potrzeba ochrony płotu | ----------- | RMQ | Tutak |

# Algorytm Grahama
### 1.Kroki algorytmu:
1. Znajdowanie punktu początkowego: Wybierany jest punkt o najmniejszej współrzędnej y (a w przypadku remisu, punkt o najmniejszej współrzędnej x).</br>
2. Sortowanie: Wszystkie punkty są sortowane według kąta polarniego względem punktu początkowego.</br>
3. Budowanie otoczki wypukłej: Punkt początkowy i dwa pierwsze punkty posortowanej listy dodaje się do stosu. Następnie przechodzi się przez pozostałe punkty, dodając je do stosu i usuwając punkty z wierzchołka stosu, jeśli nie tworzą zakrętu w lewo.</br>
### 2.Złożoność obliczeniowa
Złożoność czasowa algorytmu Grahama wynosi O(nlogn), gdzie n to liczba punktów. Jest to spowodowane przede wszystkim koniecznością sortowania punktów według kąta polarniego. Kroki związane z przeglądaniem i budowaniem otoczki wypukłej mają złożoność liniową O(n).
### 3.Niezmiennik
Niezmiennikiem w algorytmie Grahama jest fakt, że w każdej iteracji stos zawiera sekwencję punktów tworzących część otoczki wypukłej. Innymi słowy, każdy punkt na stosie jest częścią otoczki wypukłej dla punktów przetworzonych do tej pory. Dzięki temu możemy być pewni, że po przetworzeniu wszystkich punktów stos będzie zawierał pełną otoczkę wypukłą.

# Algorytm KMP
### 1.Kroki algorytmu:
1. Preprocessing: Pierwszym krokiem algorytmu jest przetwarzanie wzorca (pattern), aby utworzyć tablicę częściowych dopasowań (partial match table). Dla każdej pozycji w wzorcu, tablica ta zawiera informacje o najdłuższym prefiksie wzorca, który jest zarówno sufiksem, jak i podciągiem tego prefiksu.</br>
2. Wyszukiwanie: Główny krok algorytmu polega na przesuwaniu wzorca względem tekstu (text) i porównywaniu go z tekstem, aż do znalezienia dopasowania lub zakończenia przeszukiwania. W przypadku niezgodności, algorytm wykorzystuje tablicę częściowych dopasowań, aby określić, gdzie należy przesunąć wzorzec.
### 2.Złożoność obliczeniowa
Złożoność czasowa algorytmu KMP wynosiO(n+m), gdzie nn to długość tekstu, a m to długość wzorca. Jest to spowodowane przede wszystkim faktem, że preprocessing wzorca wymaga czasu liniowego, a samo wyszukiwanie wymaga tylko jednego przejścia przez cały tekst.
### 3.Niezmiennik
Niezmiennikiem algorytmu KMP jest fakt, że w każdej iteracji wyszukiwania pozycja wzorca w tekście zawsze znajduje się na takiej pozycji, gdzie możliwe jest dopasowanie. To oznacza, że nie ma potrzeby cofania się w tekście podczas procesu wyszukiwania, ponieważ algorytm korzysta z informacji zawartych w tablicy częściowych dopasowań, aby przesuwać wzorzec na przód, jeśli wystąpi niezgodność.

# Algorytm Huffmana
### 1.Kroki algorytmu:
1. Budowa drzewa Huffmana: Pierwszym krokiem algorytmu jest budowa drzewa Huffmana na podstawie częstości występowania symboli w tekście (lub innych danych), gdzie symbole o niższej częstości występowania mają dłuższe kody, a te o wyższej częstości mają krótsze kody. Drzewo to jest binarne, z węzłami reprezentującymi symbole oraz ich częstości, a liśćmi reprezentującymi same symbole.</br>
2. Przypisanie kodów: Następnie koduje się symbole na podstawie drzewa Huffmana, przypisując im kody binarne. Kody te są tworzone poprzez przypisanie 0 do każdej krawędzi wychodzącej w lewo z węzła i 1 do krawędzi wychodzącej w prawo. Kody są budowane poprzez przechodzenie od korzenia do liścia i zapisywanie sekwencji bitów na podstawie kierunków w drzewie.
### 2.Złożoność obliczeniowa
Złożoność czasowa budowy drzewa Huffmana wynosi O(nlogn), gdzie n to liczba symboli. Jest to spowodowane przede wszystkim sortowaniem symboli według ich częstości oraz konstrukcją drzewa binarnego. Złożoność pamięciowa algorytmu jest również O(n)O(n).
### 3.Niezmiennik
Niezmiennikiem algorytmu Huffmana jest fakt, że drzewo Huffmana zawsze zachowuje własność optymalnej kodowania, czyli sumaryczna długość kodów dla wszystkich symboli jest minimalna. Ta własność jest zachowywana podczas budowy drzewa oraz przypisywania kodów, co zapewnia optymalność uzyskanego kodu Huffmana.

# Algorytm Dijkstra
todo
### 1.Kroki algorytmu:
1. 
### 2.Złożoność obliczeniowa
Złożoność czasowa algorytmu 
### 3.Niezmiennik

# Algorytm RMQ
todo
### 1.Kroki algorytmu:
1. 
### 2.Złożoność obliczeniowa
Złożoność czasowa algorytmu 
### 3.Niezmiennik
POPRAWNOSC FORMALNA TO TRZEBA DAC OPISY NP CZEMU PETLE SIE KONCZA EWENTUALNIE JAKI JEST NIEZMIENNIK

# Wykorzystane technologie
Python, Django, JS




