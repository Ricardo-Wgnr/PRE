import numpy as np
import matplotlib.pyplot as plt
import pre

# Parametros
N = 100_000 # num de realizacoes

# Exmperimento
U = np.random.uniform(0,4,N)
X = np.empty_like(U)
idx1 = U <= 1
idx2 = U > 1
X[idx1] = np.random.uniform(0,2,idx1.sum())
X[idx2] = np.random.binomial(1,2/3,idx2.sum())

# Calculos
dx = 0.01
xs = np.arange(-0.5, 2.5, dx)
pdf_X_teo = 1/8 * (0 <= xs) * (xs < 2)
pdf_X_sim = pre.hist(X,xs)
cdf_X_teo = (
    (0)             *   (xs<0)          +
    (1/4+xs/8)      *   (0<=xs) * (xs<1)+
    (7/8+(xs-1)/8)  *   (1<=xs) * (xs<2)+
    (1)             *   (2<=xs)          
)
cdf_X_sim = np.cumsum(pdf_X_sim) * dx
ev_X_teo = 3/4
ev_X_sim = np.mean(X)

# saida
plt.subplot(2,1,1)
plt.bar(xs, pdf_X_sim, width=0.8*dx, color="y")
plt.plot(xs, pdf_X_teo, linewidth=3, color="b") #apenas a parte continua
plt.annotate("", xytext=(0,0), xy=(0,1/4), arrowprops=pre.arrowprops)
plt.annotate("", xytext=(1,0), xy=(1,1/2), arrowprops=pre.arrowprops)
plt.ylim(-0.1, 0.6)
plt.xlabel("$x$")
plt.ylabel("$f_X(x)$")
plt.grid()
plt.subplot(2,1,2)
plt.plot(xs, cdf_X_sim, color="y")
plt.plot(xs, cdf_X_teo, linewidth=2, color="b", linestyle="--")
plt.ylim(-0.2, 1.2)
plt.xlabel("$x$")
plt.ylabel("$F_X(x)$")
plt.grid()
print(f"Teo: E[X]= {ev_X_teo:g}")
print(f"Sim: E[X]= {ev_X_sim:g}")
plt.show()