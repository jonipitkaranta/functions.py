import random


def lotto():
    """Yksinkertainen lottopeli
    
       Numerot arvotaan tyhjään listaan

       Arvotaan satunnaiset numerot ja tarkistetaan ovatko ne jo arvottu

       Satunnaiset numerot appendataan tyhjään listaan ja sortataan pienimmästä suurimpaan
    """
    lottonumerot = []
    for i in range(0, 6):
        number = random.randint(1, 40)
        while number in lottonumerot:
            number = random.randint(1, 40)

        lottonumerot.append(number)

    lottonumerot.sort()

    print('>>> Lottonumerot ovat <<<')
    print(lottonumerot)


lotto()
print(lotto.__doc__)
