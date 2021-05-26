
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

root_addr = '/home/yas/PycharmProjects/elliotNew/results/AML_Lyp/'

for file_num in range(1,5):

    file1 = 'BPR_Lyapanov_ML1M_every_five_epoch.csv'
    file2 = 'BPR_Lyapanov_Foursq_every_five_epoch.csv'
    file3 = 'BPR_Lyapanov_amazon_baby_every_five_epoch.csv'
    file4 = 'BPR_Lyapanov_Yelp_every_five_epoch.csv'

    if file_num == 1:
        file = file1
        per_print = 'ML1M'
    elif file_num == 2:
        file = file2
        per_print = 'Foursq'
    elif file_num == 3:
        file = file3
        per_print = 'AmazonBaby'
    elif file_num == 4:
        file = file4
        per_print = 'Yelp'


    file1_df = pd.read_csv(root_addr + file,header=None)
    file1_df.columns = ['epoch','dim','lr','gamma','spec_pu','spec_qi','HR@5','HR@10']

    f1 = file1_df.loc[file1_df['gamma'] == 1.0]
    f2 = file1_df.loc[file1_df['gamma'] == 1.6]
    f3 = file1_df.loc[file1_df['gamma'] == 2.4]
    f4 = file1_df.loc[file1_df['gamma'] == 3.2]

    fig, ax = plt.subplots()
    ax.plot(f1['HR@5'], 'r--', label='normal')
    ax.plot(f2['HR@5'], 'k:', label='gamma=1.6')
    ax.plot(f3['HR@5'], 'k*', label='gamma=2.4')
    ax.plot(f3['HR@5'], 'k', label='gamma=3.2')

    legend = ax.legend(loc='lower left', shadow=True, fontsize='x-large')

    # Put a nicer background color on the legend.
    legend.get_frame().set_facecolor('C0')
    plt.title(per_print)
    plt.show()
    fig.savefig(per_print + '.png')
    plt.close(fig)    # close the figure window

