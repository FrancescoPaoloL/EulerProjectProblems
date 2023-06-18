'''

'''
import time

class Parenthesis():
    open = '('
    close = ')'

print('Start!')
start_time = time.time()

expression = '4 + (5 + (4 / 4) * 7))'

nrOpen = expression.count(Parenthesis.open)
nrClose = expression.count(Parenthesis.close)

if nrOpen != nrClose:
    print(f'We have found {nrOpen} open parenthesis versus {nrClose} closed parenthesis!')
else:
    print('Ok')

print("--- %s seconds ---" % (time.time() - start_time))


''''''''''''
