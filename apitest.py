from twitter import Twitter, OAuth

t = Twitter(auth=OAuth("769167810152890368-G9cEqx12feezEO75ehDt6uCNk51qqTf", "S3kDSDrJn3qGCuuB2PN16WRuJlmtq9mSrvNxJnt5gE6xO", "B3rNMcICBig8FjCNtOwY0dw4I", "ZDFmdAmzWIe12kQ7wvwCPWZFLEdKNd22rslhKl1oPfgjhChhvH"))
pythonTweets = t.search.tweets(q = "#python")
print(pythonTweets)