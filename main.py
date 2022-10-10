num = int(input("Enter any number / Adj meg egy számot: "))
szam = num%2
if szam == 0:
    print(num, "is an even number /", num, " Páros szám")
elif szam == 1:
    print(num, "is an odd number / " ,num," Páratlan szám")
else:
    print("Error, Invalid input/ Hiba, ez nem szám")