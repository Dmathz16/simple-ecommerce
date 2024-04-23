# Simple E-commerce Web Application (Backend)

## How to run?
1. Open cmd/terminal then cd to this project.
   ```cmd
   cd PATH_OF_THE_PROJECT
   ```
2. Generate and activate virtual environment:
   ```cmd
   py -3 -m venv .venv
   .venv\Scripts\activate
   ```
3. Install required modules:
    ```cmd
   pip install -r requirements.txt
    ```
4. Generate mysql database (make sure the mysql server is running):
    ```cmd
   python application/db.py
   ```
5. Run project:
   ```cmd
   flask --app application run --debug
   ```
6. Open [application](http://127.0.0.1:5000/)
