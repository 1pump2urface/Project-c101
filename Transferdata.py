import os 
import dropbox
from dropbox.files import WriteMode

class TransferData:
    def __init__ (self,access_token):
        self.access_token = access_token

    def upload_files(self, file_from , file_to):
        dbx = dropbox.Dropbox(self.access_token)
        for root,dirs,files in os.walk(file_from):
            for filename in files:
                localPath = os.path.join(root,filename)
                relativePath = os.path.relpath(localPath , file_from)
                dropboxPath = os.path.join(file_to , relativePath)
                with open(localPath,"rb") as f:
                    dbx.files_upload(f.read(), dropboxPath,mode = WriteMode("overwrite"))

def main():
    access_token = "soN3Fg8sAIgAAAAAAAAAAU_382seJyO9HzH-9qWD3WYYJ-MBWIlAwEbq1EyMrXXy"
    transferdata = TransferData(access_token)
    file_from = str(input("enter the folder path to transfer"))
    file_to = input("enter the full path to upload to dbx")
    transferdata.upload_files(file_from,file_to)
    print("file has been moved")

main()
        
