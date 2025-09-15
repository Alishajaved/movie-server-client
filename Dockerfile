# Build the Go server
FROM golang:1.25 AS builder

WORKDIR /app

COPY . .

# Build server via Makefile
RUN make build

FROM python:3.12-slim

WORKDIR /srv

COPY --from=builder /app/movie-server .
COPY --from=builder /app/movies.db .

COPY client/ ./client/
COPY pyproject.toml .
RUN pip install --no-cache-dir .

EXPOSE 8080

# run the server
ENTRYPOINT ["./movie-server"]
CMD ["-port", "8080"]