import random
from googlesearch import search

def google_search(prompt, num_results=5):
    search_results = []

    # Perform the Google search
    for result in search(prompt, num_results=num_results):
        search_results.append(result)

    return search_results

if __name__ == "__main__":
    while True:
        # Prompt for user input
        user_prompt = input("Enter your search query (type 'stopprompt' to exit): ")

        # Check if the user wants to exit
        if user_prompt.lower() == 'stopprompt':
            break

        # Perform the Google search
        results = google_search(user_prompt)

        # Display search results
        if results:
            print("\nSearch Results:")
            for i, result in enumerate(results, start=1):
                print(f"{i}. {result}")
        else:
            print("No results found.")
