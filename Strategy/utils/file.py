class File:
    def __init__(self):
        self.elements = []

    def est_vide(self):
        return len(self.elements) == 0

    def enfiler(self, item):
        self.elements.append(item)

    def defiler(self):
        if self.est_vide():
            return
        return self.elements.pop(0)

    def taille(self):
        return len(self.elements)