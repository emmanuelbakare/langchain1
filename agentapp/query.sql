-- select COUNT(*) from users

-- select * from products LIMIT 5

-- SELECT sql from sqlite_master WHERE type='table' AND name IN ('users', 'addresses', 'products', 'carts', 'orders', 'order_products');
SELECT u.name, SUM(op.amount) AS total_amount FROM users u JOIN orders o ON u.id = o.user_id JOIN order_products op ON o.id = op.order_id GROUP BY u.id ORDER BY total_amount ASC LIMIT 1