# Image Metadata

This is a repo to facilitate the use of metadata in `.jpeg` images and host them on Filestack. 

## SETUP
- The python library needed to use this repo is iptcinfo3. just type in your python environment `pip install iptcinfo3`. You can also skip this repo and use that library directly.
- Filestack is a service to host files and share them with a link. It has an easy to use API and a free option (with limitations). To upload files, create an account at [Filestack](https://dev.filestack.com/) and install their pip library with `pip install --upgrade filestack-python`.

Because this is an external service, for upload to work you need to fill the API_KEY variable in 'local_settings.py'.

If you want to sync changes but not your API key, just go to the 'Scripts' folder in terminal and type `git update-index --skip-worktree local_settings.py`. This will "ignore changes to that file, both local and upstream" as stated in this [Stack Overflow Question](https://stackoverflow.com/questions/4348590/how-can-i-make-git-ignore-future-revisions-to-a-file).

## Custom Scripting

Folder 'Scripts' is not tracked by git, so it will only update files originally in the repo. Because of this, if you want to test or write your own code, you can create a file inside said folder and it will not be tracked by git.

File 'Scripts/example.py' can be used as a guide to use all four methods in this repo.