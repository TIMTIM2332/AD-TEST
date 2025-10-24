import threading, time

def worker(name):
    for i in range(1,6):
        print(f'Thread {name}:', i)
        time.sleep(1)

threads = []
for n in ('A','B','C'):
    t = threading.Thread(target=worker, args=(n,), name=f'Thread-{n}')
    threads.append(t)
    t.start()

for t in threads:
    t.join()

print('All threads complete.')
