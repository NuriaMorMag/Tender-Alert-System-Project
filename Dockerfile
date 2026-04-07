# Use official Python image
FROM python:3.11

# Set working directory
WORKDIR /app

# Copy project files
COPY . .

# Install dependencies
RUN pip install -r requirements.txt

# Start app with Gunicorn
CMD ["gunicorn", "-c", "gunicorn.conf.py", "app:app"]