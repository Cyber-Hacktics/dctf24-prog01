# Use the official Alpine image
FROM python:3.9-alpine

# Set environment variables
ENV PYTHONUNBUFFERED=1

# Create and set working directory
WORKDIR /app

# Copy the server script into the container
COPY server.py .

# Install any dependencies
RUN pip install --no-cache-dir ast

# Expose the port the server will run on
EXPOSE 33000

# Run the server script
CMD ["python", "server.py"]
