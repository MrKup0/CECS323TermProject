-- Created by Vertabelo (http://vertabelo.com)
-- Last modification date: 2022-11-12 01:25:47.427

-- tables
-- Table: doors
CREATE TABLE doors (
    room_number int  NOT NULL,
    door_name varchar(50)  NOT NULL,
    CONSTRAINT doors_pk PRIMARY KEY (room_number,door_name)
);

-- Table: employees
CREATE TABLE employees (
    employee_id int  NOT NULL,
    amount_owed int  NOT NULL,
    CONSTRAINT employees_pk PRIMARY KEY (employee_id)
);

-- Table: hooks
CREATE TABLE hooks (
    hook_id int  NOT NULL,
    CONSTRAINT hooks_pk PRIMARY KEY (hook_id)
);

-- Table: issued_keys
CREATE TABLE issued_keys (
    employee_id int  NOT NULL,
    hook_id int  NOT NULL,
    requested_room int  NOT NULL,
    approved_room_number int  NOT NULL,
    door_name varchar(50)  NOT NULL,
    issued_date date  NOT NULL,
    return_date date  NOT NULL,
    date_returned date  NULL,
    is_valid bool  NOT NULL,
    request_date date  NOT NULL,
    CONSTRAINT issued_keys_pk PRIMARY KEY (employee_id,hook_id,approved_room_number)
);

-- Table: keys
CREATE TABLE keys (
    hook_id int  NOT NULL,
    room_number int  NOT NULL,
    door_name varchar(50)  NOT NULL,
    CONSTRAINT keys_pk PRIMARY KEY (hook_id,room_number,door_name)
);

-- Table: requests
CREATE TABLE requests (
    employee_id int  NOT NULL,
    room_number int  NOT NULL,
    request_date date  NOT NULL,
    approval_date date  NULL,
    CONSTRAINT requests_pk PRIMARY KEY (employee_id,request_date,room_number)
);

-- Table: rooms
CREATE TABLE rooms (
    room_number int  NOT NULL,
    CONSTRAINT rooms_pk PRIMARY KEY (room_number)
);

-- foreign keys
-- Reference: doors_rooms (table: doors)
ALTER TABLE doors ADD CONSTRAINT doors_rooms
    FOREIGN KEY (room_number)
    REFERENCES rooms (room_number)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: issued_keys_keys (table: issued_keys)
ALTER TABLE issued_keys ADD CONSTRAINT issued_keys_keys
    FOREIGN KEY (hook_id, approved_room_number, door_name)
    REFERENCES keys (hook_id, room_number, door_name)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: issued_keys_requests (table: issued_keys)
ALTER TABLE issued_keys ADD CONSTRAINT issued_keys_requests
    FOREIGN KEY (employee_id, request_date, requested_room)
    REFERENCES requests (employee_id, request_date, room_number)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: keys_doors (table: keys)
ALTER TABLE keys ADD CONSTRAINT keys_doors
    FOREIGN KEY (room_number, door_name)
    REFERENCES doors (room_number, door_name)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: keys_hooks (table: keys)
ALTER TABLE keys ADD CONSTRAINT keys_hooks
    FOREIGN KEY (hook_id)
    REFERENCES hooks (hook_id)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: requests_employees (table: requests)
ALTER TABLE requests ADD CONSTRAINT requests_employees
    FOREIGN KEY (employee_id)
    REFERENCES employees (employee_id)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: requests_rooms (table: requests)
ALTER TABLE requests ADD CONSTRAINT requests_rooms
    FOREIGN KEY (room_number)
    REFERENCES rooms (room_number)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- End of file.

