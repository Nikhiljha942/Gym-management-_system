# Gym-management-_system
# NIKHIL FITNESS CLUB - Gym Management System

Welcome to the **NIKHIL FITNESS CLUB** Gym Management System. This application is a desktop-based tool developed using Python and MySQL, designed to help manage gym member details such as personal information, membership details, and contact information.

## Table of Contents
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Usage](#usage)
- [Database Setup](#database-setup)
- [Future Enhancements](#future-enhancements)
- [Contributing](#contributing)
- [License](#license)

## Features
- **Member Management**: Add new gym members and store their essential details, including personal information, membership ID, and contact information.
- **Database Integration**: Connects to a MySQL database to securely store member information.
- **User Interface**: A graphical user interface created with `tkinter` for easy navigation and management of gym members.
- **Error Handling**: Error messages are displayed for any issues with database connections or operations.

## Technologies Used
- **Python**: Core programming language
- **Tkinter**: For the graphical user interface
- **MySQL**: Backend database for storing member information

## Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/Nikhiljha942/SHOPHEAVEN-WEBSITE.git
    ```

2. **Install dependencies**:
   - Ensure you have Python installed. Then install required libraries:
     ```bash
     pip install mysql-connector-python
     ```

3. **MySQL Database Setup**:
   - Create a MySQL database named `GymManagement`.
   - Create a table named `Members` with the following fields:
     - `MemberID`: `VARCHAR(20)`
     - `FirstName`: `VARCHAR(50)`
     - `LastName`: `VARCHAR(50)`
     - `DOB`: `DATE`
     - `JoinDate`: `DATE`
     - `MembershipID`: `VARCHAR(20)`
     - `PhoneNumber`: `VARCHAR(15)`
     - `Email`: `VARCHAR(100)`

4. **Configure Database Credentials**:
   - Update your database connection credentials in the code (username, password, and database name) to match your setup.

## Usage
1. **Run the Application**:
   - Start the program with:
     ```bash
     python <filename>.py
     ```
   
2. **Using the Interface**:
   - Add new members by filling out the required fields and clicking "Add Member".
   - View member details (coming soon).

## Database Setup

Create the MySQL table for storing member data:
```sql
CREATE DATABASE GymManagement;
USE GymManagement;

CREATE TABLE Members (
    MemberID VARCHAR(20) PRIMARY KEY,
    FirstName VARCHAR(50),
    LastName VARCHAR(50),
    DOB DATE,
    JoinDate DATE,
    MembershipID VARCHAR(20),
    PhoneNumber VARCHAR(15),
    Email VARCHAR(100)
);

