    import  requests
    
    lst = []
    url = "http://movie.douban.com/top250"
    res = requests.get(url)
    #requests.get(url) ...refer to client2.py
    print('log response object\n',res)
    
    #原始二进制数据
    #content = res.content
    #文本数据信息，requests自动帮我们以指定编码解析出来的内容
    #text = res.text
    #响应json数据信息，通常我们使用json模块来处理
    #json_data = res.json()
    # 响应状态码
    #status_code = res.status_code
    #响应头
    #headers = res.headers
    #响应cookies
    #cookies = res.cookies
  
    
