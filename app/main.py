from fastapi import FastAPI, HTTPException
from fastapi.responses import StreamingResponse
from schemas import QueryRequest
from services import generate_streaming_response
import logging

# Initialize FastAPI app
app = FastAPI()

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@app.post(
    "/query",
    summary="Streamed Query Response",
    description="Accepts a query and returns a streamed response combining retrieved contexts with the user query.",
    response_description="Streamed response integrating query and relevant contexts.",
)
async def query(request: QueryRequest):
    """
    Handle user queries and return a streamed response.
    """
    try:
        # Log the incoming request
        logger.info(f"Received query: {request.query}, top_k: {request.top_k}")

        # Generate a streaming response
        response_generator = generate_streaming_response(request.query, request.top_k)

        # Return the streaming response
        return StreamingResponse(response_generator, media_type="text/plain")
    except Exception as e:
        logger.error(f"Error processing request: {e}")
        raise HTTPException(status_code=500, detail="An internal error occurred.")
