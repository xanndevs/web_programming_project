<p align="center"><img src="https://raw.githubusercontent.com/xanndevs/web_programming_project/29aeeadd62a81a0125a871e05c0532203fb22bea/app/static/images/mobile-logo.png" width="200" ></p>
<h1 align="center" style="border:none; font-size:25px">Video Streaming & Uploading Platform</h1>

## Introduction
- **Objective:** Develop a web application using Flask, a lightweight Python web framework, for managing and displaying TV shows and their episodes.
- **Key Features:** User-friendly interface for adding, deleting and viewing shows and episodes, with support for uploading thumbnails and videos.

## Installation
Enter those lines to your terminal and you should be good to go.
```bash
git clone https://github.com/xanndevs/web_programming_project.git

cd web_programming_project
python -m venv venv

#on Windows
venv/Scripts/activate
#on Linux
venv/bin/activate

pip install -r ./requirements.txt
```
To run the application;
```bash
python main.py
```

## Technologies Used
- **Backend:** Python with Flask to serve the app and manage the routings of the web app.

- **Frontend:** HTML, CSS and JavaScript (jQuerry used).

- **Database:** SQLite for storing details about shows & episodes.

## Folder Structure
- **Root Directory:** Configuration files (`config.py`), build info for some cloud deployment services (`Procfile`, `wsgi.py`), and other files (`README.md`, `LICENSE`, etc.).

- **app Directory:** Contains application-specific logic, including models (`models.py`) and routes (`routes.py`), as well as directories for static assets (`static`) and HTML templates (`templates`).

- **migrations Directory:** Contains SQLAlchemy related files.

- **uploads Directory:** All the thumbnail and video files for shows & videos.

## Key Components
1. **Database Models (`models.py`):**
   - Defines SQLAlchemy models for `Show` and `Episode`.

   - Establishes a one-to-many relationship between shows and episodes.
   
2. **Route Handling (`routes.py`):**
   - Defines Flask routes for rendering HTML templates and handling form submissions.

   - Handles functionalities like adding shows and episodes, viewing show details, and watching episodes.

3. **Frontend Styling (`styles.css`):**
   - Customizes the appearance of HTML templates using CSS.

   - Ensures a visually appealing and intuitive user interface.

## Functionality Highlights
- **Adding Shows:**
  - Users can add new shows via a web form.

  - Support for uploading show titles, descriptions and thumbnails.
  <p><img src="https://raw.githubusercontent.com/xanndevs/web_programming_project/29aeeadd62a81a0125a871e05c0532203fb22bea/app/static/images/mobile-logo.png" width="200" ></p>

- **Adding Episodes:**
  - Again users can add new episodes via a web form.

  - Support for uploading episode titles, descriptions, videos.
  <p><img src="https://raw.githubusercontent.com/xanndevs/web_programming_project/29aeeadd62a81a0125a871e05c0532203fb22bea/app/static/images/mobile-logo.png" width="200" ></p>

- **Viewing Show Details and Episodes:**
  - Users can view details of each show, including its description and associated episodes.

  - Episodes can be watched directly from the web application.
  <p><img src="https://raw.githubusercontent.com/xanndevs/web_programming_project/29aeeadd62a81a0125a871e05c0532203fb22bea/app/static/images/mobile-logo.png" width="200" ></p>

- **Deleting Shows:**
  - Users can delete shows with a single click (which is a bad idea if the app is gonna be global).

  - Deleting a show also deletes all the episodes inside of the show.
  <p><img src="https://raw.githubusercontent.com/xanndevs/web_programming_project/29aeeadd62a81a0125a871e05c0532203fb22bea/app/static/images/mobile-logo.png" width="200" ></p>

  - **Deleting Episodes:**
  - Users can delete episodes with a single click.
  <p><img src="https://raw.githubusercontent.com/xanndevs/web_programming_project/29aeeadd62a81a0125a871e05c0532203fb22bea/app/static/images/mobile-logo.png" width="200" ></p>
