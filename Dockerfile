FROM python:3.12-slim

WORKDIR /app

RUN apt-get update && apt-get install -y --no-install-recommends \
    ca-certificates curl \
    && rm -rf /var/lib/apt/lists/*

COPY NetAngularAzureInterviewPrep/requirements.txt ./NetAngularAzureInterviewPrep/requirements.txt
RUN pip install --no-cache-dir -r NetAngularAzureInterviewPrep/requirements.txt

COPY NetAngularAzureInterviewPrep ./NetAngularAzureInterviewPrep
COPY DesignPatternsLearnignFolder ./DesignPatternsLearnignFolder
COPY Linq ./Linq

WORKDIR /app/NetAngularAzureInterviewPrep

EXPOSE 8501

HEALTHCHECK CMD curl --fail http://localhost:8501/_stcore/health || exit 1

CMD ["streamlit", "run", "app.py", \
     "--server.port=8501", \
     "--server.address=0.0.0.0", \
     "--server.headless=true", \
     "--browser.gatherUsageStats=false"]
