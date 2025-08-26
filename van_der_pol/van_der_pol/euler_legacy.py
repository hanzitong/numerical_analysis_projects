import matplotlib
matplotlib.use('TKAgg')
import matplotlib.pyplot as plt


def divx_vanderpol(y_n):
    return y_n

def divy_vanderpol(x_n, y_n, cons_a):
    return cons_a * (1 - x_n ** 2) * y_n - x_n


def _euler_step(x_n, y_n, cons_a, del_t):
    """
    dy/dx_n = f(x_n, y_n)   // df(x_n, y_n)/dx_n
    y(x_n + del_t) = y_n + del_t * f(x_n, y_n)
    """
    x_n1 = x_n + del_t * y_n
    # y_n1 = y_n + del_t * (cons_a * (1.0 - x_n ** 2.0) * y_n - x_n)
    y_n1 = y_n + del_t * divy_vanderpol(x_n, y_n, cons_a)

    return x_n1, y_n1


def _heun_step(x_ini, y_ini, goal_t, ):
    """
    y(x + del_t) = y_n + del_t / 2 * f(x_n, y_n) + h / 2 * f(x_n1, y_n1)
    """
    x_n1 = y_n + del_t / 2 * divx_vanderpol() + h / 2 * _euler_step(x_n, y_n, cons_a, del_t)
    y_n1 = y_n + del_t / 2 * divy_vanderpol() + h / 2 * _euler_step(x_n, y_n, cons_a, del_t)

    return x_n1, y_n1


def euler(x_ini, y_ini, goal_t, cons_a, del_t=0.1):
    del_t_rest = goal_t % del_t
    t_steps = int(goal_t // del_t)
    t_ini = 0
    results = []

    for i in range(t_steps):
        t_ini += del_t
        x_ini, y_ini = _euler_step(x_ini, y_ini, cons_a, del_t)
        results.append([t_ini, x_ini, y_ini])

    if del_t_rest > 0:
        t_ini += del_t_rest
        x_ini, y_ini = _euler_step(x_ini, y_ini, cons_a, del_t_rest)
        results.append([t_ini, x_ini, y_ini])


    return x_ini, y_ini, results




def main():
    # settings
    x_ini = 1.5
    y_ini = 1.3
    goal_t = 400
    cons_a = 1
    del_t = 0.1

    # make output
    _, _, results = euler(x_ini, y_ini, goal_t, cons_a, del_t)

    # materials for plotting
    tarr = [res[0] for res in results]
    xarr = [res[1] for res in results]
    yarr = [res[2] for res in results]
    # print(tarr)

    # plot x(t)
    plt.plot(yarr, xarr, label='x', color='blue')
    plt.xlabel('Time[s]')
    plt.ylabel('x(t)')
    plt.title(f'x(t) until {goal_t}')
    plt.grid(True)
    # plt.legend()
    plt.show()


    return 0


if __name__ == "__main__":
    main()

