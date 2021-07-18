from snownlp import SnowNLP 
import scipy
import math

def calcDanmuSentiments(danmu_list, duration):
    ans = [0]*duration
    cans = [0]*duration
    for danmu in danmu_list:
        ans[max(0,min(duration-1,int(math.ceil(float(danmu["time"])))))]+=math.pow(2*SnowNLP(danmu["text"]).sentiments-1,2)
        cans[max(0,min(duration-1,int(math.ceil(float(danmu["time"])))))]+=1
    ans=[max(ans[i]/(cans[i]+0.01),0) for i in range(duration)]
    return ans