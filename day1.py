# finding key connectors (from the book 'data science from scratch')

# Problem : To identify who the key connectors are in a social network (in this case, data scientists).

# Data given: A list of users, where each user is represented by a dictionary containing an "id" and a "name".

# Data given (second part): A list of friendships, where each friendship is represented by a tuple containing the ids of the two users who are friends.

# Approach: We will create a list of friends for each user, and then ask who has the most friends.


# Data setup
users = [
    {"id": 0, "name": "Hero"},
    {"id": 1, "name": "Dunn"},
    {"id": 2, "name": "Sue"},
    {"id": 3, "name": "Chi"},
    {"id": 4, "name": "Thor"},
    {"id": 5, "name": "Clive"},
    {"id": 6, "name": "Hicks"},
    {"id": 7, "name": "Devin"},
    {"id": 8, "name": "Kate"},
    {"id": 9, "name": "Klein"}
]

friendships = [
    (0, 1), (0, 2), (1, 2), (1, 3), (2, 3), (3, 4),
    (4, 5), (5, 6), (5, 7), (6, 8), (7, 8), (8, 9)
]

# Initialize friends list for each user
for user in users:
    user["friends"] = []

# Populate the friends lists
for i, j in friendships:
    users[i]["friends"].append(users[j])  # Add user j as a friend of user i
    users[j]["friends"].append(users[i])  # Add user i as a friend of user j

# Function to calculate number of friends
def number_of_friends(user):
    return len(user["friends"])

# Calculate total connections
total_connections = sum(number_of_friends(user) for user in users)

# Calculate the average number of connections
num_users = len(users)
avg_connections = total_connections / num_users

# Print intermediate results for debugging
print("Total connections:", total_connections)
print("Number of users:", num_users)
print("Average connections:", avg_connections)

# Create a list of (user_id, number_of_friends) tuples
number_of_friends_by_id = [(user["id"], number_of_friends(user)) for user in users]

# Sort the list by number of friends in descending order
sorted_list = sorted(number_of_friends_by_id, 
                     key=lambda user_id_num_friends: user_id_num_friends[1], 
                     reverse=True)

# Print the sorted list of users by number of friends
print("Sorted list of users by number of friends:")
for user_id, num_friends in sorted_list:
    print(f"User {user_id} has {num_friends} friends")


# Define the threshold for key connectors (e.g., users with 3 or more friends)
key_connectors_threshold = 3

print("\nThe key connectors are:")
for user_id, num_friends in sorted_list:
    if num_friends >= key_connectors_threshold:
        print(f"User {user_id} with {num_friends} friends")




    
