import random
import string


# Step 1: Create a list of random dicts (from 2 to 10)
def create_random_dicts():
    num_dicts = random.randint(2, 10)  # Randomly decide how many dicts to generate (between 2 and 10)
    dict_list = []  # List to hold our dicts

    for i in range(num_dicts):
        num_keys = random.randint(1, 5)  # Each dict will have between 1 to 5 random keys
        keys = random.sample(string.ascii_lowercase, num_keys)  # Randomly choose keys from letters (a-z)
        dict_data = {key: random.randint(0, 100) for key in keys}  # Assign random numbers (0-100) to keys
        dict_list.append(dict_data)  # Add the generated dict to the list

    return dict_list


# Step 2: Combine the list of dicts into one common dict
def combine_dicts(dict_list):
    combined_dict = {}  # Dictionary to store the final result

    # Iterate through each dict in the list
    for index, d in enumerate(dict_list):
        # Iterate through the keys of the current dictionary
        for key, value in d.items():
            new_key = f"{key}_{index + 1}" if key not in combined_dict else key
            # If the key already exists in the combined_dict, compare values and keep the max
            if key in combined_dict:
                if value > combined_dict[key]:  # If the current value is greater, update it
                    combined_dict[key] = value
                    # Renaming key to include the dict number with max value
                    combined_dict[f"{key}_{index + 1}"] = combined_dict.pop(key)
            else:
                # If it's a new key, add it to the combined_dict as is
                combined_dict[key] = value

    return combined_dict


# Testing the functions
dict_list = create_random_dicts()  # Create the list of random dicts
print("Generated List of Dicts:")
print(dict_list)

final_combined_dict = combine_dicts(dict_list)  # Combine them into one dict
print("\nCombined Dict:")
print(final_combined_dict)
