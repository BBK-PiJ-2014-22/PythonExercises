class Pair:

    def __init__(self, value, pair=None):
        self.value = value
        self.pair = pair

    def link(self, newpair):
        '''Links to pairs together

           OTHER INFORMATION

           '''
        self.pair = newpair
        newpair.pair = self
        #Asigns pair to self.pair and vice ersa


    
a = Pair(14)
b = Pair(12)

a.link(b)

print(a.pair.value)

print(
