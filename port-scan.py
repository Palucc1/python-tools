# Importando módulo 'socket'
import socket;

print("\n#### INICIANDO O PORT SCAN #### \n");
print("## Script por Guilherme Palucci, RM: 94365 ## \n");

saida = "";

while saida != "x":
    # Solicita ao usuário o IP ou domínio do servidor a ser escaneado
    host = input("Qual o domínio ou ip do servidor? ");

    # Inicia variáveis com os valores a serem utilizados no laço e inicializa o socket,
    #foi necessário adicionar no range da porta 0 à porta 1024, para que o scan teste a porta 1023.
    rangePortas = range(0,1024);
    obj_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM);

    # Cria o laço de repetição para testar o range de portas conhecidas (well known ports);
    try:
        for numeroPorta in rangePortas:
            # Verifica status da porta a ser testada
            statusPorta = obj_socket.connect_ex((host, numeroPorta));

            # No caso da porta estar aberta, o retorno da função acima é '0' e a condicional abaixo trata
            #o status e exibe, através da função 'print()', a porta e o status 
            if statusPorta == 0:
                print("Porta", numeroPorta, "está aberta.");
            else:
                print("Porta", numeroPorta, "está fechada.");

    # Caso o endereço inserido seja inválido ou esteja indisponível, notifica o usuário
    except:
        print("\nEndereço IP/domínio inválido ou indisponível. \n");

    # Após o uso, é necessário fechar o soquete para próximos usos
    obj_socket.close();

    saida = input("Digite qualquer tecla para continuar, ou x para sair: \n");