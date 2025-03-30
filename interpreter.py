def run_code(code, inp=''):
    cells = [0 for i in range(256)]
    code = ' '.join(code.replace('\n', '').replace('  ', ' ').replace('  ', ' ').split())
    cell = 0
    output = ""
    all_cycles = []
    i = 0
    is_in_not_valid_cycle = False
    while i < len(code):
        command = code[i:i+10] # get command
        if is_in_not_valid_cycle and command != "endendende":
            pass
        elif command == "dotdotdotd":
            output += chr(cells[cell])
        elif command == "pluspluspl":
            cells[cell] = (cells[cell] + 1) % 256
        elif command == "minusminus":
            cells[cell] = (cells[cell] - 1) % 256
        elif command == "commacomma":
            cells[cell] = ord(inp[0])
            inp = inp[1:]
        elif command == "leftleftle":
            cell = (cell + 1) % 256
        elif command == "rightright":
            cell = (cell - 1) % 256
        elif "nummultby" in command:
            cell = (cell * int(command[9])) % 256
        if command == "startstart":
            if cells[cell] == 0 and not is_in_not_valid_cycle:
                is_in_not_valid_cycle = True
                all_cycles.append(-1)
            else:
                all_cycles.append(i)

        if command == "endendende":
            if is_in_not_valid_cycle:
                if all_cycles[-1] == -1:
                    is_in_not_valid_cycle = False
                all_cycles = all_cycles[:-1]
            else:
                i = all_cycles[-1] - 10
                all_cycles = all_cycles[:-1]
        # print(all_cycles, cells[:3], cell, is_in_not_valid_cycle, command[3] + command[8])
        i += 10


    return output
