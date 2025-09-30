import requests, time

urls = {
    "Local": "http://localhost:8080",
    "GitHub": "https://username.github.io/reponame/"
}

for name, url in urls.items():
    times = []
    for i in range(5):  # 5 requests for average
        start = time.time()
        r = requests.get(url)
        end = time.time()
        times.append(end - start)
    print(f"{name} Average Load Time: {sum(times)/len(times):.3f} seconds")
