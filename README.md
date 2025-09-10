# SBM Django + PostgreSQL Web Application

A full-stack Django web application with PostgreSQL database, featuring CRUD operations, third-party API integration, and data visualization.

## Features

- **CRUD Operations**: Full REST API for Item management
- **Third-Party API Integration**: OpenWeatherMap API integration
- **Data Visualization**: Interactive charts using Chart.js
- **PostgreSQL Database**: Robust data storage
- **RESTful APIs**: Built with Django REST Framework

## Project Structure

```
SBM/
├── sbm_project/          # Django project settings
│   ├── __init__.py
│   ├── settings.py       # Project configuration
│   ├── urls.py          # Main URL routing
│   ├── wsgi.py          # WSGI configuration
│   └── asgi.py          # ASGI configuration
├── items/                # Main Django app
│   ├── models.py        # Database models
│   ├── views.py         # API views and dashboard
│   ├── serializers.py   # DRF serializers
│   ├── urls.py          # App URL routing
│   └── templates/       # HTML templates
│       └── items/
│           └── dashboard.html
├── manage.py            # Django management script
├── requirements.txt     # Python dependencies
├── env.example         # Environment variables template
└── README.md           # This file
```

## Setup Instructions

### Prerequisites

- Python 3.8+
- PostgreSQL 12+
- Git

### Local Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd SBM
   ```

2. **Create and activate virtual environment**
   ```bash
   python -m venv venv
   
   # On Windows
   .\venv\Scripts\Activate.ps1
   
   # On macOS/Linux
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**
   ```bash
   # Copy the example file
   cp env.example .env
   
   # Edit .env with your actual values
   # Get OpenWeatherMap API key from: https://openweathermap.org/api
   ```

5. **Set up PostgreSQL database**
   ```sql
   CREATE DATABASE sbm_db;
   CREATE USER postgres WITH PASSWORD 'password';
   GRANT ALL PRIVILEGES ON DATABASE sbm_db TO postgres;
   ```

6. **Run migrations**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

7. **Create superuser (optional)**
   ```bash
   python manage.py createsuperuser
   ```

8. **Run the development server**
   ```bash
   python manage.py runserver
   ```

9. **Access the application**
   - Dashboard: http://127.0.0.1:8000/dashboard/
   - Admin: http://127.0.0.1:8000/admin/
   - API Root: http://127.0.0.1:8000/api/

## API Documentation

### Items API

| Method | Endpoint | Description | Request Body |
|--------|----------|-------------|--------------|
| GET | `/api/items/` | List all items | - |
| POST | `/api/items/` | Create new item | `{"name": "string", "description": "string"}` |
| GET | `/api/items/{id}/` | Get specific item | - |
| PUT | `/api/items/{id}/` | Update item | `{"name": "string", "description": "string"}` |
| DELETE | `/api/items/{id}/` | Delete item | - |

#### Sample Requests

**Create Item:**
```bash
curl -X POST http://127.0.0.1:8000/api/items/ \
  -H "Content-Type: application/json" \
  -d '{"name": "Sample Item", "description": "This is a sample item"}'
```

**Get All Items:**
```bash
curl http://127.0.0.1:8000/api/items/
```

**Update Item:**
```bash
curl -X PUT http://127.0.0.1:8000/api/items/1/ \
  -H "Content-Type: application/json" \
  -d '{"name": "Updated Item", "description": "Updated description"}'
```

### Weather API

| Method | Endpoint | Description | Request Body |
|--------|----------|-------------|--------------|
| GET | `/api/weather/` | List all weather data | - |
| POST | `/api/weather/fetch_weather/` | Fetch new weather data | `{"city": "string"}` |
| GET | `/api/weather/{id}/` | Get specific weather record | - |

#### Sample Requests

**Fetch Weather Data:**
```bash
curl -X POST http://127.0.0.1:8000/api/weather/fetch_weather/ \
  -H "Content-Type: application/json" \
  -d '{"city": "London"}'
```

**Get All Weather Data:**
```bash
curl http://127.0.0.1:8000/api/weather/
```

## Data Models

### Item Model
- `id`: Primary key (auto-generated)
- `name`: CharField (max 200 characters)
- `description`: TextField (optional)
- `created_at`: DateTimeField (auto-generated)
- `updated_at`: DateTimeField (auto-updated)

### WeatherData Model
- `id`: Primary key (auto-generated)
- `city`: CharField (max 100 characters)
- `temperature`: FloatField
- `humidity`: IntegerField
- `description`: CharField (max 200 characters)
- `created_at`: DateTimeField (auto-generated)

## Dashboard Features

The dashboard (`/dashboard/`) provides:

1. **Items Chart**: Line chart showing items created over time
2. **Weather Chart**: Bar chart displaying temperature data by city
3. **Weather Form**: Interface to fetch new weather data
4. **API Documentation**: Interactive list of available endpoints

## Deployment

### Railway Deployment

1. **Prepare for deployment**
   ```bash
   # Update settings.py for production
   DEBUG = False
   ALLOWED_HOSTS = ['your-app.railway.app']
   ```

2. **Create railway.json**
   ```json
   {
     "build": {
       "builder": "NIXPACKS"
     },
     "deploy": {
       "startCommand": "python manage.py migrate && gunicorn sbm_project.wsgi:application",
       "healthcheckPath": "/dashboard/"
     }
   }
   ```

3. **Deploy to Railway**
   - Connect your GitHub repository
   - Set environment variables in Railway dashboard
   - Deploy automatically

### Environment Variables for Production

```
DB_NAME=your_production_db_name
DB_USER=your_production_db_user
DB_PASSWORD=your_production_db_password
DB_HOST=your_production_db_host
DB_PORT=5432
OPENWEATHER_API_KEY=your_openweather_api_key
SECRET_KEY=your_production_secret_key
DEBUG=False
ALLOWED_HOSTS=your-domain.com
```

## Testing the APIs

### Using curl

```bash
# Test Items API
curl -X POST http://127.0.0.1:8000/api/items/ \
  -H "Content-Type: application/json" \
  -d '{"name": "Test Item", "description": "Testing the API"}'

# Test Weather API
curl -X POST http://127.0.0.1:8000/api/weather/fetch_weather/ \
  -H "Content-Type: application/json" \
  -d '{"city": "New York"}'
```

### Using Python requests

```python
import requests

# Create an item
response = requests.post('http://127.0.0.1:8000/api/items/', 
                        json={'name': 'Python Item', 'description': 'Created via Python'})
print(response.json())

# Fetch weather data
response = requests.post('http://127.0.0.1:8000/api/weather/fetch_weather/',
                        json={'city': 'Tokyo'})
print(response.json())
```

## Troubleshooting

### Common Issues

1. **Database Connection Error**
   - Ensure PostgreSQL is running
   - Check database credentials in .env file
   - Verify database exists

2. **OpenWeatherMap API Error**
   - Ensure API key is valid
   - Check API key in environment variables
   - Verify internet connection

3. **Migration Errors**
   - Delete migration files and recreate
   - Check database permissions
   - Ensure all dependencies are installed

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## License

This project is open source and available under the MIT License.

## Support

For support, please open an issue in the GitHub repository or contact the development team.
