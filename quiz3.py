# ex) http://naver.com

url = "http://naver.com"
url = url[url.index("//")+2:]  # rule1
url = url[:url.index(".")]  # rule2
url = url[:3]+str(len(url))+str(url.count("e"))+"!"  # rule3
print("password : "+url)
