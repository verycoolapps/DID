# Getting Started with DID

Welcome to DID (Document Intelligence Design)! This guide will help you get up and running in minutes.

## Installation

### Prerequisites
- Python 3.8 or higher
- pip or conda package manager

### Quick Install
```bash
# Install from PyPI
pip install did-skill

# Or install in development mode
git clone <repository-url>
cd did-skill
pip install -e .
```

### Verify Installation
```bash
python -c "from did import DIDDocumentGenerator; print('DID installed successfully!')"
```

---

## Basic Usage

### Your First Document - 5 Minutes

```python
from did import DIDDocumentGenerator

# Create a generator for UX Design
generator = DIDDocumentGenerator(
    design_discipline="UX",
    project_name="Mobile App Redesign"
)

# Generate a document
document_path = generator.generate_document()

# Check the output
print(f"Document created: {document_path}")
```

This will:
1. Create a professional UX design document
2. Include 7 sections tailored to UX design
3. Save as `Mobile App Redesign_UX.docx`
4. Return the file path

### All Supported Disciplines

```python
disciplines = [
    "UX",           # User Experience Design
    "UI",           # User Interface Design
    "Product",      # Product Design
    "Backend",      # Backend Architecture
    "Frontend",     # Frontend Architecture
    "DevOps",       # DevOps & Infrastructure
    "QA"            # Quality Assurance
]

for discipline in disciplines:
    gen = DIDDocumentGenerator(
        design_discipline=discipline,
        project_name="Sample Project"
    )
    path = gen.generate_document()
    print(f"{discipline}: {path}")
```

---

## Common Workflows

### 1. Create a UX Design Document

```python
from did import DIDDocumentGenerator

gen = DIDDocumentGenerator(
    design_discipline="UX",
    project_name="E-commerce Platform"
)

# Generate document
doc_path = gen.generate_document()

# Check quality
quality_report = gen.get_quality_report()
print(f"Quality Score: {quality_report.score}/100")

# View document
print(f"Saved to: {doc_path}")
```

**Output**: Document with sections on research, personas, journeys, interaction patterns, wireframes, testing, and next steps.

---

### 2. Create a Backend Design Document

```python
from did import DIDDocumentGenerator

gen = DIDDocumentGenerator(
    design_discipline="Backend",
    project_name="API Gateway Service"
)

# Generate with custom output location
doc_path = gen.generate_document(
    output_path="/path/to/documents/"
)

# Get quality metrics
report = gen.get_quality_report()
print(f"Content Coherence: {report.coherence_score}")
print(f"Structure Validity: {report.structure_valid}")
```

**Output**: Document with sections on architecture, API design, database design, security, performance, error handling, and deployment.

---

### 3. Create a UI Design Document

```python
from did import DIDDocumentGenerator

gen = DIDDocumentGenerator(
    design_discipline="UI",
    project_name="Component Library"
)

# Generate document
doc_path = gen.generate_document()

# Access individual sections
sections = gen.get_all_sections()
for section in sections:
    print(f"- {section}")
```

**Output**: Document focused on visual systems, component libraries, design tokens, and accessibility.

---

### 4. Create a Product Design Document

```python
from did import DIDDocumentGenerator

gen = DIDDocumentGenerator(
    design_discipline="Product",
    project_name="Feature Launch"
)

doc_path = gen.generate_document()

# Check generated sections
sections_info = gen.get_sections_info()
for section_name, section_data in sections_info.items():
    print(f"{section_name}: {len(section_data)} characters")
```

**Output**: Document covering strategy, roadmaps, feature specifications, and go-to-market planning.

---

### 5. Create a DevOps Design Document

```python
from did import DIDDocumentGenerator

gen = DIDDocumentGenerator(
    design_discipline="DevOps",
    project_name="Infrastructure Migration"
)

# Generate and save with custom filename
doc_path = gen.generate_document(
    output_path="/docs/infrastructure/"
)

# Verify document was created
import os
if os.path.exists(doc_path):
    size_mb = os.path.getsize(doc_path) / (1024 * 1024)
    print(f"Document ready: {size_mb:.2f} MB")
```

**Output**: Document with infrastructure design, CI/CD pipelines, monitoring, and disaster recovery plans.

---

### 6. Create a QA Design Document

```python
from did import DIDDocumentGenerator

gen = DIDDocumentGenerator(
    design_discipline="QA",
    project_name="Testing Strategy"
)

doc_path = gen.generate_document()

# Get document metadata
metadata = gen.get_document_metadata()
print(f"Title: {metadata['title']}")
print(f"Created: {metadata['created_date']}")
print(f"Sections: {metadata['section_count']}")
```

