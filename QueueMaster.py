# Import the queue module for queue operations
import queue
# Import the time module for time operations
import time
# Import the random module for generating random choices and intervals
import random
# Import datetime for managing timestamps
from datetime import datetime

class Ticket:
    # Class definition for a ticket in the system
    def __init__(self, ticket_number):
        # Initialize the ticket with a number and a current timestamp
        self.ticket_number = ticket_number
        self.timestamp = datetime.now()
    
    def __str__(self):
        # Define the string representation of a ticket
        return f"Ticket #{self.ticket_number} - Issued at {self.timestamp.strftime('%Y-%m-%d %H:%M:%S')}"

# Function to generate a ticket and add it to the queue
def generate_ticket(queue, ticket_number):
    # Create a new ticket instance
    ticket = Ticket(ticket_number)
    # Add the ticket to the queue
    queue.put(ticket)
    # Print the generated ticket info
    print(f"Generated {ticket}")  
    
# Function to serve (process) the first ticket in the queue
def serve_ticket(queue):
    # Check if the queue is not empty
    if not queue.empty():
        # Remove the first ticket from the queue
        ticket = queue.get()
        # Print the serving ticket info
        print(f"Serving {ticket}")  
    else:
        # Message if no tickets are in the queue
        print("No tickets to serve.")  

# Function to simulate the ticketing system operation
def simulate_ticketing_system():
    # Initialize the ticket queue
    ticket_queue = queue.Queue()
    # Starting ticket number
    ticket_number = 1  
    
    try:
        # Infinite loop to simulate continuous operation
        while True:
            # Randomly choose to generate or serve a ticket
            action = random.choice(['generate', 'serve'])  
            
            if action == 'generate':
                # Generate a ticket
                generate_ticket(ticket_queue, ticket_number)
                # Increment the ticket number for the next ticket
                ticket_number += 1  
            else:
                # Serve (process) a ticket
                serve_ticket(ticket_queue)  
            # Random delay between actions
            time.sleep(random.randint(1, 3))
    # Catch the keyboard interrupt signal for graceful termination
    except KeyboardInterrupt:
        # Print termination message
        print("Simulation ended.")  

# Start the ticketing system simulation
simulate_ticketing_system()
