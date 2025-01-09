# M7011E: File Management System for my home server.

## Description
I have designed and developed a file management web application using Django that enables users to add, update, and delete various types of files, including PDFs, images, documents, audio, and video files.

- User Registration: Allows users to register to upload files.

- Add File: Enables users to add a title, description, and upload files in any supported format in the ```files``` folder.

- File Detail: More file description.

- File Tags: Allows the users to add specific tags to a file in order to find them more easily.

- Django Admin Interface: Provides site administrators with the ability to view, add, edit, and delete any file or user on the application.
 
Warning: for security reasons, the user must be part of a group to view and edit files and tags (named Standard here).



I used the ```drf_spectacular``` for better usage of the api.

Please note that in order to upload or modify a file, using PostMan is necessary as Swagger did not allow me to place hyperlinks as easily. All the rest is accessible through Swagger.



## Startup
```bash
python3 -m venv venv
source venv/bin/activate
pip install requirements.txt
python3 manage.py runserver
```
