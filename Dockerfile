# Package the app into docker container
FROM python:3.11-slim

# Set the working directory inside container
WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the current directory's content into container
COPY . .

# Expose port 8080
EXPOSE 8080

# Run test and start app
CMD [ "sh", "-c", "pytest pytest_app.py && python app.py" ]
