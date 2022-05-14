#Instructions

##install
```
Git clone https://github.com/segalzeyalz/class-names-visualizer.git
docker-compose up -d   
```

# Rate Limit 
OR: What to do to support more than 100 requests?
In case of a rate limit from the site we can use one of the following solutions:
1. Send requests by batches of the rate limit using the query arg: "amount" to the server: `http://127.0.0.1:5000/classNames?amount=100`. The code currently support this option.
2. Async - send a token for fetching the data, and run the whole request in batches in the server. We might consider lambda for it.
3. Send a stream 
