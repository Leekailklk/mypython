import urllib.request

def getHtml(url):
    html = urllib.request.urlopen(url).read()
    return html

def saveHtml(file_name, file_content):
    # 注意windows文件命名的禁用符，比如 /
    with open(file_name.replace('/', '_') + ".html", "wb") as f:
        # 写文件用bytes而不是str，所以要转码
        f.write(file_content)

aurl = "https://mp.weixin.qq.com/s?src=3&timestamp=1577340677&ver=1&signature=tm5l1HXZEJrpWG2hhoClPe2Tt1DPbWG*FDjhgAhMytcWf1Ua17Et3nQxS95UYnSH*RnTfHBdBy9YksUkKSb9uecEQSWUlH0SiSJLsE9SsAuDKMviHqJYWg6goouC97RKWpWtFhkVm1iB5ia7IaRTAVpuS-y4aZ-ymDclEESRzC4="
html = getHtml(aurl)
saveHtml("表面粗糙度", html)

print("下载成功")