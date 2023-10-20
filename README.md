# Insurance Management API

![App Logo](app-logo.png)

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [Database](#database)
- [Authentication](#authentication)
- [Testing](#testing)
- [Contributing](#contributing)
- [License](#license)
- [Backlog](#backlog)

## Overview

The Insurance Management API is a powerful tool for insurance companies and agents to manage policies, clients, and reminders efficiently. This API is built using Django Rest Framework and provides endpoints to perform various actions related to insurance management.

## Features

- Create, update, and delete clients.
- Create, update, and delete policies for clients.
- Automatically generate reminders for policy renewals.
- Search and filter clients and policies.
- Secure authentication system.

## Installation

To run this API on your local machine, follow these steps:

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/Bima-manager.git

2. Navigate to the project directory

    cd insurance-management-api

3. Create a virtual environment

    `python -m venv venv`

    Activate the virtual environments;

    `source venv/bin/activate`

4. Install the dependancies

    `pip install -r requirements.txt`

5. Run the Database migrations

    `python manage.py migrate`

6. Start the development server

    `python manage.py runserver`

The API should now be running locally at http://localhost:8000/.

## Backlog
 Add feature to send notifications when a policy expires.