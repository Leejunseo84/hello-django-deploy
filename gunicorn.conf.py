import multiprocessing

# worker(process) 논리코어 수 * 2 + 1
cpu_count = multiprocessing.cpu_count()
workers = (cpu_count * 2) + 1
print(f'{workers = }')

bind = '0.0.0.0:8000'
worker_class = 'uvicorn.workers.UvicornWorker'   # 하나의 
timeout = 30
threads = 4             # cpu_bound = 1 ~ 2, io_bound = 3 ~ 4

