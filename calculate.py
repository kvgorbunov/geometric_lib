import circle
import square


figs = ['circle', 'square']
funcs = ['perimeter', 'area']
sizes = {}

def calc(fig, func, size):
	'''
	Возвращает значение функции для фигуры с заданными параметрами.


		Параметры:
			fig (str): вид фигуры "circle"/"square";
			func (str): тип функции "perimeter"/"area";
			size (list): список параметров фигуры.


		Возвращаемое значение:
			Функция ничего не возвращает, выводит на экран результат вычислений.


		Пример вызова:
			>> calc('circle', 'perimeter', {5})
			perimeter of circle is 31.41592653589793

	'''
	assert fig in figs
	assert func in funcs

	result = eval(f'{fig}.{func}(*{size})')
	print(f'{func} of {fig} is {result}')

if __name__ == "__main__":
	func = ''
	fig = ''
	size = list()
    
	while fig not in figs:
		fig = input(f"Enter figure name, avaliable are {figs}:\n")
	
	while func not in funcs:
		func = input(f"Enter function name, avaliable are {funcs}:\n")
	
	while len(size) != sizes.get(f"{func}-{fig}", 1):
		size = list(map(int, input("Input figure sizes separated by space, 1 for circle and square\n").split(' ')))
	
	calc(fig, func, size)



