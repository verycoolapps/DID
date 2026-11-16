# DID API Reference

Complete documentation of the DID Python API.

## Table of Contents
1. [DIDDocumentGenerator](#diddocumentgenerator)
2. [Configuration](#configuration)
3. [Quality Reports](#quality-reports)
4. [Exceptions](#exceptions)
5. [Type Hints](#type-hints)

---

## DIDDocumentGenerator

The main class for generating design documents.

### Class Definition

```python
class DIDDocumentGenerator:
    """Generate professional design documents for specific disciplines."""
```

### Constructor

#### `__init__(design_discipline, project_name, output_path=None, validate_on_init=True)`

Initialize a document generator.

**Parameters:**
- `design_discipline` (str): One of: "UX", "UI", "Product", "Backend", "Frontend", "DevOps", "QA"
- `project_name` (str): Name of the project (1-50 characters, alphanumeric + spaces/hyphens)
- `output_path` (Optional[str]): Directory to save generated documents (default: current directory)
- `validate_on_init` (bool): Validate configuration on initialization (default: True)

**Returns:** DIDDocumentGenerator instance

**Raises:**
- `InvalidDisciplineError`: If discipline not supported
- `InvalidProjectNameError`: If project name is invalid
- `ConfigValidationError`: If configuration is invalid

**Example:**
```python
from did import DIDDocumentGenerator

# Basic initialization
gen = DIDDocumentGenerator("UX", "Mobile App")

# With custom output path
gen = DIDDocumentGenerator(
    design_discipline="Backend",
    project_name="API Service",
    output_path="/home/user/documents"
)

# Skip validation (not recommended)
gen = DIDDocumentGenerator(
    "UI",
    "Design System",
    validate_on_init=False
)
```

---

### Public Methods

#### `generate_document(output_path=None, validate=True)`

Generate and save a complete design document.

**Parameters:**
- `output_path` (Optional[str]): Override default output path
- `validate` (bool): Run QA validation before generation (default: True)

**Returns:** str (Path to generated .docx file)

**Raises:**
- `ContentGenerationError`: If content generation fails
- `QualityThresholdError`: If quality validation fails
- `DocumentGenerationError`: If DOCX creation fails
- `FileWriteError`: If file cannot be written

**Example:**
```python
gen = DIDDocumentGenerator("UX", "Redesign Project")

# Generate with validation
doc_path = gen.generate_document()
print(f"Document saved: {doc_path}")

# Generate with custom output path
doc_path = gen.generate_document(output_path="/tmp/docs/")

# Skip validation for speed
doc_path = gen.generate_document(validate=False)
```

---

#### `generate_section(section_name, section_type="body")`

Generate content for a single section.

**Parameters:**
- `section_name` (str): Name of section to generate
- `section_type` (str): Type of section ("intro", "body", "conclusion")

**Returns:** str (Generated section content)

**Raises:**
- `SectionNotFoundError`: If section not recognized
- `ContentGenerationError`: If generation fails

**Example:**
```python
gen = DIDDocumentGenerator("UX", "Project")

# Generate intro section
intro = gen.generate_section("Research & Discovery", "intro")
print(intro)

# Generate body section
body = gen.generate_section("User Journeys", "body")

# Generate conclusion section
conclusion = gen.generate_section("Next Steps", "conclusion")
```

---

#### `get_all_sections()`

Get list of all available sections for the discipline.

**Parameters:** None

**Returns:** List[str] (Names of all sections)

**Example:**
```python
gen = DIDDocumentGenerator("Backend", "API")

sections = gen.get_all_sections()
for section in sections:
    print(f"- {section}")
```

---

#### `customize_section(section_name, content)`

Replace a section with custom content.

**Parameters:**
- `section_name` (str): Name of section to customize
- `content` (str): New content for section

**Returns:** bool (True if successful)

**Raises:**
- `SectionNotFoundError`: If section doesn't exist
- `ContentValidationError`: If content is invalid

**Example:**
```python
gen = DIDDocumentGenerator("UX", "Project")

# Customize a section
gen.customize_section(
    "Research & Discovery",
    "Custom research methodology based on interviews..."
)

# Then generate document
doc_path = gen.generate_document()
```

---

#### `validate_content()`

Validate generated content without creating document.

**Parameters:** None

**Returns:** QualityReport (See Quality Reports section)

**Raises:**
- `ContentGenerationError`: If validation fails

**Example:**
```python
gen = DIDDocumentGenerator("UI", "Component Library")

# Validate content
report = gen.validate_content()

if report.passed:
    print("Quality checks passed!")
    gen.generate_document()
else:
    print(f"Quality score: {report.score}/100")
    print("Issues:")
    for issue in report.issues:
        print(f"  - {issue}")
```

---

#### `get_quality_report()`

Get quality assessment of current content.

**Parameters:** None

**Returns:** QualityReport (See Quality Reports section)

**Example:**
```python
gen = DIDDocumentGenerator("Product", "Feature Launch")
gen.generate_section("Strategy")

report = gen.get_quality_report()
print(f"Content Coherence: {report.coherence_score}/100")
print(f"Structure Validity: {report.structure_valid}")
print(f"Professional Tone: {report.tone_valid}")
print(f"Overall Score: {report.score}/100")
```

---

#### `get_document_metadata()`

Get metadata about the generated document.

**Parameters:** None

**Returns:** Dict[str, Any] with keys:
- `title` (str): Document title
- `discipline` (str): Design discipline
- `project_name` (str): Project name
- `created_date` (str): ISO format creation date
- `section_count` (int): Number of sections
- `total_characters` (int): Total content length
- `estimated_pages` (int): Approximate page count
- `quality_score` (float): Quality score (0-100)

**Example:**
```python
gen = DIDDocumentGenerator("QA", "Testing Strategy")
doc_path = gen.generate_document()

metadata = gen.get_document_metadata()
print(f"Title: {metadata['title']}")
print(f"Sections: {metadata['section_count']}")
print(f"Pages: {metadata['estimated_pages']}")
print(f"Quality: {metadata['quality_score']}/100")
```

---

#### `get_sections_info()`

Get detailed information about all sections.

**Parameters:** None

**Returns:** Dict[str, Dict[str, Any]] with section info:
- Each section has:
  - `type` (str): Section type (intro/body/conclusion)
  - `content_length` (int): Character count
  - `word_count` (int): Word count
  - `quality_score` (float): Section quality (0-100)

**Example:**
```python
gen = DIDDocumentGenerator("Frontend", "Architecture")
gen.generate_document()

sections_info = gen.get_sections_info()
for section_name, info in sections_info.items():
    print(f"{section_name}:")
    print(f"  Words: {info['word_count']}")
    print(f"  Quality: {info['quality_score']}/100")
```

---

#### `set_output_path(path)`

Set the default output directory for documents.

**Parameters:**
- `path` (str or Path): Directory path

**Returns:** bool (True if successful)

**Raises:**
- `OutputPathError`: If path is invalid or inaccessible

**Example:**
```python
from pathlib import Path

gen = DIDDocumentGenerator("UI", "Project")

# Set custom output directory
docs_dir = Path.home() / "Documents" / "Design Docs"
docs_dir.mkdir(parents=True, exist_ok=True)
gen.set_output_path(str(docs_dir))

# Future generations will use this path
doc_path = gen.generate_document()
```

---

#### `get_discipline()`

Get the current design discipline.

**Parameters:** None

**Returns:** str (Discipline name)

**Example:**
```python
gen = DIDDocumentGenerator("Backend", "Project")

discipline = gen.get_discipline()
print(f"Current discipline: {discipline}")  # Output: Backend
```

---

#### `get_project_name()`

Get the current project name.

**Parameters:** None

**Returns:** str (Project name)

**Example:**
```python
gen = DIDDocumentGenerator("Product", "Feature Launch")

project = gen.get_project_name()
print(f"Project: {project}")  # Output: Feature Launch
```

---

## Configuration

### Configuration Class

```python
class Config:
    """Configuration management for DID."""
```

Configuration is automatically handled by DIDDocumentGenerator but can be customized:

```python
from did import Config, DIDDocumentGenerator

# Access configuration
gen = DIDDocumentGenerator("UX", "Project")
config = gen.config

# Configuration properties (read-only)
print(config.discipline)      # str
print(config.project_name)    # str
print(config.output_path)     # Path
print(config.validate_on_gen) # bool
```

### Supported Disciplines

```python
SUPPORTED_DISCIPLINES = {
    "UX": "User Experience Design",
    "UI": "User Interface Design",
    "Product": "Product Design",
    "Backend": "Backend Architecture",
    "Frontend": "Frontend Architecture",
    "DevOps": "DevOps & Infrastructure",
    "QA": "Quality Assurance"
}
```

---

## Quality Reports

### QualityReport Class

```python
class QualityReport:
    """Quality assessment report for document content."""
```

**Properties:**

- `passed` (bool): Whether quality threshold was met (score ≥ 75)
- `score` (float): Overall quality score (0-100)
- `coherence_score` (float): Content coherence (0-100)
- `structure_score` (float): Structure validity (0-100)
- `formatting_score` (float): Professional formatting (0-100)
- `tone_score` (float): Professional tone (0-100)
- `issues` (List[str]): List of identified issues
- `recommendations` (List[str]): Improvement suggestions
- `timestamp` (str): Report generation timestamp

**Example:**

```python
gen = DIDDocumentGenerator("Backend", "API Design")

report = gen.validate_content()

# Check if passed
if report.passed:
    print("Quality checks passed!")
else:
    print(f"Score: {report.score}/100")
    
# View individual scores
print(f"Coherence: {report.coherence_score}/100")
print(f"Structure: {report.structure_score}/100")
print(f"Formatting: {report.formatting_score}/100")
print(f"Tone: {report.tone_score}/100")

# View issues
if report.issues:
    print("Issues found:")
    for issue in report.issues:
        print(f"  - {issue}")

# View recommendations
if report.recommendations:
    print("Recommendations:")
    for rec in report.recommendations:
        print(f"  - {rec}")
```

---

## Exceptions

All exceptions inherit from `DIDException`.

### DIDException

Base exception class for all DID errors.

```python
class DIDException(Exception):
    """Base exception for DID."""
    pass
```

### Configuration Errors

#### InvalidDisciplineError

Raised when an unsupported discipline is specified.

```python
from did import DIDDocumentGenerator
from did.exceptions import InvalidDisciplineError

try:
    gen = DIDDocumentGenerator("Invalid", "Project")
except InvalidDisciplineError as e:
    print(f"Error: {e}")
    print(f"Supported: UX, UI, Product, Backend, Frontend, DevOps, QA")
```

#### InvalidProjectNameError

Raised when project name is invalid.

```python
try:
    gen = DIDDocumentGenerator("UX", "")  # Empty name
except InvalidProjectNameError as e:
    print(f"Error: {e}")
```

#### ConfigValidationError

Raised when configuration is invalid.

```python
try:
    gen = DIDDocumentGenerator(
        "UX",
        "Project",
        output_path="/invalid/path"
    )
except ConfigValidationError as e:
    print(f"Error: {e}")
```

### Content Generation Errors

#### ContentGenerationError

Raised when content generation fails.

```python
try:
    gen = DIDDocumentGenerator("UI", "Project")
    content = gen.generate_section("Invalid Section")
except ContentGenerationError as e:
    print(f"Generation failed: {e}")
```

#### SectionNotFoundError

Raised when a section doesn't exist.

```python
try:
    gen = DIDDocumentGenerator("UI", "Project")
    gen.customize_section("Nonexistent", "content")
except SectionNotFoundError as e:
    print(f"Section not found: {e}")
```

### Quality & Validation Errors

#### QualityThresholdError

Raised when content quality is below threshold.

```python
try:
    gen = DIDDocumentGenerator("UX", "Project")
    gen.generate_document()  # With validate=True (default)
except QualityThresholdError as e:
    print(f"Quality too low: {e}")
    report = gen.get_quality_report()
    print(f"Score: {report.score}/100")
```

### Document Generation Errors

#### DocumentGenerationError

Raised when DOCX document creation fails.

```python
try:
    gen = DIDDocumentGenerator("Backend", "Project")
    doc_path = gen.generate_document()
except DocumentGenerationError as e:
    print(f"Document generation failed: {e}")
```

#### FileWriteError

Raised when file cannot be written.

```python
try:
    gen = DIDDocumentGenerator("QA", "Project")
    gen.generate_document(output_path="/read-only-path")
except FileWriteError as e:
    print(f"Cannot write file: {e}")
```

---

## Type Hints

All methods include type hints. Common types used:

```python
from typing import Optional, List, Dict, Any
from pathlib import Path

# Common parameter types
design_discipline: str              # One of supported disciplines
project_name: str                   # 1-50 chars
output_path: Optional[str]          # Directory path
content: str                        # Text content
section_name: str                   # Section identifier

# Common return types
Path                                # File path
bool                                # Success indicator
List[str]                           # List of strings
Dict[str, Any]                      # Flexible dictionary
QualityReport                        # Quality assessment
```

---

## Complete Example

```python
from did import DIDDocumentGenerator
from did.exceptions import InvalidDisciplineError, QualityThresholdError

def create_design_document():
    try:
        # Initialize generator
        gen = DIDDocumentGenerator(
            design_discipline="UI",
            project_name="Component Library v2"
        )
        
        # Get available sections
        sections = gen.get_all_sections()
        print(f"Available sections: {len(sections)}")
        
        # Customize a section
        gen.customize_section(
            "Visual Design System",
            "Custom content about our design system..."
        )
        
        # Validate before generation
        report = gen.validate_content()
        print(f"Pre-generation quality: {report.score}/100")
        
        # Generate document
        doc_path = gen.generate_document()
        print(f"Document created: {doc_path}")
        
        # Get metadata
        metadata = gen.get_document_metadata()
        print(f"Title: {metadata['title']}")
        print(f"Pages: {metadata['estimated_pages']}")
        
        # Get final quality report
        final_report = gen.get_quality_report()
        print(f"Final quality: {final_report.score}/100")
        
        return True
        
    except InvalidDisciplineError as e:
        print(f"Invalid discipline: {e}")
        return False
    except QualityThresholdError as e:
        print(f"Quality too low: {e}")
        return False
    except Exception as e:
        print(f"Unexpected error: {e}")
        return False

if __name__ == "__main__":
    success = create_design_document()
    exit(0 if success else 1)
```

---

## See Also

- [GETTING_STARTED.md](GETTING_STARTED.md) - Quick start guide
- [EXAMPLES.md](EXAMPLES.md) - Usage examples
- [FAQ.md](FAQ.md) - Frequently asked questions
- [../ARCHITECTURE.md](../ARCHITECTURE.md) - Technical architecture
