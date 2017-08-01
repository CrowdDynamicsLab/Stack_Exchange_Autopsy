import sys, getopt
import csv
import numpy as    np
from scipy.optimize import fmin_l_bfgs_b
import matplotlib.pyplot as plt
import math

import plotly.plotly as py
import plotly.graph_objs as go

all_channels = []
all_parameters = []
observed_q = []
observed_a = []
observed_c = []

final_q = []
final_a = []
final_c = []

error_q = []
error_a = []
error_c = []

avg_err_q = 0
avg_err_a = 0
avg_err_c = 0

T1 = 5
T2 = 5
T3 = 5


# parse the input csv file into [[channel_1,[time_11, type_11, intensity_11], ..., [time_1n,type_1n, intensity_1n]],....,[channel_m,[time_m1,type_m1,intensity_mn],...,[time_mn,type_mn,intensity_mn]]]s
def parseEvents(path):
    previous_channel = "null"
    tmp_list = []
    first = True
    with open(path, 'rU') as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quotechar='|')
        for row in reader:
            # print(row)
            # print(row[0])
            if row[0] != previous_channel and first == False:
                all_channels.append(tmp_list)
                first = False
                tmp_list = []
                tmp_list.append(row[0])
                tmp_list.append([int(row[1]), 0, int(row[5])])
                tmp_list.append([int(row[1]), 1, int(row[6])])
                tmp_list.append([int(row[1]), 2, int(row[7])])
                previous_channel = row[0]
            elif first == True:
                first = False
                tmp_list = []
                tmp_list.append(row[0])
                tmp_list.append([int(row[1]), 0, int(row[5])])
                tmp_list.append([int(row[1]), 1, int(row[6])])
                tmp_list.append([int(row[1]), 2, int(row[7])])
                previous_channel = row[0]
            else:
                first = False
                tmp_list.append([int(row[1]), 0, int(row[5])])
                tmp_list.append([int(row[1]), 1, int(row[6])])
                tmp_list.append([int(row[1]), 2, int(row[7])])
                previous_channel = row[0]
                # print(np.matrix(all_channels))


# Modified on 07/26/27: removing c1, c2, c3
# J_q defines the equation for generating questions based on previous questions & answers & comments
# N_q[t] = mu1 + C1 * sum(N_q[t-tau] * e ^ (-tau))  + C2 * sum(N_a[t-tau]* e ^ (-tau)) + C3 * sum(N_c[t-tau]* e ^ (-tau)))    tau = 1, ..., T1
'''
def J_q(x):
    [mu1, C1, C2, C3] = x
    expected_q = []
    global final_q
    final_q = []
    length = len(observed_q)
    # print(length)
    dif = 0
    for i in range(0, T1):
        expected_q.append(observed_q[i])
        final_q.append(observed_q[i])
    # print(np.matrix(expected_q))
    for i in range(T1, length):
        tmp_sum = mu1
        for j in range(i - T1, i):
            # print(expected_q[j][1])
            # print(observed_q[i][0])
            # print(expected_q[j][0])
            if observed_q[i][0] - observed_q[j][0] <= T1:
                tmp_sum += C1 * observed_q[j][1] * (math.exp(observed_q[j][0] - observed_q[i][0]))
            if observed_a[i][0] - observed_a[j][0] <= T1:
                tmp_sum += C2 * observed_a[j][1] * (math.exp(observed_a[j][0] - observed_a[i][0]))
            if observed_c[i][0] - observed_c[j][0] <= T1:
                tmp_sum += C3 * observed_c[j][1] * (math.exp(observed_c[j][0] - observed_c[i][0]))
        expected_q.append([int(observed_q[i][0]), tmp_sum])
        final_q.append([int(observed_q[i][0]), tmp_sum])
        dif += (observed_q[i][1] - tmp_sum) ** 2
    # print(np.matrix(observed_q))
    # print(np.matrix(expected_q))
    # final_q = expected_q
    return float(dif) / 2
'''


