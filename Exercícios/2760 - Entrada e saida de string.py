#1- Crie 3 variáveis para armazenar uma frase de no máximo 100 caracteres;
#2- Leia uma frase para a primeira variável;
#3- Leia uma frase para a segunda variável;
#4- Leia uma frase para a terceira variável;
#5- Imprima a primeira variável lida no passo 2, a segunda variável lida no passo 3, a terceira variável lida no passo 4. Não esqueça de pular linha;
#6- Imprima a primeira variável lida no passo 3, a segunda variável lida no passo 4, a terceira variável lida no passo 2. Não esqueça de pular linha;
#7- Imprima a primeira variável lida no passo 4, a segunda variável lida no passo 2, a terceira variável lida no passo 3. Não esqueça de pular linha;
#8- Repita o procedimento 5, imprimindo só 10 caracteres de cada variável.

a = str(input())
b = str(input())
c = str(input())
print(a+b+c+"\n"+b+c+a+"\n"+c+a+b+"\n"+a[0:10] + b[0:10] + c[0:10])