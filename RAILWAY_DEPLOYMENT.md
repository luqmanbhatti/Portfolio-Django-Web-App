# Railway Deployment Guide

## Prerequisites
- Railway account at [railway.app](https://railway.app)
- GitHub repository with your Django project

## Deployment Steps

### 1. Connect Repository
- Create a new project on Railway
- Connect your GitHub repository
- Railway will auto-detect the `Procfile` and deploy

### 2. Add PostgreSQL Database
- In your Railway project, click "New" → "Database" → "Add PostgreSQL"
- Railway automatically sets the `DATABASE_URL` environment variable

### 3. Configure Environment Variables
In Railway's project settings, add these variables:

```
DJANGO_SECRET_KEY=your-secret-key-here
DEBUG=False
ALLOWED_HOSTS=your-app-name.up.railway.app
```

### 4. Update CSRF Settings
After deployment, uncomment and update this line in `settings.py`:
```python
CSRF_TRUSTED_ORIGINS = ['https://your-app-name.up.railway.app']
```

### 5. Run Migrations
In Railway's deployment logs or using Railway CLI:
```bash
python manage.py migrate
python manage.py collectstatic --noinput
python manage.py createsuperuser
```

## Important Notes
- **Static Files**: Whitenoise handles static files automatically
- **Database**: PostgreSQL is used in production (via `DATABASE_URL`)
- **Security**: HSTS and secure cookies are enabled when `DEBUG=False`
- **Local Development**: Still uses SQLite when `DATABASE_URL` is not set

## Troubleshooting
- If static files don't load, ensure `collectstatic` ran successfully
- Check Railway logs for any migration errors
- Verify all environment variables are set correctly
