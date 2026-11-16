#!/bin/bash

# DID Skill - Final Assembly & Verification Script
# This script verifies all components and prepares for packaging

set -e

echo "=================================="
echo "🚀 DID SKILL - FINAL ASSEMBLY"
echo "=================================="
echo ""

# Color codes
GREEN='\033[0;32m'
RED='\033[0;31m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Counters
PASSED=0
FAILED=0

# Function to check file
check_file() {
    local file=$1
    local min_size=${2:-100}
    
    if [ -f "$file" ]; then
        local size=$(wc -c < "$file")
        if [ $size -ge $min_size ]; then
            echo -e "${GREEN}✓${NC} $file ($size bytes)"
            ((PASSED++))
            return 0
        else
            echo -e "${RED}✗${NC} $file (too small: $size bytes)"
            ((FAILED++))
            return 1
        fi
    else
        echo -e "${RED}✗${NC} $file (MISSING)"
        ((FAILED++))
        return 1
    fi
}

# Function to check directory
check_directory() {
    local dir=$1
    local expected=$2
    
    if [ -d "$dir" ]; then
        local count=$(find "$dir" -type f | wc -l)
        if [ $count -ge $expected ]; then
            echo -e "${GREEN}✓${NC} $dir ($count files)"
            return 0
        else
            echo -e "${YELLOW}⚠${NC} $dir ($count/$expected files)"
            return 1
        fi
    else
        echo -e "${RED}✗${NC} $dir (MISSING)"
        return 1
    fi
}

echo "📋 CHECKING CRITICAL FILES"
echo ""

# Root level critical files
check_file "SKILL.md" 2000
check_file "README.md" 5000
check_file "LICENSE" 10000
check_file "requirements.txt" 100
check_file ".gitattributes" 500

echo ""
echo "📂 CHECKING DIRECTORIES"
echo ""

# Check references folder (target: 14 files)
check_directory "references" 7

# Check utils (target: 3 files)
check_directory "utils" 2

# Check examples (target: 1 file)
check_directory "examples" 1

# Check docs (target: 4 files)
check_directory "docs" 3

echo ""
echo "📊 WORD COUNT ANALYSIS"
echo ""

echo "Total documentation words:"
wc -w SKILL.md README.md LICENSE references/*.md 2>/dev/null | tail -1

echo ""
echo "SKILL.md word count:"
wc -w SKILL.md | awk '{print $1}'

echo ""
echo "⚙️  PYTHON SYNTAX CHECK"
echo ""

python3 -m py_compile utils/docx_generator.py 2>/dev/null && \
    echo -e "${GREEN}✓${NC} docx_generator.py (valid)" || \
    echo -e "${RED}✗${NC} docx_generator.py (syntax error)"

python3 -m py_compile utils/design_formatter.py 2>/dev/null && \
    echo -e "${GREEN}✓${NC} design_formatter.py (valid)" || \
    echo -e "${RED}✗${NC} design_formatter.py (syntax error)"

python3 -m py_compile examples/generate_sample_did.py 2>/dev/null && \
    echo -e "${GREEN}✓${NC} generate_sample_did.py (valid)" || \
    echo -e "${RED}✗${NC} generate_sample_did.py (syntax error)"

echo ""
echo "🔐 LICENSE VERIFICATION"
echo ""

if grep -q "PT. Agra Karya Digital" LICENSE; then
    echo -e "${GREEN}✓${NC} Company name in LICENSE"
else
    echo -e "${RED}✗${NC} Company name NOT in LICENSE"
fi

if grep -q "www.vcadeveloper.com" LICENSE; then
    echo -e "${GREEN}✓${NC} Website in LICENSE"
else
    echo -e "${RED}✗${NC} Website NOT in LICENSE"
fi

if grep -q "plagiar" LICENSE; then
    echo -e "${GREEN}✓${NC} Anti-plagiarism clauses"
else
    echo -e "${RED}✗${NC} No anti-plagiarism clauses"
fi

echo ""
echo "📝 README VERIFICATION"
echo ""

if grep -q "English" README.md && grep -q "Indonesian\|Bahasa" README.md; then
    echo -e "${GREEN}✓${NC} Bilingual content"
else
    echo -e "${RED}✗${NC} Not bilingual"
fi

if grep -q "PT. Agra Karya Digital\|VeryCoolApps\|vcadeveloper" README.md; then
    echo -e "${GREEN}✓${NC} Company attribution"
else
    echo -e "${RED}✗${NC} No company attribution"
fi

echo ""
echo "📦 FILE SUMMARY"
echo ""

TOTAL_FILES=$(find . -type f | wc -l)
TOTAL_SIZE=$(du -sh . | cut -f1)
TOTAL_WORDS=$(wc -w SKILL.md README.md LICENSE references/*.md 2>/dev/null | tail -1 | awk '{print $1}')

echo "Total Files: $TOTAL_FILES"
echo "Total Size: $TOTAL_SIZE"
echo "Total Words (Documentation): $TOTAL_WORDS"

echo ""
echo "=================================="
if [ $FAILED -eq 0 ]; then
    echo -e "${GREEN}✅ ASSEMBLY COMPLETE - READY FOR PACKAGING${NC}"
    echo "=================================="
    exit 0
else
    echo -e "${YELLOW}⚠️  $FAILED checks incomplete - waiting for final agents${NC}"
    echo "=================================="
    exit 1
fi
