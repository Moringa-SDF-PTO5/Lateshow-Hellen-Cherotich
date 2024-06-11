Late Show API


Description


The Late Show API is a Flask-based API designed to track episodes of a late-night talk show, along with their guests and appearances.

It allows users to retrieve information about episodes, guests, and create new appearances.


Features

Retrieve a list of episodes

Get details of a specific episode by its ID

Retrieve a list of guests

Create a new appearance for a guest on an episode


Setup


Clone this repository to your local machine:



bash

Copy code


git clone <repository_url>


Navigate to the project directory:




bash

Copy code

cd lateshow-firstname-lastname


Set up a virtual environment:


bash

Copy code


python -m venv venv

Activate the virtual environment:


On Windows:


bash

Copy code

venv\Scripts\activate


On macOS and Linux:



bash

Copy code

source venv/bin/activate

Install the dependencies:



bash

Copy code

pip install -r requirements.txt

Set up the database:


Update the config.py file with your database credentials.



Initialize the database and perform migrations:


bash

Copy code

flask db init

flask db migrate

flask db upgrade

Run the application:



bash

Copy code

python run.py

Usage

Retrieve a list of episodes: Send a GET request to /episodes.


Get details of a specific episode by its ID: Send a GET request to /episodes/<id>, replacing <id> with the episode ID.


Retrieve a list of guests: Send a GET request to /guests.


Create a new appearance for a guest on an episode: Send a POST request to /appearances with the following JSON payload:



json

Copy code

{

  "rating": 5,
  
  "episode_id": 100,
  
  "guest_id": 123
}


Replace rating, episode_id, and guest_id with appropriate values.





License
This project is licensed under the MIT License.
