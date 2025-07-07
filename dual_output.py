# Tato třída umožňuje zapisovat na více míst současně,
# například do konzole i do souboru.

class DualOutput:
    def __init__(self, *outputs):
        self.outputs = outputs  # uloží všechny výstupy (např. konzole, soubor)

    def write(self, text):
        for output in self.outputs:
            output.write(text)  # zapíše text do každého výstupu

    def flush(self):
        for output in self.outputs:
            output.flush()  # zajistí, že se vše skutečně zapíše