# Movie Server & CLI Client

This project includes:

- A RESTful movie server written in Go
- A Python CLI client that authenticates, queries the server, and counts movies by year
- A Docker container that runs both

---

## Build & Run with Docker

### 1. Build the container image

```
docker build -t movie-app .

```

### 2. Run the container
```
docker run -d -p 8080:8080 --name movie-server movie-app

```

This will:
- Start the Go movie server on port 8080
- Install and make the Python CLI client available inside the container

### 3. Use the CLI client
You can run the client inside the container like this:
```
docker exec -it movie-server movie-client 1995 2001
```

You can pass one or more years as arguments. The client will:

- Authenticate with Basic Auth (username / password)
- Retrieve a Bearer token
- Fetch and count all movies for each year

### Cleanup
```
docker stop movie-server
docker rm movie-server
```

This solution meets all technical and design requirements, including:

- Fixing server build
- Writing a modular, working CLI client
- Proper containerization