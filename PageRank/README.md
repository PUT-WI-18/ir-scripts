#### Polish only
sorry little, blue sparrow :c

## Uruchomienie
`$ python maciez_stochatyczna.py`

## Korzystanie z programu
Czytajcie instrukacje, a będzie gituwa :>

W razie wątpliwości- DM me

## Obecna funkcjonalność

- możliwość wyboru wprowadzania danych
  - maiceż przepływów
  - macież stochastyczna
  - podawanie poszczególnych połączen wierzchołków
- generowanie układu równań liniowych
- obliczanie wartości PageRank iteracyjnie

## Co trzeba dodać
- [ ] uwzględnienie damping factor

## Info z WiPI-hintsMK+IM.pdf
### PageRank - dla określonego grafu sieci (rozmiar 3-5 stron/wierzchołków):
- zapisz macierz stochastyczną (uwaga na kolejność wierszy i kolumn (najłatwiej wypełniać kolumnami) oraz wpisywane liczby (0 lub 1/n, gdzie n jest liczbą linków wychodzących od strony z kolumny; oznacz wiersze i kolumny, jeśli kolejność nie jest narzucona z góry; strona może linkować do samej siebie));
- zapisać równania pozwalające na obliczenie wartości PageRank w wersji 
  - z narzuconym damping factor q (np. 0.2 lub 0.15) lub 
  - bez jego uwzględnienia (w tym drugim przypadku pamiętaj wtedy o równaniu normalizującym sumę wartości PageRank wszystkich stron);
- rozwiąż prosty układ równań metodą przez podstawianie (uzasadnij, dlaczego PageRank określonej strony jest dobry/słaby);
- bez obliczania dokładnych wartości PageRank uzasadnij na podstawie struktury połączeń, które strony mają najwyższy lub najniższy PageRank;
- inne zagadnienia: interpretacja PageRank (prawdopodobieństwa, zasady kierujące rozdziałem i agregacją PageRank); sposoby obliczania; wskazanie/rozpoznanie dead end lub spider trap; farma linków - sposób manipulacji i sposoby przeciwdziałania.