# Interview.AI - AI bot who takes interview


<!--   <h1> <img height="100" width="250" alt="Interview.AI" src="https://user-images.githubusercontent.com/71089075/222932602-39a29a61-7f71-4d48-a120-0bf37d851976.png"> </h1> -->
Interview.Ai is an website with AI interviewing that helps individuals with social anxiety or introvert personalities who wants to gain confidence in interviewing situations. It also helps professionals seeking to improve their interviewing skills.

 # About
  It uses Deepfake videos of known personalities for interviewing individuals which gives them the confidence.

  - Takes Interview of individuals
  - Generates Report based on the interview
  - Provides recorded video of interview
  <br>
  Built with ❤️ for Innerve 7.0 Hackathon.


## Team Name - InspiredCoder

#### Team Members :

- [Siddhiraj Kolwankar](https://github.com/Kolwankar-Siddhiraj)
- [Pankaj Jaiswal](https://github.com/PankajJaisu)
- [Dhanshree](https://github.com/dhanshree)
- [Nilesh Gawli](https://github.com/nileshgawli)

## Tech Stack

- Frontend

  <img alt="HTML" src="https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white"/>
  <img alt="CSS" src="https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white"/> 
    <img alt="Bootstrap" src="https://img.shields.io/badge/bootstrap%20-%23563D7C.svg?&style=for-the-badge&logo=bootstrap&logoColor=white"/>
  <img alt="JavaScript" src="https://img.shields.io/badge/JavaScript-323330?style=for-the-badge&logo=javascript&logoColor=F7DF1E"/>
  <img alt="JQuery" src="https://img.shields.io/badge/jQuery-0769AD?style=for-the-badge&logo=jquery&logoColor=white"/> 

- Server

  <img alt="Django" src="https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white"/>
  <img alt="Django" src="https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white"/> 
  <img alt="Python" src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white"/>
  
  ## 👇 Prerequisites

Before installation, please make sure you have already installed the following tools:

- [Python](https://www.python.org/downloads/release/python-3916/)
- [PostgreSQL](https://www.postgresql.org/download/)

## 🛠️ Installation

1. Clone Mingle

bash
  git clone https://github.com/Team-InspiredCoder/InspiredCoder_Innverve_07.git


2. Move into the project

bash
  cd my-project/


3. Create environment and activate it.

bash
  # install environment package
  pip install virtualenv

  # create environment
  virtualenv virtualenv_name

  # activate virtual environment
  # Windows
  venv\Scripts\activate
  # Linux
  source venv/bin/activate
  # Mac os
  source venv/bin/activate


4. Install packages.

bash
pip install -r requirements.txt


5. To connect to PostgresSQL database rename .env.sample to .env file inside project directory and add the below variables in it.

python
DB_NAME= db_name
DB_USER= db_username
DB_PASSWORD= db_password
DB_HOST= db_host
DB_PORT= db_port


6. Run Django app.

bash
# runserver
python manage.py runserver


7. Apply database migrations

bash
# migrate changes
python manage.py makemigrations
python manage.py migrate


<br/>
<br/>
<div align="center">
  <img src="https://forthebadge.com/images/badges/built-with-love.svg">
  <img src="https://forthebadge.com/images/badges/made-with-python.svg">
</div>
