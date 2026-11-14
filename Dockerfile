
FROM python:3.9-slim

WORKDIR /app

COPY . .

RUN chmod +x .github/scripts/entrypoint.sh \
    && chmod +x .github/scripts/update_index.sh

ENTRYPOINT ["/app/.github/scripts/entrypoint.sh"]
