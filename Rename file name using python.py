
# coding: utf-8

# In[17]:

import os
def rename_files():
    #(1)get the filenames from the folder - path of the folder
    file_list = os.listdir("/Users/yogeshsharma/Documents/UDACITY/prank")
    print(file_list)
    #define what is current directory
    saved_path = os.getcwd()
    print("The current working directory is"+saved_path)
    # change the directory 
    os.chdir("/Users/yogeshsharma/Documents/UDACITY/prank")
    #(2)rename each file in the folder
    for file_name in file_list:
    #file_name.translate is translate function
        os.rename(file_name,file_name.translate (None,"0123456789"))
    os.chdir(saved_path)
rename_files ()
    


# In[ ]:



