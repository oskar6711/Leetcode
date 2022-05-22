def pref(strs):

    pref = strs[0]

    for i in range(1, len(strs)):
        while pref != strs[i][0:len(pref)]:
            pref = pref[0:len(pref) - 1]

    return pref


