password = input("Enter your very secret")
commonwordslist = ["admin", "123456","123","8888","password","king"]
def lenpoint(password):
    if len(password) < 8 :
        return 0
    elif 8 <= len(password) <= 11:
        return 1
    elif len(password) >= 12:
        return 2

def strong(password):
    points = 0
    lowers = [x for x in password if x.islower()]
    uppers = [y for y in password if y.isupper()]
    nums = [z for z in password if z.isdigit()]
    difrent = [v for v in password if not v.isdigit() and not v ==" " and not v.isalpha()]

    if lowers:
        points +=1
    if uppers:
        points +=1
    if nums:
        points +=1
    if difrent:
        points +=1
    return points


def commonwords(password):
    minuspoints = 0
    for comword in commonwordslist:
        if comword in password.lower():
            minuspoints -=2
    return minuspoints


final_points = lenpoint(password) + strong(password) + commonwords(password)
if final_points<=0:
    print("BAD PASSWORD!")
if 0<final_points<=3:
    print("mid password")
if final_points>=4:
    print("GREAT PASSWORD!!")