"""
foreign_exchange.py

def getnaira(dollar):
    naira = dollar * 1550
    return naira

def getdollar(naira):
    dollar = naira / 1550
    return dollar

"""

def get_naira(dollar):
    naira = dollar * 1550
    return naira

def get_dollar(naira):
    dollar = round(naira / 1550, 3)
    return dollar

print("$",get_naira(20))

print("$",get_dollar(3000))
