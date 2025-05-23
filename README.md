# Agent Carro

A Python-based agent system built with Poetry for dependency management.

## Prerequisites

- Python 3.x
- Poetry (Python package manager)
- Google Cloud SDK (for deployment)

## Setup

1. Install dependencies using Poetry:

```bash
poetry install
```

2. Set up your environment variables:

```bash
cp .env.example .env
```

Edit the `.env` file with your specific configuration values.

## Running Locally

To run the application locally with the debug UI:

```bash
poetry run adk web
```

or

```bash
poetry run python main.py
```

Note: Your agent implementation must be defined in a file named `agent.py` and expose the main agent instance under a variable named `root_agent`.

Alternatively you can run a local FastAPI server with:

```bash
poetry run adk api_server
```

## Deployment

To deploy an all in one service to Google Cloud Run, use the following command:

```bash
adk deploy cloud_run \
  --project=$GOOGLE_CLOUD_PROJECT \
  --region=$GOOGLE_CLOUD_LOCATION \
  --service_name=$SERVICE_NAME \
  --app_name=$APP_NAME \
  --with_ui \
  $AGENT_PATH
```

or for more control over session db, etc:

```bash
gcloud run deploy $SERVICE_NAME \
--source . \
--region $GOOGLE_CLOUD_LOCATION \
--project $GOOGLE_CLOUD_PROJECT \
--allow-unauthenticated \
--set-env-vars="GOOGLE_CLOUD_PROJECT=$GOOGLE_CLOUD_PROJECT,GOOGLE_CLOUD_LOCATION=global,GOOGLE_GENAI_USE_VERTEXAI=TRUE,CARRO_API_KEY=$CARRO_API_KEY"
# Add any other necessary environment variables your agent might need
```

Make sure you have the following environment variables set:

- `GOOGLE_CLOUD_PROJECT`: Your Google Cloud project ID
- `GOOGLE_CLOUD_LOCATION`: Your desired deployment region
- `SERVICE_NAME`: Name for your Cloud Run service
- `APP_NAME`: Name of your application
- `AGENT_PATH`: Path to your agent implementation

## Development

The project uses Poetry for dependency management. To add new dependencies:

```bash
poetry add <package-name>
```

To update dependencies:

```bash
poetry update
```
