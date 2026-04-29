from multiplier import even_odd_multiplier

try:
    even_odd_multiplier().integers_identifier()
except FileNotFoundError:
    print("\nThere are no files found.\n")