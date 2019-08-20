'''043: Desenvolva uma lógica que leia o peso e a altura de uma pessoa,
 calcule seu Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:

- IMC abaixo de 18,5: Abaixo do Peso
- Entre 18,5 e 25: Peso Ideal
- 25 até 30: Sobrepeso
- 30 até 40: Obesidade
- Acima de 40: Obesidade Mórbida'''

altura = float(input('Digite sua Altura: (Metros) '))
peso = float(input('Digite seu peso: (KG) '))
imc = peso / (altura*altura)
if imc < 18.5:
    print('Seu IMC é {:.2f}, Abaixo do Peso'.format(imc))
elif imc >18.5 and imc < 25:
    print('Seu IMC é {:.2f}, Peso Ideal'.format(imc))
elif imc > 25 and imc < 30:
    print('Seu IMC é {:.2f}, Sobrepeso'.format(imc))
elif imc > 30and imc < 40:
    print('Seu IMC é {:.2f}, Obesidade!'.format(imc))
elif imc > 40:
    print('Seu IMC é {:.2f}, Obesidade Mórbida!'.format(imc))
