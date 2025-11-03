def stock_span(prices):
    n = len(prices)
    spans = [0]*n
    stack = []
    for i, price in enumerate(prices):
        while stack and prices[stack[-1]] <= price:
            stack.pop()
        spans[i] = i - stack[-1] if stack else i + 1
        stack.append(i)
    return spans


def next_greater_to_right(arr, sentinel=-1):
    n = len(arr)
    out = [sentinel]*n
    stack = []
    for i, val in enumerate(arr):
        while stack and arr[stack[-1]] < val:
            idx = stack.pop()
            out[idx] = val
        stack.append(i)
    return out


def next_smaller_to_right(arr, sentinel=-1):
    n = len(arr)
    out = [sentinel]*n
    stack = []
    for i, val in enumerate(arr):
        while stack and arr[stack[-1]] > val:
            idx = stack.pop()
            out[idx] = val
        stack.append(i)
    return out


def daily_temperatures(temps):
    n = len(temps)
    res = [0]*n
    stack = []
    for i, t in enumerate(temps):
        while stack and temps[stack[-1]] < t:
            prev = stack.pop()
            res[prev] = i - prev
        stack.append(i)
    return res


if __name__ == "__main__":
    # Helper to read a list by count (no defaults; user must enter valid values)
    def read_list_by_count(name):
        while True:
            cnt = input(f"Enter number of elements for {name}: ").strip()
            try:
                n = int(cnt)
                if n <= 0:
                    print("Count must be a positive integer. Try again.")
                    continue
                break
            except ValueError:
                print("Invalid count. Please enter a positive integer.")

        while True:
            s = input(f"Enter {n} integers for {name} (space separated): ").strip()
            parts = s.split()
            if len(parts) != n:
                print(f"Expected {n} integers, got {len(parts)}. Please try again.")
                continue
            try:
                vals = [int(x) for x in parts]
                return vals
            except ValueError:
                print("All entries must be integers. Please try again.")


    # Read inputs for all four functions (no defaults)
    prices = read_list_by_count("stock prices")
    arr_for_ngtr = read_list_by_count("array for Next Greater to Right")
    arr_for_nstr = read_list_by_count("array for Next Smaller to Right")
    temps = read_list_by_count("temperatures for Daily Temperatures")


    # Compute and print results
    print("\nOutputs:")
    print("Stock spans:", stock_span(prices))
    print("Next greater to right:", next_greater_to_right(arr_for_ngtr))
    print("Next smaller to right:", next_smaller_to_right(arr_for_nstr))
    print("Daily temperatures (days to wait):", daily_temperatures(temps))

