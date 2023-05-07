convidados = ['Lana Del Rey', 'Jonathan Calleri', 'Jade Picon', 'Neymar Jr', 'Taylor Swift']

for convidado in convidados:
    print(f"Olá {convidado}, você está convidado para o meu jantar em casa!")

print("Infelizmente, Jade Picon não poderá comparecer.")
convidados.remove('Jade Picon')
print("Os seguintes convidados ainda estão confirmados:")
for convidado in convidados:
    print(convidado)

print("Vou convidar Filipe Ret em vez de Jane Picon.")
convidados.append('Filipe Ret')
convidados.remove('Lana Del Rey')
print("Os seguintes convidados ainda estão confirmados:")
for convidado in convidados:
    print(convidado)

for convidado in convidados:
    print(f"Olá {convidado}, você está convidado para o meu jantar em casa! Espero vê-lo lá.")