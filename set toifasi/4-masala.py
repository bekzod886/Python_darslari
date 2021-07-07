matem = ["Ibrohim","Ali","Vali"]
fizika = ["Ali","Saman","Vali"]
informatika = ["Ali","Saman"]
matem = set(matem)
fizika = set(fizika)
informatika = set(informatika)
alim = matem.union(fizika).union(informatika)
print(alim)
