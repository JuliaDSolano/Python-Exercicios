#!/bin/env python3
# coding: utf-8

# Marco André <marcoandre@gmail.com>
# Exercícios de revisão P1


def calcula_aumento_salario1(salario):
    """Calcula aumento do salário. """

    if salario <= 280:
        percentual_aumento = 20
        aumento = salario / 100*20
        novo_salario = salario + aumento

        return salario, percentual_aumento, aumento, novo_salario

    elif salario <= 700:
        percentual_aumento = 15
        aumento = salario / 100*15
        novo_salario = salario + aumento
        return salario, percentual_aumento, aumento, novo_salario

    elif salario <= 1500:
        percentual_aumento = 10
        aumento = salario / 100*10
        novo_salario = salario + aumento

        return salario, percentual_aumento, aumento, novo_salario

    elif salario > 1500:
        percentual_aumento = 5
        aumento = salario / 100*5
        novo_salario = salario + aumento

        return salario, percentual_aumento, aumento, novo_salario

def calcula_idade(ano_nascimento, ano_atual):
    """Calcula idade."""

    return ano_atual - ano_nascimento


def calcula_media(prova, trabalho, exercicio):
    """ Calcula media:
    Prova com peso 7
    Trabalho com peso 2
    Exercício com peso 1
    """
    return (prova*0.7)+(trabalho*0.2)+ (exercicio * 0.1)


def calcula_idade_canina(idade_humana, porte_do_cao):
    '''Calcule sua idade canina:
    - cães de porte pequeno: dividir sua idade por 5
    - cães de porte médio: dividir sua idade por 6
    - cães grandes: dividir sua idade por 7'''

    if porte_do_cao == 'pequeno':
        return int(idade_humana/5)

    elif porte_do_cao == 'medio':
        return int(idade_humana/6)

    elif porte_do_cao == 'grande':
        return int(idade_humana/7)


def calcula_aumento_salario(salario_atual):
    ''' Calcule o aumento de salário de acordo com a seguinte tabela:
    - até 1 SM(inclusive): aumento de 20%
    - de 1 até 2 SM(inclusive): aumento de 15%
    - de 2 até 5 SM(inclusive): aumento de 10%
    - acima de 5 SM: aumento de 5%
    Salário mínimo para referência: R$ 724,00
    '''

    if salario_atual <= 724:
        aumento = (salario_atual / 100)*20
        novo_salario = salario_atual + aumento

        return novo_salario

    elif salario_atual > 724 and salario_atual<= 1448:
        aumento = (salario_atual / 100) * 15
        novo_salario = salario_atual + aumento

        return novo_salario

    elif salario_atual > 1448 and salario_atual <= 3620:
        aumento = (salario_atual / 100) * 10
        novo_salario = salario_atual + aumento

        return novo_salario

    elif salario_atual > 3620:
        aumento = (salario_atual / 100) * 5
        novo_salario = salario_atual + aumento

        return novo_salario



# Área de testes: só mexa aqui se souber o que está fazendo!
acertos = 0
total = 0


def test(obtido, esperado):
    global acertos, total
    total += 1
    if obtido != esperado:
        prefixo = '\033[31m%s' % 'Falhou'
    else:
        prefixo = '\033[32m%s' % 'Passou'
        acertos += 1
    print('%s Esperado: %s \tObtido: %s\033[1;m' % (prefixo, repr(esperado),
                                                    repr(obtido)))


def main():
    print('Calcula aumento salário:')
    test(calcula_aumento_salario1(100), (100, 20, 20.0, 120.0))
    test(calcula_aumento_salario1(1500), (1500, 10, 150.0, 1650.0))
    test(calcula_aumento_salario1(3000), (3000, 5, 150.0, 3150.0))

    print('Calcula idade:')
    test(calcula_idade(1973, 2015), 42)
    test(calcula_idade(2000, 2015), 15)
    test(calcula_idade(2015, 2015), 0)

    print('Idade canina:')
    test(calcula_idade_canina(40, 'pequeno'), 8)
    test(calcula_idade_canina(40, 'medio'), 6)
    test(calcula_idade_canina(40, 'grande'), 5)

    print('Calcula média:')
    test(calcula_media(10, 10, 10), 10)
    test(calcula_media(7, 7, 7), 7)
    test(calcula_media(5, 8, 10), 6.1)

    print('Aumento salarial:')
    # até 1 SM: 20%
    test(calcula_aumento_salario(500.00), 600.00)
    test(calcula_aumento_salario(724.00), 868.80)
    # 1-2 SM: 15%
    test(calcula_aumento_salario(725.00), 833.75)
    test(calcula_aumento_salario(1448.00), 1665.20)
    # 2-5 SM: 10%
    test(calcula_aumento_salario(1449.00), 1593.90)
    test(calcula_aumento_salario(3620.00), 3982.00)
    # >5 SM: 5%
    test(calcula_aumento_salario(3621.00), 3802.05)
    test(calcula_aumento_salario(4000.00), 4200.00)


if __name__ == '__main__':
    main()
    print("\n%d Testes, %d Ok, %d Falhas: Nota %.1f" % (total, acertos,
                                                        total - acertos, float(acertos * 10) / total))
    if total == acertos:
        print("Parabéns, seu programa rodou sem falhas!")