retezec = "abcdefg"
# Funkce len() vrátí počet znaků v řetězci.
print(len(retezec))
# Vytiskne prázdný řádek
print()
# Vytiskne celý řetězec
print(retezec[:])
# Vytiskne celý řetězec (krok 1 znamená každý znak)
print(retezec[::1])
# Vytiskne znaky od začátku po index 5 (index 6 už ne)
print(retezec[:6])
# Vytiskne znaky od začátku po index 6 (index 7 už ne)
print(retezec[:7])
print()
# Vytiskne každý druhý znak z řetězce (od začátku)
print(retezec[::2])
# Vytiskne celý řetězec pozpátku
print(retezec[::-1])
# Vytiskne každý druhý znak pozpátku
print(retezec[::-2])
# Vytiskne znaky od indexu 1 do 6 (index 7 už ne)
print(retezec[1:7])
print()
# Vytiskne znak na pozici 0
print(retezec[0])
# Vytiskne znak na pozici 1
print(retezec[1])
# Vytiskne znak na pozici 6
print(retezec[6])
# Vytiskne znaky od indexu 3 do 6 po dvou (index 7 už ne)
print(retezec[3:7:2])

# Vytiskne prázdný řádek
print()

# Převod znaku na ASCII a zpět:
print(ord("a"))
print(chr(97))

