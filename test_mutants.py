import importlib
import sys

# List of mutant files (relative to the mutants directory)
mutants = [
    'mutant_1',
    'mutant_2',
    'mutant_3',
    'mutant_4',
    'mutant_5',
    'mutant_6',
    'mutant_7',
    'mutant_8',
    'mutant_9',
    'mutant_10',
    'mutant_11',
    'mutant_12',
    'mutant_13',
    'mutant_14',
    'mutant_15',
    'mutant_16',
    'mutant_17',
    'mutant_18',
    'mutant_19',
    'mutant_20'
]

def run_tests(mutant_name):
    """Replace the bubble_sort function with the mutant and run the tests."""
    try:
        # Dynamically import the mutant module
        mutant_path = f"mutants.{mutant_name}"
        mutant_module = importlib.import_module(mutant_path)
        
        # Import test functions
        from test_mrs import test_reverse_relation, test_constant_addition_relation

        # Run the tests
        print(f"Running tests for {mutant_name}...")
        test_reverse_relation(mutant_module.bubble_sort)
        test_constant_addition_relation(mutant_module.bubble_sort)
        print(f"{mutant_name} passed all tests.")
    except AssertionError as e:
        print(f"{mutant_name} failed: {e}")
    except Exception as e:
        print(f"An error occurred with {mutant_name}: {e}")

if __name__ == "__main__":
    # Add the mutants directory to the system path
    sys.path.append('./mutants')
    
    for mutant in mutants:
        run_tests(mutant)
