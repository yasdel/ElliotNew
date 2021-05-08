
import pandas as pd

addr = '/home/yas/PycharmProjects/elliotNew/data/'
read_ds =  addr + 'AmazonDigMusic/ratings_Digital_Music.csv'
write_ds =  addr+ 'AmazonDigMusic/ratings_Digital_Music_deli_tab.csv'

#read_ds =  addr + 'Epinions/ratings_data.txt'
#write_ds =  addr+ 'Epinions/ratings_data_deli_tab.csv'

csv_data = pd.read_csv(read_ds)
print(csv_data.head())

print(csv_data.shape)

csv_data.to_csv(write_ds, index= False, sep = '\t')




