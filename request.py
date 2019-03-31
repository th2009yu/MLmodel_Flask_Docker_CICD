import requests

url = 'http://0.0.0.0:5000/api'
feature = [[5.8, 4.0, 1.2, 0.2]]
labels = {
    0: "setosa",
    1: "versicolor",
    2: "virginica"
}

r = requests.post(url, json={'feature': feature})
print(labels[r.json()])
