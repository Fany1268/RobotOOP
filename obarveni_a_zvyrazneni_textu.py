# Červený text – příklad
print("\033[31m" + "Toto je červený text" + "\033[0m")
# \033[31m – začátek červené barvy
# \033[0m – reset (konec barvy, aby dál nebyl barevný text)

print("\033[1m" + "Toto je tučný text" + "\033[0m")

print("\033[4m" + "Toto je podtržený text" + "\033[0m")

"""
změna pozadí i barvy textu probíhá pomocí tzv. ANSI escape kódů, kde:
31 = barva textu (červená)
43 = barva pozadí (žlutá)
"""
print("\033[31;43m" + "Červený text na žlutém pozadí" + "\033[0m")
print("\033[30;46m" + "Červený text na žlutém pozadí" + "\033[0m")
"""
🎨 Přehled barev pro text i pozadí:
Barva	Text (foreground)	Pozadí (background)
Černá	30	                40
Červená	31	                41
Zelená	32	                42
Žlutá	33	                43
Modrá	34	                44
Fialová	35	                45
Tyrkysová 36	            46
Bílá	37	                47
"""




# Univerzální funkce pro obarvení textu
def obarvi_text(text, barva="cervena"):
    barvy = {
        "cervena": "\033[31m",
        "zelena": "\033[32m",
        "zluta": "\033[33m",
        "modra": "\033[34m",
        "fialova": "\033[35m",
        "tyrkysova": "\033[36m",
        "bila": "\033[37m",
        "reset": "\033[0m"
    }
    barva_kod = barvy.get(barva.lower(), barvy["reset"])
    return f"{barva_kod}{text}{barvy['reset']}"

print(obarvi_text("\nAhoj, tohle je červený text!\n"))
print(obarvi_text(12345, "fialova"))



# Univerzální funkce pro zvíraznění textu
def zvyrazni_text(text, styl="bold"):
    styly = {
        "bold": "\033[1m",
        "underline": "\033[4m",
        "reverse": "\033[7m",  # pozadí a barva se prohodí
        "red_on_yellow": "\033[31;43m",
        "reset": "\033[0m"
    }
    kod = styly.get(styl, styly["reset"])
    return f"{kod}{text}{styly['reset']}"

print(zvyrazni_text("Toto je tučně", "bold"))
print(zvyrazni_text("Toto je podtrženo", "underline"))
print(zvyrazni_text("Varování!", "red_on_yellow"))


# Příklad převodu do proměné a vypisu Fstringem v Pythonu
symbol = "a"
ascii_hodnota = ord(symbol)
print(f"ASCII hodnota znaku '{symbol}' je: {ascii_hodnota}")

# Příklady práce s barevným výstupem v Pythonu pomocí ANSI escape kódů
print(f"\033[31m ASCII hodnota znaku {symbol} je: {ascii_hodnota} \033[0m")

#vysvětlení
print(f"    \033[31m    Toto je   {symbol}   červený text    \033[0m    ")
"""
📌 Vysvětlení:
\033[31m = začátek červené barvy (ANSI escape sekvence),

\033[0m = reset barvy zpět na výchozí,

f"..." = formátovaný řetězec, do kterého vkládáš proměnné.
"""
