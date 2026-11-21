def hanoi_solver(n):
    # Initialize three rods with integers representing disk sizes
    # Rod A starts with disks n down to 1
    rods = {
        'A': list(range(n, 0, -1)),
        'B': [],
        'C': []
    }
    
    moves = []

    def record_state():
        # Record the current state of rods in A B C order
        state_str = f"{rods['A']} {rods['B']} {rods['C']}"
        moves.append(state_str)

    def move_disks(disks_to_move, source, target, auxiliary):
        if disks_to_move == 1:
            # Move the top disk
            rods[target].append(rods[source].pop())
            record_state()
            return

        # Move top n-1 disks from source to auxiliary rod
        move_disks(disks_to_move - 1, source, auxiliary, target)
        
        # Move remaining largest disk from source to target rod
        rods[target].append(rods[source].pop())
        record_state()
        
        # Move the n-1 disks from auxiliary rod to target rod
        move_disks(disks_to_move - 1, auxiliary, target, source)

    # Record starting configuration
    record_state()
    
    # Solve puzzle moving all disks from A to C using B as auxiliary
    move_disks(n, 'A', 'C', 'B')

    return "\n".join(moves)

print(hanoi_solver(3))
