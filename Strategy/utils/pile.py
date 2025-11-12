class Pile:
    def __init__(self):
        self.elements = []

    def est_vide(self):
        return len(self.elements) == 0

    def empiler(self, item):
        self.elements.append(item)

    def depiler(self):
        if self.est_vide():
            return
        return self.elements.pop()

    def taille(self):
        return len(self.elements)