def J_q(x):
    [mu1, C1, C2, C3] = x
    # expected_q = []
    global final_q
    global error_q
    global avg_err_q
    error_q = []
    avg_err_q = 0
    final_q = []
    length = len(observed_q)
    dif = 0
    for i in range(0, T1):
        # expected_q.append(observed_q[i])
        final_q.append(observed_q[i])
        error_q.append(0)
    for i in range(T1, length):
        tmp_sum = mu1
        for j in range(i - T1, i):
            if observed_q[i][0] - observed_q[j][0] <= T1:
                tmp_sum += C1 * observed_q[j][1] * (math.exp(observed_q[j][0] - observed_q[i][0]))
            if observed_a[i][0] - observed_a[j][0] <= T1:
                tmp_sum += C2 * observed_a[j][1] * (math.exp(observed_a[j][0] - observed_a[i][0]))
            if observed_c[i][0] - observed_c[j][0] <= T1:
                tmp_sum += C3 * observed_c[j][1] * (math.exp(observed_c[j][0] - observed_c[i][0]))
        # expected_q.append([int(observed_q[i][0]),tmp_sum])
        final_q.append([int(observed_q[i][0]), tmp_sum])
        dif += (observed_q[i][1] - tmp_sum) ** 2
        tmp_err = 100 * abs(observed_q[i][1] - tmp_sum) / float(observed_q[i][1])
        error_q.append(tmp_err)
        avg_err_q += tmp_err
    avg_err_q /= float(length)
    return float(dif) / 2


# J_a defines the equation for generating answers based on previous questions & answers & comments
# N_a[t] = mu2 + C1 * sum(N_q[t-tau] * e ^ (-tau))  + C2 * sum(N_a[t-tau]* e ^ (-tau)) + C3 * sum(N_c[t-tau]* e ^ (-tau)))   tau = 1, ..., T2
'''
def J_a(x):
    [mu2, C1, C2, C3] = x
    expected_a = []
    global final_a
    final_a = []
    length = len(observed_a)
    dif = 0
    for i in range(0, T2):
        expected_a.append(observed_a[i])
        final_a.append(observed_a[i])
    for i in range(T2, length):
        tmp_sum = mu2
        for j in range(i - T2, i):
            if observed_a[i][0] - observed_a[j][0] <= T2:
                tmp_sum += C2 * observed_a[j][1] * (math.exp(observed_a[j][0] - observed_a[i][0]))
            if observed_q[i][0] - observed_q[j][0] <= T2:
                tmp_sum += C1 * observed_q[j][1] * (math.exp(observed_q[j][0] - observed_q[i][0]))
            if observed_c[i][0] - observed_c[j][0] <= T2:
                tmp_sum += C3 * observed_c[j][1] * (math.exp(observed_c[j][0] - observed_c[i][0]))
        expected_a.append([int(observed_a[i][0]), tmp_sum])
        final_a.append([int(observed_a[i][0]), tmp_sum])
        dif += (observed_a[i][1] - tmp_sum) ** 2

    return float(dif) / 2
'''


def J_a(x):
    [mu2, C1, C2, C3] = x
    # expected_a = []
    global final_a
    global error_a
    global avg_err_a
    error_a = []
    avg_err_a = 0
    final_a = []
    length = len(observed_a)
    dif = 0
    for i in range(0, T2):
        # expected_a.append(observed_a[i])
        final_a.append(observed_a[i])
        error_a.append(0)
    for i in range(T2, length):
        tmp_sum = mu2
        for j in range(i - T2, i):
            if observed_q[i][0] - observed_q[j][0] <= T2:
                tmp_sum += C1 * observed_q[j][1] * (math.exp(observed_q[j][0] - observed_q[i][0]))
            if observed_a[i][0] - observed_a[j][0] <= T2:
                tmp_sum += C2 * observed_a[j][1] * (math.exp(observed_a[j][0] - observed_a[i][0]))
            if observed_c[i][0] - observed_c[j][0] <= T2:
                tmp_sum += C3 * observed_c[j][1] * (math.exp(observed_c[j][0] - observed_c[i][0]))
        # expected_a.append([int(observed_a[i][0]),tmp_sum])
        final_a.append([int(observed_a[i][0]), tmp_sum])
        dif += (observed_a[i][1] - tmp_sum) ** 2
        tmp_err = 100 * abs(observed_a[i][1] - tmp_sum) / float(observed_a[i][1])
        error_a.append(tmp_err)
        avg_err_a += tmp_err

    avg_err_a /= float(length)
    return float(dif) / 2


