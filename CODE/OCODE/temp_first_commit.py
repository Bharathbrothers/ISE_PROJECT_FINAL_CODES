import requests

# this gives the first 10 commits to a repo
owner = 'mozilla'
repo = 'ActiveData-ETL'
url = 'https://api.github.com/repos/{}/{}/commits'.format(owner, repo)
req = requests.get(url)
json_data = req.json()

first_commit_hash =[]
print(req.headers.get('Link'))
if req.headers.get('Link'):
        page_url = req.headers.get('Link').split(',')[1].split(';')[0].split('<')[1].split('>')[0]
        print(page_url)
        req_last_commit = requests.get(page_url+'&per_page=100')
        url_split = page_url.split('=')[0]
        old_pgnum = int(page_url.split('=')[1])
        print(old_pgnum)
        if(old_pgnum>4):
                pgnum = 4
        else:
                pgnum = old_pgnum
        for i in range(0,pgnum):
                older_pgnum = old_pgnum-i
                paged_url = url_split+''+str(older_pgnum)+'&per_page=100'
                req_last_commit = requests.get(paged_url)
                first_commit = req_last_commit.json()
                idx=0
                for i in first_commit:
                    idx = idx-1
                    first_commit_hash.append(i['sha'])#first_commit[idx]['sha']
else:
        idx=0
        for i in json_data:#range(0,10):
            idx = idx-1
            first_commit_hash.append(i['sha'])#json_data[idx]['sha'])

print(len(first_commit_hash))
print(first_commit_hash)

