# 1. ON DÉFINIT LA FONCTION (On fabrique la machine)
def admission(moy):
    positive = "admis"
    negative = "Rattrapage"
    if moy >= 10:
        return positive
    else:
        return negative


josephine = admission(17)
print(josephine)