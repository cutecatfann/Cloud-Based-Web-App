# Cloud-Based Web Application

This repository holds a robust, scalable web application designed for listing charities and social services. The application has been developed using a range of modern technologies including Python with Flask for the backend, SQLite for initial database operations, and Google Cloud Platform services for scalability and containerization.

## Key Features

- **Submission & Viewership**: Users can submit information about charities or social services. These entries can be viewed on a separate page.
- **Data Entry Attributes**: Users can input various attributes about a charity such as:
  - Name
  - Description
  - Street Address
  - Type of Service
  - Phone Number
  - Hours of Operation
  - Reviews
- **Backend Implementation**: The backend is designed with abstraction in mind, featuring an abstract model class that can support multiple databases. The initial implementation is backed by SQLite.


## Technologies Used:

- **Google Cloud Platform (GCP)**: Used for deploying the application ensuring scalability and performance.
- **Docker**: The application is containerized using Docker, enabling consistency across multiple development, staging, and deployment environments.
- **Flask**: A lightweight WSGI web application framework used to simplify tasks such as setting up the backend of the web service.
- **SQLite**: Employed as a database backend for the application.
- **Google Cloud Platform**: 
  - **Cloud Build**: Managed service for building Docker containers.
  - **Container Registry**: Private container registry where Docker images are stored.
  - **Cloud Run**: Managed compute platform to deploy and manage containers.
  - **Cloud Datastore**: Scalable NoSQL cloud database for web and mobile applications.

## Application Structure:

- **MVP Pattern**: The application follows the Model-View-Presenter pattern.
- **Routes/Views**: Supports default landing page, a route for viewing all previously submitted entries, and a route for inserting new entries via an HTML form.
- **Backend Implementation**: Consists of an abstract model class supporting individual fields with varying data types.

## Running the Application:
### How to Run Locally

1. Setup the environment:
   ```bash
   python3 -m venv env
   source env/bin/activate
   ```

2. Install required packages:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the Flask app:
   ```bash
   python app.py
   ```
   The app will be accessible at `http://localhost:5000`.

### Run Via Docker
1. Ensure that Docker is installed on your machine.
2. Clone the repository and navigate to the directory containing the Dockerfile.
3. Build the Docker image by running the following command:
   ```
   docker build -f Dockerfile.large -t <your_dockerhub_id>/webapp .
   ```
4. Push the Docker image to Docker Hub:
   ```
   docker push <your_dockerhub_id>/webapp
   ```
5. Deploy the Docker container locally by mapping your machine’s port 8000 to the container’s port 5000:
   ```
   docker run -p 8000:5000 <your_dockerhub_id>/webapp
   ```

   Alternatively, deploy the container to GCP Cloud Run as described in the following steps.

### Deploying to GCP Cloud Run:

1. Build the container image in Cloud Build and store it in `gcr.io` by running the following command:
   ```
   gcloud builds submit --tag gcr.io/${GOOGLE_CLOUD_PROJECT}/webapp-proxy
   ```
2. Deploy the container on Cloud Run from Cloud Shell using the command:
   ```
   gcloud run deploy webapp-proxy \
     --image gcr.io/${GOOGLE_CLOUD_PROJECT}/webapp-proxy \
     --platform=managed --region=us-west1 --allow-unauthenticated
   ```

After successful deployment, a URL will be provided to access the running container on Cloud Run.

## Application Adaptation:

The application has been adapted to use Cloud Datastore as the backend, ensuring enhanced scalability and performance. Deployment involves containerization of the adapted application and hosting on Cloud Run.

## Note:

For successful deployment and running, ensure the necessary APIs are enabled on your GCP project, and the Google Cloud SDK is installed on your local machine. Follow the detailed instructions as outlined above for deployment on both local and cloud environments.

## Repository Structure

- `app.py`: Main application script.
- `model.py`: Abstract model class for backend operations.
- `model_sqlite3.py`: SQLite implementation of the abstract model class.
- `requirements.txt`: List of Python dependencies.
- `Dockerfile.large`: Dockerfile using Ubuntu 18.04 as the base image.
- `Dockerfile.small`: Optimized Dockerfile with minimal base image.

## Contribution

Feel free to fork this repository and contribute. Make sure to follow the existing coding style and submit a pull request. 

**Note**: Ensure to keep sensitive data, API keys, and credentials out of the source code.

## License

This project is licensed under the MIT License. See the LICENSE file for details.
