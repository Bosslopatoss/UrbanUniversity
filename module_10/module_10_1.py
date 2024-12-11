import time
import threading

start1 = time.time()

def write_words(word_count, file_name):
    for i in range(1, word_count+1):  
        with open(file_name, 'a') as file:
            file.write(f"Some word N {i}\n")
    time.sleep(0.1)
    print(f"Finished writing to file {file_name}")
        
write_words(10, 'example1.txt')
write_words(30, 'example2.txt')
write_words(200, 'example3.txt')
write_words(100, 'example4.txt')

end1 = time.time()
print(f'work of thread: {end1 - start1}')
start2 = time.time()

threads = []
args = [(10, 'example5.txt'),
        (30, 'example6.txt'),
        (200, 'example7.txt'),
        (100, 'example8.txt')]

for i in range(4):
    t = threading.Thread(target=write_words, args=(args[i]))
    threads.append(t)    
for t in threads:
    t.start()
for t in threads:
    t.join()   

end2 = time.time()
print(f'work of threads: {end2 - start2}')
