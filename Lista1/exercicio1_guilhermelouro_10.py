cigarros = int(input('Quantos cigarros você fuma por dia: '))
    anos = int(input('\nPor quantos anos você fuma: '))
    minutosPerdidos = (cigarros * 10) * anos
    diasPerdidos = minutosPerdidos / 1440 # 1440 é a quantidade de minutos que 1 dia tem
    print('\nVocê perdeu {} dias da sua vida fumando'.format(round(diasPerdidos, 2))) # round, 2 é para arredondar em duas casas decimais
