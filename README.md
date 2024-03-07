# Ticketing-System-Simulation

## Description

This Python program simulates a ticketing system for a service center where customers take a number and wait for their turn to be served. It employs a queue-based system to manage ticket issuance and processing in a first-in, first-out (FIFO) manner.

The simulation includes two main phases: the **Generate Tickets Phase**, where customer tickets are generated and added to the queue at random intervals, and the **Process Tickets Phase**, where tickets are dequeued and served, simulating the serving of customers.

A `Ticket` class is used to represent individual tickets, containing details such as the ticket number and the timestamp when the ticket was issued. The program makes use of Python's `queue.Queue` from the standard library to implement the queue.

## Running Behavior

The program is designed to run indefinitely, continuously simulating the generation and processing of tickets. This allows for a dynamic demonstration of how the ticketing system would operate over time.

## How to Stop/Terminate the Program

To terminate the simulation, you will need to manually interrupt the program. Depending on your operating system, the method to do this is as follows:

- **Windows**: Press `Ctrl+C` in the command prompt or PowerShell window where the program is running.
- **Mac**: Press `Ctrl+C` in the Terminal window.
- **Linux**: Press `Ctrl+C` in the terminal.

These keyboard shortcuts send an interrupt signal to the program, which is programmed to catch this signal and terminate the simulation by exiting the loop and ending the program execution.

