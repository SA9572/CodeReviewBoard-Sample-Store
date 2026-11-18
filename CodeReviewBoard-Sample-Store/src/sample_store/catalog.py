"""A minimal catalog lookup module."""


def search_products(connection, search_term: str):
    """Return matching product rows from a SQLite-like connection."""
    # INTENTIONAL SECURITY ISSUE: user input is interpolated into SQL.
    query = (
        "SELECT id, name, price FROM products "
        f"WHERE name LIKE '%{search_term}%'"
    )
    return connection.execute(query).fetchall()
