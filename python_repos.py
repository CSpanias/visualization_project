import requests

# make an API call and store the response

# store the URL of the API call
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
headers = {'Accept': 'application/vnd.github.v3+json'}
# make the API call
r = requests.get(url, headers=headers)
# status code: 200 = successful response
print(f"Status code: {r.status_code}")

# store API response in a variable while converting JSON to DICT
response_dict = r.json()
print(f"Total repos: {response_dict['total_count']}")

# explore info about the repos
repo_dicts = response_dict['items']
print(f"Repos returned: {len(repo_dicts)}")

# examine the first repo
repo_dict = repo_dicts[0]

print("\nSelected info about each repo:")
for repo_dict in repo_dicts:
    print(f"Name: {repo_dict['name']}")
    print(f"Owner: {repo_dict['owner']['login']}")
    print(f"Stars: {repo_dict['stargazers_count']}")
    print(f"\nKeys: {repo_dict['html_url']}")
    print(f"Created: {repo_dict['created_at']}")
    print(f"Updated: {repo_dict['updated_at']}")
    print(f"Description: {repo_dict['description']}")
