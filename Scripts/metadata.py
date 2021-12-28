from iptcinfo3 import IPTCInfo
from filestack import Client
import requests
import os

def read_metadata(filename: str):
    '''
    Reads a file metadata

    Parameter: File path as a str
    Returns: Returns IPTCInfo object filled with metadata from the given image
    file.
    '''
    info = IPTCInfo(f'Images/{filename}')
    return info

def change_metadata(filename: str, new_metadata: dict, save_as=''):
    '''
    Changes a file metadata and if a name is provided, creates a copy of the specified file with the given name.

    Parameter: File path as a str, new_metadata as dictiorary and an optional name for a new file with the specified metadata.
    Returns: Returns IPTCInfo object filled with the new metadata from the given image.
    file.
    '''
    info = IPTCInfo(f'Images/{filename}')

    for item in new_metadata:
        info[item] = new_metadata[item]

    info.save_as(f'Images/{save_as}') if save_as else info.save()

    # Delete *.jpeg~ files created
    os.system('rm -rf `find . -type f -name *.jpeg~`')

    return(info)

def download_file(url: str, filename: str):
    '''
    Downloads an image from a url. The  image is saved with a designated name inside 'Images' folder

    Parameter: Image url str, and a name for the saved Image.
    Returns: Returns the image path.
    '''
    with requests.get(url) as req:
        with open(f'Images/{filename}', 'wb') as f:
            for chunk in req.iter_content(chunk_size=8192):
                if chunk:
                    f.write(chunk)
        print(f'File saved as: {filename}')
        return f'Images/{filename}'

def upload_file(filename: str):
    '''
    Uploads a file to Filestack. Requires an 'api_key' from Filestack set up in config.py.

    Parameter: File path as a str.
    Returns: Returns the link of the image on Filestack servers.
    '''
    
    from local_settings import API_KEY
    client = Client(API_KEY)

    new_filelink = client.upload(filepath=f'Images/{filename}')
    print(f'File {filename} uploaded to Filestack server with link: {new_filelink.url}')

    with open('Images/index.txt', 'a') as f:
        f.write('\n')
        f.write(f'{filename}: {new_filelink.url}')

    return new_filelink.url