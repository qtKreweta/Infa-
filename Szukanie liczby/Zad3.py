def MiniMaks(tab):
    najmniejszy = tab[0]
    największy = tab[0]

    for x in tab:
        if x < najmniejszy:
            najmniejszy = x
        if x > największy:
            największy = x

    return najmniejszy, największy


# --- Program główny ---
tab = [5, 2, 9, 1, 7, 3]

mini, maksi = MiniMaks(tab)
print("Najmniejszy:", mini)
print("Największy:", maksi)
