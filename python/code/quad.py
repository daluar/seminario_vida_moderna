import scipy.integrate as integrate
import scipy.special as special
result = integrate.quad(
            lambda x: special.jv(2.5,x), 
            0, 4.5)
print(result)

# resultado            error absoluto estimado
# (1.1178179380783249, 7.8663172481899801e-09)