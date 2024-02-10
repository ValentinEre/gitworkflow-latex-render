import os
from pydrive2.auth import GoogleAuth
from pydrive2.drive import GoogleDrive

def get_drive():
    gauth = GoogleAuth()
    gauth.LocalWebserverAuth()

    drive = GoogleDrive(gauth)

    return drive

def find_pdf_files(directory):
    pdf_files = []

    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".pdf"):
                pdf_files.append(os.path.join(file))

    return pdf_files

def send_pdf_to_disk(files,my_drive):
    for file_pdf in files:
        file = my_drive.CreateFile({'title': f'{file_pdf}'})
        file.SetContentFile(f'{file_pdf}')
        file.Upload()


if __name__ == "__main__":
    send_pdf_to_disk(find_pdf_files("."),get_drive())
