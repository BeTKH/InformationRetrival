-- schema Definition DDL

-- Create the customer table 
CREATE TABLE customer (
    customer_id INT,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE,
    birth_date DATE,
    phone_num VARCHAR(15),
    PRIMARY KEY (customer_id)
);

-- Create the orders table 
CREATE TABLE orders (
    order_id INT,
    cust_id INT,
    product_name VARCHAR(100),
    order_date DATE NOT NULL,
    PRIMARY KEY (order_id),
    FOREIGN KEY (cust_id) REFERENCES customer(customer_id)
);


-- Insert some dummy data 
INSERT INTO customer (customer_id, first_name, last_name, email, birth_date, phone_num)
VALUES
    (1, 'Bek', 'Kobro', 'bekalue.korbro@ndsu.com', '1955-01-15', '+1234567890'),
    (2, 'Walter', 'White', 'walt@gerymatter-technologies.com', '1945-05-20', '+15051178987'),
    (3, 'Netsanet', 'Berhanu', 'ntbd@yahoo.com', '1965-09-10', '+251911461088');

-- Insert  data into the orders table
INSERT INTO orders (order_id, cust_id, product_name, order_date)
VALUES
    (101, 1, 'laptop cover','2023-09-15'),
    (102, 2, 'chemistry lab safety glass','2023-09-16'),
    (103, 1, 'Lift Master Controller','2023-09-17'),
    (104, 3, 'Geo Max Survey  equipment','2023-09-18');
