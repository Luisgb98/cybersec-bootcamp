Project made with [@cherrero42](https://github.com/cherrero42).

## What is this project about?
We need to create a `blockchain`. The proof-of-work algorithm should be simple, for example, finding the number that, concatenated with the previous proof-of-work, matches the result of the `SHA-256` hash ending in `4242`. The chain of blocks will not be persistent, it will be stored in the memory of the server but the server will not be connected to any specific database software. When developing mining, three things must be done:
- Calculate proof of work
- Reward miners (one transaction)
- Creation of the new block and add it to the chain
Once the `blockchain` is created, you can interact with it through different `HTTP requests` on a `text-based API`:
- `POST` /transactions/new : Post a new transaction to add to the next block.
- `GET` /mine : Execute the proof of work and create a new block.
- `GET` /chain : Returns information about the full `blockchain` (blocks, transactions, etc).

## How to use it
You need to run the program with the following command:
```bash
python3 blockchain.py
```
Then, you can interact with the `API` at `http://localhost:5000/`.

Here is a [video](https://youtu.be/lbwK7kLjm4Y) that helps you to understand how `blockchain` works using Python.