# J_c defines the equation for generating comments based on previous questions & answers & comments
# N_c[t] = mu3 + C1 * sum(N_q[t-tau] * e ^ (-tau))  + C2 * sum(N_a[t-tau]* e ^ (-tau)) + C3 * sum(N_c[t-tau]* e ^ (-tau)))    tau = 1, ..., T3
'''
def J_c(x):
    [mu3, C1, C2, C3] = x
    expected_c = []
    global final_c
    final_c = []
    length = len(observed_c)
    dif = 0
    for i in range(0, T3):
        expected_c.append(observed_c[i])
        final_c.append(observed_c[i])
    for i in range(T3, length):
        tmp_sum = mu3
        for j in range(i - T3, i):
            if observed_c[i][0] - observed_c[j][0] <= T3:
                tmp_sum += C3 * observed_c[j][1] * (math.exp(observed_c[j][0] - observed_c[i][0]))
            if observed_a[i][0] - observed_a[j][0] <= T3:
                tmp_sum += C2 * observed_a[j][1] * (math.exp(observed_a[j][0] - observed_a[i][0]))
            if observed_q[i][0] - observed_q[j][0] <= T3:
                tmp_sum += C1 * observed_q[j][1] * (math.exp(observed_q[j][0] - observed_q[i][0]))
        expected_c.append([int(observed_c[i][0]), tmp_sum])
        final_c.append([int(observed_c[i][0]), tmp_sum])
        dif += (observed_c[i][1] - tmp_sum) ** 2
    # final_c = expected_c
    return float(dif) / 2
'''


def J_c(x):
    [mu3, C1, C2, C3] = x
    # expected_c = []
    global final_c
    global error_c
    global avg_err_c
    error_c = []
    avg_err_c = 0
    final_c = []
    length = len(observed_c)
    dif = 0
    for i in range(0, T3):
        # expected_c.append(observed_c[i])
        final_c.append(observed_c[i])
        error_c.append(0)
    for i in range(T3, length):
        tmp_sum = mu3
        for j in range(i - T3, i):
            if observed_q[i][0] - observed_q[j][0] <= T3:
                tmp_sum += C1 * observed_q[j][1] * (math.exp(observed_q[j][0] - observed_q[i][0]))
            if observed_a[i][0] - observed_a[j][0] <= T3:
                tmp_sum += C2 * observed_a[j][1] * (math.exp(observed_a[j][0] - observed_a[i][0]))
            if observed_c[i][0] - observed_c[j][0] <= T3:
                tmp_sum += C3 * observed_c[j][1] * (math.exp(observed_c[j][0] - observed_c[i][0]))
        # expected_c.append([int(observed_c[i][0]),tmp_sum])
        final_c.append([int(observed_c[i][0]), tmp_sum])
        dif += (observed_c[i][1] - tmp_sum) ** 2
        tmp_err = 100 * abs(observed_c[i][1] - tmp_sum) / float(observed_c[i][1])
        error_c.append(tmp_err)
        avg_err_c += tmp_err

    avg_err_c /= float(length)
    return float(dif) / 2


def J_combine(x):
    [mu2, C2, c2, theta2, C1, c1, theta1, C3, c3, theta3] = x
    expected_a = []
    global final_a
    final_a = []
    length = len(observed_a)
    dif = 0
    for i in range(0, T2):
        expected_a.append(observed_a[i])
        final_a.append(observed_a[i])
    for i in range(T2, length):
        tmp_sum = mu2
        for j in range(i - T2, i):
            tmp_sum += C2 * expected_a[j][1] * ((observed_a[i][0] - expected_a[j][0] + c2) ** (-(1 + theta2)))
            tmp_sum += C1 * observed_q[j][1] * ((observed_q[i][0] - observed_q[j][0] + c1) ** (-(1 + theta1)))
            tmp_sum += C3 * observed_c[j][1] * ((observed_c[i][0] - observed_c[j][0] + c3) ** (-(1 + theta3)))
        expected_a.append([int(observed_a[i][0]), tmp_sum])
        final_a.append([int(observed_a[i][0]), tmp_sum])
        dif += (observed_a[i][1] - tmp_sum) ** 2

    return float(dif) / 2


