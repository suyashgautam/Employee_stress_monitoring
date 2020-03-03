import os, uuid, sys
from azure.storage.blob import BlockBlobService, PublicAccess

def upload_files(hello12):
    #replace account_name with your azure storage account name and account key with your key

    block_blob_service = BlockBlobService(account_name='<Enter account name>',
                                          account_key='<Enter account key>')


    # Create a container called 'quickstartblobs'.
    container_name = '<Enter container name>'
    block_blob_service.create_container(container_name)

    # Set the permission so the blobs are public.
    block_blob_service.set_container_acl(container_name, public_access=PublicAccess.Container)

    path12="C:\\Users\\<user name>\\Desktop\\project\\pics\\"+hello12 #replace <user name> with your user name for the testing computer
    print(path12)
    for file in os.listdir(path12):
        
        #path12 = os.path.abspath(os.path.dirname(file)) + "\\pics\\" + hello12 + "\\" + file
        path12=path12+'\\'+file
        
        block_blob_service.create_blob_from_path(container_name, "pics"+'\\'+hello12 + '\\' + file, path12)
