# Django Boilerplate with Basic GET APIs

## What's included
- Minimal Django project (`myproject`)
- App `api` with simple GET endpoints:
  - `/` → Home (JSON)
  - `/status/` → Service status (JSON)
  - `/items/` → List of items (JSON array)
  - `/items/<id>/` → Item detail (JSON)

## Run (recommended inside a virtualenv)
1. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
   If `pip` is not available, try:
   ```
   py -m pip install -r requirements.txt
   ```

2. Apply migrations:
   ```
   python manage.py migrate
   ```

3. Run development server:
   ```
   python manage.py runserver
   ```

The API will be available at `http://127.0.0.1:8000/`.

## Notes
- If you're on Python 3.14 and encounter compatibility issues with dependencies, consider using Python 3.13 (see earlier conversation notes).
- This is a minimal starter app — add models, serializers, auth, and tests as needed.
