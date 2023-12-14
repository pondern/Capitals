# Capitals - Flashcard App

Welcome to the Capitals Flashcard App designed to help you learn the capitals of different countries!

## Overview

This Python-based flashcard application allows users to test their knowledge of country capitals. It utilizes SQL with the Peewee ORM to manage data and provides a simple interface for quizzing users on country capitals. Users can also contribute by adding new flashcards for countries not already in the app's database.

## Setup and Usage

### Installation

1. **Clone the repository:**

   ```
   git clone git@github.com:pondern/Capitals.git
   cd Capitals
   ```

2. **Install the required dependencies:**

   ```
   pipenv install
   ```

3. **Add your User:**

   In psql, add worldcapitals as a superuser, or else edit main.py to create your own user:

   ```
   db = PostgresqlDatabase('countries', user='<USERNAME>', password='<PASSWORD>',
                       host='localhost', port=5432)
   ```

4. **Seed Initial Data:**

   Before using the app, seed the initial data by running:

   ```
   python seed.py
   ```

### Usage

- **Run the app using the following command:**

  ```
  python flashcards.py
  ```

### How to Use

1. **Quiz Mode:** Test your knowledge by answering country capital questions.
2. **Add New Flashcards:** If a country is missing, use the option to add a new flashcard.

## Dependencies

- Python 3.x
- Peewee ORM
- PostgreSQL

## Author

Nic Ponder
