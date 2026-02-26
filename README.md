# 🗺️ TZ Tourism - Backend API

> Django REST API for Tanzania tourism platform with GPS-accurate attraction data, real-time weather, and seasonal planning guides.

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Django](https://img.shields.io/badge/Django-4.2+-green.svg)](https://www.djangoproject.com/)
[![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)](https://www.python.org/)
[![DRF](https://img.shields.io/badge/DRF-3.14+-red.svg)](https://www.django-rest-framework.org/)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](CONTRIBUTING.md)


- **Live Deployment** : https://twenzetusafari.netlify.app/
- **Live API:** https://cf89615f228bb45cc805447510de80.pythonanywhere.com/
- **Frontend Repo:** [twenzetu-safari-api](https://github.com/cleven12/twenzetu-safari-api)
- **API Docs:** [docs/API.md](docs/API.md)

---

## About

This is the **backend API** for TZ Tourism platform - providing GPS-accurate data for Tanzania's tourist attractions, real-time weather information, and comprehensive REST API for developers.

**Frontend repository:** [twenzetu-safari-web](https://github.com/cleven12/twenzetu-safari-web)

---

## Architecture

**Backend API Structure:**
```
twenzetu-safari-api/
├── src/
│   ├── attractions/      # Attractions app (models, views, serializers)
│   ├── regions/          # Regions app
│   ├── weather/          # Weather integration (Open-Meteo)
│   ├── cofig/         # Main API configuration & settings
│   └── manage.py         # Django management script
├── docs/                 # API documentation
└── legal/                # Terms, Privacy, Moderation policies
```

### **Core Features:**
- RESTful API with Django REST Framework
- PostgreSQL/MySQL database support
- Real-time weather integration (Open-Meteo API)
- JWT authentication
- GPS-accurate location data
- Historical weather patterns
- Content moderation system
- OpenAPI/Swagger documentation

---

## Quick Start

### **Prerequisites**
- Python 3.10+
- PostgreSQL (or SQLite for dev)
- pip & virtualenv

### **Installation**

```bash
# Clone repository
https://github.com/cleven12/twenzetu-safari-api.git
cd twenzetu-safari-api

# Create virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Set up environment variables
cp .env.example .env
# Edit .env with your database credentials and API keys

# Run migrations
python src/manage.py migrate

# Create superuser
python src/manage.py createsuperuser

# Load initial data (optional)
python src/manage.py loaddata initial_data.json

# Start development server
python src/manage.py runserver
```

**API runs at:** `http://localhost:8000/api/v1/`  
**Admin panel:** `http://localhost:8000/admin/`  
**API docs:** `http://localhost:8000/api/docs/`

> **🌐 Production API:** https://cf89615f228bb45cc805447510de80.pythonanywhere.com/

---

## API Endpoints

### **Core Endpoints**

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/api/v1/attractions/` | GET | List all attractions |
| `/api/v1/attractions/:id/` | GET | Attraction details |
| `/api/v1/attractions/:id/weather/` | GET | Current weather at location |
| `/api/v1/attractions/:id/seasonal/` | GET | Seasonal weather patterns |
| `/api/v1/regions/` | GET | List all regions |
| `/api/v1/regions/:id/` | GET | Region details |
| `/api/v1/weather/current/` | GET | Weather by GPS coordinates |
| `/api/v1/auth/login/` | POST | User authentication |
| `/api/v1/auth/register/` | POST | User registration |

### **Example Response**

```json
{
  "id": 1,
  "name": "Mount Kilimanjaro",
  "region": {
    "id": 1,
    "name": "Kilimanjaro"
  },
  "latitude": -3.0674,
  "longitude": 37.3556,
  "altitude_meters": 5895,
  "difficulty": "difficult",
  "nearest_airport": "Kilimanjaro International Airport (JRO)",
  "description": "Africa's highest mountain and world's tallest free-standing mountain...",
  "weather": {
    "temperature_c": 22.5,
    "condition": "Clear",
    "wind_speed_kmh": 12.3,
    "rain_mm": 0.0,
    "updated_at": "2026-02-15T14:30:00Z"
  },
  "seasonal_info": {
    "dry_season": "June-October, January-February",
    "rainy_season": "March-May (long rains), November-December (short rains)",
    "best_time_to_visit": "June-October"
  },
  "is_verified": true,
  "created_at": "2026-01-15T08:00:00Z",
  "updated_at": "2026-02-01T10:00:00Z"
}
```

**Full API Documentation:** [docs/API.md](docs/API.md)

---

## Testing

```bash
# Run all tests
pytest src/

# Run with coverage
pytest --cov=src

# Run specific test file
pytest src/attractions/tests.py

# Run with verbose output
pytest -v src/
```

---

## Tech Stack

- **Framework:** Django 4.2+ / Django REST Framework 3.14+
- **Database:** PostgreSQL (production) / SQLite (dev)
- **Authentication:** JWT (djangorestframework-simplejwt)
- **Weather API:** Open-Meteo
- **Documentation:** drf-spectacular (OpenAPI/Swagger)
- **Testing:** pytest + pytest-django
- **Code Quality:** black, flake8, isort
- **CORS:** django-cors-headers
- **Hosting:** [PythonAnywhere](https://cf89615f228bb45cc805447510de80.pythonanywhere.com/)

---

## Key Features

### **For API Consumers:**
- RESTful design with predictable endpoints
- Comprehensive OpenAPI documentation
- JWT authentication support
- Fast response times with database optimization
- Pagination & filtering support
- Free & open-source

### **For Developers:**
- Well-tested codebase (pytest)
- Clear code structure & documentation
- Easy to extend with Django apps
- Docker support (coming soon)
- CI/CD with GitHub Actions

---

## 🤝 Contributing

We welcome contributions! Here's how to help:

### **Development Setup:**

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/your-feature`
3. Make your changes
4. Run tests: `pytest`
5. Format code: `black . && isort .`
6. Commit: `git commit -m "Add your feature"`
7. Push: `git push origin feature/your-feature`
8. Open a Pull Request

### **Contribution Ideas:**
- Add new attractions
- Fix bugs
- Improve documentation
- Add tests
- Propose new features
- Add translations

**Read:** [CONTRIBUTING.md](CONTRIBUTING.md) | [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md)

---

## Project Status

### **Current Features:**
- Core attraction database models
- REST API with DRF
- Real-time weather integration
- JWT authentication
- Admin panel
- Content moderation system
- OpenAPI documentation

### **Roadmap:**
- User reviews API
- Tour operator directory
- Image upload & management
- Advanced search & filters
- Rate limiting & caching
- Docker containerization
- GraphQL API (optional)
- Multi-language support

---

## Environment Variables

Create a `.env` file in the root directory:

```env
# Django
SECRET_KEY=your-secret-key-here
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1

# Database
DB_ENGINE=django.db.backends.postgresql
DB_NAME=tz_tourism
DB_USER=postgres
DB_PASSWORD=your-password
DB_HOST=localhost
DB_PORT=5432

# Weather API
OPEN_METEO_API_URL=https://api.open-meteo.com/v1

# CORS (Frontend URL)
CORS_ALLOWED_ORIGINS=http://localhost:3000,https://twenzetu-safari-web.vercel.app

# JWT
JWT_SECRET_KEY=your-jwt-secret
JWT_ACCESS_TOKEN_LIFETIME=60  # minutes
JWT_REFRESH_TOKEN_LIFETIME=1440  # minutes (24 hours)
```

---

## Documentation

- [API Documentation](docs/API.md)
- [Contributing Guide](CONTRIBUTING.md)
- [Code of Conduct](CODE_OF_CONDUCT.md)
- [Terms of Service](legal/TERMS.md)
- [Privacy Policy](legal/PRIVACY.md)
- [Moderation Policy](legal/MODERATION.md)

---

## Disclaimers

This API provides data **for planning purposes only**.

**We are NOT responsible for:**
- Injuries or accidents during travel
- Weather-related incidents
- Inaccurate or outdated information
- Third-party services

**Data Sources:**
- Weather: Open-Meteo API
- Attraction data: Community-contributed & moderated
- Difficulty ratings: Subjective estimates

**Full Terms:** [legal/TERMS.md](legal/TERMS.md)

---

## License

MIT License - see [LICENSE](LICENSE) for details.

**Summary:** Free to use, modify, and distribute. No warranty provided.

---

## About

Built to provide **honest, accurate tourism data** for Tanzania through an open, well-documented API.

**Mission:** Enable safe, informed tourism through accessible data.

**Frontend:** [twenzetu-safari-web](https://github.com/cleven12/twenzetu-safari-web)

---

## Contact

- **Issues:** [GitHub Issues](https://github.com/cleven12/twenzetu-safari-api/issues)
- **Email:** cf89615f228bb45cc805447510de802dfb4bae17@proton.me
- **API Support:** cf89615f228bb45cc805447510de802dfb4bae17@proton.me

---

## 🙏 Acknowledgments

- Weather data: [Open-Meteo](https://open-meteo.com)
- Framework: [Django](https://djangoproject.com) & [DRF](https://www.django-rest-framework.org)
- Community contributors: [See all](https://github.com/cleven12/twenzetu-safari-api/graphs/contributors)

---

**⚡ Built with Django + DRF | 🇹🇿 Made in Tanzania | 🌍 For the World**
