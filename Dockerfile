# Use the Playwright Python base image
FROM mcr.microsoft.com/playwright/python:v1.41.0-jammy

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /tests
COPY . /app

# Install dependencies
RUN pip install -r requirements.txt

# Install Playwright browsers
RUN playwright install

# Switch to non-root user
USER pwuser

# Command to run the tests
CMD ["pytest", "--tb=short", "-p", "no:warnings"]