def main(argv):
    inputfile = ''
    outputfile = ''
    try:
        opts, args = getopt.getopt(argv, "hi:o:", ["ifile=", "ofile="])
    except getopt.GetoptError:
        print("BFGS.py -i <inputfile> -o <outputfile>")
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print("BFGS.py -i <inputfile> -o <outputfile>")
        elif opt in ("-i", "--ifile"):
            inputfile = arg
        elif opt in ("-o", "--ofile"):
            outputfile = arg
    print("inputfile is", inputfile, "outputfile is", outputfile)
    parseEvents(inputfile)
    try:
        out = open(outputfile, 'w')
    except:
        print("Fail to open outputfile")
    outwriter = csv.writer(out, delimiter=',')

    outwriter.writerow(
        ["channel_name", "par_asker", "avg_err_asker", "par_answerer", "avg_err_answerer", "par_commenter",
         "avg_err_commenter"])

    # py.plotly.tools.set_credentials_file(username='alicehz', api_key='r0ohfB3ZfTwaIt7l7TvW')
    # py.plotly.tools.set_credentials_file(username='shizuku775', api_key='EG7TELLZedHPVd3vqcYT')

    cnt = 0
    for channel in all_channels:
        channel_name = channel[0]
        observed_q[:] = []
        observed_a[:] = []
        observed_c[:] = []
        first = True
        for event in channel:
            if first:
                first = False
                continue
            if event[1] == 0:
                observed_q.append([event[0], event[2]])
            elif event[1] == 1:
                observed_a.append([event[0], event[2]])
            elif event[1] == 2:
                observed_c.append([event[0], event[2]])
        # print(np.matrix(observed_q))
        # print(np.matrix(observed_a))
        # print(np.matrix(observed_c))
        if len(observed_q) <= T1:
            continue
        x0 = np.array([5, 1, 1, 1])
        x1 = np.array([5, 1, 1, 1])
        x2 = np.array([5, 1, 1, 1])

        res_q = fmin_l_bfgs_b(J_q, x0, approx_grad=True)
        print(res_q)
        res_a = fmin_l_bfgs_b(J_a, x1, approx_grad=True)
        print(res_a)
        res_c = fmin_l_bfgs_b(J_c, x2, approx_grad=True)
        print(res_c)

        '''
        dif_q = J_q(res_q[0])
        dif_a = J_a(res_a[0])
        dif_c = J_c(res_c[0])
        # print(np.matrix(final_q))
        # print(np.matrix(final_a))
        # print(np.matrix(final_c))

        outwriter.writerow(
            [channel_name, "q", res_q[:], "dif_q", dif_q, "a", res_a[:], "dif_a", dif_a, "c", res_c[:], "dif_c", dif_c])

        '''

        J_q(res_q[0])
        J_a(res_a[0])
        J_c(res_c[0])
        outwriter.writerow(
            [channel_name, res_q[0], avg_err_q, res_a[0], avg_err_a, res_c[0], avg_err_c])

        '''
        month = []
        o_q = []
        e_q = []
        o_a = []
        e_a = []
        o_c = []
        e_c = []
        length = len(observed_q)
        for k in range(0, length):
            month.append(observed_q[k][0])
            o_q.append(observed_q[k][1])
            e_q.append(final_q[k][1])
            o_a.append(observed_a[k][1])
            e_a.append(final_a[k][1])
            o_c.append(observed_c[k][1])
            e_c.append(final_c[k][1])


        fig = plt.figure()
        plt.plot(month, o_q, 'r--', label='Observed Questions')
        plt.plot(month, e_q, 'r^', label='Expected Questions')
        plt.plot(month, o_a, 'b--', label='Observed Answers')
        plt.plot(month, e_a, 'b^', label='Expected Answers')
        plt.plot(month, o_c, 'g--', label='Observed Comments')
        plt.plot(month, e_c, 'g^', label='Expected Comments')
        plt.legend()

        fig.suptitle(channel_name)
        plt.xlabel('Day')
        plt.ylabel('Number of Activities')
        # plt.show()
        fig.savefig(channel_name + '_daily_exp')


        trace0 = go.Scatter(
            x = month,
            y = o_q,
            name = 'Observed Questions',
            line = dict(
                color = ('rgb(255,165,0)'),
                width = 4,
                dash='dash')
        )

        trace1 = go.Scatter(
            x=month,
            y=e_q,
            name='Expected Questions',
            line=dict(
                color=('rgb(0,0,255)'),
                width=4,
                dash = 'dot')
        )

        trace2 = go.Scatter(
            x=month,
            y=o_a,
            name='Observed Answers',
            line=dict(
                color=('rgb(32,178,170)'),
                width=4,
                dash = 'dash')
        )
        trace3 = go.Scatter(
            x=month,
            y=e_a,
            name='Expected Answers',
            line=dict(
                color=('rgb(138,43,226)'),
                width=4,
                dash='dot')
        )
        trace4 = go.Scatter(
            x=month,
            y=o_c,
            name='Observed Comments',
            line=dict(
                color=('rgb(50,205,50)'),
                width=4,
                dash = 'dash')
        )
        trace5 = go.Scatter(
            x=month,
            y=e_c,
            name='Expected Comments',
            line=dict(
                color=('rgb(220,20,60)'),
                width=4,
                dash='dot')
        )
        data = [trace0, trace1, trace2, trace3, trace4, trace5]
        layout = dict(title = channel_name,
                      xaxis = dict(title = 'Day'),
                      yaxis = dict(title = 'Number of Activities'),
                      )

        fig = dict(data = data, layout = layout)
        py.plot(fig, filename = channel_name + '_daily_exp')

        data = [trace0, trace1]
        layout = dict(title=channel_name + ' Q',
                      xaxis=dict(title='Day'),
                      yaxis=dict(title='Number of Questions'),
                      )
        fig = dict(data=data, layout=layout)
        py.plot(fig, filename=channel_name + '_daily_Q_exp')

        data = [trace2, trace3]
        layout = dict(title=channel_name + ' A',
                      xaxis=dict(title='Day'),
                      yaxis=dict(title='Number of Answers'),
                      )
        fig = dict(data=data, layout=layout)
        py.plot(fig, filename=channel_name + '_daily_A_exp')

        data = [trace4, trace5]
        layout = dict(title=channel_name + ' C',
                      xaxis=dict(title='Day'),
                      yaxis=dict(title='Number of Commments'),
                      )
        fig = dict(data=data, layout=layout)
        py.plot(fig, filename=channel_name + '_daily_C_exp')
        '''
        '''
        month = []
        length = len(observed_q)
        for k in range(0, length):
            month.append(observed_q[k][0])

        trace0 = go.Scatter(
            x=month,
            y=error_q,
            name='Question Errors',
            line=dict(
                color=('rgb(255,165,0)'),
                width=4,
                dash='dash')
        )

        trace1 = go.Scatter(
            x=month,
            y=error_a,
            name='Answer Errors',
            line=dict(
                color=('rgb(0,0,255)'),
                width=4,
                dash='dash')
        )

        trace2 = go.Scatter(
            x=month,
            y=error_c,
            name='Comment Errors',
            line=dict(
                color=('rgb(32,178,170)'),
                width=4,
                dash='dash')
        )

        data = [trace0, trace1, trace2]
        layout = dict(title=channel_name,
                      xaxis=dict(title='Day'),
                      yaxis=dict(title='Relative Errors'),
                      )

        fig = dict(data=data, layout=layout)
        py.plot(fig, filename=channel_name + '_daily_error_exp')
        '''


if __name__ == "__main__":
    main(sys.argv[1:])


