import re
import pandas  as pd
# from geopy import geocoders
import geocoder
import time

df = pd.read_excel('./fun.xlsx', skip_blank_lines=False)
print(df)
new_df = pd.DataFrame({'Geo ID':df['city'].iloc[::6].values,'Latitude':df['city'].iloc[1::6].values,
	'Logtitude':df['city'].iloc[2::6].values, 'Country':df['city'].iloc[3::6].values,
	'State':df['city'].iloc[4::6].values, 'Timezone':df['city'].iloc[5::6].values})

new_df.to_excel('./sample.xlsx',index = False)

# df = pd.read_excel('./exist1.xlsx')
# df1 = df[df['geo_id'] != 'None']
# df1.to_excel('./nonempty.xlsx',index =False)