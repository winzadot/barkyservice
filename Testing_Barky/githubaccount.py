import requests

class GithubAccountTest:
    
    def test_connect_github():
        githubtest_username = "winzadot"
        next_page_of_results = f"https://api.github.com/users/{githubtest_username}/starred"
        while next_page_of_results:
            stars_response = requests.get(
                next_page_of_results,
                headers={"Accept": "application/vnd.github.v3.star+json"},
            )
            next_page_of_results = stars_response.links.get("next", {}).get("url")
            
        return  stars_response.json()
