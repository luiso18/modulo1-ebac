

print("teste de calculadora")
while True:
  num1 = int(input("digite o primeiro numero: "))
  num2 = int(input("digite o segundo numero: "))
  print("digite o tipo de calculo \n+ adição \n- subtração  \n/ divisão  \n* multiplicação")
  calculo = str(input("escolha: "))

  if calculo == "+":
   print(num1 + num2)
  if calculo == "-":
   print(num1 - num2)
  if calculo == "/":
   print(num1 / num2)
  if calculo == "*":
    (print(num1 * num2))
  print("continuar?")
  continuar = str(input("s/n: "))
  if continuar == "s":
    continue

  else :
    print("invalido")


else :
  print("invalido")

