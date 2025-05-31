import threading

# Define a function to run in a thread
def coder(number,yigit):
    print(f'Coder ID: {number} , {yigit}')

# Create and start 5 threads
threads = []
for k in range(5):
    for b in range(5):
        t = threading.Thread(target=coder, args=(b,k))
        threads.append(t)
        t.start
        t.start()