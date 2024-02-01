def draw_stars(n):
    if n == 3:
        return ['  *  ', ' * * ', '*****']
    x = draw_stars(n // 2)
    stars = []
    for star in x:
        stars.append(' ' * (n // 2) + star + ' ' * (n // 2))
    for star in x:
        stars.append(star + ' ' + star)
    return stars


n = int(input())
print('\n'.join(draw_stars(n)))
