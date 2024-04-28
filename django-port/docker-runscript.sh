#!/bin/bash

for dockerfile in "$@"; do
  image_name=$(basename "$dockerfile" ".Dockerfile")  # Extract image name

  # Build the Docker image
  docker build -t "$image_name" -f "$dockerfile" . || {
      echo "Error building image from Dockerfile: $dockerfile"
      exit 1  # Exit on failure
  }
done

# All builds successful, execute Docker Compose
echo "Images built successfully, starting services"
docker-compose up
