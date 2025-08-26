

def _diffx(y_n):
    """
    A part of van-der-pol equation.
    The differential of x(t) with respect to t.

    Args:
        x_n(float): current value of x

    Returns:
        float:
    """
    return y_n


def _diffy(x_n, y_n, cons_a):
    """
    A part of van-der-pol equation.
    The differential of y(t) with respect to t.

    Args:
        x_n(float): current value of x
        y_n(float): current value of y
        cons_a(float): constant 'a' inside the van-der-pol differential equation

    Returns:
        float:
    """
    if x_n == 1:
        return -1       # - x_n
    else:
        return cons_a * (1 - x_n) * (1 + x_n) * y_n - x_n
        ## Original Expression
        ## cons_a * (1 - x_n ** 2) * y_n - x_n
        ##
        ## This expression can cause loss of significance, 
        ## when x_n is extreamly close to "1" like 0.9 < x_n < 1.1.


def _euler_step(x_n, y_n, cons_a, del_t):
    """
    It calculates next step with Euler method.

    Args:
        x_n(float): current value of x
        y_n(float): current value of y
        cons_a(float): constant a inside the van-der-pol differential equation
        del_t(float): step size

    Returns:
        tapple: next value of x & y. (x_n1(float), y_n1(float))

    Euler Method:
        dx/dt = diffx(y_n)
            = y_n
        x(x_n + del_t) = x_n + del_t * diffx(x_n, y_n)

        dy/dt = diffy(x_n, y_n)
            = cons_a * (1 - x_n ** 2) * y_n - x_n
        y(x_n + del_t) = y_n + del_t * diffy(x_n, y_n)
    """
    x_n1 = x_n + del_t * _diffx(y_n)
    y_n1 = y_n + del_t * _diffy(x_n, y_n, cons_a)


    return x_n1, y_n1


def _heun_step(x_n, y_n, cons_a, del_t):
    """
    It calculates next step with Heun method.

    Args:
        x_n(float):current value of x
        y_n(float):current value of y
        cons_a(float):constant a inside the van-der-pol differential equation
        del_t(float):step size

    Returns:
        tapple:next value of x & y. (x_n1(float), y_n1(float))

    Heun Method:
        dx/dt = diffx(y_n)
            = y_n
        x(x + del_t) = x_n + del_t / 2 * diffx(x_n, y_n) + h / 2 * diffx(x_n1, y_n1)
        where, diffx(x_n1, y_n1) = euler_step(y_n)

        dy/dt = diffy(x_n, y_n)
            = cons_a * (1 - x_n ** 2) * y_n - x_n
        y(x + del_t) = y_n + del_t / 2 * diffy(x_n, y_n) + h / 2 * diffy(x_n1, y_n1)
        where, diffy(x_n1, y_n1) = euler_step(x_n, y_n)
    """
    x_n1_euler, y_n1_euler = _euler_step(x_n, y_n, cons_a, del_t)
    x_n1 = x_n + del_t / 2 * (_diffx(y_n) + _diffx(y_n1_euler))
    y_n1 = y_n + del_t / 2 * (_diffy(x_n, y_n, cons_a) + _diffy(x_n1_euler, y_n1_euler, cons_a))


    return x_n1, y_n1


def _calc_xy(x_ini, y_ini, cons_a, t_goal, del_t, step_func):
    """
    It calculates x & y untill specified time and return its results for plotting

    Args:
        x_n(float): initial value of x
        y_n(float): initial value of y
        cons_a(float): constant a inside the van-der-pol differential equation
        t_goal(float): time to stop
        del_t(float): step size
        step_func(): a function that computes one step of the numerical method.
                     It must accept parameters (x, y, cons_a, del_t) and return updated values of x & y.

    Returns:
        tapple: final value of x & y & t. (x_goal(float), y_goal(float), (t, x, y)(tapple))

    """
    results = []
    t_ini = 0
    t_now = t_ini
    del_t_rest = t_goal % del_t
    t_steps = int(t_goal // del_t) + 1

    for i in range(t_steps):
        t_now = t_ini + i * del_t
        x_ini, y_ini = step_func(x_ini, y_ini, cons_a, del_t)
        results.append([t_now, x_ini, y_ini])

    if del_t_rest > 0:
        t_now += del_t_rest
        x_ini, y_ini = step_func(x_ini, y_ini, cons_a, del_t_rest)
        results.append([t_now, x_ini, y_ini])


    return x_ini, y_ini, results


def euler(x_ini, y_ini, cons_a, t_goal, del_t):
    """
    With Euler Method, it calculates x & y untill specified time and return its results for plotting

    Args:
        x_n(float): initial value of x
        y_n(float): initial value of y
        cons_a(float): constant a inside the van-der-pol differential equation
        t_goal(float): time to stop
        del_t(float): step size

    Returns:
        tapple: x_goal(float), y_goal(float), (t, x, y)(tapple)
        It returns final value of x & y, and tapple that contains materials for plotting.
    """
    return _calc_xy(x_ini, y_ini, cons_a, t_goal, del_t, _euler_step)


def heun(x_ini, y_ini, cons_a, t_goal, del_t):
    """
    With Heun Method, it calculates x & y untill specified time and return its results for plotting

    Args:
        x_n(float): initial value of x
        y_n(float): initial value of y
        cons_a(float): constant a inside the van-der-pol differential equation
        t_goal(float): time to stop
        del_t(float): step size

    Returns:
        tapple: x_goal(float), y_goal(float), (t, x, y)(tapple)
        It returns final value of x & y, and tapple that contains materials for plotting.
    """
    return _calc_xy(x_ini, y_ini, cons_a, t_goal, del_t, _heun_step)



