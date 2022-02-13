'''
If the numbers 1 to 5 are written out in words:
    one, two, three, four, five,
then there are
    (one) 3 + (two) 3 + (three) 5 + (four) 4 + (four) 4

19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive
were written out in words, how many letters would be used?

NB: Do not count spaces or hyphens.

For example,

    342 (three hundred and forty-two)

contains 23 letters and

115 (one hundred and fifteen)

    contains 20 letters.

The use of "and" when writing out numbers is in compliance
with British usage.

----
#1.0
one
two
three
four
five
six
seven
eight
nine

#1.1
ten
eleven
twelve

#2
thirteen
fourteen
fifteen
sixteen
seventeen
eighteen
nineteen

#3
twenty (#1.0)
thirty (#1.0)
forty (#1.0)
fifty (#1.0)
sixty (#1.0)
seventy (#1.0)
eighty (#1.0)
ninety (#1.0)

(#1.0) hundred (#2 /#3)


ex 978
    900 + 70 + 8 =  Nine  Hundred  Seventy  Eight
'''

import time

dctNumbers = {
                1: "one",
                2: "two",
                3: "three",
                4: "four",
                5: "five",
                6: "six",
                7: "seven",
                8: "eight",
                9: "nine",
                10: "ten",
                11: "eleven",
                12: "twelve",
                13: "thirteen",
                14: "fourteen",
                15: "fifteen",
                16: "sixteen",
                17: "seventeen",
                18: "eighteen",
                19: "nineteen",
                20: "twenty",
                30: "thirty",
                40: "forty",
                50: "fifty",
                60: "sixty",
                70: "seventy",
                80: "eighty",
                90: "ninety"
}


def translate(number):
    ret = ""
    if number == 0:
        return ret
    kLimit = 4
    sNr = str(number)
    lngSNr = len(sNr)
    if lngSNr > kLimit:
        return f"The number you entered ({number}) must be < 9999!"
    t0 = []
    t0.append(sNr[:1])
    t0.append(sNr[1:len(sNr)])

    if lngSNr == kLimit:
        if int(t0[0]) > 0:
            ret = dctNumbers.get(int(t0[0])) + " thousand "
        ret += translate(int(t0[1]))
    elif lngSNr == kLimit-1:
        if int(t0[0]) > 0:
            ret = dctNumbers.get(int(t0[0])) + " hundred "
            if (int(t0[1])) > 0:
                ret += "and "
        ret += translate(int(t0[1]))
    elif lngSNr == kLimit-2:
        if int(t0[0]) > 0 and int(t0[1]) == 0:
            ret += dctNumbers.get(int(t0[0]+t0[1]))
        if int(t0[1]) > 0:
            if number <= 19 and number >= 10:
                ret = dctNumbers.get(number)
            else:
                ret += dctNumbers.get(int(t0[0]+"0"))
                ret += '-' + translate(int(t0[1]))
    else:
        ret += dctNumbers.get(number)

    return ret


print('Start!')
start_time = time.time()

sum = 0
for i in range(1, 1001):
    s = translate(i)
    print(s)
    sum += len(s) - s.count(' ') - s.count('-')

print(f'For all the numbers from 1 to 1000 inclusive, \
we have used {sum} letters (no spaces / no hypen)')
print("--- %s seconds ---" % (time.time() - start_time))
