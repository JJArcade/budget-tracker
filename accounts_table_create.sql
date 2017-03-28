CREATE TABLE IF NOT EXISTS accounts
(acc_id		TEXT 	NOT NULL 	PRIMARY KEY,
acc_name	TEXT 	NOT NULL,
acc_type	TEXT 	NOT NULL,
interest_rate 	REAL,
amount 		REAL 	NOT NULL	DEFAULT 0);
