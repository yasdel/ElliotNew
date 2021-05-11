
import pandas as pd
import numpy as np

root_addr = '/home/yas/PycharmProjects/elliotNew/results/AML_Lyp/'

for file_num in range(1,5):

    file1 = 'BPR_RecSys_Lyapanov_ML1M_finalepoch.csv'
    file2 = 'BPR_RecSys_Lyapanov_Foursq_finalepoch.csv'
    file3 = 'BPR_RecSys_Lyapanov_amazon_baby_finalepoch.csv'
    file4 = 'BPR_RecSys_Lyapanov_Yelo_large_search_finalepoch.csv'


    if file_num == 1:
        file = file1
    elif file_num == 2:
        file = file2
    elif file_num == 3:
        file = file3
    elif file_num == 4:
        file = file4


    file1_df = pd.read_csv(root_addr + file,header=None)
    file1_df.columns = ['epoch','dim','lr','gamma','spec_pu','spec_qi','HR@5','HR@10']


    grouped_df = file1_df.groupby("gamma")
    maximums = grouped_df.max("HR@5")
    maximums = maximums.reset_index()

    a_normal = round(maximums["HR@5"][0],5)
    a_g1 = round(maximums["HR@5"][1],5)
    a_g2 = round(maximums["HR@5"][2],5)
    a_g3 = round(maximums["HR@5"][3],5)

    grouped_df = file1_df.groupby("gamma")
    maximums = grouped_df.max("HR@10")
    maximums = maximums.reset_index()

    b_normal = round(maximums["HR@10"][0],5)
    b_g1 = round(maximums["HR@10"][1],5)
    b_g2 = round(maximums["HR@10"][2],5)
    b_g3 = round(maximums["HR@10"][3],5)

    cnt = np.array([a_normal, a_g1, a_g2, a_g3])
    m = max(cnt)
    result = np.where(cnt == max(cnt))


    if file_num == 1:
        ds = "ML-1M "
    elif file_num == 2:
        ds = 'Foursq '
    elif file_num == 3:
        ds = 'AmazonBaby '
    elif file_num == 4:
        ds = 'Yelp '

    if result[0] == 0:
        print(ds + "&" + '\\textbf{' + str(a_normal) + '}' + " & " + str(a_g1) + " & " + str(a_g2) + " & " + str(a_g3) + " & " + '-' + "\%" )
    elif result[0] == 1:
        r = round(100*(a_g1-a_normal)/a_normal,3)
        print(ds + "&"  + str(a_normal)  + " & " + '\\textbf{' + str(a_g1) + "}" +" & " + str(a_g2) + " & " + str(a_g3) + " & " + str(r) + "\%" )
    elif result[0] == 2:
        r = round(100*(a_g2-a_normal)/a_normal,3)
        print(ds + "&" + str(a_normal)  + " & " + str(a_g1) + " & "  + '\\textbf{' + str(a_g2) + "}" +" & " + str(a_g3) + " & " + str(r)+ "\%" )
    elif result[0] == 3:
        r = round(100*(a_g3-a_normal)/a_normal,3)
        print(ds + "&"  + str(a_normal) + " & " + str(a_g1) + " & " + str(a_g2) + " & " + '\\textbf{' + str(a_g3) + "}" +" & "+ str(r))



    cnt = np.array([b_normal, b_g1, b_g2, b_g3])
    m = max(cnt)
    result = np.where(cnt == max(cnt))

    if result[0] == 0:
        print("&" + '\\textbf{' + str(b_normal) + '}' + " & " + str(b_g1) + " & " + str(b_g2) + " & " + str(b_g3) + " & " + '-' + "\%" + " \\\\ \\hline")
    elif result[0] == 1:
        r = round(100*(b_g1-b_normal)/b_normal,3)
        print("&"  + str(b_normal)  + " & " + '\\textbf{' + str(b_g1) + "}" +" & " + str(b_g2) + " & " + str(b_g3) + " & " + str(r) + "\%" + " \\\\ \\hline")
    elif result[0] == 2:
        r = round(100*(b_g2-b_normal)/b_normal,3)
        print("&" + str(b_normal)  + " & " + str(b_g1) + " & "  + '\\textbf{' + str(b_g2) + "}" +" & " + str(b_g3) + " & " + str(r) + "\%" + " \\\\ \\hline")
    elif result[0] == 3:
        r = round(100*(b_g3-b_normal)/b_normal,3)
        print("&" + str(b_normal) + " & " + str(b_g1) + " & " + str(b_g2) + " & " + '\\textbf{' + str(b_g3) + "}" +" & " + str(r) + "\\%" + " \\\\ \\hline")



