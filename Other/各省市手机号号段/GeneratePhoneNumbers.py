import sys
from multiprocessing import Pool, cpu_count, Manager
import os
import time

# 生成号码段的所有号码
def generate_full_numbers(segment, numbers_list):
    numbers = [segment + str(i).zfill(4) for i in range(10000)]
    numbers_list.extend(numbers)
    return segment  # 返回号码段以用于打印进度

# 打印进度的回调函数
def print_progress(segment):
    progress = progress_counter.value
    progress_counter.value += 1
    total_segments = len(segments)
    print(f"Processed segment {progress}/{total_segments} ({segment})")
    sys.stdout.flush()

# 主函数
def main(input_file, output_file, num_processes=None):
    start_time = time.time()  # 记录开始时间

    if num_processes is None:
        num_processes = cpu_count()  # 默认使用所有可用的CPU核心

    with Manager() as manager:
        numbers_list = manager.list()  # 在进程间共享的列表
        global progress_counter
        progress_counter = manager.Value('i', 1)  # 用于追踪进度

        with open(input_file, 'r') as file:
            global segments  # 在回调函数中使用
            segments = [line.strip() for line in file.readlines()]

        with Pool(processes=num_processes) as pool:
            for segment in segments:
                pool.apply_async(generate_full_numbers, (segment, numbers_list), callback=print_progress)
                
            pool.close()
            pool.join()

        # 将生成的号码写入文件
        with open(output_file, 'w') as file:
            for number in numbers_list:
                file.write(number + '\n')

    end_time = time.time()  # 记录结束时间
    print(f"Completed generating phone numbers in {end_time - start_time:.2f} seconds.")

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python script.py input_file output_file num_processes")
        sys.exit(1)

    input_file, output_file, num_processes = sys.argv[1], sys.argv[2], int(sys.argv[3])
    main(input_file, output_file, num_processes)
