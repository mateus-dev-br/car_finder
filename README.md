# 🚗 Car Finder - C2S Technical Challenge

This project was developed as part of the technical challenge for the Python Developer position at C2S.

It is a command-line application featuring a virtual agent, communication via a custom MCP (socket) protocol, and data persistence using SQLAlchemy.

---

## 📚 Overview

- Vehicle data model with 10+ attributes
- Database seeded with 100 fictional vehicles
- Client-server communication using TCP sockets (MCP protocol)
- Interactive virtual agent via terminal
- Modular, testable, and well-organized codebase

---

## 🧪 Tech Stack

- Python 3.10+
- SQLAlchemy
- Faker
- Socket (TCP)
- Pytest

---

## 📁 Project Structure
   ```bash
   car_finder/
   ├── app/
   │   ├── client/        # Virtual agent (TCP client)
   │   │   └── agent.py
   │   ├── db/            # DB connection and seed logic
   │   │   ├── constants.py
   │   │   └── seed.py
   │   ├── models/        # Car data model
   │   │   └── car.py
   │   ├── server/        # MCP server
   │   │   └── server.py
   │   └── tests/         # Unit and integration tests
   │       ├── test_agent.py
   │       ├── test_count.py
   │       ├── test_filters.py
   │       └── test_invalid_inputs.py
   ├── cars.db            # SQLite database
   ├── run.py             # Main command-line interface
   ├── requirements.txt
   └── README.md
   ```

---

## ⚙️ Installation

1. Clone the repository:

   Visit the [repository on GitHub](https://github.com/mateus-dev-br/car_finder) and follow the instructions to clone it to your local machine.

2. Create and activate a virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # macOS/Linux
   venv\Scripts\activate     # Windows


3. Install the dependencies:
    ```bash
    pip install -r requirements.txt

## ▶️ How to Run
All commands are executed via ``run.py``:

| Command                | Description                              |
| ---------------------- | ---------------------------------------- |
| `python run.py seed`   | Populate the database with 100 fake cars |
| `python run.py server` | Start the MCP server (port 5050)         |
| `python run.py agent`  | Launch the virtual agent in the terminal |



## 🧠 Example Interaction
   ```bash
   python run.py agent
   ```

   ```yaml
   🚗 Hello! Let's find your ideal car.

   Which brand are you looking for?
   Available options: Honda, Ford, Toyota
   Type a brand: honda

   Models available for Honda: Civic, Hr-v, Fit
   Type a model: hr-v

   What is your preferred fuel type?
   Available options: Flex, Gasoline, Diesel
   Type a fuel type (or press Enter to skip): flex

   🔍 Resultados encontrados:

   1. Honda Hr-v (2020)
      Color: Black
      Mileage: 35,800.0 km
      Transmission: Automatic | Fuel: Flex
      Price: R$ 98.000,00
   ----------------------------------------

   ```


## ✅ Running Tests
   With the server running in another terminal:
   ``` bash
   pytest
   ```

👨‍💻 Developed by Mateus Pereira \
https://www.linkedin.com/in/mateus-assuncao/

