from scipy.stats import poisson,expon,bernoulli,laplace,norm
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
import pdb

x_list = []
mu = .5

for i in range(10000):
	#x = poisson.rvs(.5, size=1000)
	#x = expon.rvs(size = 1000)
	#x = bernoulli.rvs(mu, size = 1000)
	x = laplace.rvs(size = 10000)
	#x = norm.rvs(size = 10000)
	x_list.append(sum(x)/10000)

(mu, sigma) = norm.fit(x_list)


n, bins, patches = plt.hist(x_list,bins=50,density=True)
pdb.set_trace()
y = mlab.normpdf( bins, mu, sigma)
l = plt.plot(bins, y, 'r--', linewidth=2)

plt.show()




