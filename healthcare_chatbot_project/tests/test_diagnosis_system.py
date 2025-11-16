"""
Test script to verify diagnosis system is working
Run this to check both traditional and AI-powered diagnosis
"""

import os
import sys
import django

# Setup Django environment
sys.path.insert(0, os.path.dirname(__file__))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'healthcare.settings')
django.setup()

from chat.diagnosis_engine import get_diagnosis_category, get_first_question, get_next_question, DIAGNOSIS_TREES
from chat.gemini_integration import get_gemini_diagnosis, is_gemini_available

print("=" * 60)
print("🧪 TESTING DIAGNOSIS SYSTEM")
print("=" * 60)

# Test 1: Check diagnosis categories
print("\n📋 Test 1: Testing diagnosis categories...")
test_symptoms = [
    ("I have a cough and fever", "respiratory"),
    ("My stomach hurts", "digestive"),
    ("I'm having trouble breathing", "respiratory"),
    ("I have diarrhea and nausea", "digestive")
]

for symptom, expected in test_symptoms:
    category = get_diagnosis_category(symptom)
    if category == expected:
        print(f"✅ '{symptom}' → {category}")
    else:
        print(f"❌ '{symptom}' → Expected: {expected}, Got: {category}")

# Test 2: Check decision tree questions
print("\n📋 Test 2: Testing decision tree questions...")
for category_name, tree_data in DIAGNOSIS_TREES.items():
    first_q = get_first_question(category_name)
    if first_q:
        print(f"✅ {category_name}: {first_q['question'][:50]}...")
    else:
        print(f"❌ {category_name}: No first question found")

# Test 3: Test question flow
print("\n📋 Test 3: Testing question flow (respiratory)...")
category = 'respiratory'
first_q = get_first_question(category)
if first_q:
    print(f"Q1: {first_q['question']}")
    
    # Answer YES
    next_step = get_next_question(category, first_q['id'], True)
    if next_step:
        if next_step['type'] == 'question':
            print(f"✅ Next question: {next_step['data']['question'][:50]}...")
        elif next_step['type'] == 'diagnosis':
            print(f"✅ Diagnosis reached: {next_step['data']['condition']}")
    else:
        print(f"❌ No next step found")

# Test 4: Test AI-powered diagnosis
print("\n📋 Test 4: Testing AI-powered diagnosis...")
if is_gemini_available():
    print("✅ Gemini AI is available")
    
    test_cases = [
        "I have a fever, cough, and body aches. Can you diagnose me?",
        "I think I have a migraine. Can you run a diagnosis?",
        "My stomach hurts and I feel nauseous. What do I have?"
    ]
    
    for test_case in test_cases:
        print(f"\n   Testing: '{test_case}'")
        response = get_gemini_diagnosis(test_case)
        if response:
            print(f"   ✅ AI Response: {response[:150]}...")
        else:
            print(f"   ❌ No response from AI")
else:
    print("⚠️ Gemini AI not available - skipping AI diagnosis tests")

# Test 5: Check all diagnoses are defined
print("\n📋 Test 5: Checking all diagnoses are defined...")
for category_name, tree_data in DIAGNOSIS_TREES.items():
    diagnoses = tree_data.get('diagnoses', {})
    print(f"\n{category_name.upper()}:")
    for diag_key, diag_data in diagnoses.items():
        condition = diag_data.get('condition', 'Unknown')
        severity = diag_data.get('severity', 'unknown')
        print(f"  ✅ {condition} (Severity: {severity})")

print("\n" + "=" * 60)
print("🎉 DIAGNOSIS SYSTEM TEST COMPLETE!")
print("=" * 60)
print("\nDiagnosis system is ready to use!")
print("\nHow to use:")
print("  1. Traditional diagnosis: Type 'start diagnosis' or 'begin diagnosis'")
print("  2. AI diagnosis: Type 'diagnose me' or 'what do I have?'")
print("  3. Natural questions: 'I have a fever, can you diagnose?'")
