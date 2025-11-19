class Ticket:
    def __init__(self, ticket_id, customer_name, issue):
        self.ticket_id = ticket_id
        self.customer_name = customer_name
        self.issue = issue
        self.next = None
class Queue:
    def __init__(self, front, rear):
        self.front = None
        self.rear = None
    def enqueue(self, ticket_id, customer_name, issue):
        if self.rear is None:
            self.front = self.rear = Ticket(ticket_id, customer_name, issue)
            return
        else:
            self.rear.next = Ticket(ticket_id, customer_name, issue)
            self.rear = self.rear.next
            return
    def dequeue(self):
        if self.front is None:
            return None
        else:
            removed = self.front
            self.front = self.front.next
            if self.front is None:
                self.rear = None
            return removed
    def peek(self):
        if self.front is None:
            return None
        else:
            return self.front
    def is_empty(self):
        return self.front is None
    def display(self):
        current = self.front
        while current:
            print(f"Ticket {current.ticket_id}: {current.customer_name} - {current.issue}")
            current = current.next
    def find_ticket(self,ticket_id):
        current = self.front
        while current:
            if current.ticket_id == ticket_id:
                return current
            current = current.next
        else:
            return None
    def total_tickets(self):
        count = 0
        current = self.front
        while current:
            count += 1
            current = current.next
        return count
import random
def simulate_day(queue):
    new_tickets = random.randint(3,7)
    print(f"Simulating {new_tickets} tickets")
    processed = random.randint(1,4)
    print(f"Processing {processed} tickets")
    ticket







