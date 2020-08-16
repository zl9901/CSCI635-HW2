

from scipy.stats import poisson,expon,bernoulli,laplace,norm
import matplotlib.pyplot as plt
import numpy as np


def bernoulliFunction():
    x=[i*0.001 for i in range(1001)]
    """
    calculate probability of uniform distribution
    """
    px=[1/1001]*1001
    """
    calculate P(X=x)=prob.pdf(X=x)/Z
    """
    probBernoulli=bernoulli(.7).pmf(x)/sum(bernoulli(.7).pmf(x))
    print('value of Z for bernoulli distribution is ',end='')
    print(sum(bernoulli(.7).pmf(x)))

    """
    calculate KL(u||x), term causes a numerical error then the value of that term should be 0
    """
    KL=0.0
    for i in range(1001):
        if px[i]==0 or probBernoulli[i]==0:
            continue
        else:
            KL+=px[i]*np.log((px[i])/(probBernoulli[i]))
    print('value of KL(u||x) is ',end='')
    print(KL)

    """
    calculate KL(x||u), term causes a numerical error then the value of that term should be 0
    """
    tmp=0.0
    for i in range(1001):
        if px[i]==0 or probBernoulli[i]==0:
            continue
        else:
            tmp+=probBernoulli[i]*np.log((probBernoulli[i])/(px[i]))
    print('value of KL(x||u) is ',end='')
    print(tmp)
    print()


    plt.plot(x,probBernoulli)
    plt.show()

def normFunction():
    x=[i*0.001 for i in range(1001)]
    """
    calculate probability of uniform distribution
    """
    px = [1/1001] * 1001
    """
    calculate P(X=x)=prob.pdf(X=x)/Z
    """
    probGaussian = norm.pdf(x) / sum(norm.pdf(x))

    print('value of Z for gaussian distribution is ', end='')
    print(sum(norm.pdf(x)))

    """
    calculate KL(u||x), term causes a numerical error then the value of that term should be 0
    """
    KL = 0.0
    for i in range(1001):
        if px[i]==0 or probGaussian[i]==0:
            continue
        else:
            KL += px[i] * np.log((px[i]) / (probGaussian[i]))
    print('value of KL(u||x) is ', end='')
    print(KL)

    """
    calculate KL(x||u), term causes a numerical error then the value of that term should be 0
    """
    tmp = 0.0
    for i in range(1001):
        if px[i]==0 or probGaussian[i]==0:
            continue
        else:
            tmp += probGaussian[i] * np.log((probGaussian[i]) / (px[i]))
    print('value of KL(x||u) is ', end='')
    print(tmp)
    print()

    plt.plot(x,probGaussian)
    plt.show()


def laplaceFunction():
    x=[i*0.001 for i in range(1001)]
    """
    calculate probability of uniform distribution
    """
    px = [1/1001] * 1001
    """
    calculate P(X=x)=prob.pdf(X=x)/Z
    """
    probLaplace = laplace.pdf(x) / sum(laplace.pdf(x))

    print('value of Z for laplace distribution is ', end='')
    print(sum(laplace.pdf(x)))

    """
    calculate KL(u||x), term causes a numerical error then the value of that term should be 0
    """
    KL = 0.0
    for i in range(1001):
        if px[i]==0 or probLaplace[i]==0:
            continue
        else:
            KL += px[i] * np.log((px[i]) / (probLaplace[i]))
    print('value of KL(u||x) is ', end='')
    print(KL)

    """
    calculate KL(x||u), term causes a numerical error then the value of that term should be 0
    """
    tmp = 0.0
    for i in range(1001):
        if px[i]==0 or probLaplace[i]==0:
            continue
        else:
            tmp += probLaplace[i] * np.log((probLaplace[i]) / (px[i]))
    print('value of KL(x||u) is ', end='')
    print(tmp)
    print()

    plt.plot(x,probLaplace)
    plt.show()


def exponFunction():
    x=[i*0.001 for i in range(1001)]
    """
    calculate probability of uniform distribution
    """
    px = [1/1001] * 1001
    """
    calculate P(X=x)=prob.pdf(X=x)/Z
    """
    probExponent = expon.pdf(x) / sum(expon.pdf(x))

    print('value of Z for exponential distribution is ', end='')
    print(sum(expon.pdf(x)))

    """
    calculate KL(u||x), term causes a numerical error then the value of that term should be 0
    """
    KL = 0.0
    for i in range(1001):
        if px[i]==0 or probExponent[i]==0:
            continue
        else:
            KL += px[i] * np.log((px[i]) / (probExponent[i]))
    print('value of KL(u||x) is ', end='')
    print(KL)

    """
    calculate KL(x||u), term causes a numerical error then the value of that term should be 0
    """
    tmp = 0.0
    for i in range(1001):
        if px[i]==0 or probExponent[i]==0:
            continue
        else:
            tmp += probExponent[i] * np.log((probExponent[i]) / (px[i]))
    print('value of KL(x||u) is ', end='')
    print(tmp)
    print()

    plt.plot(x,probExponent)
    plt.show()


def poissonFunction():
    x=[i*0.001 for i in range(1001)]
    """
    calculate probability of uniform distribution
    """
    px = [1/1001]*1001
    """
    calculate P(X=x)=prob.pdf(X=x)/Z
    """
    probPoisson = poisson(.3).pmf(x) / sum(poisson(.3).pmf(x))

    print('value of Z for poisson distribution is ', end='')
    print(sum(poisson(.3).pmf(x)))

    """
    calculate KL(u||x), term causes a numerical error then the value of that term should be 0
    """
    KL = 0.0
    for i in range(1001):
        if px[i]==0 or probPoisson[i]==0:
            continue
        else:
            KL += px[i] * np.log((px[i]) / (probPoisson[i]))
    print('value of KL(u||x) is ', end='')
    print(KL)

    """
    calculate KL(x||u), term causes a numerical error then the value of that term should be 0
    """
    tmp = 0.0
    for i in range(1001):
        if px[i]==0 or probPoisson[i]==0:
            continue
        else:
            tmp += probPoisson[i] * np.log((probPoisson[i]) / (px[i]))
    print('value of KL(x||u) is ', end='')
    print(tmp)
    print()

    plt.plot(x,probPoisson)
    plt.show()


bernoulliFunction()
normFunction()
laplaceFunction()
exponFunction()
poissonFunction()





