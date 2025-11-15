# alx_travel_app_0x00

This project is a backend exercise designed to help learners understand how to build core Django components for a travel booking application.  
It includes database models, API serializers, and a custom management command for seeding sample data.

---

## 🧠 Project Objective

The goal of this task is to:

✔ Define database models (Listing, Booking, Review)  
✔ Create DRF serializers for API data representation  
✔ Implement a management command to seed the database  
✔ Test and validate seeded data using Django CLI

---

## 📁 Project Structure


---

## 🏗️ Models Included

### **Listing**
Represents a property available for booking.

Fields:
- `title`
- `description`
- `location`
- `price_per_night`
- `created_at`

### **Booking**
Represents a customer booking for a listing.

Fields:
- `listing` (ForeignKey to Listing)
- `customer_name`
- `start_date`
- `end_date`
- `total_price`
- `created_at`

### **Review**
Represents a customer review for a listing.

Fields:
- `listing` (ForeignKey)
- `rating`
- `comment`
- `created_at`

---

## 🔄 Serializers

Located in **listings/serializers.py**

Serializers created:
- `ListingSerializer`
- `BookingSerializer`

These prepare model data to be returned as JSON in API responses.

---

## 🌱 Database Seeding

A custom Django management command is included to populate the database with sample listing data.

### Seeder Location:
