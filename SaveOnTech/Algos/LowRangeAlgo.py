def LowFive(P):
    P.sort(key=lambda x: x.discount,reverse=True)
    return P[0:5]