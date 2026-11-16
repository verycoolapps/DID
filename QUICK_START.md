# DID Skill - Quick Start Guide

## 🚀 Get Started in 5 Minutes

### 1. Installation

```bash
# Clone the repository
git clone https://github.com/verycoolapps/DID.git
cd DID

# Install Python dependencies
pip install -r requirements.txt
```

### 2. Basic Usage

```python
from utils.docx_generator import DIDDocumentGenerator
from utils.design_formatter import ArchitecturalFormatter

# Create a new DID document
did = DIDDocumentGenerator(
    project_title="Modern Commercial Building",
    client_name="Your Client",
    document_version="1.0"
)

# Add sections
did.add_executive_summary("This is a three-storey commercial building...")
did.add_project_objectives(["Objective 1", "Objective 2", "Objective 3"])
did.add_functional_requirements(["Requirement 1", "Requirement 2"])

# Apply architectural formatting
formatter = ArchitecturalFormatter()
formatted_content = formatter.format_spatial_design(did.content)

# Generate DOCX
did.generate_docx("output/my_project_DID.docx")
```

### 3. Choose Your Design Discipline

DID automatically adapts to your project type:

- **Architecture** → Spatial planning, zoning, building specs
- **Interior Design** → Rooms, materials, furniture, lighting
- **Graphic Design** → Composition, typography, color systems
- **3D Modeling** → Geometry, materials, rendering specs
- **UI/UX Design** → User journeys, components, interactions
- **Branding** → Visual identity, color, typography guidelines
- **Product Design** → Dimensions, materials, functionality

### 4. Available Formatters

```python
from utils.design_formatter import (
    ArchitecturalFormatter,
    InteriorFormatter,
    GraphicFormatter,
    ThreeDFormatter,
    UIUXFormatter
)
```

### 5. Generate Your First DID

Run the included example:

```bash
python examples/generate_sample_did.py
```

This generates `sample_architectural_DID.docx` with:
- Professional formatting
- Complete documentation structure
- Realistic example content
- Ready-to-use template

### 6. Key Documents to Read

1. **README.md** - Full documentation in English & Indonesian
2. **SKILL.md** - Master operating system and core philosophy
3. **docs/GETTING_STARTED.md** - Detailed setup guide
4. **references/14-templates-and-examples.md** - Design discipline examples

### 7. Common Workflows

#### Workflow 1: Create Architectural Brief
```bash
python examples/generate_sample_did.py --discipline=architecture
```

#### Workflow 2: Create Interior Design Brief
```bash
python examples/generate_sample_did.py --discipline=interior
```

#### Workflow 3: Create 3D Environment Brief
```bash
python examples/generate_sample_did.py --discipline=3d
```

### 8. Document Sections Included

✅ Executive Summary
✅ Project Background
✅ Design Vision & Philosophy
✅ Target Users & Stakeholders
✅ Functional Requirements
✅ Design Specifications
✅ Dimensions & Technical Parameters
✅ Material & Resource Specifications
✅ Visual Direction
✅ Constraints & Risk Analysis
✅ Design Deliverables
✅ Quality Standards
✅ Design Execution Roadmap
✅ Final Design Instructions
✅ Validation & Approval

### 9. Customization

Edit `.env.example` for your preferences:

```bash
cp .env.example .env
# Customize:
# - Output directory
# - Document colors
# - Font preferences
# - Margins and spacing
```

### 10. Next Steps

1. ✅ Read SKILL.md to understand DID philosophy
2. ✅ Review references/ folder for discipline-specific guidance
3. ✅ Run generate_sample_did.py for a working example
4. ✅ Check docs/EXAMPLES.md for 5+ complete walkthroughs
5. ✅ Start with your own project!

---

## 🎯 Pro Tips

- **Start with examples** → Learn by looking at complete DIDs
- **Follow the structure** → Don't skip sections, they're all important
- **Be specific** → Generic requirements lead to generic designs
- **Measure everything** → Dimensions matter in architecture/3D
- **Validate assumptions** → Flag what you're not sure about

## 📚 Resources

- **API Reference**: `docs/API_REFERENCE.md`
- **FAQ**: `docs/FAQ.md`
- **Architecture**: `ARCHITECTURE.md`
- **Contributing**: `CONTRIBUTING.md`

## 🆘 Need Help?

1. Check `docs/FAQ.md` for common questions
2. Review examples in `references/14-templates-and-examples.md`
3. Read `docs/TROUBLESHOOTING.md`
4. Open an issue on GitHub

---

**Made by PT. Agra Karya Digital (VeryCoolApps)**
© 2026 | Licensed under DID Protective License
www.vcadeveloper.com
