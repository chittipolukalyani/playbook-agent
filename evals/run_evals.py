import json
import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'backend'))

with open(os.path.join(os.path.dirname(__file__), '..', 'playbooks', 'playbooks.json'), encoding='utf-8') as f:
    playbooks = json.load(f)

with open(os.path.join(os.path.dirname(__file__), 'test_cases.json'), encoding='utf-8') as f:
    test_cases = json.load(f)

def match_playbook(problem: str):
    problem_lower = problem.lower()
    for playbook in playbooks:
        for keyword in playbook["keywords"]:
            if keyword in problem_lower:
                return playbook["id"]
    return playbooks[0]["id"]

total = len(test_cases)
passed = 0
failed = []

for test in test_cases:
    result = match_playbook(test["problem"])
    if result == test["expected_playbook"]:
        passed += 1
    else:
        failed.append({
            "problem": test["problem"],
            "expected": test["expected_playbook"],
            "got": result
        })

accuracy = (passed / total) * 100

print("=" * 50)
print("AI PLAYBOOK AGENT - EVAL RESULTS")
print("=" * 50)
print(f"Total Test Cases : {total}")
print(f"Passed           : {passed}")
print(f"Failed           : {total - passed}")
print(f"Accuracy         : {accuracy:.1f}%")
print("=" * 50)

if failed:
    print("\nFailed Cases:")
    for f in failed:
        print(f"  Problem  : {f['problem']}")
        print(f"  Expected : {f['expected']}")
        print(f"  Got      : {f['got']}")
        print()