**Output**: Document covering test strategy, automation, quality metrics, and risk assessment.

---

## Advanced Usage

### Customizing Section Content

```python
from did import DIDDocumentGenerator

gen = DIDDocumentGenerator(
    design_discipline="UX",
    project_name="Redesign Project"
)

# Customize a section before generation
gen.customize_section(
    section_name="Research & Discovery",
    content="Custom research methodology and findings..."
)

# Generate with custom content
doc_path = gen.generate_document()
```

---

### Specifying Output Location

```python
from did import DIDDocumentGenerator
from pathlib import Path

gen = DIDDocumentGenerator(
    design_discipline="UI",
    project_name="Design System v2"
)

# Set custom output directory
output_dir = Path.home() / "Documents" / "Design Documents"
output_dir.mkdir(parents=True, exist_ok=True)

doc_path = gen.generate_document(output_path=str(output_dir))
print(f"Document saved to: {doc_path}")
```

---

### Checking Quality Before Export

```python
from did import DIDDocumentGenerator

gen = DIDDocumentGenerator(
    design_discipline="Backend",
    project_name="API Design"
)

# Check quality without exporting
quality_report = gen.validate_content()

if quality_report.passed:
    # Quality is good, generate document
    doc_path = gen.generate_document()
    print(f"Document generated: {doc_path}")
else:
    # Quality issues found
    print(f"Quality Score: {quality_report.score}/100")
    print("Recommendations:")
    for rec in quality_report.recommendations:
        print(f"  - {rec}")
```

---

## Troubleshooting

### "Invalid discipline" Error

```python
# WRONG
gen = DIDDocumentGenerator(design_discipline="Website Design")

# CORRECT - Use supported disciplines only
gen = DIDDocumentGenerator(design_discipline="UI")
```

**Solution**: Use one of the 7 supported disciplines (UX, UI, Product, Backend, Frontend, DevOps, QA).

---

### "Project name too long" Error

```python
# WRONG
gen = DIDDocumentGenerator(
    design_discipline="UX",
    project_name="This is a very long project name that exceeds the character limit..."
)

# CORRECT
gen = DIDDocumentGenerator(
    design_discipline="UX",
    project_name="Mobile Redesign"  # Keep it concise
)
```

**Solution**: Project names should be 50 characters or fewer.

---

### "Invalid output path" Error

```python
# WRONG
gen.generate_document(output_path="/invalid/path/that/doesnt/exist")

# CORRECT - Create directory first
from pathlib import Path
output_dir = Path("/custom/path")
output_dir.mkdir(parents=True, exist_ok=True)
gen.generate_document(output_path=str(output_dir))
```

**Solution**: Ensure output directory exists before generation.

---

### Document Quality Below Threshold

```python
from did import DIDDocumentGenerator

gen = DIDDocumentGenerator(
    design_discipline="UX",
    project_name="Project"
)

quality = gen.get_quality_report()

if quality.score < 75:
    print("Quality issues detected:")
    print(f"- Coherence: {quality.coherence_score}/100")
    print(f"- Structure: {quality.structure_score}/100")
    print(f"- Formatting: {quality.formatting_score}/100")
    
    # Try again or customize
    gen.customize_section("Research & Discovery", "Better content...")
```

**Solution**: Review the quality report and customize sections as needed.

---

## Next Steps

1. **API Reference**: Learn all available methods in [API_REFERENCE.md](API_REFERENCE.md)
2. **Examples**: See more examples in [EXAMPLES.md](EXAMPLES.md)
3. **FAQ**: Common questions answered in [FAQ.md](FAQ.md)
4. **Contributing**: Contribute to DID in [CONTRIBUTING.md](../CONTRIBUTING.md)

---

## Common Questions

**Q: Can I use DID with Python 3.7?**
A: No, DID requires Python 3.8+. Consider upgrading your Python version.

**Q: Can I modify the generated document after creation?**
A: Yes! The output is a standard .docx file that can be edited in Microsoft Word, Google Docs, or any compatible editor.

**Q: How long does document generation take?**
A: Typically 3-7 seconds depending on system resources and customizations.

**Q: Can I generate multiple documents in a batch?**
A: Yes, see the batch example in [EXAMPLES.md](EXAMPLES.md).

**Q: Is there a way to preview content before saving?**
A: Yes, use `validate_content()` to check quality and get the generated content.

---

## Getting Help

- **Documentation**: Browse the [docs/](.) folder
- **Issues**: Check [GitHub Issues](../../issues) or create a new issue
- **Examples**: See [EXAMPLES.md](EXAMPLES.md) for 10+ working examples
- **API Docs**: Full reference in [API_REFERENCE.md](API_REFERENCE.md)

Happy documenting! 🚀
