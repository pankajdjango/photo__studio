
-- Create tables in the 'general' schema
CREATE SCHEMA IF NOT EXISTS general;
CREATE SCHEMA IF NOT EXISTS erp;

-- pythn manage.py inspectdb general.account_profile
CREATE TABLE IF NOT EXISTS general.account_profile (
    userid BIGSERIAL PRIMARY KEY,
    full_name VARCHAR(80) NOT NULL,
    email VARCHAR(254) UNIQUE,
    mobile VARCHAR(10),
    address VARCHAR(80),
    password VARCHAR(200) NOT NULL,
    gender VARCHAR(10) CHECK (gender IN ('Male', 'Female', 'Other')) DEFAULT NULL,
    generated INTEGER,
    updated_on INTEGER,
    city INTEGER REFERENCES general.city_master(city_id),
    pincode INTEGER, --REFERENCES general.pincode_master(pincode),
    active BOOLEAN DEFAULT true,
    profile_photo VARCHAR(100)

);
-- Create a trigger function to set the generated column on insert
CREATE OR REPLACE FUNCTION set_generated_column() RETURNS TRIGGER AS $$ BEGIN NEW.generated := EXTRACT(EPOCH FROM NOW())::INTEGER; RETURN NEW; END;
$$ LANGUAGE plpgsql;
CREATE OR REPLACE FUNCTION set_updated_on_column() RETURNS TRIGGER AS $$ BEGIN NEW.updated_on := EXTRACT(EPOCH FROM NOW())::INTEGER; RETURN NEW; END;
$$ LANGUAGE plpgsql;
-- Create a trigger to execute the set_generated_column function on insert
CREATE TRIGGER set_generated_trigger BEFORE INSERT ON general.account_profile FOR EACH ROW EXECUTE FUNCTION set_generated_column();
CREATE TRIGGER set_last_updated_trigger BEFORE UPDATE ON general.account_profile FOR EACH ROW EXECUTE FUNCTION set_updated_on_column();


-- CREATE TABLE IF NOT EXISTS general.user_profile (
--     id BIGSERIAL PRIMARY KEY,
--     organization_name VARCHAR(255) ,
--     organization_type VARCHAR(100) ,
--     website VARCHAR(200) ,
--     bio TEXT ,
--     profile_picture VARCHAR(100) ,
--     userid BIGINT NOT NULL REFERENCES general.account_profile(userid) DEFERRABLE INITIALLY DEFERRED
-- );
-- CREATE TABLE IF NOT EXISTS general.service_provider_profile (
--     id BIGSERIAL PRIMARY KEY,
--     bio TEXT,
--     portfolio_url VARCHAR(200),
--     expertise VARCHAR(100),
--     instagram_handle VARCHAR(100),
--     facebook_handle VARCHAR(100),
--     twitter_handle VARCHAR(100),
--     profile_picture VARCHAR(100),
--     user_id BIGINT NOT NULL REFERENCES general.account_profile(userid) DEFERRABLE INITIALLY DEFERRED
-- );


create table general.url_history(
id serial primary key ,
userid BIGINT NOT NULL REFERENCES general.account_profile(userid) DEFERRABLE INITIALLY DEFERRED,
url_visited varchar(100),
generated integer
);
ALTER TABLE general.url_history ALTER COLUMN url_visited TYPE TEXT;

CREATE TRIGGER set_generated_trigger_url_history BEFORE INSERT ON general.url_history FOR EACH ROW EXECUTE FUNCTION set_generated_column();


CREATE TABLE IF NOT EXISTS general.account_type (
    account_type VARCHAR(100) PRIMARY KEY,
    generated TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);



CREATE TABLE IF NOT EXISTS general.event_type (
    event_id serial PRIMARY KEY,
    event_name VARCHAR(100) NOT NULL UNIQUE
);



CREATE TABLE IF NOT EXISTS general.event_status (
    status VARCHAR(50) primary key
);





CREATE TABLE IF NOT EXISTS general.event_booking_master (
    id BIGINT GENERATED BY DEFAULT AS IDENTITY PRIMARY KEY,
    city INTEGER REFERENCES general.city_master(city_id),
    event_id INTEGER REFERENCES general.event_type(event_id),
    userid INTEGER REFERENCES general.account_profile(userid),
    area_address TEXT,
    mobile VARCHAR(10),
    event_date TIMESTAMP WITH TIME ZONE NOT NULL, -- use IST time
    message TEXT ,
    status VARCHAR(50) NOT NULL REFERENCES general.event_status(status) DEFERRABLE INITIALLY DEFERRED,
    is_confirmed BOOLEAN default false,
    generated INTEGER,
    updated_on INTEGER
);
-- event_id BIGINT NOT NULL REFERENCES general.event_type(event_id) DEFERRABLE INITIALLY DEFERRED,
    -- userid BIGINT NOT NULL REFERENCES general.account_profile(userid) DEFERRABLE INITIALLY DEFERRED,
    -- client_id BIGINT NOT NULL,
    -- FOREIGN KEY (client_id) REFERENCES account_client(id) DEFERRABLE INITIALLY DEFERRED,

CREATE TRIGGER set_generated_trigger_event_booking_request BEFORE INSERT ON general.event_booking_master FOR EACH ROW EXECUTE FUNCTION set_generated_column();
CREATE TRIGGER set_last_updated_trigger_event_booking_request BEFORE UPDATE ON general.event_booking_master FOR EACH ROW EXECUTE FUNCTION set_updated_on_column();
ALTER SEQUENCE event_booking_master_id_seq RESTART WITH 1;


ALTER TABLE general.event_booking_master ADD COLUMN updated_by INTEGER REFERENCES general.account_profile(userid) NULL;
alter table general.event_booking_master drop column is_confirmed;



CREATE TABLE IF NOT EXISTS general.role_master (
    role_id SERIAL PRIMARY KEY,
    role_name VARCHAR(50),
    generated INTEGER
);
CREATE TABLE IF NOT EXISTS general.user_roles (
    uniq_id SERIAL PRIMARY KEY,
    role_id INTEGER REFERENCES general.role_master(role_id),
    userid INTEGER REFERENCES general.account_profile(userid),
    generated INTEGER
);
-- DROP TRIGGER IF EXISTS set_generated_trigger_event_booking_master ON general.event_booking_master;
-- DROP FUNCTION IF EXISTS set_generated_column_event_booking_master() CASCADE;
CREATE TRIGGER set_generated_trigger_role_master BEFORE INSERT ON general.role_master FOR EACH ROW EXECUTE FUNCTION set_generated_column();
CREATE TRIGGER set_generated_trigger_account_profile BEFORE INSERT ON general.user_roles FOR EACH ROW EXECUTE FUNCTION set_generated_column();
