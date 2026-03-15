# Django REST Framework — Modular Entity and Mapping System

## Tech Stack
- Python
- Django
- Django REST Framework
- drf-yasg

## Setup Steps

### 1. Clone the repository
git clone https://github.com/Dhiraj2k5/Django-rest-api.git
cd <project-folder>

### 2. Create and activate virtual environment
python -m venv venv
venv\Scripts\activate

### 3. Install dependencies
pip install -r requirements.txt

### 4. Run migrations
python manage.py makemigrations
python manage.py migrate

### 5. Create superuser
python manage.py createsuperuser

### 6. Run server
python manage.py runserver

## Installed Apps
- vendor
- product
- course
- certification
- vendor_product_mapping
- product_course_mapping
- course_certification_mapping

## API Documentation
- Swagger UI: http://localhost:8000/swagger/
- ReDoc: http://localhost:8000/redoc/
- Admin Panel: http://localhost:8000/admin/

## API Endpoints

### Vendors
- GET /api/vendors/ — list all vendors
- POST /api/vendors/ — create vendor
- GET /api/vendors/{id}/ — retrieve vendor
- PUT /api/vendors/{id}/ — update vendor
- PATCH /api/vendors/{id}/ — partial update
- DELETE /api/vendors/{id}/ — delete vendor

### Products
- GET /api/products/
- POST /api/products/
- GET /api/products/{id}/
- PUT /api/products/{id}/
- PATCH /api/products/{id}/
- DELETE /api/products/{id}/

### Courses
- GET /api/courses/
- POST /api/courses/
- GET /api/courses/{id}/
- PUT /api/courses/{id}/
- PATCH /api/courses/{id}/
- DELETE /api/courses/{id}/

### Certifications
- GET /api/certifications/
- POST /api/certifications/
- GET /api/certifications/{id}/
- PUT /api/certifications/{id}/
- PATCH /api/certifications/{id}/
- DELETE /api/certifications/{id}/

### Vendor Product Mappings
- GET /api/vendor-product-mappings/?vendor_id=1
- POST /api/vendor-product-mappings/
- GET /api/vendor-product-mappings/{id}/
- PUT /api/vendor-product-mappings/{id}/
- PATCH /api/vendor-product-mappings/{id}/
- DELETE /api/vendor-product-mappings/{id}/

### Product Course Mappings
- GET /api/product-course-mappings/?product_id=1
- POST /api/product-course-mappings/
- GET /api/product-course-mappings/{id}/
- PUT /api/product-course-mappings/{id}/
- PATCH /api/product-course-mappings/{id}/
- DELETE /api/product-course-mappings/{id}/

### Course Certification Mappings
- GET /api/course-certification-mappings/?course_id=1
- POST /api/course-certification-mappings/
- GET /api/course-certification-mappings/{id}/
- PUT /api/course-certification-mappings/{id}/
- PATCH /api/course-certification-mappings/{id}/
- DELETE /api/course-certification-mappings/{id}/

## Validations Implemented
- Required field validation
- Unique code per master entity
- Duplicate mapping prevention
- Single primary mapping per parent
- Valid foreign key validation
