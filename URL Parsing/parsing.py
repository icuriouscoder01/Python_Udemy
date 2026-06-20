url = "https://www.kaggle.com/datasets"
protocol = url[0:url.find(":")]
print(f"Protocol: {protocol}")
dot1 = url.find(".")
dot2 = url.find(".", dot1 + 1)
domain = url[dot1 + 1:dot2]
print(f"Domain: {domain}")
page = url[url.find("/", dot2): ]
print(f"Page: {page}")