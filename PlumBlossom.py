import re
import zhdate
from datetime import datetime

yin = '___ ___'
yang = '_______'

water = [yin, yang, yin]
mountain = [yang, yin, yin]
mine = [yin, yin, yang]
wind = [yang, yang, yin]
fire = [yang, yin, yang]
land = [yin, yin, yin]
swamp = [yin, yang, yang]
sky = [yang, yang, yang]

veteran = [water, mountain, mine, wind, fire, land, swamp, sky]
congenital = [land, sky, swamp, fire, mine, wind, water, mountain]

"""
起因：The cause of
经过：after that
结果：The result is

manifestation of a divination
"""


def y_clock():
    hor = datetime.today().hour

    if hor >= 23 or hor < 1:
        return 1
    elif 1 <= hor < 3:
        return 2
    elif 3 <= hor < 5:
        return 3
    elif 5 <= hor < 7:
        return 4
    elif 7 <= hor < 9:
        return 5
    elif 9 <= hor < 11:
        return 6
    elif 11 <= hor < 13:
        return 1
    elif 13 <= hor < 15:
        return 2
    elif 15 <= hor < 17:
        return 3
    elif 17 <= hor < 19:
        return 4
    elif 19 <= hor < 21:
        return 5
    elif 21 <= hor < 23:
        return 6


def tyl():
    temp = str(zhdate.ZhDate.from_datetime(
        datetime(
            datetime.today().year,
            datetime.today().month,
            datetime.today().day
        )
    ))
    x = re.findall(r'(\d)月(\d)日', temp)
    return x


def tyl_chinese():
    di = '子丑寅卯辰巳午未申酉戌亥'.index(zhdate.ZhDate.from_datetime(
        datetime(
            datetime.today().year,
            datetime.today().month,
            datetime.today().day
        )
    ).chinese()[-7])
    return di + 1


# 报数起卦
def countDivination(up, down):
    theCauseOf = congenital[up % 8] + congenital[down % 8]
    afterThat = theCauseOf[1:4] + theCauseOf[2:5]
    v = [6, 1, 2, 3, 4, 5][(up + down + y_clock()) % 6]
    # print((up + down + t) % 6)
    tmp = theCauseOf.copy()
    tmp.reverse()
    if tmp[v - 1] == yin:
        tmp[v - 1] = yang
    elif tmp[v - 1] == yang:
        tmp[v - 1] = yin
    tmp.reverse()
    theResultIs = tmp
    for i in range(6):
        print("{} {} {}".format(theCauseOf[i], afterThat[i], theResultIs[i]))


# 现时起卦
def nowTimeDivination():
    up = int(tyl()[0][0]) + int(tyl()[0][1]) + tyl_chinese()
    down = up + y_clock()
    theCauseOf = congenital[up % 8] + congenital[down % 8]
    afterThat = theCauseOf[1:4] + theCauseOf[2:5]
    v = [6, 1, 2, 3, 4, 5][down % 6]
    tmp = theCauseOf.copy()
    tmp.reverse()
    if tmp[v - 1] == yin:
        tmp[v - 1] = yang
    elif tmp[v - 1] == yang:
        tmp[v - 1] = yin
    tmp.reverse()
    theResultIs = tmp
    for i in range(6):
        print("{} {} {}".format(theCauseOf[i], afterThat[i], theResultIs[i]))


if __name__ == '__main__':
    countDivination(19, 25)
    print()
    nowTimeDivination()

