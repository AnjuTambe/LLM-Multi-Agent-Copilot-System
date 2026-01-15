def web_search_tool(query: str):
    """
    Mock web search tool. In a real app, this would use Google Custom Search or Tavily.
    """
    # Demo/Mock responses based on query keywords
    query_lower = query.lower()
    
    if "seattle" in query_lower:
        return [
            "1. Space Needle - Iconic observation tower.",
            "2. Pike Place Market - Famous for fish tossing and Starbucks.",
            "3. Chihuly Garden and Glass - Amazing glass art.",
            "4. Museum of Pop Culture (MoPOP) - Music and sci-fi museum."
        ]
    elif "weather" in query_lower:
        return ["The weather looks sunny with a high of 72°F."]
    elif "python" in query_lower:
        return ["Python is a high-level, general-purpose programming language."]
    else:
        return [
            f"Result 1 for {query}",
            f"Result 2 for {query}",
            f"Result 3 for {query}"
        ]
