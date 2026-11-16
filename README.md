# DID DOCX Generator - Design Instructions Document Generation Engine

Professional Python implementation for generating high-quality Design Instructions Documents (DIDs) in Microsoft Word format (.docx).

## Overview

The DID DOCX Generator provides a production-ready document generation engine for creating professional Design Instructions Documents across multiple design disciplines:

- **Architectural Design** - Building standards, construction details, material specs
- **Interior Design** - Space planning, materials, lighting, aesthetics
- **Graphic Design** - Branding guidelines, typography, color systems
- **3D Design** - Mesh specs, textures, lighting, animation principles
- **UI/UX Design** - Component systems, interaction patterns, accessibility

## Features

### Core Capabilities
- Professional document styling and formatting
- Cover pages with custom branding
- Auto-generated Table of Contents
- Multiple heading levels with proper hierarchy
- Headers and footers with page numbering
- Styled paragraphs with custom formatting
- Professional table formatting with colors
- Image insertion with captions
- Bulleted and numbered lists
- Code blocks with monospace fonts
- Highlight boxes (info, warning, note)
- Section breaks and page breaks
- Comprehensive style management

### Design Discipline Support
- Discipline-specific color palettes
- Formatting guidelines per discipline
- Recommended section structures
- Professional styling rules

### Production Quality
- Full error handling and validation
- Comprehensive logging
- Type hints for better code quality
- Clear docstrings on all methods
- Zero placeholders - fully functional

## Installation

### Requirements
- Python 3.7 or higher
- Dependencies listed in requirements.txt

### Setup

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Copy configuration template:
```bash
cp .env.example .env
```

3. Customize .env as needed for your environment

## Quick Start

### Basic Usage

```python
from utils.docx_generator import DIDDocumentGenerator

# Create a new document
generator = DIDDocumentGenerator(
    title="My Design Standards",
    author="Design Team"
)

# Add cover page
generator.add_cover_page(
    main_title="Design Standards",
    version="1.0",
    subtitle="Professional Design Guide",
    company="ACME Corp"
)

# Add table of contents
generator.add_table_of_contents()

# Add content
generator.add_heading("Chapter 1: Design Principles", level=1)
generator.add_paragraph("Your content here...")

# Save document
generator.save("output/my_did.docx")
```

## Running Examples

```bash
# Generate sample documents
python examples/generate_sample_did.py

# Output:
# - output/sample_architectural_did.docx
# - output/sample_uiux_did.docx
```

## Project Structure

```
DID_SKILL/
├── requirements.txt              # Python dependencies
├── .env.example                  # Configuration template
├── README.md                     # This file
├── utils/
│   ├── __init__.py              # Package init
│   ├── docx_generator.py        # Main DOCX generator engine
│   └── design_formatter.py      # Discipline-specific formatters
├── examples/
│   ├── __init__.py              # Examples package init
│   └── generate_sample_did.py   # Complete working example
└── output/                       # Generated documents (created on first run)
```

## API Overview

### DIDDocumentGenerator

Main class with methods for:
- Document structure (cover, TOC, page breaks)
- Content (headings, paragraphs, lists)
- Tables and data
- Media (images, code blocks)
- Formatting (footers, page numbers)
- File management (save, summary)

### Design Formatters

Discipline-specific configuration:
- ArchitecturalFormatter
- InteriorFormatter
- GraphicFormatter
- ThreeDFormatter
- UIUXFormatter

### FormatterFactory

Simple factory for getting formatters by discipline name.

## Documentation

Full API documentation is in docstrings. Key methods:

```python
# Document structure
add_cover_page(main_title, version, subtitle=None, company=None)
add_table_of_contents()
add_page_break()
add_section_break(section_title=None)

# Content
add_heading(text, level=1, add_to_toc=True)
add_paragraph(text, style="Normal", bold=False, italic=False, indent=0.0)
add_bulleted_list(items, level=0)
add_numbered_list(items)

# Tables and data
add_table(rows, cols, header_row=None, data=None)

# Media
add_image(image_path, width=5.5, caption=None, align="center")
add_code_block(code, language="text")
add_highlight_box(text, box_type="info")

# Formatting and saving
add_footer_with_page_numbers(text="")
save(output_path)
get_summary()
```

## Configuration

Edit .env file (created from .env.example) to customize:

- Output directories
- Font families and sizes
- Colors (RGB tuples)
- Margins and spacing
- Document features (TOC, footers, etc.)
- Design discipline
- Logging levels

## Examples

See examples/generate_sample_did.py for:
- Architectural Design Standards document (comprehensive example)
- UI/UX Design System document (alternative discipline)

Both demonstrate all major features with real content.

## Error Handling

All methods include proper validation and error handling:

```python
try:
    generator.add_image("design.png", width=4.5)
except FileNotFoundError:
    print("Image file not found")

try:
    generator.save("output/doc.txt")  # Wrong extension
except ValueError:
    print("File must be .docx")
```

## Logging

Enable comprehensive logging to see all operations:

```python
import logging
logging.basicConfig(level=logging.INFO)
```

## Best Practices

1. Use discipline-specific formatters for appropriate colors
2. Plan document structure using recommended sections
3. Keep content concise and well-organized
4. Test documents after generation in Word
5. Use consistent styling throughout
6. Add images to support text
7. Include metadata (cover, TOC)
8. Ensure accessibility with proper contrast

## Support

For issues:
1. Check error messages and logging
2. Review example code
3. Verify configuration in .env
4. Check method docstrings for parameters
