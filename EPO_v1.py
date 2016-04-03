import time
import array
from collections import deque
import plotly 
import plotly.graph_objs as go

tab_m, tab_s, tab_d = ([] for i in range(3))
def tablice(ilosc=1,iteracje='plik'):
	print("----------------- TABLICE -----------------")
	print("ILOŚĆ ITERACJI - {0}".format(iteracje))
	start_time = time.time()
	if iteracje=='plik':
		array_1=array.array('l',[])
		with open('baza.txt','r') as f:
			for line in f:
				array_1.append(line.strip())
	else:
		array_1=array.array('d',[x*ilosc for x in range(1,iteracje)])
	array_1.append(5*ilosc)
	array_1.insert(1,5*ilosc)
	array_1.remove(3*ilosc)
	1*ilosc in array_1
	elapsed_time = time.time() - start_time
	print("{0} Iteracji, Liczby x{1} Czas wykonania: {2}".format(iteracje,ilosc, elapsed_time))
	del array_1
	return elapsed_time

def listy(ilosc=1,iteracje='plik'):
	print("------------------ LISTY ------------------")
	print("ILOŚĆ ITERACJI - {0}".format(iteracje))
	start_time = time.time()
	if iteracje=='plik':
		list_1=[]
		with open('baza.txt','r') as f:
			for line in f:
				list_1.append(float(line.strip()))
	else:
		list_1=[x*ilosc for x in range(1,iteracje)]
	list_1.append(5*ilosc)
	list_1.insert(1,5*ilosc)
	list_1.remove(3*ilosc)
	3*ilosc in list_1
	elapsed_time = time.time() - start_time
	print("{0} Iteracji, Liczby x{1} Czas wykonania: {2}".format(iteracje,ilosc, elapsed_time))
	del list_1
	return elapsed_time
def stos(ilosc=1,iteracje='plik'):
	print("------------------ STOS -------------------")
	print("ILOŚĆ ITERACJI - {0}".format(iteracje))
	start_time = time.time()
	if iteracje=='plik':
		stack_1=[]
		with open('baza.txt','r') as f:
			for line in f:
				stack_1.append(float(line.strip()))
	else:
		stack_1=[x*ilosc for x in range(1,iteracje)]
	stack_1.append(5*ilosc)
	stack_1.pop()
	elapsed_time = time.time() - start_time
	print("{0} Iteracji, Liczby x{1} Czas wykonania: {2}".format(iteracje,ilosc, elapsed_time))
	del stack_1
	return elapsed_time

def kolejka(ilosc=1,iteracje='plik'):
	print("------------------ KOLEJKA ------------------")
	print("ILOŚĆ ITERACJI - {0}".format(iteracje))
	start_time = time.time()
	if iteracje=='plik':
		queue_1=deque([])
		with open('baza.txt','r') as f:
			for line in f:
				queue_1.append(float(line.strip()))
	else:
		queue_1=deque([x*ilosc for x in range(1,iteracje)])
	queue_1.append(5*ilosc)
	queue_1.popleft()
	elapsed_time = time.time() - start_time
	print("{0} Iteracji, Liczby x{1} Czas wykonania: {2}".format(iteracje,ilosc, elapsed_time))
	del queue_1
	return elapsed_time

def plotowanie(nazwapliku):
	trace1 = go.Bar(x=['10000 wykonań', '10000000 wykonań', '30000000 wykonań'],y=tab_m, name='Małe liczby 1-10000')
	trace2 = go.Bar(x=['10000 wykonań', '10000000 wykonań', '30000000 wykonań'],y=tab_s, name='Średnie liczby 10000-100000000')
	trace3 = go.Bar(x=['10000 wykonań', '10000000 wykonań', '30000000 wykonań'],y=tab_d, name='Duże liczby 10000000-100000000000')
	data = [trace1, trace2, trace3]
	layout = go.Layout(
		barmode='group',
		yaxis=dict(
        title='Czas[s]',
        titlefont=dict(family='Courier New, monospace', size=18, color='#7f7f7f')
        	  	  ),
		xaxis=dict(
    	title='Iteracje',
    	titlefont=dict(family='Courier New, monospace', size=18, color='#7f7f7f')
       		 	  )
					 )
	fig = go.Figure(data=data, layout=layout)
	plot_url = plotly.offline.plot(fig, filename=nazwapliku + '.html')

print("""
EPO labolatorium nr. I. Program działa na tablicach, listach, kolejce oraz stosie oraz wykonuje operacje takie jak:
- dodawanie
- usuwanie
- wyszukanie elementu (zwraca True jeśli znajdzie)
- oblicza czas wykonanych operacji

Dla zdefinowanych wcześniej wartości:

Małe liczby    (1,10000)
Średnie liczby (10000,100000000)
Duże liczby    (10000000,100000000000)

Ilość iteracji 10000,	10000000,	30000000

Lub wczytuje wartość z pliku



Czy wczytać dla zdefiniowanych wcześniej wartości ? T/N
Jeśli wybierzesz opcje inną niż "T' program wczyta wartości z pliku baza.txt dla tablic, list, stosu i kolejki i nie narysuje wykresu otrzymanych wartości
""")
inp=input()
if inp=="T" or "t":
	tab_m.append(tablice(1,1000))
	tab_s.append(tablice(1000,1000))
	tab_d.append(tablice(10000000,1000))
	tab_m.append(tablice(1,10000000))
	tab_s.append(tablice(1000,10000000))
	tab_d.append(tablice(10000000,10000000))
	tab_m.append(tablice(1,30000000))
	tab_s.append(tablice(1000,30000000))
	tab_d.append(tablice(10000000,30000000))
	plotowanie(nazwapliku='Tablice')
	del tab_m, tab_s, tab_d
	tab_m, tab_s, tab_d = ([] for i in range(3))
	# tab_m.append(listy(1,1000))
	# tab_s.append(listy(1000,1000))
	# tab_d.append(listy(10000000,1000))
	# tab_m.append(listy(1,10000000))
	# tab_s.append(listy(1000,10000000))
	# tab_d.append(listy(10000000,10000000))
	# tab_m.append(listy(1,30000000))
	# tab_s.append(listy(1000,30000000))
	# tab_d.append(listy(10000000,30000000))
	# plotowanie(nazwapliku='Lista1')
	# del tab_m, tab_s, tab_d
	# tab_m, tab_s, tab_d = ([] for i in range(3))
	# tab_m.append(stos(1,1000))
	# tab_s.append(stos(1000,1000))
	# tab_d.append(stos(10000000,1000))
	# tab_m.append(stos(1,10000000))
	# tab_s.append(stos(1000,10000000))
	# tab_d.append(stos(10000000,10000000))
	# tab_m.append(stos(1,30000000))
	# tab_s.append(stos(1000,30000000))
	# tab_d.append(stos(10000000,30000000))
	# plotowanie(nazwapliku='Stos')
	del tab_m, tab_s, tab_d
	tab_m, tab_s, tab_d = ([] for i in range(3))
	# tab_m.append(kolejka(1,1000))
	# tab_s.append(kolejka(1000,1000))
	# tab_d.append(kolejka(10000000,1000))
	# tab_m.append(kolejka(1,10000000))
	# tab_s.append(kolejka(1000,10000000))
	# tab_d.append(kolejka(10000000,10000000))
	# tab_m.append(kolejka(1,30000000))
	# tab_s.append(kolejka(1000,30000000))
	# tab_d.append(kolejka(10000000,30000000))
	# plotowanie(nazwapliku='Kolejka')
	# del tab_m, tab_s, tab_d
else:
	tablice()
	listy()
	stos()
	kolejka()

