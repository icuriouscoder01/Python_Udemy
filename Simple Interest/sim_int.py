def sim_int(*,p,r,t):
    return (p*r*t)/100

si = int(sim_int(p=10000, r=10, t=1))

print(f"Simple Interest: {si}")