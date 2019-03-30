import requests

url = 'http://0.0.0.0:5000/api'
feature = [[6.7, 3.3, 5.7, 2.1]]
labels = {
    0: "setosa",
    1: "versicolor",
    2: "virginica"
}

r = requests.post(url, json={'feature': feature})
print(labels[r.json()])
