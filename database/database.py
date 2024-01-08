import sqlite3

class DatabaseHandler:
    def __init__(self, db_name):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self):
        """Create a table in the database if it doesn't exist."""
        try:
            self.cursor.execute('''
                CREATE TABLE IF NOT EXISTS data (
                    id INTEGER PRIMARY KEY,
                    name TEXT,
                    value INTEGER
                )
            ''')
            self.conn.commit()
        except Exception as e:
            print(f"Error creating table: {e}")

    def add_data(self, name, value):
        """Add a new record to the database."""
        try:
            self.cursor.execute('''
                INSERT INTO data (name, value)
                VALUES (?, ?)
            ''', (name, value))
            self.conn.commit()
        except Exception as e:
            print(f"Error adding data: {e}")

    def get_data(self, data_id):
        """Retrieve a record from the database by ID."""
        try:
            self.cursor.execute('''
                SELECT * FROM data WHERE id=?
            ''', (data_id,))
            return self.cursor.fetchone()
        except Exception as e:
            print(f"Error getting data: {e}")

    def update_data(self, data_id, new_name, new_value):
        """Update a record in the database."""
        try:
            self.cursor.execute('''
                UPDATE data SET name=?, value=? WHERE id=?
            ''', (new_name, new_value, data_id))
            self.conn.commit()
        except Exception as e:
            print(f"Error updating data: {e}")

    def delete_data(self, data_id):
        """Delete a record from the database by ID."""
        try:
            self.cursor.execute('''
                DELETE FROM data WHERE id=?
            ''', (data_id,))
            self.conn.commit()
        except Exception as e:
            print(f"Error deleting data: {e}")

    def close_connection(self):
        """Close the database connection."""
        self.conn.close()
