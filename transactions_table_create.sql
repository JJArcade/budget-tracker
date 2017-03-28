CREATE TABLE IF NOT EXISTS transactions
(trans_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
acc_id TEXT NOT NULL,
catergory TEXT NOT NULL,
description TEXT,
trans_date DATE NOT NULL,
amount REAL NOT NULL DEFAULT 0,
FOREIGN KEY(catergory) REFERENCES catergories(catergory),
FOREIGN KEY(acc_id) REFERENCES accounts(acc_id)
);
