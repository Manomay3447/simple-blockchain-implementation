import hashlib

class Node:
    def __init__(self, data, prev_hash):
        self.data = data
        self.next = None
        self.prev_hash = prev_hash
        current_data = data
        if prev_hash:
            current_data += prev_hash.encode('UTF-8')  # Ensure data is bytes
        self.curr_hash = hashlib.sha256(current_data).hexdigest()

class BlockChain:
    def __init__(self,data):
        self.head = Node(data,None)

    def insertAtEnd(self, data):

        current_node = self.head
        while current_node.next:
            current_node = current_node.next
        
        current_node.next = Node(data,current_node.curr_hash)

    def remove_last_node(self):
        if self.head:
            print("Cannot Delete Genesis")
            return

        current_node = self.head
        while current_node.next and current_node.next.next:
            current_node = current_node.next

        if current_node.next:
            current_node.next = None

    def sizeOfLL(self):
        size = 0
        if self.head:
            current_node = self.head
            while current_node:
                size += 1
                current_node = current_node.next
        return size-1

    def printLL(self):
        current_node = self.head
        print("Genesis:")
        print(f"Current_Hash: {current_node.curr_hash}")
        current_node = current_node.next
        while current_node:
            print(f"Previous_Hash: {current_node.prev_hash}")
            print(f"Data: {current_node.data.decode('UTF-8')}")
            print(f"Current_Hash: {current_node.curr_hash}")
            current_node = current_node.next

# Test the LinkedList class
test = BlockChain("Piyush".encode('UTF-8'))
test.insertAtEnd("Manomay".encode('UTF-8'))
test.insertAtEnd("Shreyash".encode('UTF-8'))
test.printLL()
