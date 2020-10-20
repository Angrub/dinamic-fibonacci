from bokeh.plotting import figure, output_file, show

def fibonacci_dinamico(n, pasos, memo = {}):
    pasos[0] += 1
    if n == 0 or n == 1:
        return 1

    try:
        return memo[n]

    except KeyError:
        resultado = fibonacci_dinamico(n - 1, pasos, memo) + fibonacci_dinamico(n - 2, pasos, memo)
        memo[n] = resultado
        #print(f'n: {n}, resultado: {resultado}, memo: {memo}')
        return resultado

def graficado_de_fibonacci():
    output_file('graficado_simple.html')
    fig = figure()

    total_vals = int(input('¿Cuántos números de fibonacci va a calcular?'))
    lista_vals = list(range(total_vals))
    
    x_vals = []
    y_vals = []
    pasos = [0]
    

    for i in lista_vals:
        valor = int(input(f'Ingrese n fibonacci a calcular: '))
        x_vals.append(valor)

    for fib in x_vals:
        pasos[0] = 0
        #print(pasos[0])
        fibonacci_dinamico(fib, pasos, memo = {})
        #print(pasos[0])
        y_vals.append(pasos[0])
        #print(f'{fib} -- {y_vals}')
        

    fig.line(x_vals, y_vals, line_width=2)
    show(fig)

if __name__ == '__main__':
    
    graficado_de_fibonacci()