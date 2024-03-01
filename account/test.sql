DROP TABLE IF EXISTS account_bookingrequest, account_customuser, account_eventtype, account_notification, account_photo, account_review, account_client, account_event, account_location, account_payment, account_photographer CASCADE;

DROP TABLE IF EXISTS account_bookingrequest CASCADE;
DROP TABLE IF EXISTS account_event CASCADE;
DROP TABLE IF EXISTS account_notification CASCADE;
DROP TABLE IF EXISTS account_photographer CASCADE;
DROP TABLE IF EXISTS account_client CASCADE;
DROP TABLE IF EXISTS account_eventtype CASCADE;
DROP TABLE IF EXISTS account_payment CASCADE;
DROP TABLE IF EXISTS account_review CASCADE;
DROP TABLE IF EXISTS account_customuser CASCADE;
DROP TABLE IF EXISTS account_location CASCADE;
DROP TABLE IF EXISTS account_photo CASCADE;


-- Create tables in the 'general' schema
  CREATE SCHEMA IF NOT EXISTS general;
  CREATE SCHEMA IF NOT EXISTS erp;
  CREATE SCHEMA IF NOT EXISTS test;

CREATE TABLE IF NOT EXISTS general.account_profile (
    userid BIGSERIAL PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(254) UNIQUE,
    mobile VARCHAR(10),
    address VARCHAR(80),
    password VARCHAR(200) NOT NULL,
    generated INTEGER,
    updated_on INTEGER,
    city INTEGER REFERENCES general.city_master(city_id),
    pincode INTEGER, --REFERENCES general.pincode_master(pincode),
    active BOOLEAN DEFAULT true,
    profile_photo VARCHAR(100)
);
-- Service Provider
-- service_provider
-- Service User / Customer / Client / Buyer
-- Create a trigger function to set the generated column on insert
CREATE OR REPLACE FUNCTION set_generated_column() RETURNS TRIGGER AS $$ BEGIN NEW.generated := EXTRACT(EPOCH FROM NOW())::INTEGER; RETURN NEW; END;
$$ LANGUAGE plpgsql;
CREATE OR REPLACE FUNCTION set_updated_on_column() RETURNS TRIGGER AS $$ BEGIN NEW.updated_on := EXTRACT(EPOCH FROM NOW())::INTEGER; RETURN NEW; END;
$$ LANGUAGE plpgsql;
-- Create a trigger to execute the set_generated_column function on insert
CREATE TRIGGER set_generated_trigger BEFORE INSERT ON general.account_profile FOR EACH ROW EXECUTE FUNCTION set_generated_column();
CREATE TRIGGER set_last_updated_trigger BEFORE UPDATE ON general.account_profile FOR EACH ROW EXECUTE FUNCTION set_updated_on_column();

CREATE TABLE IF NOT EXISTS general.user_profile (
    id BIGSERIAL PRIMARY KEY,
    organization_name VARCHAR(255) ,
    organization_type VARCHAR(100) ,
    website VARCHAR(200) ,
    bio TEXT ,
    profile_picture VARCHAR(100) ,
    userid BIGINT NOT NULL REFERENCES general.account_profile(userid) DEFERRABLE INITIALLY DEFERRED
);

CREATE TABLE IF NOT EXISTS general.service_provider_profile (
    id BIGSERIAL PRIMARY KEY,
    bio TEXT,
    portfolio_url VARCHAR(200),
    expertise VARCHAR(100),
    instagram_handle VARCHAR(100),
    facebook_handle VARCHAR(100),
    twitter_handle VARCHAR(100),
    profile_picture VARCHAR(100),
    user_id BIGINT NOT NULL REFERENCES general.account_profile(userid) DEFERRABLE INITIALLY DEFERRED
);
