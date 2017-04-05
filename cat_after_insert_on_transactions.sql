CREATE TRIGGER update_cats_after_trans_update 
	AFTER UPDATE
	ON transactions
BEGIN
	UPDATE catergories SET transactions=(
		SELECT sum(amount) FROM transactions WHERE catergory=NEW.catergory)
		WHERE cat_name=NEW.catergory;
	UPDATE accounts SET amount=(
		SELECT sum(amount) FROM transactions WHERE acc_id=NEW.acc_id)
		WHERE acc_id=NEW.acc_id;
END;
