RED='\033[1;31m'
GREEN='\033[1;32m'
NC='\033[0m' # No Color
echo "==evaluating correctness=="
for i in $(seq 1 5); do
    python3 stack_queue.py --input input_${i}.txt --output1 output_stack_${i}.txt --output2 output_queue_${i}.txt --output3 output_queue_by_stack_${i}.txt
    dline_stack=$(diff output_stack_${i}.txt golden_stack_${i}.txt | wc | awk -F ' ' '{print $1}')
    if [ "${dline_stack}" == "0" ] && [ -f output_stack_${i}.txt ]; then
        echo -e "${GREEN}The stack of stack_queue.py is correct in test case: input_${i}.txt${NC}"
    else
        echo -e "${RED}The stack of stack_queue.py is incorrect in test case: input_${i}.txt${NC}"
    fi
    dline_queue=$(diff output_queue_${i}.txt golden_queue_${i}.txt | wc | awk -F ' ' '{print $1}')
    if [ "${dline_queue}" == "0" ] && [ -f output_queue_${i}.txt ]; then
        echo -e "${GREEN}The queue of stack_queue.py is correct in test case: input_${i}.txt${NC}"
    else
        echo -e "${RED}The queue of stack_queue.py is incorrect in test case: input_${i}.txt${NC}"
    fi
    dline_queue_by_stack=$(diff output_queue_by_stack_${i}.txt golden_queue_by_stack_${i}.txt | wc | awk -F ' ' '{print $1}')
    if [ "${dline_queue_by_stack}" == "0" ] && [ -f output_queue_by_stack_${i}.txt ] ; then
        echo -e "${GREEN}The queue_by_stack of stack_queue.py is correct in test case: input_${i}.txt${NC}"
    else
        echo -e "${RED}The queue_by_stack of stack_queue.py is incorrect in test case: input_${i}.txt${NC}"
    fi
done
echo "==evaluating runtime=="
for i in $(seq 1 6); do
    python3 stack_queue.py --input input_${i}.txt
done
