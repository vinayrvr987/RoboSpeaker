FROM python:3.10-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the contents of the current directory to the working directory inside the container
COPY . /app

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Run the Python script when the container starts
CMD ["python", "main.py"]
