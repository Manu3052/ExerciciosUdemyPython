arquivo = open("Arquivo do usuário.txt","a")
arquivo.write(input("\nAdicione o texto"))
arquivo = open("Arquivo do usuário.txt","r")
ler_arquivo = arquivo.readline()
print(ler_arquivo)