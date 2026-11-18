# Use official lightweight Python image
FROM python:3.11-slim

# Set working directory inside the container
WORKDIR /app

# Copy the program files into the container
COPY factorial.py test_factorial.py ./

# Run unit tests during build to ensure validity
RUN python -m unittest test_factorial.py

# Default command: run factorial program with sample input 5
CMD ["python", "factorial.py", "5"]
