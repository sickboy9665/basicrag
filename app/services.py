from typing import Generator
from mock_datastore import retrieve_contexts
import logging

# Configure logging
logger = logging.getLogger(__name__)

def generate_streaming_response(query: str, top_k: int = 5) -> Generator[str, None, None]:
    """
    Generate a streaming response by combining retrieved contexts and the user query.
    """
    try:
        # Handle invalid top_k
        if top_k <= 0:
            top_k = 5  # Default to 5 if invalid
            yield "Warning: 'top_k' was invalid. Using default value of 5.\n"

        # Retrieve relevant contexts
        contexts = retrieve_contexts(query, top_k)

        if not contexts:
            yield "No relevant contexts found for your query.\n"
            return

        logger.info(f"Retrieved {len(contexts)} contexts for query '{query}'. Streaming response...")

        # Mock generation logic: Combine query with retrieved contexts
        for i, context in enumerate(contexts, start=1):
            logger.info(f"Streaming Step {i}: {context['title']} - {context['description']}")
            yield f"{i}: {context['title']} - {context['description']}\n"

        yield f"Based on your query '{query}', we retrieved {len(contexts)} relevant contexts.\n"
    
    except Exception as e:
        logger.error(f"Error during streaming response generation: {e}")
        yield "An error occurred while processing your request. Please try again later.\n"
