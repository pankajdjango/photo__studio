-- Table for user accounts
CREATE TABLE IF NOT EXISTS general.account_profile (
    id BIGSERIAL PRIMARY KEY,
    username VARCHAR(150) UNIQUE NOT NULL,
    email VARCHAR(254) UNIQUE NOT NULL,
    password VARCHAR(200) NOT NULL,
    date_joined TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    account_type BIGINT NOT NULL REFERENCES general.account_type(account_type) DEFERRABLE INITIALLY DEFERRED
);

-- Table for photographer profiles
CREATE TABLE IF NOT EXISTS general_photographer (
    id BIGSERIAL PRIMARY KEY,
    bio TEXT NOT NULL,
    portfolio_url VARCHAR(200) NOT NULL,
    expertise VARCHAR(100) NOT NULL,
    instagram_handle VARCHAR(100) NOT NULL,
    facebook_handle VARCHAR(100) NOT NULL,
    twitter_handle VARCHAR(100) NOT NULL,
    profile_picture VARCHAR(100) NOT NULL,
    user_id BIGINT NOT NULL REFERENCES account_customuser(id) DEFERRABLE INITIALLY DEFERRED
);


-- Table for client profiles
CREATE TABLE IF NOT EXISTS general_client (
    id BIGSERIAL PRIMARY KEY,
    organization_name VARCHAR(255) NOT NULL,
    organization_type VARCHAR(100) NOT NULL,
    website VARCHAR(200) NOT NULL,
    bio TEXT NOT NULL,
    profile_picture VARCHAR(100) NOT NULL,
    user_id BIGINT NOT NULL REFERENCES account_customuser(id) DEFERRABLE INITIALLY DEFERRED
);


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


CREATE TABLE IF NOT EXISTS general.photographer (
    id BIGINT GENERATED BY DEFAULT AS IDENTITY PRIMARY KEY,
    bio TEXT NOT NULL,
    portfolio_url VARCHAR(200) NOT NULL,
    expertise VARCHAR(100) NOT NULL,
    instagram_handle VARCHAR(100) NOT NULL,
    facebook_handle VARCHAR(100) NOT NULL,
    twitter_handle VARCHAR(100) NOT NULL,
    profile_picture VARCHAR(100) NOT NULL,
    user_id BIGINT NOT NULL,
    FOREIGN KEY (user_id) REFERENCES account_customuser(id) DEFERRABLE INITIALLY DEFERRED
);

CREATE TABLE IF NOT EXISTS general.client (
    id BIGINT GENERATED BY DEFAULT AS IDENTITY PRIMARY KEY,
    organization_name VARCHAR(255) NOT NULL,
    organization_type VARCHAR(100) NOT NULL,
    website VARCHAR(200) NOT NULL,
    bio TEXT NOT NULL,
    profile_picture VARCHAR(100) NOT NULL,
    user_id BIGINT NOT NULL,
    FOREIGN KEY (user_id) REFERENCES account_customuser(id) DEFERRABLE INITIALLY DEFERRED
);