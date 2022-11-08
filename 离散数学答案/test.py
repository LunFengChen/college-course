# import requests
# from lxml import etree
# from urllib.parse import urljoin
#
#
# f = open("离散数学答案.html", mode='r',encoding="utf8")
#
# tree = etree.HTML(f.read())
#
# div_lst = tree.xpath("//div[@class='webpreview-item']")
#
# dic = {
#
# }
#
#
# for div in div_lst:
#     data_id = div.xpath("./@data-id")
#     src = div.xpath("./img/@src")
#     if not src:
#         src = div.xpath("./img/@data-src")
#
#     if src and data_id:
#         data_id = data_id[0]
#         src = urljoin("https://max.book118.com/html/2019/0610/6140212205002035.shtm", src[0])
#         dic[data_id] = src
#
# from my_fake_useragent import  UserAgent
# headers = {
#     "user-agent": UserAgent().random()
# }
#
# for id, src in dic.items():
#     resp = requests.get(url=src, headers=headers)
#     with open(f"./src/{id}.png", mode="wb") as f:
#         f.write(resp.content)


# s = r"![1](F:\1_爬虫\src\1.png)"
#
# for i in range(1, 71+1):
#     print(fr"![{i}](F:\1_爬虫\src\{i}.png)")
