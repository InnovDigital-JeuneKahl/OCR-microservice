from typing import List, Dict, Optional
import json

def save_results_to_json(results: Dict, output_path: str):
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(results, f, ensure_ascii=False, indent=2)

def print_contexts(contexts: Dict[str, List[Dict[str, Optional[str]]]]):
    for term, occurrences in contexts.items():
        print(f"\n{'='*80}")
        print(f"Term: '{term}' - Found {len(occurrences)} occurrence(s)")
        print(f"{'='*80}")
        
        for i, ctx in enumerate(occurrences, 1):
            print(f"\nContext {i}:")
            if ctx['prev']:
                print(f"[Previous] {ctx['prev']}")
            print(f"[Match]    {ctx['match']}")
            if ctx['next']:
                print(f"[Next]     {ctx['next']}")
            print("-" * 40)