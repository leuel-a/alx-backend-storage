-- Creates a trigger that decreases the number of items in stock when an order is placed
DELIMITER //

CREATE TRIGGER update_items_in_stock
AFTER INSERT ON orders
FOR EACH ROW
BEGIN
    UPDATE items
    SET quantity = quantity - NEW.number
    WHERE name = NEW.item_name;
END;
//

DELIMITER ;
