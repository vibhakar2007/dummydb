"""
MockDB: A Lightweight In-Memory Database for Python
===================================================

MockDB is a pure-Python, lightweight, schema-free in-memory database designed
for developers who need fast and flexible data storage without external dependencies.

It mimics the basic behavior of real-world databases like MongoDB or SQLite,
but operates entirely in memory — ideal for testing, prototyping, or rapid development.

---------------------------------------------------
⚙️  Key Features
---------------------------------------------------
- 🧠 In-memory data storage (no files, no setup)
- 📦 Table-like collections with flexible schema
- 🔍 Powerful query filters (like Mongo-style find/query)
- 🧹 CRUD operations: insert, find, update, delete
- 🪶 Optional JSON serialization for quick save/load
- 🚀 Perfect for mock environments or small data apps

---------------------------------------------------
📘 Example Usage
---------------------------------------------------
>>> from mockdb import Database
>>> db = Database()

# Create a new collection (like a table)
>>> users = db.create_table("users")

# Insert documents (records)
>>> users.insert({"name": "Vibhakar", "age": 17})
>>> users.insert({"name": "Jasmine", "age": 16})

# Query data
>>> users.find({"age": 17})
[{'name': 'Vibhakar', 'age': 17}]

# Update and delete
>>> users.update({"name": "Jasmine"}, {"age": 17})
>>> users.delete({"name": "Vibhakar"})

---------------------------------------------------
🧩 Author
---------------------------------------------------
Developed by Vibhakar (2025)
GitHub: https://github.com/vibhakar2007
"""

from .main import Database, Table

__all__ = ["Database", "Table"]
__version__ = "0.1.1"
__author__ = "Vibhakar S"
__license__ = "MIT"
