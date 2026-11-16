# Frequently Asked Questions (FAQ)

## Table of Contents

1. [Design Discipline Questions](#design-discipline-questions)
2. [Technical Questions](#technical-questions)
3. [Output & Formatting Questions](#output--formatting-questions)
4. [Customization Questions](#customization-questions)
5. [Performance Questions](#performance-questions)
6. [Troubleshooting](#troubleshooting)

---

## Design Discipline Questions

### Q: What disciplines does DID support?

**A:** DID supports 7 design disciplines:

1. **UX (User Experience Design)** - User research, personas, journeys, interactions
2. **UI (User Interface Design)** - Visual systems, components, design tokens
3. **Product Design** - Strategy, roadmaps, feature specs, go-to-market
4. **Backend Design** - Architecture, APIs, databases, security
5. **Frontend Design** - Component architecture, state management, performance
6. **DevOps Design** - Infrastructure, CI/CD, monitoring, disaster recovery
7. **QA Design** - Test strategy, automation, metrics, risk assessment

Each discipline has 7 tailored sections with discipline-specific guidelines.

---

### Q: Can I add my own design disciplines?

**A:** Not in v1.0. DID is locked to the 7 built-in disciplines for quality consistency.

**Workaround:** You can customize any discipline's sections with your own content using `customize_section()`.

**Future:** v2.0 will support custom discipline definitions with custom section templates.

---

### Q: Which discipline should I use for X?

**A:** Choose based on the focus:

| Need | Discipline | Why |
|------|-----------|-----|
| User flows, wireframes | **UX** | Focus on user interaction |
| Component library, visual design | **UI** | Focus on visual systems |
| Feature planning, roadmap | **Product** | Focus on product strategy |
| System architecture, APIs | **Backend** | Focus on server-side design |
| Component structure, state | **Frontend** | Focus on client-side architecture |
| Infrastructure, deployments | **DevOps** | Focus on operations |
| Testing plan, QA strategy | **QA** | Focus on quality |

**Multiple disciplines:** Create separate documents for each perspective.

---

### Q: Can I merge multiple discipline documents?

**A:** Yes, manually merge .docx files:
1. Open in Microsoft Word
2. Use "Insert" → "Object" → "Text from File"
3. Insert sections from each document
4. Reformat as needed

**Planned for v2.0:** Automatic document composition.

---

## Technical Questions

### Q: What Python versions does DID support?

**A:** Python 3.8, 3.9, 3.10, 3.11, and 3.12.

**Not supported:** Python 3.7 or earlier, Python 2.x

```bash
# Check your version
python --version

# Update Python
brew install python@3.11  # macOS
apt install python3.11    # Linux
# Or download from python.org
```

---

### Q: What are DID's dependencies?

**A:** Minimal production dependencies:

- **python-docx** (0.8.11+) - DOCX file generation
- **pydantic** (2.0+) - Data validation

**Development dependencies:**
- pytest (testing)
- black (formatting)
- flake8 (linting)
- mypy (type checking)

```bash
# Check installed versions
pip show python-docx pydantic
```

---

### Q: Can I use DID in a web application?

**A:** Yes! DID is a pure Python library and can be integrated with:

- **Flask/FastAPI** - Web API wrapper
- **Django** - As a document generation service
- **Celery** - Async task processing
- **Cloud Functions** - AWS Lambda, Google Cloud Functions

**Example with FastAPI:**
```python
from fastapi import FastAPI
from did import DIDDocumentGenerator

app = FastAPI()

@app.post("/generate/{discipline}/{project}")
def generate(discipline: str, project: str):
    gen = DIDDocumentGenerator(discipline, project)
    doc_path = gen.generate_document()
    # Return file or file path
    return {"document": doc_path}
```

---

### Q: Does DID work offline?

**A:** Yes, DID is completely offline. No internet required.

**Requires:**
- Local Python installation
- Dependencies installed via pip

**Can't do:**
- Access external APIs
- Download templates
- Cloud storage integration (v1.0)

---

### Q: Can I use DID in a Docker container?

**A:** Yes! Create a Dockerfile:

```dockerfile
FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENTRYPOINT ["python", "-m", "did.cli"]
```

Then build and run:
```bash
docker build -t did-generator .
docker run did-generator UX "My Project"
```

---

## Output & Formatting Questions

### Q: What format is the output file?

**A:** Standard Microsoft Word .docx (Office Open XML format).

**Compatible with:**
- Microsoft Word (2010+)
- Google Docs (import/edit)
- LibreOffice Writer
- Apple Pages
- Online editors

**Output naming:** `[ProjectName]_[Discipline].docx`

Example: `Mobile_App_Redesign_UX.docx`

---

### Q: Can I export to other formats?

**A:** Not in v1.0 (only .docx).

**Workarounds:**
1. Open .docx in Word/Google Docs, export to PDF/HTML
2. Use online converters
3. Use `python-docx` to programmatically convert

**v1.1 planned features:**
- PDF export
- HTML export
- Markdown export
- PowerPoint export

---

### Q: Can I customize the document styling?

**A:** Limited customization in v1.0:
- Section content (via `customize_section()`)
- Project name and discipline
- Output filename

**Can't change in v1.0:**
- Fonts (fixed to Calibri)
- Colors (fixed to professional theme)
- Page margins (fixed to 1 inch)
- Heading styles (fixed hierarchy)

**v1.1 planned:** Advanced styling options.

---

### Q: How many pages will my document be?

**A:** Approximately 10-15 pages depending on:
- Discipline (7-9 sections each)
- Section customization
- Content length
- Font size and spacing

**Typical breakdown:**
- Cover: 1 page
- Each section: 1-2 pages
- Total: 10-15 pages

---

### Q: Can I add images to the document?

**A:** Not directly in DID v1.0 (text-only content).

**Workaround:**
1. Generate .docx with DID
2. Open in Word
3. Insert images manually
4. Save

**v1.1 planned:** Image embedding support.

---

## Customization Questions

### Q: How do I customize a section?

**A:** Use `customize_section()`:

```python
gen = DIDDocumentGenerator("UX", "Project")

gen.customize_section(
    "Research & Discovery",
    "Your custom content here..."
)

gen.generate_document()
```

**Available section names:** See `get_all_sections()`

---

### Q: Can I add or remove sections?

**A:** No in v1.0. Each discipline has fixed sections.

**Workarounds:**
1. Leave a section mostly empty (but still required)
2. Add all custom content to available sections
3. Manually edit .docx after generation

**v1.1 planned:** Custom section management.

---

### Q: Can I change the document title/author?

**A:** The title is generated from discipline and project name:

```
[Discipline] Design Document - [Project Name]
```

**Example:**
- Input: `DIDDocumentGenerator("UX", "Mobile App")`
- Title: `UX Design Document - Mobile App`

**Can't change in v1.0, but future feature planned.**

---

### Q: How do I add company branding?

**A:** DID doesn't support branding in v1.0.

**Workarounds:**
1. Generate document
2. Open in Word/Google Docs
3. Add company logo, colors, watermark
4. Save as branded template

**Future:** Branding templates planned for v2.0.

---

## Performance Questions

### Q: How long does generation take?

**A:** Typical times:
- Initialization: < 1 second
- Content generation: 2-3 seconds
- Validation: < 1 second
- DOCX writing: < 1 second
- **Total: 3-7 seconds**

**Factors affecting speed:**
- System CPU
- RAM available
- Disk speed
- Section customization

---

### Q: Can I generate documents in parallel?

**A:** Yes, use threading or multiprocessing:

```python
from concurrent.futures import ThreadPoolExecutor
from did import DIDDocumentGenerator

def generate_doc(discipline, project):
    gen = DIDDocumentGenerator(discipline, project)
    return gen.generate_document()

disciplines = ["UX", "UI", "Backend"]

with ThreadPoolExecutor(max_workers=3) as executor:
    futures = [
        executor.submit(generate_doc, d, "Project")
        for d in disciplines
    ]
    results = [f.result() for f in futures]
```

---

### Q: What's the maximum document size?

**A:** No hard limit in DID.

**Practical limits:**
- Python-docx handles documents up to ~100 MB
- Word performance degrades with 500+ sections
- Recommended: 50-100 sections max

**Typical documents:** 10-20 sections, < 2 MB.

---

### Q: Can I use DID with large batch processing?

**A:** Yes, see [EXAMPLES.md - Batch Processing](EXAMPLES.md#batch-processing).

**Performance tips:**
1. Use process pool for heavy loads
2. Generate to SSD (faster I/O)
3. Avoid customization of many sections
4. Use `validate=False` for speed (not recommended)

---

## Troubleshooting

### Q: "No module named 'did'"

**Problem:** DID not installed.

**Solution:**
```bash
pip install did-skill
# Or from source:
git clone <repo>
cd did-skill
pip install -e .
```

---

### Q: "InvalidDisciplineError: Unknown discipline"

**Problem:** Discipline name misspelled or unsupported.

**Solution:**
```python
# WRONG
gen = DIDDocumentGenerator("ux design", "Project")  # Lowercase
gen = DIDDocumentGenerator("User Experience", "Project")  # Full name

# CORRECT
gen = DIDDocumentGenerator("UX", "Project")  # Exact name
```

**Supported:** UX, UI, Product, Backend, Frontend, DevOps, QA

---

### Q: "InvalidProjectNameError: Project name too long"

**Problem:** Project name exceeds 50 characters.

**Solution:**
```python
# WRONG
gen = DIDDocumentGenerator("UX", "My Very Long Project Name That Is Way Too Long For DID To Handle")

# CORRECT
gen = DIDDocumentGenerator("UX", "Mobile App Redesign")
```

---

### Q: "FileWriteError: Permission denied"

**Problem:** No write permission to output directory.

**Solution:**
```python
# Check permissions
import os
path = "/path/to/output"
if not os.access(path, os.W_OK):
    print("No write permission!")

# Use home directory instead
from pathlib import Path
home_dir = Path.home() / "Documents"
gen.generate_document(output_path=str(home_dir))
```

---

### Q: "QualityThresholdError: Quality score too low"

**Problem:** Generated content doesn't meet quality threshold (75+).

**Solution:**
```python
gen = DIDDocumentGenerator("Backend", "Project")

# Check what failed
report = gen.validate_content()
print(f"Score: {report.score}/100")
print("Issues:", report.issues)

# Customize low-quality sections
sections_info = gen.get_sections_info()
for section, info in sections_info.items():
    if info['quality_score'] < 75:
        gen.customize_section(section, "Better content...")

# Try again
gen.generate_document()
```

---

### Q: Document file is corrupted

**Problem:** .docx file won't open.

**Likely causes:**
- Disk full during write
- File path contains special characters
- Improper shutdown during generation

**Solutions:**
1. Check disk space: `df -h`
2. Use simple filename: no unicode, special chars
3. Try again with different output path

---

### Q: Generated content is repetitive

**Problem:** Sections have similar or duplicate content.

**Solution:** Customize sections with specific content:

```python
gen = DIDDocumentGenerator("UX", "Project")

# Replace generic sections with project-specific content
gen.customize_section("Research & Discovery", "Your findings...")
gen.customize_section("User Journeys", "Your journey maps...")

gen.generate_document()
```

---

### Q: How do I see the generated content without saving?

**Solution:** Use `generate_section()`:

```python
gen = DIDDocumentGenerator("UX", "Project")

# View individual sections
for section in gen.get_all_sections():
    content = gen.generate_section(section)
    print(f"=== {section} ===")
    print(content)
    print()
```

---

## Still Have Questions?

- **Documentation:** Read [GETTING_STARTED.md](GETTING_STARTED.md)
- **Examples:** See [EXAMPLES.md](EXAMPLES.md)
- **API Reference:** Check [API_REFERENCE.md](API_REFERENCE.md)
- **Issues:** Report on GitHub Issues
- **Discussions:** Start a GitHub Discussion

---

## Related Documentation

- [GETTING_STARTED.md](GETTING_STARTED.md) - Quick start
- [API_REFERENCE.md](API_REFERENCE.md) - Complete API
- [EXAMPLES.md](EXAMPLES.md) - 15+ working examples
- [../ARCHITECTURE.md](../ARCHITECTURE.md) - Technical design
- [../CONTRIBUTING.md](../CONTRIBUTING.md) - Contributing
