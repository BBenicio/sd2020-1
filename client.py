import rpyc
conn = rpyc.connect("localhost", 12345)

running = True
while running:
    print("-- Deseja realizar qual operação? 1: Cadastrar nota, 2: Consultar Nota, 3: Consultar Todas as Notas, 4: Consultar CR, 0: Sair --")
    op = int(input("Operacao: "))
    if op == 0:
        running = False
    elif op == 1:
        print("Insira a matricula, codigo da disciplina e nota")
        matricula = input("Matricula: ")
        cod_disc = input("Codigo da Disciplina: ")
        nota = input("Nota: ")
        print(conn.root.cadastrar_nota(matricula, cod_disc, nota))
    elif op == 2:
        print("Insira a matricula e codigo da disciplina")
        matricula = input("Matricula: ")
        cod_disc = input("Codigo da Disciplina: ")
        print(conn.root.consultar_nota(matricula, cod_disc))
    elif op == 3:
        print("Insira a matricula")
        matricula = input("Matricula: ")
        print(conn.root.consultar_notas(matricula))
    elif op == 4:
        print("Insira a matricula")
        matricula = input("Matricula: ")
        print(conn.root.consultar_cr(matricula))
    else:
        print("Operacao Invalida")
    #
#
