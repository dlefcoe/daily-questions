from tqdm import tqdm
import time

for i in tqdm(range(10), desc="running the loops:"):
    time.sleep(0.5)

# def update_progress(progress):
#     print '\r[{0}] {1}%'.format('#'*(progress/10), progress)