# print(isinstance(12, int))
# print(isinstance(12.3, float))
# print(isinstance("hej", str))

#                  *
#           gren1 / \ gren2
#                   /\
#           ugren1 /  \ ugren2
#                     /\
#              gren3 / \ gren4

ugren1_varde = {"gren3": 55, "ugren4": "hejsan"}
gren2_varde = {"ugren1": ugren1_varde, "ugren2": "hej"}
trad = {"gren1": "k", "gren2": gren2_varde}


def berakna_djup(trad: dict, djup=0):
    djup = djup + 1
    #    print(trad.keys())
    #    print(trad.items())
    #    for item in trad.items():
    #       print(item)
    for key, value in trad.items():  # unpacking av dictionary
        if isinstance(value, dict):
            ret_djup = berakna_djup(value, djup)
            if ret_djup > djup:
                djup = ret_djup
    #            print("hittade en", value)
    # print(trad[key])
    # print(key)
    # print(value)
    return djup


berakna_djup(trad)

print("djupet är: ", berakna_djup(trad))
