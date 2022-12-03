import pandas as pd
import matplotlib.pyplot as mp
import os
import pdb

directory_list = os.listdir()
import_list = []
for n in directory_list :
    if n.endswith('xlsx') :
        import_list.append(n)

df_list = []
#df_list.append(pd.read_excel(import_list[0]))
print(import_list)
data_start_row = 211


df_list = []
vertical_scale = []
inc = 0
row_to_keep = 10

output_path = "processed_data/"
date = '_031222'

print(output_path)

for n in import_list :
    # Append list with dataframe from csv
    df_list.append(pd.read_excel(n))

    # Extract the vertical scale factor
    vertical_scale.append(float(df_list[inc].iloc[13]['Column2']))
 
    # Extract the data
    df_list[inc] = df_list[inc].iloc[data_start_row:,:]

    # Giving columns descriptive names
    channel = import_list[inc].split('.')[0]
    df_list[inc] = df_list[inc].rename(columns={"Column1": "time", "Column2": channel})
    
    # Create a smaller dataframe 
    df_list[inc] = df_list[inc][df_list[inc].index % row_to_keep == 0]

    # Reseting the index
    df_list[inc] = df_list[inc].reset_index(drop=True)


     
    # Convert column content to float
    df_list[inc]['time'] = df_list[inc]['time'].astype(float)
    df_list[inc][channel] = df_list[inc][channel].astype(float)
    print("Done exporting " + channel)
    # Scaling the voltage 
    #df_list[inc][channel] = df_list[inc][channel] * vertical_scale[inc]

    # Export dataframes to csv-file
    df_list[inc].to_csv(output_path + channel + date + '.csv', index=False)  
    inc += 1

#pdb.set_trace()