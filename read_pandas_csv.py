
import pandas as pd

addr = '/home/yas/PycharmProjects/elliotNew/data/'
read_ds =  addr + 'AmazonDigMusic/ratings_Digital_Music.csv'
write_ds =  addr+ 'AmazonDigMusic/ratings_Digital_Music_deli_tab.csv'

read_ds =  addr + 'Epinions/ratings_data.txt'
write_ds =  addr+ 'Epinions/ratings_data_deli_tab.csv'

read_ds = addr + 'Foursq/dataset_ubicomp2013_checkins.txt'
write_ds =  addr+ 'Foursq/dataset_ubicomp2013_checkins_deli_tab.csv'

read_ds = addr + 'AmazonOffice/ratings_Office_Products.csv'
write_ds = addr + 'AmazonOffice/ratings_Office_Products_del_tab.csv'


#csv_data = pd.read_csv(read_ds, sep=' ')
csv_data = pd.read_csv(read_ds,sep = ',')
print(csv_data.head())

print(csv_data.shape)

#csv_data.columns = ['UserId','ItemId']
#csv_data['new'] = csv_data.apply(lambda x: 1, axis=1)
#print(csv_data)

csv_data.to_csv(write_ds, index= False, sep = '\t', header=False)




