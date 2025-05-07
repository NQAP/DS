RED='\033[1;31m'
GREEN='\033[1;32m'
NC='\033[0m' # No Color
echo "==evaluating correctness=="
for i in $(seq 1 3); do
    python3 BSTree.py --input input_${i}.txt --output output_${i}.txt
    dline_py=$(diff output_${i}.txt ./linux_golden/golden_${i}.txt |  wc | awk -F ' ' '{print $1}')
    if [ "${dline_py}" == "0" ] && [ -f output_${i}.txt ] && [ -f ./linux_golden/golden_${i}.txt ] ; then
        echo -e "${GREEN}BSTree.py is correct in test case: input_${i}.txt${NC}"
    else
        echo -e "${RED}BSTree.py is incorrect in test case: input_${i}.txt${NC}"
    fi
done
echo "==evaluating runtime=="
for i in $(seq 1 5); do
    python3 BSTree.py --input input_${i}.txt
    echo "Running test case input_${i}.txt"
    { time timeout 40s python3 BSTree.py --input input_${i}.txt; } 2>&1 | grep real

    if [ $? -eq 124 ]; then
        echo -e "${RED}Test case input_${i}.txt exceeded 30 seconds and was terminated.${NC}"  # 25s for test4 40s for test5 #
    fi
done
