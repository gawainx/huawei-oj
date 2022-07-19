import sys

if __name__ == '__main__':
    table = [[-2, -2] for _ in range(10001)]
    data = sys.stdin.readline().split()
    list_data = data[2:-1]
    head_val = int(data[1])
    # [prev, next]
    table[head_val] = [-1, -1]
    # 初始化链表
    for i in range(0, len(list_data), 2):
        cur_val, prev_val = int(list_data[i]), int(list_data[i + 1])
        if table[prev_val][1] == -1:
            # prev node is tail node
            # table[prev_val][1] = cur_val
            table[cur_val][1] = -1
        else:
            # prev node is not a tail node
            nxt_node = table[prev_val][1]
            table[cur_val][1] = nxt_node
            table[nxt_node][0] = cur_val
        table[prev_val][1] = cur_val
        table[cur_val][0] = prev_val
        # table[cur_val][1] = -1

    to_be_deleted = int(data[-1])
    node_prev = table[to_be_deleted][0]
    node_next = table[to_be_deleted][1]
    if node_prev == -1:
        # is head node
        if node_next != -1:
            head_val = node_next
            table[node_next][0] = -1
        else:
            print()
    else:
        # not head node
        table[node_prev][1] = node_next
        if node_next != -1:
            table[node_next][0] = node_prev

    node = head_val
    while node > 0:
        sys.stdout.write(f"{node} ")
        node = table[node][1]


