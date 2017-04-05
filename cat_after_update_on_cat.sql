CREATE TRIGGER update_remainders_update
	AFTER UPDATE ON catergories
BEGIN
	UPDATE catergories SET remainder_amount=
		(NEW.budget_amount+NEW.transactions)
		WHERE cat_id=new.cat_id;
END;
