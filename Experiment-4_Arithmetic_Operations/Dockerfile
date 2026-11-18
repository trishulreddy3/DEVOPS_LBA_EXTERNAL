FROM python:3.11-slim

WORKDIR /app

# Copy python files
COPY arithmetic.py test_arithmetic.py app.py ./

# Execute unit tests during docker build
RUN python -m unittest test_arithmetic.py

# Expose microservice port
EXPOSE 8080

# Start HTTP server
CMD ["python", "app.py"]
