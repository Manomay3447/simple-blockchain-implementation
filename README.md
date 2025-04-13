# Simple Blockchain Implementation in Python

This is a minimal implementation of a Blockchain using Python. It demonstrates the core concepts of how blocks are connected using cryptographic hashes, similar to a linked list structure.

## Features

- Each block stores:
  - Data (as bytes)
  - A reference to the previous block's hash
  - Its own hash computed using SHA-256
- Genesis block (the first block) is created manually
- New blocks can be added to the chain
- The chain can be printed to view its structure

## How It Works

- The `Node` class represents a single block.
- The `BlockChain` class manages the chain of blocks.
- Each block's hash is calculated using the block's data + the previous block's hash, ensuring immutability.

## Usage

python
# Create a new Blockchain with the Genesis block
test = BlockChain("AnyString".encode('UTF-8'))

# Add new blocks
test.insertAtEnd("TestString".encode('UTF-8'))
test.insertAtEnd("String234".encode('UTF-8'))

# Print the blockchain
test.printLL()
