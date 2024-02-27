def towers_of_hanoi(n, source, target, auxiliary):
    if n > 0:
        # Move n-1 disks from source to auxiliary peg
        towers_of_hanoi(n - 1, source, auxiliary, target)

        # Move the nth disk from source to target peg
        print(f"Move disk {n} from {source} to {target}")

        # Move the n-1 disks from auxiliary peg to target peg
        towers_of_hanoi(n - 1, auxiliary, target, source)

# Example usage:
num_disks = 3
source_peg = "A"
target_peg = "C"
auxiliary_peg = "B"

print(f"Solving Towers of Hanoi for {num_disks} disks:")
towers_of_hanoi(num_disks, source_peg, target_peg, auxiliary_peg)
