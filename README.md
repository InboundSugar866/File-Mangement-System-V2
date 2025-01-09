# M7011E: File Management System for my home server.

## Description
I have designed and developed a file management web application using Django that enables users to add, update, and delete various types of files, including PDFs, images, documents, audio, and video files.

- User Registration: Allows users to register to upload files, while already uploaded files can be downloaded without logging in.

- Add File: Enables users to add a title, description, and upload files in any supported format.

- Edit File: Permits users to modify the details of uploaded files.

- Delete File: Allows users to remove files they have uploaded.

- Profile Management: Users can edit their profile description and details.

- Django Admin Interface: Provides site administrators with the ability to view, add, edit, and delete any file or user on the application.



## Startup
```bash
python3 -m venv venv
source venv/bin/activate
pip install requirements.txt
python3 manage.py runserver
```
