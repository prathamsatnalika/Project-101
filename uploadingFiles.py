import dropbox
import os


class TransferData:
    def __init__(self, access_token):
        self.aT = access_token

    def upload_file(self, file_from):
        db = dropbox.Dropbox(self.aT)
        fileName = os.path.split(
            file_from)[1]

        dropbox_file = '/CloudStorage/'+fileName

        with open(file_from, "rb") as f:
            db.files_upload(f.read(), dropbox_file,
                            mode=dropbox.files.WriteMode.overwrite)


AToken = "sl.ArS2rG_co_X3eSxdnce0i7XZyWbgtiuwjUcHIIV7uHSN2pDX0bjSJBzbScaSOaQkl3CW8yYfGYr2vMbY2xfzWqfbfU2IDXsevpYCDPVUEtjqT7_HR_PJpvtGbLEMnOgOEHqUNuY"

cloudStoring = TransferData(AToken)

fileFrom = input("Please Give the File Path To Transfer ")

while(os.path.isfile(fileFrom) == False):
    print("Pls Give The Path Of A File")
    fileFrom = input("Please Give the File Path To Transfer ")

cloudStoring.upload_file(fileFrom)

print("Files Have Been Stored On Dropbox ;)")
