import area
import os
if __name__ == '__main__':
    opcao = input(
        'digite 1 para circulo, 2 para quadrado, 3 para triangulo:  ')

    if opcao == '1':
        circ_ = input('digite o raio do circulo em cm:  ')
        area_circulo = area.circulo(float(circ_))
        print(f'a area do circulo é {area_circulo} cm quadrados')
    elif opcao == '2':
        lado_quadrado = input('Digite o lado do quadrado em cm:  ')
        area_quadrado = area.quadrado(float(lado_quadrado))
        print(f'A area do quadrado é {area_quadrado} cm quadrados')
    elif opcao == '3':
        base_triangulo = float(input('digite a base do triangulo em cm:  '))
        altura_triangulo = float(
            input('digite a altura do triangulo em cm :  '))
        area_triangulo = area.triangulo(base_triangulo, altura_triangulo)
        print(f'a area do triangulo é {area_triangulo}  cm quadrados ')
    else:
        print('vc nao digitou nenhuma opção correta')
os.system('PAUSE')
