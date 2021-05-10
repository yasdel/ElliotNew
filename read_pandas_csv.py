
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

read_ds = addr + 'Yelp_min/Yelp_checkins.txt'
write_ds = addr + 'Yelp_min/Yelp_checkins_del_tab.csv'

read_ds = addr + 'amazon_baby/all_interactions.tsv'
write_ds = addr + 'amazon_baby/all_interactions_del_tab.tsv'

#csv_data = pd.read_csv(read_ds, sep=' ')
csv_data = pd.read_csv(read_ds,sep = '\t', header=None)
print(csv_data.head())

print(csv_data.shape)

csv_data.columns = ['UserId','ItemId','time_stamp']
csv_data['new'] = csv_data.apply(lambda x: 1, axis=1)
columns_titles = ['UserId','ItemId','new','time_stamp']
csv_data=csv_data.reindex(columns=columns_titles)
print(csv_data.head())

print(csv_data.shape)
csv_data.to_csv(write_ds, index= False, sep = '\t', header=False)




