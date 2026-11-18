# Lightweight Python image
FROM python:3.11-slim

WORKDIR /app

# Copy scripts and tests
COPY prime.py test_prime.py app.py ./

# Run unit tests to verify correctness during build
RUN python -m unittest test_prime.py

# Expose port 8000 for Kubernetes Service
EXPOSE 8000

# Start HTTP microservice
CMD ["python", "app.py"]
