import json
import time
import argparse
import heapq

# --- TODO START --- #
# You can define any class or function
# You can import any python standard library : https://docs.python.org/3/library/
# However, you are not allowed to import any libraries other than python standard library, (such as numpy)

# --- TODO END --- #


def solution(arr,k):
    # --- TODO START --- #
    json_sum = [0] * k
    minheap = []
    length = 0
    origin_length = len(arr)
    partial_sum = []
    minimal = -1000000
    for i in range(origin_length):
        for j in range(origin_length):
            if i == 0:
                partial_sum.append((arr[j], j, i))
            else:
                value, idx, order = partial_sum[j]
                index = (j+i) % origin_length
                value += arr[index]
                order = i
                partial_sum[j] = (value, idx, order)
            if length < k:
                heapq.heappush(minheap, partial_sum[j])
                length += 1
                minimal = minheap[0][0]
            else:
                if partial_sum[j][0] >= minimal:
                    heapq.heappop(minheap)
                    heapq.heappush(minheap, partial_sum[j])
                    minimal = minheap[0][0]
    for i in range(length):
        json_sum[length - i - 1] = heapq.heappop(minheap)[0]
    print(json_sum)
    # --- TODO END --- #
    return json_sum

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', default='input_1.json')
    parser.add_argument('--output', default='output_1.json')
    args = parser.parse_args()
    json_input = json.load(open(args.input, "r"))
    t1 = time.time()
    json_output = solution(json_input["array"],json_input["topk"])
    t2 = time.time()
    json.dump(json_output, open(args.output, "w"))
    print("runtime of %s : %s" % (args.input, t2 - t1))