# root_addr = '/home/yas/PycharmProjects/elliotNew/results/AML_Lyp/'
#
# for file_num in range(1,5):
#
#     file1 = 'BPR_RecSys_Lyapanov_ML1M_finalepoch.csv'
#     #file2 = 'BPR_RecSys_Lyapanov_Foursq_finalepoch.csv'
#     file2 = 'BPR_RecSys_Lyapanov_FourSq_large_search_finalepoch_update_after_50.csv'
#     file3 = 'BPR_RecSys_Lyapanov_amazon_baby_finalepoch.csv'
#     file4 = 'BPR_RecSys_Lyapanov_Yelo_large_search_finalepoch.csv'
#
#
#     if file_num == 1:
#         file = file1
#     elif file_num == 2:
#         file = file2
#     elif file_num == 3:
#         file = file3
#     elif file_num == 4:
#         file = file4
#
#
#     file1_df = pd.read_csv(root_addr + file,header=None)
#     file1_df.columns = ['epoch','dim','lr','gamma','spec_pu','spec_qi','HR@5','HR@10']
#
#
#     grouped_df = file1_df.groupby("gamma")
#     maximums = grouped_df.max("HR@5")
#     maximums = maximums.reset_index()
#
#     a_normal = round(maximums["HR@5"][0],5)
#     a_g1 = round(maximums["HR@5"][1],5)
#     a_g2 = round(maximums["HR@5"][2],5)
#     a_g3 = round(maximums["HR@5"][3],5)
#
#     grouped_df = file1_df.groupby("gamma")
#     maximums = grouped_df.max("HR@10")
#     maximums = maximums.reset_index()
#
#     b_normal = round(maximums["HR@10"][0],5)
#     b_g1 = round(maximums["HR@10"][1],5)
#     b_g2 = round(maximums["HR@10"][2],5)
#     b_g3 = round(maximums["HR@10"][3],5)
#
#     cnt = np.array([a_normal, a_g1, a_g2, a_g3])
#     m = max(cnt)
#     result = np.where(cnt == max(cnt))
#
#
#     if file_num == 1:
#         ds = "ML-1M "
#     elif file_num == 2:
#         ds = 'Foursq '
#     elif file_num == 3:
#         ds = 'AmazonBaby '
#     elif file_num == 4:
#         ds = 'Yelp '
#
#     if result[0] == 0:
#         print(ds + "&" + '\\textbf{' + str(a_normal) + '}' + " & " + str(a_g1) + " & " + str(a_g2) + " & " + str(a_g3) + " & " + '-' + "\%" )
#     elif result[0] == 1:
#         r = round(100*(a_g1-a_normal)/a_normal,3)
#         print(ds + "&"  + str(a_normal)  + " & " + '\\textbf{' + str(a_g1) + "}" +" & " + str(a_g2) + " & " + str(a_g3) + " & " + str(r) + "\%" )
#     elif result[0] == 2:
#         r = round(100*(a_g2-a_normal)/a_normal,3)
#         print(ds + "&" + str(a_normal)  + " & " + str(a_g1) + " & "  + '\\textbf{' + str(a_g2) + "}" +" & " + str(a_g3) + " & " + str(r)+ "\%" )
#     elif result[0] == 3:
#         r = round(100*(a_g3-a_normal)/a_normal,3)
#         print(ds + "&"  + str(a_normal) + " & " + str(a_g1) + " & " + str(a_g2) + " & " + '\\textbf{' + str(a_g3) + "}" +" & "+ str(r))
#
#
#
#     cnt = np.array([b_normal, b_g1, b_g2, b_g3])
#     m = max(cnt)
#     result = np.where(cnt == max(cnt))
#
#     if result[0] == 0:
#         print("&" + '\\textbf{' + str(b_normal) + '}' + " & " + str(b_g1) + " & " + str(b_g2) + " & " + str(b_g3) + " & " + '-' + "\%" + " \\\\ \\hline")
#     elif result[0] == 1:
#         r = round(100*(b_g1-b_normal)/b_normal,3)
#         print("&"  + str(b_normal)  + " & " + '\\textbf{' + str(b_g1) + "}" +" & " + str(b_g2) + " & " + str(b_g3) + " & " + str(r) + "\%" + " \\\\ \\hline")
#     elif result[0] == 2:
#         r = round(100*(b_g2-b_normal)/b_normal,3)
#         print("&" + str(b_normal)  + " & " + str(b_g1) + " & "  + '\\textbf{' + str(b_g2) + "}" +" & " + str(b_g3) + " & " + str(r) + "\%" + " \\\\ \\hline")
#     elif result[0] == 3:
#         r = round(100*(b_g3-b_normal)/b_normal,3)
#         print("&" + str(b_normal) + " & " + str(b_g1) + " & " + str(b_g2) + " & " + '\\textbf{' + str(b_g3) + "}" +" & " + str(r) + "\\%" + " \\\\ \\hline")
#
#
#
# root_addr = '/home/yas/PycharmProjects/elliotNew/results/AML_Lyp/'
#
#
#
# for file_num in range(3,4):
#
#     #file1 = 'BPR_RecSys_Lyapanov_ML1M_finalepoch.csv'
#     #file2 = 'BPR_RecSys_Lyapanov_FourSq_large_search_finalepoch_update_after_50.csv'
#     file3 = 'BPR_RecSys_Lyapanov_Yelp_large_search_finalepoch_update_after_50.csv'
#     #file3 = 'BPR_RecSys_Lyapanov_amazon_baby_finalepoch.csv'
#     #file4 = 'BPR_RecSys_Lyapanov_Yelo_large_search_finalepoch.csv'
#
#
#     if file_num == 1:
#         file = file1
#     elif file_num == 2:
#         file = file2
#     elif file_num == 3:
#         file = file3
#     elif file_num == 4:
#         file = file4
#
#
#     file1_df = pd.read_csv(root_addr + file,header=None)
#     file1_df.columns = ['epoch','dim','lr','gamma','spec_pu','spec_qi','HR@5','HR@10']
#
#
#     grouped_df = file1_df.groupby("gamma")
#     maximums = grouped_df.max("HR@5")
#     maximums = maximums.reset_index()
#
#
#     a_normal = round(maximums["HR@5"][0],5)
#     a_g1 = round(maximums["HR@5"][1],5)
#     a_g2 = round(maximums["HR@5"][2],5)
#     a_g3 = round(maximums["HR@5"][3],5)
#     a_g4 = round(maximums["HR@5"][4],5)
#     a_g5 = round(maximums["HR@5"][5],5)
#     a_g6 = round(maximums["HR@5"][6],5)
#     a_g7 = round(maximums["HR@5"][7],5)
#     a_g8 = round(maximums["HR@5"][8],5)
#
#
#     grouped_df = file1_df.groupby("gamma")
#     maximums = grouped_df.max("HR@10")
#     maximums = maximums.reset_index()
#
#     b_normal = round(maximums["HR@10"][0],5)
#     b_g1 = round(maximums["HR@10"][1],5)
#     b_g2 = round(maximums["HR@10"][2],5)
#     b_g3 = round(maximums["HR@10"][3],5)
#     b_g4 = round(maximums["HR@10"][4],5)
#     b_g5 = round(maximums["HR@10"][5],5)
#     b_g6 = round(maximums["HR@10"][6],5)
#     b_g7 = round(maximums["HR@10"][7],5)
#     b_g8 = round(maximums["HR@10"][8],5)
#
#     cnt = np.array([a_normal, a_g1, a_g2, a_g3, a_g4, a_g5, a_g6, a_g7, a_g8])
#     m = max(cnt)
#     result = np.where(cnt == max(cnt))
#
#
#     if file_num == 1:
#         ds = "ML-1M "
#     elif file_num == 2:
#         ds = 'Foursq '
#     elif file_num == 3:
#         ds = 'AmazonBaby '
#     elif file_num == 4:
#         ds = 'Yelp '
#
#     if result[0] == 0:
#         print(ds + "&" + '\\textbf{' + str(a_normal) + '}' + " & " + str(a_g1) + " & " + str(a_g2) + " & " + str(a_g3) + " & " + str(a_g4) + " & " + str(a_g5) + " & " + str(a_g6) + " & " + str(a_g7) + " & " + str(a_g8) + " & " + '-' + "\%" )
#     elif result[0] == 1:
#         r = round(100*(a_g1-a_normal)/a_normal,3)
#         print(ds + "&"  + str(a_normal)  + " & " + '\\textbf{' + str(a_g1) + "}" +" & " + str(a_g2) + " & " + str(a_g3) + " & " + str(a_g4) + " & " + str(a_g5) + " & " + str(a_g6) + " & " + str(a_g7) + " & " + str(a_g8) + " & " + str(r) + "\%" )
#     elif result[0] == 2:
#         r = round(100*(a_g2-a_normal)/a_normal,3)
#         print(ds + "&" + str(a_normal)  + " & " + str(a_g1) + " & "  + '\\textbf{' + str(a_g2) + "}" +" & " + str(a_g3) + " & " + str(a_g4) + " & " + str(a_g5) + " & " + str(a_g6) + " & " + str(a_g7) + " & " + str(a_g8) + " & " + str(r)+ "\%" )
#     elif result[0] == 3:
#         r = round(100*(a_g3-a_normal)/a_normal,3)
#         print(ds + "&"  + str(a_normal) + " & " + str(a_g1) + " & " + str(a_g2) + " & " + '\\textbf{' + str(a_g3) + "}" + " & " + str(a_g4) + " & " + str(a_g5) + " & " + str(a_g6) + " & " + str(a_g7) + " & " + str(a_g8) +" & "+ str(r))
#     elif result[0] == 4:
#         r = round(100*(a_g4-a_normal)/a_normal,3)
#         print(ds + "&"  + str(a_normal) + " & " + str(a_g1) + " & " + str(a_g2) + " & " + str(a_g3)  + " & " + '\\textbf{' + str(a_g4) + "}" + " & " + str(a_g5) + " & " + str(a_g6) + " & " + str(a_g7) + " & " + str(a_g8) +" & "+ str(r))
#     elif result[0] == 5:
#         r = round(100*(a_g5-a_normal)/a_normal,3)
#         print(ds + "&"  + str(a_normal) + " & " + str(a_g1) + " & " + str(a_g2) + " & " + str(a_g3) + " & " + str(a_g4) + " & "  + '\\textbf{' + str(a_g5) + "}" + " & " + str(a_g6) + " & " + str(a_g7) + " & " + str(a_g8) +" & "+ str(r))
#     elif result[0] == 6:
#         r = round(100*(a_g6-a_normal)/a_normal,3)
#         print(ds + "&"  + str(a_normal) + " & " + str(a_g1) + " & " + str(a_g2) + " & " + '\\textbf{' + str(a_g3) + "}" + " & " + str(a_g4) + " & " + str(a_g5) + " & " + '\\textbf{' + str(a_g6)  + "}" + " & " + str(a_g7) + " & " + str(a_g8) +" & "+ str(r))
#     elif result[0] == 7:
#         r = round(100*(a_g7-a_normal)/a_normal,3)
#         print(ds + "&"  + str(a_normal) + " & " + str(a_g1) + " & " + str(a_g2) + " & " + '\\textbf{' + str(a_g3) + "}" + " & " + str(a_g4) + " & " + str(a_g5) + " & " + str(a_g6) + " & " + '\\textbf{' + str(a_g7) + "}" + " & " + str(a_g8) +" & "+ str(r))
#     elif result[0] == 8:
#         r = round(100*(a_g8-a_normal)/a_normal,3)
#         print(ds + "&"  + str(a_normal) + " & " + str(a_g1) + " & " + str(a_g2) + " & " + '\\textbf{' + str(a_g3) + "}" + " & " + str(a_g4) + " & " + str(a_g5) + " & " + str(a_g6) + " & " + str(a_g7) + " & " + '\\textbf{' + str(a_g8) + "}" +" & "+ str(r))
#
#
#
#
#     cnt = np.array([b_normal, b_g1, b_g2, b_g3, b_g4, b_g5, b_g6, b_g7, b_g8])
#     m = max(cnt)
#     result = np.where(cnt == max(cnt))
#
# if result[0] == 0:
#     print(ds + "&" + '\\textbf{' + str(a_normal) + '}' + " & " + str(a_g1) + " & " + str(a_g2) + " & " + str(
#         a_g3) + " & " + str(a_g4) + " & " + str(a_g5) + " & " + str(a_g6) + " & " + str(a_g7) + " & " + str(
#         a_g8) + " & " + '-' + "\%")
# elif result[0] == 1:
#     r = round(100 * (a_g1 - a_normal) / a_normal, 3)
#     print(ds + "&" + str(b_normal) + " & " + '\\textbf{' + str(a_g1) + "}" + " & " + str(a_g2) + " & " + str(
#         a_g3) + " & " + str(a_g4) + " & " + str(a_g5) + " & " + str(a_g6) + " & " + str(a_g7) + " & " + str(
#         a_g8) + " & " + str(r) + "\%")
# elif result[0] == 2:
#     r = round(100 * (a_g2 - a_normal) / a_normal, 3)
#     print(ds + "&" + str(a_normal) + " & " + str(a_g1) + " & " + '\\textbf{' + str(a_g2) + "}" + " & " + str(
#         a_g3) + " & " + str(a_g4) + " & " + str(a_g5) + " & " + str(a_g6) + " & " + str(a_g7) + " & " + str(
#         a_g8) + " & " + str(r) + "\%")
# elif result[0] == 3:
#     r = round(100 * (a_g3 - a_normal) / a_normal, 3)
#     print(ds + "&" + str(a_normal) + " & " + str(a_g1) + " & " + str(a_g2) + " & " + '\\textbf{' + str(
#         a_g3) + "}" + " & " + str(a_g4) + " & " + str(a_g5) + " & " + str(a_g6) + " & " + str(a_g7) + " & " + str(
#         a_g8) + " & " + str(r))
# elif result[0] == 4:
#     r = round(100 * (a_g4 - a_normal) / a_normal, 3)
#     print(ds + "&" + str(a_normal) + " & " + str(a_g1) + " & " + str(a_g2) + " & " + str(
#         a_g3) + " & " + '\\textbf{' + str(a_g4) + "}" + " & " + str(a_g5) + " & " + str(a_g6) + " & " + str(
#         a_g7) + " & " + str(a_g8) + " & " + str(r))
# elif result[0] == 5:
#     r = round(100 * (a_g5 - a_normal) / a_normal, 3)
#     print(ds + "&" + str(a_normal) + " & " + str(a_g1) + " & " + str(a_g2) + " & " + str(a_g3) + " & " + str(
#         a_g4) + " & " + '\\textbf{' + str(a_g5) + "}" + " & " + str(a_g6) + " & " + str(a_g7) + " & " + str(
#         a_g8) + " & " + str(r))
# elif result[0] == 6:
#     r = round(100 * (a_g6 - a_normal) / a_normal, 3)
#     print(ds + "&" + str(a_normal) + " & " + str(a_g1) + " & " + str(a_g2) + " & " + '\\textbf{' + str(
#         a_g3) + "}" + " & " + str(a_g4) + " & " + str(a_g5) + " & " + '\\textbf{' + str(a_g6) + "}" + " & " + str(
#         a_g7) + " & " + str(a_g8) + " & " + str(r))
# elif result[0] == 7:
#     r = round(100 * (a_g7 - a_normal) / a_normal, 3)
#     print(ds + "&" + str(a_normal) + " & " + str(a_g1) + " & " + str(a_g2) + " & " + '\\textbf{' + str(
#         a_g3) + "}" + " & " + str(a_g4) + " & " + str(a_g5) + " & " + str(a_g6) + " & " + '\\textbf{' + str(
#         a_g7) + "}" + " & " + str(a_g8) + " & " + str(r))
# elif result[0] == 8:
#     r = round(100 * (a_g8 - a_normal) / a_normal, 3)
#     print(ds + "&" + str(a_normal) + " & " + str(a_g1) + " & " + str(a_g2) + " & " + '\\textbf{' + str(
#         a_g3) + "}" + " & " + str(a_g4) + " & " + str(a_g5) + " & " + str(a_g6) + " & " + str(
#         a_g7) + " & " + '\\textbf{' + str(a_g8) + "}" + " & " + str(r))
#
#     cnt = np.array([b_normal, b_g1, b_g2, b_g3, b_g4, b_g5, b_g6, b_g7, b_g8])
#     m = max(cnt)
#     result = np.where(cnt == max(cnt))
#
#
# if result[0] == 0:
#     print(ds +"&" + '\\textbf{' + str(b_normal) + '}' + " & " + str(b_g1) + " & " + str(b_g2) + " & " + str(b_g3) + " & " + str(b_g4) + " & " + str(b_g5) + " & " + str(b_g6) + " & " + str(b_g7) + " & " + str(b_g8) + " & " + '-' + "\%"  + " \\\\ \\hline")
# elif result[0] == 1:
#     r = round(100*(b_g1-b_normal)/b_normal,3)
#     print(ds + "&"  + str(b_normal)  + " & " + '\\textbf{' + str(b_g1) + "}" +" & " + str(b_g2) + " & " + str(b_g3) + " & " + str(b_g4) + " & " + str(b_g5) + " & " + str(b_g6) + " & " + str(b_g7) + " & " + str(b_g8) + " & " + str(r) + "\%"  + " \\\\ \\hline")
# elif result[0] == 2:
#     r = round(100*(b_g2-b_normal)/b_normal,3)
#     print(ds + "&" + str(b_normal)  + " & " + str(b_g1) + " & "  + '\\textbf{' + str(b_g2) + "}" +" & " + str(b_g3) + " & " + str(b_g4) + " & " + str(b_g5) + " & " + str(b_g6) + " & " + str(b_g7) + " & " + str(b_g8) + " & " + str(r)+ "\%"  + " \\\\ \\hline")
# elif result[0] == 3:
#     r = round(100*(b_g3-b_normal)/b_normal,3)
#     print(ds + "&"  + str(a_normal) + " & " + str(b_g1) + " & " + str(b_g2) + " & " + '\\textbf{' + str(b_g3) + "}" + " & " + str(b_g4) + " & " + str(b_g5) + " & " + str(b_g6) + " & " + str(b_g7) + " & " + str(b_g8) +" & "+ str(r) + " \\\\ \\hline")
# elif result[0] == 4:
#     r = round(100*(b_g4-b_normal)/b_normal,3)
#     print(ds + "&"  + str(b_normal) + " & " + str(b_g1) + " & " + str(b_g2) + " & " + str(b_g3)  + " & " + '\\textbf{' + str(b_g4) + "}" + " & " + str(b_g5) + " & " + str(b_g6) + " & " + str(b_g7) + " & " + str(b_g8) +" & "+ str(r) + " \\\\ \\hline")
# elif result[0] == 5:
#     r = round(100*(b_g5-b_normal)/b_normal,3)
#     print(ds + "&"  + str(b_normal) + " & " + str(b_g1) + " & " + str(b_g2) + " & " + str(b_g3) + " & " + str(b_g4) + " & "  + '\\textbf{' + str(b_g5) + "}" + " & " + str(b_g6) + " & " + str(b_g7) + " & " + str(b_g8) +" & "+ str(r) + " \\\\ \\hline")
# elif result[0] == 6:
#     r = round(100*(b_g6-b_normal)/b_normal,3)
#     print(ds + "&"  + str(b_normal) + " & " + str(b_g1) + " & " + str(b_g2) + " & " + str(b_g3) + " & " + str(b_g4) + " & " + str(b_g5) + " & " + '\\textbf{' + str(b_g6)  + "}" + " & " + str(b_g7) + " & " + str(b_g8) +" & "+ str(r) + " \\\\ \\hline")
# elif result[0] == 7:
#     r = round(100*(b_g7-b_normal)/b_normal,3)
#     print(ds + "&"  + str(b_normal) + " & " + str(b_g1) + " & " + str(b_g2) + " & " + '\\textbf{' + str(b_g3) + "}" + " & " + str(b_g4) + " & " + str(b_g5) + " & " + str(b_g6) + " & " + '\\textbf{' + str(b_g7) + "}" + " & " + str(b_g8) +" & "+ str(r) + " \\\\ \\hline")
# elif result[0] == 8:
#     r = round(100*(b_g8-b_normal)/b_normal,3)
#     print(ds + "&"  + str(b_normal) + " & " + str(b_g1) + " & " + str(b_g2) + " & " + '\\textbf{' + str(b_g3) + "}" + " & " + str(b_g4) + " & " + str(b_g5) + " & " + str(b_g6) + " & " + str(b_g7)  + " & " + '\\textbf{' + str(b_g8) + "}" + " & "+ str(r) + " \\\\ \\hline")
