CREATE TABLE catergories
(cat_id	INT NOT NULL PRIMARY KEY,
cat_name TEXT NOT NULL,
cat_date DATE NOT NULL,
budget_amount REAL NOT NULL DEFAULT 0,
transactions REAL,
remainder_amount REAL,
carry_over_debt INT NOT NULL DEFAULT 0);
