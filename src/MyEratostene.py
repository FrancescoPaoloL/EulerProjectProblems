kLimit = 100000

lstNr = list(range(2, kLimit + 1))
lstSz = len(lstNr)
lstPN = []

for d in range(2, lstNr[-1]):
    for x in range(0, lstSz):
        if (x > 1) and (lstNr[x] != d):
            if lstNr[x] % d == 0:
                lstNr[x] = 0

lstPN = [x for x in lstNr if x != 0]

print(len(lstPN))
