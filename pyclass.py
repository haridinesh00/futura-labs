class Library:
    def __init__(self, fiction, nonfiction):
        self.fiction = fiction
        self.nonfiction = nonfiction
    def display(self):
        print(self.fiction)
        print(self.nonfiction)
class Lender(Library):
    def __init__(self, id, name, fiction, nonfiction):
        self.id = id
        self.name = name
        Library.__init__(fiction, nonfiction)
a = Lender