import logging
# Configure logging
logger = logging.getLogger(__name__)
mock_data = {
    "jobs": [
        {"title": "Software Engineer", "description": "Responsible for building and maintaining software applications."},
        {"title": "Data Scientist", "description": "Focuses on analyzing data to extract meaningful insights."},
        {"title": "AI Engineer", "description": "Develops AI models and systems for intelligent automation."},
        {"title": "Full Stack Developer", "description": "Handles both frontend and backend development tasks."},
        {"title": "DevOps Engineer", "description": "Ensures smooth software deployment and infrastructure management."},
        {"title": "Cybersecurity Specialist", "description": "Protects computer systems and networks from cyber threats."},
        {"title": "UX/UI Designer", "description": "Creates user-centered design experiences for software applications."},
        {"title": "Business Analyst", "description": "Analyzes business needs and develops solutions to improve operations."},
        {"title": "Cloud Architect", "description": "Designs and builds cloud computing systems for scalability and efficiency."},
        {"title": "Network Architect", "description": "Manages and maintains computer networks for optimal performance."},
    ]
}

def retrieve_contexts(query: str, top_k: int = 5) -> list[dict]:
    """
    Simulate retrieval of job descriptions based on the query.
    """
    try:
        # Simple mock logic: Find jobs where the title contains the query (case-insensitive)
        results = [
            job for job in mock_data["jobs"] if query.lower() in job["title"].lower()
        ]
        return results[:top_k]
    except Exception as e:
        logger.error(f"Error retrieving contexts for query '{query}': {e}")
        return []
