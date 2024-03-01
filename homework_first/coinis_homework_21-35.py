import math
from datetime import datetime

# task_21
# Otkrili ste algoritam kojim možete doći do šifre koja otvara sef. U sefu se nalazi knjiga
# koja krije tajne o nastanku univerzuma. Šifra se dobija kada se od kvadrata zbira prve i
# poslednje cifre četvorocifrenog broja oduzme razlika kvadrata druge i trece cifre.


# def task_21(number):

#     first = int(number[0])
#     second = int(number[1])
#     third = int(number[2])
#     fourth = int(number[3])

#     summ = pow((first + fourth), 2)
#     devide_sqr = pow(second, 2) - pow(third, 2)

#     result = summ - devide_sqr

#     print(f"Result = {result}")


# task_21(input("Enter 4 digit num "))


# ----------------------------------------------------------------

# task_22
# 22. Na takmičenju iz matematike učestvovalo je N učenika. Izveštaj o broju poena
# odštampan je na dvije strane. Nastavnik greškom nije ponio prvu stranu izveštaja, ali se
# sjeća da je na dnu strane pisalo da je prosječan broj poena za tu stranu bio p1. Na
# drugoj strani (koju ima kod sebe) su podaci o K učenika i prosječan broj poena za tu
# stranu je p2. Napisati program kojim se određuje koliki je prosječan broj poena svih
# učenika.
# Ulaz: Na standardnom ulazu nalaze se
# • u prvoj liniji prirodan broj N ukupna broj učenika
# • u drugoj liniji prirodan broj K broj učenika na drugoj strani
# • u trećoj liniji realan broj p1 prosječan broj poena učenika na prvoj strani
# • u četvrtoj liniji realan broj p2 prosječan broj poena učenika na drugoj strani
# Izlaz: Na standarnom izlazu prikazati, na dvije decimale, prosječan broj bodova svih
# učenika.
# Primjer
# Ulaz: 80, 30, 78.20, 89.30
# Izlaz: 82.36


# def task_22(n, k2, p1, p2):

#     k1 = n - k2

#     summ_points_p1 = p1 * k1
#     summ_points_p2 = p2 * k2

#     result = (summ_points_p1 + summ_points_p2) / n
#     print(round(result, 2))


# task_22(
#     int(input("Enter N: ")),
#     int(input("Enter K2: ")),
#     float(input("Enter p1: ")),
#     float(input("Enter p2: ")),
# )

# ----------------------------------------------------------------
# task_ 23

# Napisati program koji za unijete parametre a i b vraća srednju vrijednost.
# Npr. ako je a = 2, b = 3, rezultat funkcije treba da bude 2.5. Ako je a = -2, b = 4,
# rezultat treba da bude 1. Ako je a = -4, b = 2, rezultat treba da bude - 1.

# def task_23(a,b):

#     result = (a + b) /2

#     print(result)

# task_23(int(input('Enter number a: ')),int(input('Enter number b: ')))


# ----------------------------------------------------------------
# task_24

# 24.Za Milicu i Anu se čuva koliko puta su obišle teren u 40 minuta. Međutim,
# prilikom unosa podataka desila se zabuna, pa je u varijabli x sačuvana vrijednost
# koja je trebala biti sačuvana u varijabli y i obrnuto. Napisati kod koji mijenja
# mjesta vrijednostima u promjenljivim x i y. Npr. ako je x = 7 i y = 10, poslije
# izvršavanja koda treba da bude x=10 i y=7.

# def task_24(x,y):

#      time_var = y
#      y = x
#      x = time_var

#      print(f' x = {x} ,y = {y}')

# task_24(int(input('Enter number x: ')),int(input('Enter number y: ')))

# ----------------------------------------------------------------

# task_25
# Dato je rastojanje u centimetrima između ulaza u dvije različite kancelarije.
# Odrediti koliko cijelih metara ima u tom rastojanju. Npr. 324cm imaju 3 metra.

# def task_25(cm):
#     result = cm / 100

#     print(f'Result : {int(result)} m')

# task_25(int(input('Enter cm : ')))

# ----------------------------------------------------------------
# task26
# Dat je četvorocifreni prirodan broj koji predstavlja broj stambene jedinice u
# zgradi. Na osnovu zadatog broja potrebno je odrediti sprat na kome se nalazi
# stambena jedinica. Poznato je da se to može otkriti iz pretposlednje cifre zadatog
# broja.


# def task_26(num):

#     floor = int(num[2])

#     print(f"Floor : {floor}")


# task_26(input("Enter 4 digit num : "))

# ----------------------------------------------------------------
# task27
# Dat je četvorocifreni prirodan broj. Napisati kod koji štampa kvadrat zbira cifara
# tog broja.

# def task_27(num):

#     first = int(num[0])
#     second = int(num[1])
#     third = int(num[2])
#     fourth = int(num[3])

#     sum = first + second + third + fourth

#     sqr = pow(sum, 2)

#     print(sqr)


# task_27(input("Enter 4 digit num : "))

