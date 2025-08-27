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
# pdf_X_teo = ...
pdf_X_sim = pre.hist(X,xs)
# cdf_X_teo = ...
cdf_X_sim = np.cumsum(pdf_X_sim) * dx
# ev_X_teo = ...
ev_X_sim = np.mean(X)

# saida
plt.subplot(2,1,1)
plt.bar(xs, pdf_X_sim, width=0.8*dx)
plt.ylim(-0.1, 0.6)
plt.xlabel("$x$")
plt.ylabel("$f_X(x)$")
plt.grid()
plt.subplot(2,1,2)
plt.plot(xs, cdf_X_sim)
plt.ylim(-0.2, 1.2)
plt.xlabel("$x$")
plt.ylabel("$F_X(x)$")
plt.grid()
print(f"Sim: E[X]= {ev_X_sim:g}")
plt.show()