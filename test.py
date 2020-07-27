import pnom
import time

start_time = time.time()

n = int(input("please inter n: "))

pnom.PerfectNumber(n)

print("---%s second ---" % (time.time() - start_time))
