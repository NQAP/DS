import Median
import argparse

def Min_Test(numbers, output_file, out):
	heap = Median.MinHeap()
	for number in numbers:
		heap.insert(number)
		if out:
			output_file.write(" ".join(map(str, heap.showMinHeap())) + "\n")
	heap.removeMin()
	output_file.write(" ".join(map(str, heap.showMinHeap())) + "\n")

def Max_Test(numbers, output_file, out):
	heap = Median.MaxHeap()
	for number in numbers:
		heap.insert(number)
		if out:
			output_file.write(" ".join(map(str, heap.showMaxHeap())) + "\n")
	heap.removeMax()
	output_file.write(" ".join(map(str, heap.showMaxHeap())) + "\n")

def Median_Test(numbers, output_file):
	median = Median.FindMedian()
	median.AddNewValues(numbers)
	output_file.write(f"{median.ShowMedian()}\n")
	for i in range(len(numbers)-1):
		median.RemoveMedian()
		output_file.write(f"{median.ShowMedian()}\n")

def compare_files(file1, file2):
	with open(file1, 'r') as f1, open(file2, 'r') as f2:
		lines1 = f1.readlines()
		lines2 = f2.readlines()

	if len(lines1) != len(lines2):
		return False

	for line1, line2 in zip(lines1, lines2):
		if line1.strip() != line2.strip():
			return False

	return True

if __name__== '__main__':
	parser = argparse.ArgumentParser()
	parser.add_argument('-i', '--input', type=str, default="input_0.txt", help='Input file name')
	parser.add_argument('-o0', '--output0', type=str, default="output_min_0.txt", help='Output file name for MinHeap')
	parser.add_argument('-o1', '--output1', type=str, default="output_max_0.txt", help='Output file name for MaxHeap')
	parser.add_argument('-o2', '--output2', type=str, default="output_median_0.txt", help='Output file name for Median')
	parser.add_argument('-g0', '--golden0', type=str, default="golden_min_0.txt", help='Golden file name for MinHeap')
	parser.add_argument('-g1', '--golden1', type=str, default="golden_max_0.txt", help='Golden file name for MaxHeap')
	parser.add_argument('-g2', '--golden2', type=str, default="golden_median_0.txt", help='Golden file name for Median')
	parser.add_argument('-m', '--mode', type=int, default=-1, help='Mode: 0 for MinHeap, 1 for MaxHeap, 2 for Median')
	parser.add_argument('-p', '--print', type=int, default=1, help='Print intermediate results')
	args = parser.parse_args()
	with open(args.input, "r") as input_file:
		lines = input_file.readlines()
	if args.mode == 0:
		with open(args.output0, "w") as output_file:
			for index, line in enumerate(lines):
				output_file.write("MinHeap" + str(index) + "\n")
				numbers = list(map(int, line.split()))
				Min_Test(numbers, output_file, args.print)
		if args.print:
			if compare_files(args.output0, args.golden0):
				print("MinHeap test passed.")
			else:
				print("MinHeap test failed.")
	elif args.mode == 1:
		with open(args.output1, "w") as output_file:
			for index, line in enumerate(lines):
				output_file.write("MaxHeap" + str(index) + "\n")
				numbers = list(map(int, line.split()))
				Max_Test(numbers, output_file, args.print)
		if args.print:
			if compare_files(args.output1, args.golden1):
				print("MaxHeap test passed.")
			else:
				print("MaxHeap test failed.")
	elif args.mode == 2:
		with open(args.output2, "w") as output_file:
			for index, line in enumerate(lines):
				output_file.write("Median" + str(index) + "\n")
				numbers = list(map(int, line.split()))
				Median_Test(numbers, output_file)
		if compare_files(args.output2, args.golden2):
			print("Median test passed.")
		else:
			print("Median test failed.")
	else:
		with open(args.output0, "w") as output_file0, open(args.output1, "w") as output_file1, open(args.output2, "w") as output_file2:
			for index, line in enumerate(lines):
				output_file0.write("MinHeap" + str(index) + "\n")
				output_file1.write("MaxHeap" + str(index) + "\n")
				output_file2.write("Median" + str(index) + "\n")
				numbers = list(map(int, line.split()))
				Min_Test(numbers, output_file0, args.print)
				Max_Test(numbers, output_file1, args.print)
				Median_Test(numbers, output_file2)
		if args.print:
			if compare_files(args.output0, args.golden0):
				print("MinHeap test passed.")
			else:
				print("MinHeap test failed.")
			if compare_files(args.output1, args.golden1):
				print("MaxHeap test passed.")
			else:
				print("MaxHeap test failed.")
		if compare_files(args.output2, args.golden2):
			print("Median test passed.")
		else:
			print("Median test failed.")