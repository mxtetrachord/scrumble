class Calculator:
    tables = {
        'scrabble': dict(
            blank=2, a=1, b=3, c=3, d=2, e=1, f=4, g=2, h=4,
            i=1, j=7, k=5, l=1, m=3, n=1, o=1, p=3, q=10,
            r=1, s=1, t=1, u=1, v=4, w=4, x=8, y=4, z=10
        ),

        'words_with_friends': dict(
            blank=0, a=1, b=4, c=4, d=2, e=1, f=4, g=3, h=3,
            i=1, j=10, k=5, l=2, m=4, n=2, o=1, p=4, q=10,
            r=1, s=1, t=1, u=2, v=5, w=4, x=8, y=3, z=10
        )
    }
    def __init__(self, variant='scrabble'):
        self.variant = variant

    def calculate(self, word):
        table = self.tables[self.variant]
        return sum([table[letter] for letter in word])
