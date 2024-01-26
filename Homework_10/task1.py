class Soda:
    def __init__(self, flavor=None):
        self.flavor = flavor

    def __str__(self):
        if self.flavor:
            return f"У вас газировка со вкусом '{self.flavor}'"
        else:
            return "У вас обычная газировка"

if __name__=="__main__":
    soda1 = Soda("Клубника")
    print(soda1)

    soda2 = Soda()
    print(soda2)
