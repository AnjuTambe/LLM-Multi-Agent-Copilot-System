
def run_search(query: str):
	# Mocking the response for now
	return {
		"search_results": [
			f"Top-rated spots in response to: {query}",
			"1. Pike Place Market",
			"2. Space Needle",
			"3. Mount Rainier Day Tour"
		]
	}

# Example manual test
# print(run_search("Seattle trip"))
