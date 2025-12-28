# DevZone

DevZone is a communication platform for tech developers and enthusiasts. It allows developers to showcase their projects, connect with other developers, share skills, and receive feedback through a voting system.

## Features

- **User Profiles**: Create and customize developer profiles with bio, skills, and social links
- **Project Showcase**: Share your projects with descriptions, demo links, and source code links
- **Voting System**: Users can upvote or downvote projects with reviews
- **Skills Management**: Add and display your technical skills
- **Messaging System**: Send messages to other developers
- **REST API**: Full REST API with JWT authentication
- **Tag System**: Organize projects with tags
- **Search & Filter**: Find projects and developers easily

## Tech Stack

- **Backend**: Django 5.2.5
- **API**: Django REST Framework
- **Authentication**: JWT (Simple JWT)
- **Database**: PostgreSQL
- **Static Files**: WhiteNoise
- **Containerization**: Docker & Docker Compose
- **Python**: 3.13

## Prerequisites

- Python 3.13+
- PostgreSQL (or use Docker)
- Docker and Docker Compose (optional, for containerized setup)

## Installation

### Option 1: Using Docker (Recommended)

1. Clone the repository:
```bash
git clone https://github.com/yourusername/devzone.git
cd devzone
```

2. Create a `.env` file in the root directory:
```env
DJANGO_SECRET_KEY=your-secret-key-here
DEBUG=True
DJANGO_ALLOWED_HOSTS=localhost,127.0.0.1

DATABASE_NAME=devzone_db
DATABASE_USERNAME=devzone_user
DATABASE_PASSWORD=your-database-password
DATABASE_HOST=db
DATABASE_PORT=5432

EMAIL_BACKEND=django.core.mail.backends.smtp.EmailBackend
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_HOST_USER=your-email@gmail.com
EMAIL_HOST_PASSWORD=your-email-password
```

3. Build and run with Docker Compose:
```bash
docker-compose up --build
```

The application will be available at `http://localhost:8000`

### Option 2: Local Development

1. Clone the repository:
```bash
git clone https://github.com/yourusername/devzone.git
cd devzone
```

2. Create a virtual environment:
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Set up PostgreSQL database and create a `.env` file (see above)

5. Run migrations:
```bash
python manage.py migrate
```

6. Create a superuser:
```bash
python manage.py createsuperuser
```

7. Collect static files:
```bash
python manage.py collectstatic
```

8. Run the development server:
```bash
python manage.py runserver
```

## Environment Variables

Create a `.env` file in the root directory with the following variables:

| Variable | Description | Required |
|----------|-------------|----------|
| `DJANGO_SECRET_KEY` | Django secret key | Yes |
| `DEBUG` | Debug mode (True/False) | Yes |
| `DJANGO_ALLOWED_HOSTS` | Comma-separated list of allowed hosts | Yes |
| `DATABASE_NAME` | PostgreSQL database name | Yes |
| `DATABASE_USERNAME` | PostgreSQL username | Yes |
| `DATABASE_PASSWORD` | PostgreSQL password | Yes |
| `DATABASE_HOST` | Database host (default: 'db') | No |
| `DATABASE_PORT` | Database port (default: '5432') | No |
| `EMAIL_BACKEND` | Email backend | Yes |
| `EMAIL_HOST` | SMTP host | Yes |
| `EMAIL_PORT` | SMTP port | Yes |
| `EMAIL_USE_TLS` | Use TLS (True/False) | Yes |
| `EMAIL_HOST_USER` | Email username | Yes |
| `EMAIL_HOST_PASSWORD` | Email password | Yes |

## API Endpoints

### Authentication
- `POST /api/users/token/` - Obtain JWT token pair
- `POST /api/users/token/refresh/` - Refresh access token

### Projects
- `GET /api/projects/` - List all projects
- `GET /api/projects/project/<slug>/` - Get project details
- `POST /api/projects/<slug>/vote/` - Vote on a project (requires authentication)
- `DELETE /api/remove-tag/` - Remove tag from project

### API Usage Example

```bash
# Get access token
curl -X POST http://localhost:8000/api/users/token/ \
  -H "Content-Type: application/json" \
  -d '{"username": "your_username", "password": "your_password"}'

# Get all projects
curl http://localhost:8000/api/projects/

# Vote on a project (requires authentication)
curl -X POST http://localhost:8000/api/projects/my-project/vote/ \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"value": "up"}'
```

## Project Structure

```
devzone/
├── api/              # REST API endpoints
├── core/             # Django project settings
├── main/             # Main/home app
├── projects/         # Projects app (models, views, templates)
├── users/            # Users app (profiles, skills, messages)
├── static/           # Static files (CSS, JS, images)
├── templates/        # HTML templates
├── docker-compose.yml
├── Dockerfile
├── manage.py
└── requirements.txt
```

## Running Tests

```bash
python manage.py test
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is open source and available under the [MIT License](LICENSE).

## Author

Your Name - [Your GitHub](https://github.com/yourusername)

## Acknowledgments

- Django community
- Django REST Framework
- All contributors