# ----------------------------------------------------------------
# task28
# Dat je trocifren broj. Odrediti broj koji se dobija zamjenom prve i posljednje cifre.


# def task_28(num):

#     first = num[0]
#     second = num[1]
#     third = num[2]

#     new_var = int(third + second + first)

#     print(f'New var = {new_var}')


# task_28(input("Enter 3 digit num : "))

# ----------------------------------------------------------------
# task29
# Korisnik unosi koordinate dvije tačke (x1, y1) i (x2, y2) koje predstavljaju početne
# tačke dva studenta koji su se dogovorili da se sretnu na lokaciji (x3, y3) koja je
# nalazi tačno na sredini njihovog puta. Program treba da odredi tu lokaciju i
# izračuna rastojanje od početne pozicije do tačke susreta, koristeći Euklidsko
# rastojanje.


# def task_29(x1, y1, x2, y2,):

#     x3 = (x1+x2) / 2
#     y3 = (y1+y2) / 2

#     c= math.sqrt(pow(x3,2) + pow(y3,2))

#     print(f'\nThe coordinates of the meeting : x = {x3}, y = {y3},\nDistance = {c}')

# task_29(
#     int(input("Enter x1: ")),
#     int(input("Enter y1: ")),
#     int(input("Enter x2: ")),
#     int(input("Enter y2: ")),
# )
# ----------------------------------------------------------------
# task30

# Dimenzije pravougaonika su 543 i 130. Koliko kvadrata stranice 65 je moguće
# izrezati iz tog pravougaonika?

# def task_30():
#     width = 130
#     height = 543

#     s= height*width
#     result = int(s /60)

#     print (result)

# task_30()

# ----------------------------------------------------------------
# task31
# Napisati program koji računa površinu ekrana monitora pravougaonog oblika,
# ukoliko je poznata dužina njegove dijagonale (d = 50) i odnos stranica (aspect
# ratio = 16:9).

# def task_31():
#     d = 50
#     a = 16
#     b = 9

#     width = math.sqrt((pow(d, 2) * pow(a, 2)) / (pow(a, 2) + pow(b, 2)))
#     height = (width * b) / a

#     screen_area = width * height

#     print('Screen Area:', screen_area)


# task_31()

# ----------------------------------------------------------------
# task32
# Dat je šestocifreni broj n (n=abcdef). Provjeriti da li važi a* c + 2 + f = b + d*e.
# Pomoć: razmisliti o provjeri uslova (boolean operator) - samostalno isprobati
# implementaciju iste u Python-u. Ovo ćemo svakako raditi tokom naredne
# sedmice.

# def task_32(n):

#     if len(n) == 6:
#              first = int(n[0])
#              second = int(n[1])
#              third = int(n[2])
#              fourth = int(n[3])
#              fifth = int(n[4])
#              sixth = int(n[5])

#              if first * third + 2 + sixth == second + fourth * fifth:
#                print(True)
#              else:
#                 print(False)
#     else:
#         print('wrong number')


# task_32(input('Enter a 6 digit number: '))


# ----------------------------------------------------------------
# task33
# Napisati program koji provjerava koliko se poligona kvadratnog oblika i zadatih
# dimenzija može kreirati na jednoj poljani za koju su poznate njena širina i dužina.

# def task_33(width,height,square):

#     s = height * width
#     result = int(s / square)

#     print(f'Result = {result}')


# task_33(int(input('Enter a Width:')),int(input('Enter a Height:')),int(input('Enter a Square:')))


# ----------------------------------------------------------------
# task34

# Dobili ste zadatak da generišete specijalni identifikacioni broj za pristup tajnom
# laboratorijskom sektoru. Otkrili ste da se identifikacioni broj može dobiti na
# osnovu poznatog šestocifrenog broja tako što se kvadrira suma cifara tog broja,
# a zatim od tog rezultata oduzme proizvod treće i četvrte cifre istog broja. Kao
# rezultat prikazati identifikacioni broj.

# def task_34(n):
#     if len(n) == 6:
#         first = int(n[0])
#         second = int(n[1])
#         third = int(n[2])
#         fourth = int(n[3])
#         fifth = int(n[4])
#         sixth = int(n[5])

#         sum = first + second + third + fourth + fifth + sixth
#         multiplication = third * fourth
#         result = pow(sum, 2) - multiplication
#         print(result)

#     else:
#         print("wrong number")


# task_34(input("Enter a 6 digit number: "))


# ----------------------------------------------------------------
# task35
# Dat je petocifreni prirodan broj koji predstavlja broj stambene jedinice u zgradi.
# Na osnovu zadatog broja potrebno je odrediti sprat na kome se nalazi stambena
# jedinica. Poznato je da se to može otkriti kada se na vrijednost srednje cifre
# zadatog broja doda vrijednost poslednje cifre. Štampati taj zbir.

def task_35(num):
    floor = int(num[2]) + int(num[4])

    print(f"Floor : {floor}")

task_35(input('Enter 5 digit number: '))