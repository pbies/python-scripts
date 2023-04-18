#!/usr/bin/env python3
import os
import random
import hashlib
from pycoin.key import Key
from pycoin.encoding import a2b_hashed_base58, b2a_hashed_base58
import sqlite3

# Connect to database
conn = sqlite3.connect("bitcoin_keys.db")
cursor = conn.cursor()

# Create table
cursor.execute("CREATE TABLE IF NOT EXISTS keys (private_key TEXT, public_key TEXT, address TEXT)")

# Generate 100 million random private keys
for i in range(10000000):
    private_key = os.urandom(32)
    key = Key.from_secret_exponent(private_key)
    public_key = key.public_pair()
    address = key.address()

    # Insert keys into database
    cursor.execute("INSERT INTO keys VALUES (?, ?, ?)", (b2a_hashed_base58(private_key), b2a_hashed_base58(public_key), address))

conn.commit()
conn.close()

print("Keys generated and written to database.")
