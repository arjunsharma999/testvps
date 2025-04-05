from fastapi import FastAPI, Query
from fastapi.responses import PlainTextResponse
import logging
import uvicorn
from typing import Optional

# Set up logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[logging.FileHandler("iot_data.log"), logging.StreamHandler()]
)
logger = logging.getLogger('iot_endpoint')

# Initialize FastAPI app
app = FastAPI(title="IoT Data Receiver")

@app.get("/home.php", response_class=PlainTextResponse)
async def receive_iot_data(
    id: str = Query(..., description="Device ID"),
    data: str = Query(..., description="Comma-separated sensor data")
):

    logger.info(f"Received data from device {id}: {data}")
    
    if data:
        try:
    
            data_values = data.split(',')
            

            logger.info(f"Parsed {len(data_values)} values from device {id}")
            
            if len(data_values) > 0 and len(data_values[0]) == 10:
                timestamp = data_values[0]
                logger.info(f"Timestamp: {timestamp}")
            

            
        except Exception as e:
            logger.error(f"Error processing data: {e}")
            
    
    return "ACK"

# Add a health check endpoint
@app.get("/health", response_class=PlainTextResponse)
async def health_check():
    return "OK"

if __name__ == "__main__":
    # Run the server using Uvicorn
    uvicorn.run(app, host="0.0.0.0", port=5000)