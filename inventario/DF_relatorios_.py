#!/usr/bin/env python
# coding: utf-8

# In[939]:


import pandas as pd
import os
from pathlib import Path
import json
from pprint import pprint
from datetime import date
from openpyxl import Workbook


# In[940]:


#adicionar nome do arquivo no df
#adicionar endereço mac
#adicionar gpu, ram e armazenamento (dps)
#criar uma planilha completona tb, com todos os dados pra caso necessario


# In[ ]:





# In[941]:


wd = Path('/mnt/c/Users/MarceloRamalhodeRodr/OneDrive - Hy Brazil Energia S.A/Documentos/Programas/json_relatorios')


# In[942]:


json_files = list(wd.glob('*.json'))


# In[943]:


j = 0

#lista_relatorios = []
#lista_computer_info = []
#lista_net_adapter = []
file_Net_adapter = []
file_Computer_info = []
file = []
for i in range (len(json_files)):
    lista_relatorios.append(str(json_files))
    if "ComputerInfo" in str(json_files[i]):
        #print(json_files[i])
        with open(json_files[i], 'rb') as f:
            file_Computer_info.append(json_files[i])
            file.append(json.load(f))
            j+=1
    else:
        file_Net_adapter.append(json_files[i])
            #print(str(json_files[j]))
            


# In[944]:


#type(json_files)
#type(file_Computer_info)


# In[945]:


#print(file_Computer_info)


# In[946]:


#len(file[5])
#list(lista_computer_info)


# In[947]:


#list(lista_net_adapter)


# In[948]:


print("Relatorios ao todo relatorios: ", len(json_files))
print("ComputerInfo relatorios: ", len(file_Computer_info))
print("NetAdapter relatorios: ", len(file_Net_adapter))


# In[949]:


pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)


# In[950]:


columns = [key for index, key in enumerate(df.columns)]


# In[951]:


df = pd.json_normalize(file)


# In[952]:


#print(df)


# In[953]:


df1 = df[['WindowsRegisteredOwner','BiosSeralNumber', 'CsCaption', 'CsManufacturer', 'CsSystemFamily', 'CsModel', 'CsProcessors', 'CsTotalPhysicalMemory', 'OsName','OsArchitecture','BiosManufacturer', 'BiosName','BiosBIOSVersion']]


# In[954]:


#print(df1)


# In[955]:


pd.DataFrame(data=df1, index=df.index)


# In[956]:


dataframe1 = pd.DataFrame(data=df1, index=df.index)


# In[957]:


#print(dataframe1)


# In[958]:


data = str(date.today())
file_name = ('HyBrazil_relatorio_maquinas_{}.xlsx'.format(data))
print(file_name)
#type(data)


# In[959]:


dataframe1.to_excel('/mnt/c/Users/MarceloRamalhodeRodr/OneDrive - Hy Brazil Energia S.A/Documentos/Programas/{}'.format(file_name))
#print('DataFrame is written to Excel File successfully.')


# In[960]:


#df1 = dataframe1.copy()
#with pd.ExcelWriter('file_name') as writer: 
#    dataframe1.to_excel(writer, sheet_name='Sheet_name_1')


# In[961]:


#infolist = list(df.values)
#print(infolist)


# In[962]:


#df.loc[:,'WindowsBuildLabEx']


# In[963]:


#with pd.ExcelWriter('output.xlsx',
#                    mode='a') as writer:  
#   df.to_excel(writer, sheet_name='Sheet_name_3')
#apend no excel existente hybrazil...


# In[964]:


#for s in file_Computer_info:
#    print(len(df.columns))


# In[965]:


#list(df.columns)


# In[966]:


#df[['WindowsBuildLabEx']]


# In[967]:


#df.index = index_


# In[968]:


#index_ = df.columns
#print(index_[192])


# In[969]:


#df[df['Name']==contractor]["Tick"].values


# In[970]:


type(file)


# In[ ]:





# In[ ]:





# In[ ]:




