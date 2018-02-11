z = 1 + 1j

while abs(z) < 100:
    if z.imag == 0:
        break
    z = z**2 + 1