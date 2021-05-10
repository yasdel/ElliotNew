
import pandas as pd

root_addr = '/home/yas/PycharmProjects/elliotNew/results/AML_Lyp/'

file1 = 'BPR_RecSys_Lyapanov_ML1M_finalepoch.csv'
file2 = 'BPR_RecSys_Lyapanov_Foursq_finalepoch.csv'
file3 = 'BPR_RecSys_Lyapanov_amazon_baby_finalepoch.csv'
file4 = 'BPR_RecSys_Lyapanov_Yelp_finalepoch.csv'

file1_df = pd.read_csv(root_addr + file4,header=None)
file1_df.columns = ['epoch','dim','lr','gamma','spec_pu','spec_qi','HR@5','HR@10']

print(file1_df)

grouped_df = file1_df.groupby("gamma")
maximums = grouped_df.max("HR@5")
maximums = maximums.reset_index()
print(maximums)

grouped_df = file1_df.groupby("gamma")
maximums = grouped_df.max("HR@10")
maximums = maximums.reset_index()
print(maximums)