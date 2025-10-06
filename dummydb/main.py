"""
core.py — Core logic for MockDB
===============================

Implements the main database and table structures for MockDB.
This is the heart of the in-memory storage system.
"""

import json
from copy import deepcopy


class Table:
    """Represents a single in-memory table (or collection)."""

    def __init__(self, name: str):
        """
        Initializes a new Table.

        Args:
            name (str): The name of the table.
        """
        self.name = name
        self.records = []

    def insert(self, data: dict):
        """
        Insert a new record (dictionary) into the table.

        Args:
            data (dict): Record to insert.

        Returns:
            bool: True if insertion was successful.

        Raises:
            TypeError: If `data` is not a dictionary.
        """
        if not isinstance(data, dict):
            raise TypeError("Inserted data must be a dictionary.")
        self.records.append(deepcopy(data))
        return True

    def find(self, query: dict = None):
        """
        Find records matching a query.

        Args:
            query (dict, optional): Key-value pairs to match. If None, returns all records.

        Returns:
            list: List of records (dictionaries) matching the query.
        """
        if not query:
            return deepcopy(self.records)

        def match(record):
            return all(record.get(k) == v for k, v in query.items())

        return [deepcopy(r) for r in self.records if match(r)]

    def update(self, query: dict, new_data: dict):
        """
        Update records matching a query.

        Args:
            query (dict): Key-value pairs to match records.
            new_data (dict): Fields to update in matching records.

        Returns:
            int: Number of records updated.

        Raises:
            TypeError: If `query` or `new_data` is not a dictionary.
        """
        if not isinstance(query, dict) or not isinstance(new_data, dict):
            raise TypeError("Both query and new_data must be dictionaries.")

        count = 0
        for record in self.records:
            if all(record.get(k) == v for k, v in query.items()):
                record.update(new_data)
                count += 1
        return count

    def delete(self, query: dict):
        """
        Delete records matching a query.

        Args:
            query (dict): Key-value pairs to match records for deletion.

        Returns:
            int: Number of records deleted.
        """
        before = len(self.records)
        self.records = [
            record for record in self.records
            if not all(record.get(k) == v for k, v in query.items())
        ]
        return before - len(self.records)

    def to_json(self):
        """
        Convert the table data to a JSON string.

        Returns:
            str: JSON-formatted string of all records in the table.
        """
        return json.dumps(self.records, indent=2)

    def __repr__(self):
        """
        Return a human-readable summary of the table.

        Returns:
            str: Table name and number of records.
        """
        return f"<Table name='{self.name}' records={len(self.records)}>"


class Database:
    """Main Mock Database class that manages multiple tables."""

    def __init__(self):
        """
        Initializes an empty in-memory database.
        """
        self.tables = {}

    def create_table(self, name: str):
        """
        Create a new table in the database.

        Args:
            name (str): Name of the table.

        Returns:
            Table: The newly created Table object.

        Raises:
            ValueError: If a table with the same name already exists.
        """
        if name in self.tables:
            raise ValueError(f"Table '{name}' already exists.")
        self.tables[name] = Table(name)
        return self.tables[name]

    def get_table(self, name: str):
        """
        Retrieve a table by name.

        Args:
            name (str): Name of the table.

        Returns:
            Table: The Table object with the given name.

        Raises:
            KeyError: If the table does not exist.
        """
        if name not in self.tables:
            raise KeyError(f"Table '{name}' does not exist.")
        return self.tables[name]

    def drop_table(self, name: str):
        """
        Delete a table from the database.

        Args:
            name (str): Name of the table to delete.

        Returns:
            bool: True if deletion was successful, False if the table did not exist.
        """
        if name in self.tables:
            del self.tables[name]
            return True
        return False

    def save_to_file(self, filepath: str):
        """
        Save the entire database to a JSON file.

        Args:
            filepath (str): Path to save the JSON file.
        """
        with open(filepath, "w", encoding="utf-8") as f:
            json.dump({k: v.records for k, v in self.tables.items()}, f, indent=2)

    def load_from_file(self, filepath: str):
        """
        Load database data from a JSON file.

        Args:
            filepath (str): Path of the JSON file to load from.
        """
        with open(filepath, "r", encoding="utf-8") as f:
            data = json.load(f)
        for name, records in data.items():
            table = self.create_table(name)
            table.records = records

    def __repr__(self):
        """
        Return a human-readable summary of the database.

        Returns:
            str: Names of tables in the database.
        """
        return f"<MockDB tables={list(self.tables.keys())}>"
