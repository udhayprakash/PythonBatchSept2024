import objgraph
import time

# Initial count of objects
print("Initial object count:")
objgraph.show_most_common_types()
print()

def my_leaky_func():
    # This function creates a memory leak
    leaky_list = []
    
    # Create some data that won't be cleaned up
    for i in range(1000):
        temp_dict = {'data': f'item_{i}', 'more_data': [1, 2, 3] * 100}
        leaky_list.append(temp_dict)
    
    # Create a circular reference
    leaky_list.append(leaky_list)
    
    # Store in global scope (making it leak)
    global leaked_data
    leaked_data = leaky_list

# Start tracking growth
print("Starting growth tracking...")
objgraph.show_growth(limit=10)
print()

# Run leaky function multiple times
for _ in range(3):
    my_leaky_func()
    time.sleep(1)  # Give some time between calls

# Show memory growth
print("After running leaky function:")
objgraph.show_growth(limit=10)

# Optional: Show reference chain for leaked objects
# objgraph.show_chain(
#     objgraph.find_backref_chain(
#         leaked_data,
#         objgraph.is_proper_module
#     ),
#     filename='chain.png'
# )