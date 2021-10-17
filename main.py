'''
Returneaza true daca n este prim si false daca nu.
'''
def is_prime(n):
  if (n > 1):
    for i in range(2, int(n / 2) + 1):
      if (n % i == 0):
        print("Numarul", n, "nu este prim")
        break
    else:
      print("Numarul", n, "este prim")
  else:
    print("Numarul", n, "nu este prim")


'''
Returneaza produsul numerelor din lista lst.
'''
def get_product(lst):
  p = 1
  for x in lst:
    p *= x
  return p


'''
Returneaza CMMDC a doua numere x si y folosind primul algoritm.
'''
def get_cmmdc_v1(x, y):
  if (x < y):
    a = x
    x = y
    y = a
  while (y):
    a = x % y
    x = y
    y = a
  return x



'''
Returneaza CMMDC a doua numere x si y folosind al doilea algoritm.
'''
def get_cmmdc_v2(x, y):
    while (x != y):
      if (x > y):
        x = x - y
      else:
        y = y - x
    return x


def main():
  P=int(input("Selecteaza problema: "))
  if(P==1):
    print("Ai ales problema 1")
    n=int(input("Numarul citit este: "))
    print(is_prime(n))
  elif(P==2):
    print("Ai ales problema 2")
    n=int(input("Numarul de elemente citite este: "))
    lst = []
    print("Numere care se citesc sunt:")
    for i in range (0,n):
      ele = int(input())
      lst.append(ele)
    print("Produsul numerelor din lista este:", get_product(lst))
  elif(P==3):
    print("Ai ales problema 3\nPerechea de elemente citite este")
    x = int(input())
    y = int(input())
    print("Cel mai mare divizor comun ale lui", x, "si", y, "este", get_cmmdc_v1(x, y))
  elif(P==4):
    print("Ai ales problema 4\nPerechea de elemente citite este")
    x = int(input())
    y = int(input())
    print("Cel mai mare divizor comun ale lui", x, "si", y, "este", get_cmmdc_v2(x, y))
if __name__ == '__main__':
  main()
