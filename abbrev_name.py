def abbrev_name(name):

    abbrev = {
        'Sam Harris': 'S.H',
        'Patrick Feeney': 'P.F',
    }

    return abbrev[name]

print(abbrev_name('Sam Harris'))
print(abbrev_name('Patrick Feeney'))