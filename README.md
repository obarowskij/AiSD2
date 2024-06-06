
# Zespół nr: 1
Skład zespołu wraz z funkcjami:<br />

Dorota Harasimiuk - sekretarz<br />
Jakub Obarowski – przywódca<br />
Marcel Tutak - zastępca<br /><br />

# role
koordynator - Jakub Obarowski, Dorota Harasimiuk<br />
programista - cały zespół<br />
strona graficzna - Dorota Harasimiuk<br />
tester - cały zespół<br />
autor dokumentacji - Dorota Harasimiuk<br />
#FlatWorld
![kraina](https://github.com/obarowskij/AiSD/assets/146991219/70d9dfba-e964-468b-bb6d-59a82b36d572)

# Wystartowanie projektu

## Krok 1.
pobranie paczki requirements
```bash
pip install -r requirements.txt
```

## Krok 2.
Migracje
```bash
python manage.py migrate
```

## Krok 3.
Uruchomienie aplikacji
```bash
python manage.py runserver
```
Serwer uruchomi się domyślnie pod adresem http://127.0.0.1:8000

## Uruchomienie Testów
```bash
pytest
```

# Dokumentacja
| L.p | Specyfikacja problemu (dane i wyniki) | Do jakich treści w zadaniu odnosi się algorytm | Zastosowane struktury danych | Informacje o zastosowanym algorytmie | Osoba realizująca |
| --- | -------------------------------------- | --------------------------------------------- | ---------------------------- | ----------------------------------- | ------------------ |
| 1.  | Dane: zbiór punktów orientacyjnych tworzących obszar Krainy <br /> Wynik: bliczenie otoczki wypukłej Krainy | Zdefiniowanie obszaru w którym żyją płaszczaki na Stronie | stos, klasa, listy | Algorytm Grahama - wpierw losujemy punkty obserwacyjne i sortujemy je biegunowo. Później wkładamy je na stos i mamy gotową wypukłą otoczkę, którą zwizualiujemy biblioteką matplotlib | Harasimiuk |
| 2.  | Dane: Tragarze przedstawieni jako punkty w przestrzeni, gdzie każdy tragarz reprezentowany jest przez dwa punkty (np. jeden punkt to położenie tragarza, a drugi to położenie jego rąk, przy założeniu pewnej ustalonej odległości między nimi)<br /> Wynik: Lista tragarzy, którzy mogą współpracować ze sobą przy transporcie odcinków z fabryki | Dobranie tragarzy do transportu odcinków z fabryki | listy? | Geometria obliczeniowa na płaszczyźnie | Harasimiuk |
| 3.  | Dane: Otoczka wypukła Krainy oraz lista tragarzy gotowych do współpracy<br /> Wynik: Minimalny czas potrzebny do zbudowania płotu wokół Krainy | Zbudowanie płotu wokół Krainy | kolejka, klasa | Mając otoczkę grahama przedstawiamy to jako sieć przepływową i aby znaleźć, ile razy płaszczaki muszą się zbierać do budowy płotu, możemy użyć algorytmu Forda-Fulkersona, aby znaleźć maksymalny przepływ z punktu źródłowego (gdzie zaczynają się prace budowlane) do punktu ujściowego (gdzie prace się kończą), uwzględniając ograniczenia przepustowości na krawędziach. Ostatecznie, maksymalny przepływ w tej sieci przepływowej będzie reprezentować maksymalną liczbę tragarzy, które mogą być przenoszone od fabryki do miejsca budowy płotu, co pośrednio może odzwierciedlać, ile razy płaszczaki muszą się zbierać, aby zbudować płot. | Obarowski |
| 4.  | Dane: Ciąg znaków reprezentujący zmienioną melodię (opowieść-melodia) oraz ciąg znaków zawierający zmienioną wersję melodi, gdzie jedna litera została zastąpiona przez inną (koszmarna-melodia)<br /> Wynik: Oryginalna melodia | Znalezienie oryginalnej melodii | Lista | Algorytm Rabina-Karpa, Algorytm KMP | Obarowski |
| 5.  | Dane: Ciąg znaków a1a2...an reprezentujący opowieść-melodię<br /> Wynik: Ustalenie kodowania dla ciągu znaków, umożliwiającego kompresję danych | Problem niewystarczającej ilości pamięci na komputerze informatyka płaszczaka | słowniki | Huffman - polega na analizie częstotliwości występowania liter w zdaniu i na tej podstawie przypisywaniu skróconych kodów dla symboli | Obarowski |
| 7.  | Dane: Lista strażników <br /> Wynik: Harmonogram pracy strażników ustawiany według minimalnej liczby odsłuchań melodii w trakcie pracy | Potrzeba ochrony płotu | ----------- | ----------- | Tutak |

# Harmonogram realizacji
![Bez tytułu](https://github.com/obarowskij/AiSD2/assets/146991219/c3907114-ce10-45a8-899f-a0694477bbb2)

# Ogólny opis
Nasz projekt Flatworld to historia - zasiadasz, odpalasz aplikację webową i stopniowo tworzysz świat, w którym żyją płaszczaki.
## Algorytmy
todo
# Algorytm Grahama
todo
# Algorytm KMP
todo
# Algorytm Huffmana
todo
# Algorytm Dijkstra
todo
# Algorytm RMQ
todo 
POPRAWNOSC FORMALNA TO TRZEBA DAC OPISY NP CZEMU PETLE SIE KONCZA EWENTUALNIE JAKI JEST NIEZMIENNIK

# Wykorzystane technologie
Python, Django, JS




