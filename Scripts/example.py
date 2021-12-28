import metadata as md
import os

def main():
    url = 'https://images.unsplash.com/photo-1569060368645-4ab30c8d8b0e?ixlib=rb-1.2.1&amp;ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&amp;auto=format&amp;fit=crop&amp;w=870&amp;q=80'
    filename = 'original_image.jpeg'
    new_filename = 'modified_image.jpeg'
    metadata = {
        'credit': 'Modified credit',
        'by-line': 'Modified by-line',
        'source': 'Modified source'
    }

    md.download_file(url, filename)
    md.change_metadata(filename, metadata, save_as=new_filename)
    published_url = md.upload_file(filename)
    print(published_url)

if __name__ == '__main__':
    main()
    print(md.read_metadata('original_image.jpeg'))
    
    # Delete `__pycache__` folder created
    os.system('rm -rf `find . -type d -name __pycache__`')
    