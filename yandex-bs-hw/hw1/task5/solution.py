import requests

auth = None


def closed_issues_numbers(repo='microsoft/dotnet', page_size=30, auth=auth):
    closed_issues = []
    url = f'https://api.github.com/repos/{repo}/issues?'
    params = {
        'page': 1,
        'per_page': page_size,
        'state': 'closed'
    }
    while True:
        r = requests.get(url, auth=auth, params=params)
        res = r.json()
        if not res:
            break
        closed_issues += [issue['number'] for issue in res]
        params['page'] += 1

    return closed_issues


print(closed_issues_numbers()[:15])
