import requests


auth = None


def closed_issues_numbers(repo='microsoft/dotnet', page_size=30, auth=None):
    url = f'https://api.github.com/repos/{repo}/issues?'
    params = {
        'page': 1,
        'per_page': page_size,
        'state': 'closed'
    }

    def page_gen(res):
        for issue in res:
            yield issue['number']

    def req_gen():
        while True:
            r = requests.get(url, auth=auth, params=params)
            res = r.json()
            if not res:
                break
            yield from page_gen(res)
            params['page'] += 1

    return req_gen()


issues = closed_issues_numbers()
print(next(issues), next(issues))
