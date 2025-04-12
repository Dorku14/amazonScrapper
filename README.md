# amazonScrapper

## Description
This application extracts product information from Amazon using web scraping techniques. The extracted data is stored in an SQLite database for further analysis and querying.

## Dependencies
To run this application, make sure to install the following dependencies:

- **Python 3.13**: Base language of the project.
- **Python Libraries**:
  - `requests`: For making HTTP requests.
  - `beautifulsoup4`: For parsing and extracting data from HTML.
  - `sqlite3`: For interacting with the SQLite database.
  - `notifications` (possibly implemented in [`notification.py`](notification.py)): For sending alerts or notifications.

## Database
The application uses SQLite as the database system. The database file is located in the directory `bd/productosAmazon.db`.

## Usage
1. Activate the virtual environment located in `.env/`:
   ```bash
   .env/Scripts/activate
## Install dependecies
pip install -r requirements.txt
## run app
python amazon.py

Project Structure
amazon.py: Main application file.
bd.py: Database management.
error.py: Error handling.
notification.py: Notification sending.
utils.py: Auxiliary functions.