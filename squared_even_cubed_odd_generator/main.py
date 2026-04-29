from multiplier import EvenOddMultiplier

try:
    EvenOddMultiplier().integers_identifier()
except FileNotFoundError:
    print("\nThere are no files found.\n")