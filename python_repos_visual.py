import requests

from plotly.graph_objs import Bar
from plotly import offline

# store the URL of the API call
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
headers = {'Accept': 'application/vnd.github.v3+json'}
# make the API call
r = requests.get(url, headers=headers)
# status code: 200 = successful response
print(f"Status code: {r.status_code}")

# process results
# store API response in a variable while converting JSON to DICT
response_dict = r.json()
# explore info about the repos
repo_dicts = response_dict['items']
repo_names, stars = [], []

for repo_dict in repo_dicts:
    repo_names.append(repo_dict['name'])
    stars.append(repo_dict['stargazers_count'])
    
# make visualization
data = [{
    'type': 'bar',
    'x': repo_names,
    'y': stars,
    }]

my_layout = {
    'title': 'Most-Starred Python Projects on GitHub',
    'xaxis': {'title': 'Repository'},
    'yaxis': {'title': 'Stars'},
    }

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='python_repos.html')