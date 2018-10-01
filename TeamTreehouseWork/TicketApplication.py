TICKET_PRICE = 10
SERVICE_CHARGE = 2

tickets_remaining = 100

# Create a function that calculates the cost of tickets
def calculate_cost_of_tickets(num_tickets):
    # Add the service charge
    return (num_tickets * TICKET_PRICE) + SERVICE_CHARGE

# Run this code continuously until we run out of tickets
while tickets_remaining >= 1:
    # Output how many tickets are remaining using the tickets_remaining variable
    print("There are {} tickets remaining.".format(tickets_remaining))
    # Gather the user's name and assign it to a new variable
    name = input("What is your name?  ")
    # Prompt the user by name and ask how many tickets they would like
    num_tickets = input("How many tickets would you like, {}?  ".format(name))
    # ADD A TRY EXCEPT AS USER CAN ENTER A STRING HERE
    try:
        # Convert num_tickets to int
        num_tickets = int(num_tickets)
        # Raise a value error if the request is for more tickets than available
        if num_tickets > tickets_remaining:
            raise ValueError("There are only {} tickets remaining".format(tickets_remaining))
    except ValueError as err:
        # Deal with error
        print("Issue with input. {}. Please try again!".format(err))
    else:
        # Calculate the price (number of tickets multiplied by the price) and assign it to a variable
        amount_due = calculate_cost_of_tickets(num_tickets)
        # Output the price to the screen
        print("The total due is ${}".format(amount_due))
        # Prompt user if they want to proceed.  Y/N?
        should_proceed = input("Do you want to proceed?  Y/N  ")

        # If they want to proceed
        if should_proceed.lower() == "y":
            # print out to the screen "SOLD!" to confirm purchase
            # TODO: Gather credit card information and process it.
            print("SOLD!")
            # and then decrement the tickets remaining by the number of tickets purchased
            tickets_remaining -= num_tickets
        # Otherwise....
        else:
            # Thank them by name
            print("Thank you anyways, {}!".format(name))

# Notify user that the tickets are sold out
print("Sorry the tickets are all sold out!!! :(")
