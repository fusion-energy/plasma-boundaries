import numpy as np
import sympy as sp


def derivatives(f, coefficients_c, A, order):
    """Computes the derivatives of magnetic flux.
    Does not computes xy or yx derivatives.

    Args:
        f (callable f(x, y, coefficients_c, pkg)): function of magnetic flux
        coefficients_c (list): coefficients ci
        order (int): order of differenciation

    Returns:
        list: [x_derivative, y_derivative]
    """
    x, y = sp.symbols("x y")
    f_ = f(
        X=x, Y=y, coefficients_c=coefficients_c,
        A=A, pkg=sp)
    f_x = sp.diff(f_, *[x for i in range(order)])
    f_y = sp.diff(f_, *[y for i in range(order)])
    return [f_x, f_y]


def psi_up_down_symmetric(X, Y, coefficients_c, A, pkg=np):
    """returns the value of magnetic flux at point (X, Y)
     according to coefficients ci

    Args:
        X (float or numpy.array): x coordinate
        Y (float or numpy.array): y coordinate
        coefficients_c (list): list of floats, the ci coefficients
        pkg (callable, optional): if set to np (resp. sp), numpy (resp. sympy)
         objects will be used. Defaults to np.

    Returns:
        float or numpy.array: value(s) of magnetic flux
    """
    psi_1 = 1
    psi_2 = X**2
    psi_3 = Y**2 - X**2*pkg.log(X)
    psi_4 = X**4 - 4*X**2*Y**2
    psi_5 = 2*Y**4 - 9*Y**2*X**2 + 3*X**4*pkg.log(X) - 12*X**2*Y**2*pkg.log(X)
    psi_6 = X**6 - 12*X**4*Y**2 + 8*X**2*Y**4
    psi_7 = 8*Y**6 - 140*Y**4*X**2 + 75*Y**2*X**4 - 15*X**6*pkg.log(X) + \
        180*X**4*Y**2*pkg.log(X) - 120*X**2*Y**4*pkg.log(X)

    psis = [psi_1, psi_2, psi_3, psi_4, psi_5, psi_6, psi_7]
    val = X**4/8 + A*(1/2*X**2*pkg.log(X) - X**4/8) + \
        sum([coefficients_c[i]*psis[i] for i in range(len(coefficients_c))])
    return val


def psi_up_down_asymetric(X, Y, coefficients_c, A, pkg=np):
    """returns the value of magnetic flux at point (X, Y)
     according to coefficients ci

    Args:
        X (float or numpy.array): x coordinate
        Y (float or numpy.array): y coordinate
        coefficients_c (list): list of floats, the ci coefficients
        pkg (callable, optional): if set to np (resp. sp), numpy (resp. sympy)
         objects will be used. Defaults to np.

    Returns:
        float or numpy.array: value(s) of magnetic flux
    """

    psi_1 = 1
    psi_2 = X**2
    psi_3 = Y**2 - X**2*pkg.log(X)
    psi_4 = X**4 - 4*X**2*Y**2
    psi_5 = 2*Y**4 - 9*Y**2*X**2 + 3*X**4*pkg.log(X) - 12*X**2*Y**2*pkg.log(X)
    psi_6 = X**6 - 12*X**4*Y**2 + 8*X**2*Y**4
    psi_7 = 8*Y**6 - 140*Y**4*X**2 + 75*Y**2*X**4 - 15*X**6*pkg.log(X) + \
        180*X**4*Y**2*pkg.log(X) - 120*X**2*Y**4*pkg.log(X)
    psi_8 = Y
    psi_9 = Y*X**2
    psi_10 = Y**3 - 3*Y*X**2*pkg.log(X)
    psi_11 = 3*Y*X**4 - 4*Y**3*X**2
    psi_12 = 8*Y**5 - 45*Y*X**4 - 80*Y**3*X**2*pkg.log(X) + \
        60*Y*X**4*pkg.log(X)

    psis = [
        psi_1, psi_2, psi_3, psi_4, psi_5, psi_6, psi_7, psi_8, psi_9,
        psi_10, psi_11, psi_12]

    val = X**4/8 + A*(1/2*X**2*pkg.log(X) - X**4/8) + \
        sum([coefficients_c[i]*psis[i] for i in range(len(coefficients_c))])
    return val