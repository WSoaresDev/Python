angulo = float(input('Digite o valor do ângulo: '))
from math import sin, cos, tan, radians
seno = sin(radians(angulo))
cosseno = cos(radians(angulo))
tangente = tan(radians(angulo))
print('O seno de {} é {:.2f}, o cosseno é {:.2f} e a tangente é {:.2f}'.format(angulo, seno, cosseno, tangente))