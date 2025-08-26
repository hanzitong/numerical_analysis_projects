import matplotlib
matplotlib.use('TKAgg')
import matplotlib.pyplot as plt

from van_der_pol import numerical_method as nm


def main():
    x_ini = 1.5     # initial value
    y_ini = 1.3     # initial value
    t_goal = 50    # time to stop

    for method in ['euler_', 'heun_']:
        for cons_a in [2, 10]:
            for del_t in [0.1, 0.01, 0.001]:
                if method == 'euler_':
                    _, _, results = nm.euler(x_ini, y_ini, cons_a, t_goal, del_t)
                else:
                    _, _, results = nm.heun(x_ini, y_ini, cons_a, t_goal, del_t)
                tarr = [res[0] for res in results]
                xarr = [res[1] for res in results]
                yarr = [res[2] for res in results]

                ## x(t) & y(t)
                fig = plt.figure()
                ax1 = fig.add_subplot(2, 1, 1)
                ax2 = fig.add_subplot(2, 1, 2)
                # x(t)
                ax1.plot(tarr, xarr, label='x(t)')
                ax1.set_xlabel('t')
                ax1.set_ylabel('x(t)')
                ax1.set_title(method + f'x(t), a={cons_a}, tau={del_t}')
                ax1.grid(True)
                # y(t)
                ax2.plot(tarr, yarr, label='x(t)')
                ax2.set_xlabel('t')
                ax2.set_ylabel('y(t)')
                ax2.set_title(method + f'y(t), a={cons_a}, tau={del_t}')
                ax2.grid(True)
                # save fig
                plt.tight_layout()
                plt.savefig('fig/' + method + f'xt&yt_a{cons_a}_tau{del_t}.png')
                plt.show()

                ## (x(t), y(t))
                plt.plot(xarr, yarr, label='', color='blue')
                plt.xlabel('x(t)')
                plt.ylabel('y(t)')
                plt.title(method + f'x(t)&y(t)_a{cons_a}_tau{del_t}_tgoal{t_goal}')
                plt.grid(True)
                # save fig
                plt.tight_layout()
                plt.savefig('fig/' + method + f'xt&yt_a{cons_a}_tau{del_t}.png')
                plt.show()


    return 0


if __name__ == "__main__":
    main()
