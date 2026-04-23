def queue_time(customers, n):
    # Create a list representing each till (worker) programatically
    # As example: if there are 3 Tills will be [0, 0, 0]. If there is 5 Tills will be [0, 0, 0, 0, 0]
    tills = [0] * n

    # Go through each customer in the queue (in order)
    for c in customers:
        # Find the till that will be free the soonest
        # (i.e., the one with the smallest accumulated time)
        min_value = min(tills)

        # Get the index (which till it is)
        index = tills.index(min_value)

        # Assign this customer to that till
        # This increases that till's workload
        tills[index] += c

    # After all customers are assigned,
    # the total time required is when the busiest till finishes
    return max(tills)


# Challenge: https://www.codewars.com/kata/57b06f90e298a7b53d000a86/train/python