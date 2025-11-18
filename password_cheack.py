password = input("Enter your very secret")

def lenpoint(password):
    if len(password) < 8 :
        return 0
    elif 8 < len(password) < 11:
        return 1
    elif len(password) > 12:
        return 2

def strong(password):
    lowers = [x for x in password if x.islower()]
    uppers = []

