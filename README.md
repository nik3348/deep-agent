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

Note: Your agent implementation must be defined in a file named `agent.py` and expose the main agent instance under a variable named `root_agent`.

## Deployment

To deploy to Google Cloud Run, use the following command:

```bash
adk deploy cloud_run \
  --project=$GOOGLE_CLOUD_PROJECT \
  --region=$GOOGLE_CLOUD_LOCATION \
  --service_name=$SERVICE_NAME \
  --app_name=$APP_NAME \
  --with_ui \
  $AGENT_PATH
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