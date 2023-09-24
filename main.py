import argparse

from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse, Response
import uvicorn

TIMEOUT_KEEP_ALIVE = 5  # seconds.

app = FastAPI()


@app.post("/generate", response_model=dict)
async def generate(request: Request) -> Response:
    """Generate completion for the request.

    The request should be a JSON object with the following fields:
    - prompt: the prompt to use for the generation.
    - sampling_params: the sampling parameters (See `SamplingParams` for details).
    """

    return JSONResponse({
        "text": ["Generated text goes here..."]
    })


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--host", type=str, default="localhost")
    parser.add_argument("--port", type=int, default=8000)
    args = parser.parse_args()

    uvicorn.run(
        app,
        host=args.host,
        port=args.port,
        log_level="debug",
        timeout_keep_alive=TIMEOUT_KEEP_ALIVE,
    )