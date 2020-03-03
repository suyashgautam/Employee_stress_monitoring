from azure.storage.blob import BlockBlobService, PublicAccess
import os

def download():

    # Create the BlockBlockService that is used to call the Blob service for the storage account
    block_blob_service = BlockBlobService(account_name='<account name>', account_key='<account key>')

    # Create a container called 'quickstartblobs'.
    container_name ='<container name>'
    block_blob_service.create_container(container_name)

    # name of the container
    generator = block_blob_service.list_blobs(container_name)

    # code below lists all the blobs in the container and downloads them one after another
    dpath="C:\\Users\\<user name>\\Desktop\\data\\" #replace <user name> with your user name

    for blob in generator:
        print(blob.name)
        print("{}".format(blob.name))
        # check if the path contains a folder structure, create the folder structure
        if "/" in "{}".format(blob.name):
            print("there is a path in this")
            # extract the folder path and check if that folder exists locally, and if not create it
            head, tail = os.path.split("{}".format(blob.name))
            print(head)
            print(tail)
            if (os.path.isdir(dpath + "\\" + head)):
                # download the files to this directory
                print("directory and sub directories exist")
                block_blob_service.get_blob_to_path('suyash', blob.name, dpath + "\\" + head + "\\" + tail)
            else:
                # create the diretcory and download the file to it
                print("directory doesn't exist, creating it now")
                os.makedirs(dpath + "\\" + head, exist_ok=True)
                print("directory created, download initiated")
                block_blob_service.get_blob_to_path('suyash', blob.name, dpath + "\\" + head + "\\" + tail)
        else:
            block_blob_service.get_blob_to_path('suyash', blob.name, blob.name)
