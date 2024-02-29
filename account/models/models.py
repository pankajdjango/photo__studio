from django.db import models
from django.contrib.auth.hashers import make_password, check_password

class CustomUser(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=10)
    password = models.CharField(max_length=128)  # Store hashed password

    # def set_password(self, raw_password):
    #     self.password = make_password(raw_password)

    # def check_password(self, raw_password):
    #     return check_password(raw_password, self.password)

    def __str__(self):
        return self.email

class Photographer(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    bio = models.TextField()
    portfolio_url = models.URLField()
    expertise = models.CharField(max_length=100)
    instagram_handle = models.CharField(max_length=100)
    facebook_handle = models.CharField(max_length=100)
    twitter_handle = models.CharField(max_length=100)
    profile_picture = models.ImageField(upload_to='photographer_profiles/')

class Client(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    organization_name = models.CharField(max_length=255)
    organization_type = models.CharField(max_length=100)
    website = models.URLField()
    bio = models.TextField()
    profile_picture = models.ImageField(upload_to='client_profiles/')

class Location(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=10)
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    description = models.TextField()
    photo = models.ImageField(upload_to='location_photos/')

class EventType(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Event(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    date = models.DateTimeField()
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    photographer = models.ForeignKey(Photographer, on_delete=models.CASCADE)
    event_type = models.ForeignKey(EventType, on_delete=models.CASCADE)
    duration_hours = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    is_published = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

class BookingRequest(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    status = models.CharField(max_length=20)
    message = models.TextField()
    booking_date = models.DateTimeField()
    updated_at = models.DateTimeField(auto_now=True)
    is_confirmed = models.BooleanField(default=False)

class Photo(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='event_photos/')
    description = models.TextField()
    taken_at = models.DateTimeField()
    uploaded_at = models.DateTimeField(auto_now_add=True)
    photographer = models.ForeignKey(Photographer, on_delete=models.CASCADE)

class Payment(models.Model):
    booking = models.ForeignKey(BookingRequest, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_date = models.DateTimeField(auto_now_add=True)
    payment_method = models.CharField(max_length=100)
    transaction_id = models.CharField(max_length=100)
    is_successful = models.BooleanField(default=False)

class Review(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    photographer = models.ForeignKey(Photographer, on_delete=models.CASCADE)
    rating = models.PositiveSmallIntegerField()
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Notification(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)


# CustomUser
# Photographer
# Client
# Location
# EventType
# Event
# BookingRequest
# Photo
# Payment
# Review
# Notification
'''
-- CustomUser
CREATE TABLE erp.custom_user (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(100),
    last_name VARCHAR(100),
    email VARCHAR(254) UNIQUE,
    phone_number VARCHAR(15),
    address VARCHAR(255),
    city VARCHAR(100),
    state VARCHAR(100),
    zip_code VARCHAR(10),
    password VARCHAR(128)
);

-- Photographer
CREATE TABLE erp.photographer (
    id SERIAL PRIMARY KEY,
    user_id INTEGER UNIQUE REFERENCES custom_user(id) ON DELETE CASCADE,
    bio TEXT,
    portfolio_url VARCHAR(200),
    expertise VARCHAR(100),
    instagram_handle VARCHAR(100),
    facebook_handle VARCHAR(100),
    twitter_handle VARCHAR(100),
    profile_picture VARCHAR(255)
);

-- Client
CREATE TABLE general.client (
    id SERIAL PRIMARY KEY,
    user_id INTEGER UNIQUE REFERENCES custom_user(id) ON DELETE CASCADE,
    organization_name VARCHAR(255),
    organization_type VARCHAR(100),
    website VARCHAR(200),
    bio TEXT,
    profile_picture VARCHAR(255)
);

-- Location
CREATE TABLE location (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    address VARCHAR(255),
    city VARCHAR(100),
    state VARCHAR(100),
    zip_code VARCHAR(10),
    latitude DECIMAL(9,6),
    longitude DECIMAL(9,6),
    description TEXT,
    photo VARCHAR(255)
);

-- EventType
CREATE TABLE event_type (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100)
);

-- Event
CREATE TABLE event (
    id SERIAL PRIMARY KEY,
    title VARCHAR(255),
    description TEXT,
    date TIMESTAMP,
    location_id INTEGER REFERENCES location(id) ON DELETE CASCADE,
    photographer_id INTEGER REFERENCES photographer(id) ON DELETE CASCADE,
    event_type_id INTEGER REFERENCES event_type(id) ON DELETE CASCADE,
    duration_hours INTEGER,
    price DECIMAL(10,2),
    is_published BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- BookingRequest
CREATE TABLE booking_request (
    id SERIAL PRIMARY KEY,
    client_id INTEGER REFERENCES client(id) ON DELETE CASCADE,
    event_id INTEGER REFERENCES event(id) ON DELETE CASCADE,
    status VARCHAR(20),
    message TEXT,
    booking_date TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    is_confirmed BOOLEAN DEFAULT FALSE
);

-- Photo
CREATE TABLE photo (
    id SERIAL PRIMARY KEY,
    event_id INTEGER REFERENCES event(id) ON DELETE CASCADE,
    image VARCHAR(255),
    description TEXT,
    taken_at TIMESTAMP,
    uploaded_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    photographer_id INTEGER REFERENCES photographer(id) ON DELETE CASCADE
);

-- Payment
CREATE TABLE payment (
    id SERIAL PRIMARY KEY,
    booking_id INTEGER REFERENCES booking_request(id) ON DELETE CASCADE,
    amount DECIMAL(10,2),
    payment_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    payment_method VARCHAR(100),
    transaction_id VARCHAR(100),
    is_successful BOOLEAN DEFAULT FALSE
);

-- Review
CREATE TABLE review (
    id SERIAL PRIMARY KEY,
    client_id INTEGER REFERENCES client(id) ON DELETE CASCADE,
    photographer_id INTEGER REFERENCES photographer(id) ON DELETE CASCADE,
    rating SMALLINT,
    comment TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Notification
CREATE TABLE notification (
    id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES custom_user(id) ON DELETE CASCADE,
    message TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    is_read BOOLEAN DEFAULT FALSE
);
'''
