from matplotlib.matlab import *
t = arange(0.0, 1.0, 0.05)
s = sin(2*pi*t) + 0.5*rand(len(t))
X = zeros((len(t),2), Float)
X[:,0] = t
X[:,1] = s
file('../data/binary_data.dat', 'w').write(X.tostring())
