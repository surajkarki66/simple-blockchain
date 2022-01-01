# simple-blockchain

## To run it locally

```bash
  $ pip install -r "requirements.txt"
  $ python main.py
```

## To run it in docker

```bash
  $ docker build -t simple-blockchain .
  $ docker run -it -p <port>:<port> simple-blockchain:latest
```

Now all apis are live.

## Endpoints

##### 1) To mine a block in a blockchain:

GET Request on: `http://localhost:5000/mine_block`

##### 2) To get full blockchain

GET Request on: `http://localhost:5000/get_chain`

##### 3) To check if the chain is valid or not

GET Request on: `http://localhost:5000/is_valid`
