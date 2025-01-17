#### Query Streaming API

This project provides a FastAPI-based service that accepts a user query and returns a streamed response combining retrieved contexts and the query. The service leverages mock data to simulate a retrieval system for job descriptions.

##### Features

Receive Queries: Accepts a user query (such as a job title) to retrieve relevant job descriptions.
Streamed Responses: Returns a streamed response that combines the query and the retrieved contexts.
Customizable Results: You can specify the number of top contexts to retrieve via the top_k parameter.


##### Project Structure
main.py: FastAPI application that handles incoming HTTP requests, processes them, and streams the response.
schemas.py: Contains the request model used to validate the query and top_k value.
services.py: Contains the logic to generate a streaming response and retrieve relevant job descriptions from mock data.
mock_datastore.py: Simulates a data store of job descriptions for demonstration purposes.
Setup

##### Prerequisites
Ensure you have Python 3.7+ installed on your system.

##### Install Dependencies
To install the required dependencies, run the following command:
pip install -r requirements.txt

Once the dependencies are installed, you can run the FastAPI server using uvicorn:
uvicorn main:app --reload
The application will be available at http://127.0.0.1:8000.

#### API Documentation
You can access the automatically generated Swagger UI documentation at:
http://127.0.0.1:8000/docs

#### Endpoints
POST /query
Accepts a query and returns a streamed response integrating relevant contexts from the mock datastore.

Request Body:
{
  "query": "Engineer",
  "top_k": 5
}
query: The search query (e.g., "Engineer") to retrieve relevant job descriptions.
top_k (Optional): The number of top contexts to retrieve. Defaults to 5 if not provided.

Response:
The response will be streamed, with each step including a retrieved context and the final generated response based on the provided query.

#### Mock Data
The mock datastore contains a list of job descriptions with titles such as "Software Engineer", "Data Scientist", "AI Engineer", etc. The service simulates a search for relevant job titles based on the user's query.

#### License
This project is licensed under the MIT License - see the LICENSE file for details.