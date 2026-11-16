#!/usr/bin/env python3
"""
Sample DID Document Generator - Complete Working Example

This example demonstrates how to use the DIDDocumentGenerator to create
a professional architectural Design Instructions Document (DID).

Shows usage of:
- Cover pages with branding
- Table of contents
- Multiple heading levels
- Styled paragraphs
- Lists (bulleted and numbered)
- Professional tables
- Images with captions
- Highlight boxes
- Footers with page numbering
- Section breaks
- Code blocks

Usage:
    python examples/generate_sample_did.py

Output:
    Creates: output/sample_architectural_did.docx
"""

import sys
from pathlib import Path

# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent))

from utils.docx_generator import DIDDocumentGenerator
from utils.design_formatter import FormatterFactory
import logging


# Configure logging for visibility
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)


def generate_architectural_did():
    """
    Generate a complete sample architectural Design Instructions Document.

    This example demonstrates:
    - Professional document structure
    - Architectural-specific content
    - Best practices for DID creation
    """

    # Get architectural formatter for color palette and guidelines
    formatter = FormatterFactory.get_formatter("architecture")
    config = formatter.get_config()

    # Create document generator with custom config
    generator = DIDDocumentGenerator(
        title="Architectural Design Standards",
        author="Architecture Department",
        config={
            "primary_color": config["primary_color"],
            "accent_color": config["accent_color"],
        },
    )

    print("Creating sample architectural DID...")

    # 1. ADD COVER PAGE
    generator.add_cover_page(
        main_title="Architectural Design Standards",
        version="2.1.0",
        subtitle="Building Design Guidelines and Construction Details",
        company="Global Architecture Standards Board",
    )

    # 2. ADD TABLE OF CONTENTS
    generator.add_table_of_contents()

    # 3. SECTION: DESIGN PHILOSOPHY
    generator.add_heading("Design Philosophy", level=1)
    generator.add_paragraph(
        "These architectural design standards establish the foundational principles "
        "and guidelines for all structural and aesthetic decisions. Every building "
        "design must adhere to these standards to ensure consistency, safety, and "
        "quality across all projects."
    )

    generator.add_bulleted_list([
        "Prioritize structural integrity and long-term sustainability",
        "Ensure compliance with all applicable building codes",
        "Create designs that enhance the built environment",
        "Balance aesthetic considerations with practical functionality",
        "Promote accessibility and inclusive design practices",
    ])

    # 4. SECTION: BUILDING CODES AND STANDARDS
    generator.add_heading("Building Codes and Standards", level=1)

    generator.add_heading("Compliance Requirements", level=2)
    generator.add_paragraph(
        "All designs must comply with the following standards:"
    )

    # Create compliance table
    headers = ["Standard", "Requirement", "Verification Method"]
    data = [
        ["IBC 2021", "International Building Code", "Third-party inspection"],
        ["LEED v4.1", "Green building certification", "USGBC verification"],
        ["ADA Standards", "Accessibility requirements", "Accessibility audit"],
        ["Energy Code", "Building energy efficiency", "Energy modeling"],
        ["Fire Safety", "NFPA 101 Life Safety Code", "Fire safety review"],
    ]

    generator.add_table(5, 3, header_row=headers, data=data)

    # 5. SECTION: MATERIAL SPECIFICATIONS
    generator.add_heading("Material Specifications", level=1)

    generator.add_heading("Structural Steel", level=2)
    generator.add_paragraph(
        "All structural steel must meet ASTM A992 specifications with Grade 50 "
        "minimum yield strength. Fabrication and welding must comply with AWS D1.1."
    )

    generator.add_highlight_box(
        "Critical: All steel connections must be designed for ductile behavior "
        "and have a Safety Factor of at least 2.0 for dead and live loads.",
        box_type="warning"
    )

    # Numbered list for steel specifications
    generator.add_numbered_list([
        "Verify material certs before fabrication begins",
        "Conduct mill test reports for all primary structural members",
        "Inspect welding processes using X-ray fluoroscopy",
        "Perform stress relief per AWS specifications",
        "Apply protective coating per design specifications",
    ])

    generator.add_heading("Concrete", level=2)
    generator.add_paragraph(
        "Concrete mixes must achieve minimum 4,000 PSI compressive strength at 28 days. "
        "All concrete must be air-entrained and include chemical admixtures for "
        "durability in exposed environments."
    )

    # 6. SECTION: STRUCTURAL GUIDELINES
    generator.add_heading("Structural Guidelines", level=1)

    generator.add_heading("Load Analysis", level=2)
    generator.add_paragraph(
        "Perform complete load analysis using industry-standard engineering software."
    )

    # Code block example
    generator.add_code_block(
        """
# Load combinations for structural analysis
Dead Load (DL) + Live Load (LL): 1.2 DL + 1.6 LL
Seismic Load: 1.0 DL + 0.5 LL + 1.0 E
Wind Load: 1.0 DL + 1.6 W
        """,
        language="structural"
    )

    # 7. SECTION: CONSTRUCTION DETAILS
    generator.add_section_break("Part 2: Construction Details")

    generator.add_heading("Construction Details", level=1)

    # Table with construction detail specifications
    detail_headers = ["Detail Type", "Scale", "File Name", "Updated"]
    detail_data = [
        ["Foundation Details", "1:4", "FND-001.dwg", "2024-11-01"],
        ["Column Connections", "1:2", "COL-002.dwg", "2024-11-01"],
        ["Beam Details", "1:4", "BEM-003.dwg", "2024-10-15"],
        ["Roof Assembly", "1:4", "ROF-004.dwg", "2024-10-20"],
    ]

    generator.add_table(4, 4, header_row=detail_headers, data=detail_data)

    # 8. SECTION: QUALITY ASSURANCE
    generator.add_heading("Quality Assurance", level=1)

    generator.add_paragraph(
        "All construction must undergo rigorous quality assurance testing."
    )

    generator.add_heading("Testing Schedule", level=2)
    generator.add_bulleted_list([
        "Weekly inspections during structural phase",
        "Concrete strength testing at 7, 14, and 28 days",
        "Welding inspection with certified inspectors",
        "Final walkthrough before occupancy permit",
    ])

    # 9. SECTION: SUSTAINABILITY
    generator.add_heading("Sustainability Requirements", level=1)

    generator.add_highlight_box(
        "All new construction must achieve a minimum LEED v4.1 Silver certification. "
        "LEED Gold or Platinum is strongly encouraged for all major projects.",
        box_type="info"
    )

    generator.add_heading("Energy Efficiency", level=2)
    generator.add_paragraph(
        "Design buildings to exceed energy code requirements by minimum 15%. "
        "Consider renewable energy systems, high-performance envelope design, "
        "and efficient HVAC systems."
    )

    generator.add_numbered_list([
        "Conduct energy modeling during design phase",
        "Use high-performance insulation materials",
        "Specify Energy Star certified equipment",
        "Design for natural ventilation where possible",
        "Implement smart controls for HVAC and lighting",
    ])

    # 10. SECTION: ACCESSIBILITY
    generator.add_heading("Accessibility Requirements", level=1)

    generator.add_paragraph(
        "All designs must fully comply with the Americans with Disabilities Act (ADA) "
        "and ANSI/ASIS Accessibility Guidelines. Accessibility is not an afterthought "
        "but an integral part of the design process."
    )

    # Accessibility specifications table
    access_headers = ["Feature", "ADA Requirement", "Recommended Practice"]
    access_data = [
        ["Ramps", "1:12 slope", "1:20 slope for comfort"],
        ["Doorways", "32\" clear", "36\" clear preferred"],
        ["Parking", "1 accessible per 25", "2 per 25 recommended"],
        ["Elevators", "Required > 3 stories", "In all buildings preferred"],
    ]

    generator.add_table(4, 3, header_row=access_headers, data=access_data)

    # 11. CONCLUSION
    generator.add_page_break()
    generator.add_heading("Summary", level=1)
    generator.add_paragraph(
        "This Design Instructions Document provides comprehensive guidelines for all "
        "architectural projects. Adherence to these standards ensures consistent quality, "
        "safety, and sustainability across all designs."
    )

    generator.add_highlight_box(
        "For questions or clarifications about these standards, contact the "
        "Architecture Standards Board at standards@architecture.org",
        box_type="note"
    )

    # 12. ADD FOOTER
    generator.add_footer_with_page_numbers("Architectural Design Standards v2.1.0")

    # 13. SAVE DOCUMENT
    output_dir = Path(__file__).parent.parent / "output"
    output_path = output_dir / "sample_architectural_did.docx"

    generator.save(str(output_path))

    # 14. PRINT SUMMARY
    summary = generator.get_summary()
    print("\n" + "=" * 60)
    print("DOCUMENT GENERATION COMPLETE")
    print("=" * 60)
    print(f"Title: {summary['title']}")
    print(f"Author: {summary['author']}")
    print(f"Created: {summary['creation_date']}")
    print(f"Sections: {summary['section_count']}")
    print(f"Paragraphs: {summary['paragraph_count']}")
    print(f"Tables: {summary['table_count']}")
    print(f"Output: {output_path}")
    print("=" * 60)

    return output_path


def generate_uiux_did():
    """
    Generate a sample UI/UX Design Instructions Document.

    This example shows how to create a DID for a different discipline.
    """

    # Get UI/UX formatter
    formatter = FormatterFactory.get_formatter("uiux")
    config = formatter.get_config()

    generator = DIDDocumentGenerator(
        title="UI/UX Design System Guidelines",
        author="Product Design Team",
        config={
            "primary_color": config["primary_color"],
            "accent_color": config["accent_color"],
        },
    )

    print("Creating sample UI/UX DID...")

    # Cover
    generator.add_cover_page(
        main_title="UI/UX Design System",
        version="1.0.0",
        subtitle="Component Library and Interaction Guidelines",
        company="Digital Products Division",
    )

    generator.add_table_of_contents()

    # Design System Overview
    generator.add_heading("Design System Overview", level=1)
    generator.add_paragraph(
        "This design system provides a comprehensive library of components, patterns, "
        "and guidelines for creating consistent user experiences across all digital products."
    )

    # Visual Design Principles
    generator.add_heading("Visual Design Principles", level=1)
    generator.add_bulleted_list([
        "Clarity: Clear communication through visual hierarchy",
        "Consistency: Unified patterns across all interfaces",
        "Accessibility: WCAG 2.1 AA compliance for all users",
        "Responsiveness: Optimal experience on all screen sizes",
        "Efficiency: Minimal friction in user workflows",
    ])

    # Component Library
    generator.add_heading("Component Library", level=1)

    components = [
        ["Button", "Primary, Secondary, Danger", "buttons.figma"],
        ["Input Field", "Text, Email, Password", "inputs.figma"],
        ["Modal Dialog", "Confirmation, Form", "modals.figma"],
        ["Navigation", "Top Nav, Side Nav", "navigation.figma"],
    ]

    generator.add_table(4, 3, header_row=["Component", "Variants", "File"], data=components)

    # Footer
    generator.add_footer_with_page_numbers("UI/UX Design System v1.0.0")

    output_dir = Path(__file__).parent.parent / "output"
    output_path = output_dir / "sample_uiux_did.docx"

    generator.save(str(output_path))
    print(f"UI/UX DID saved to: {output_path}")

    return output_path


if __name__ == "__main__":
    """
    Main entry point - generates sample documents.

    Creates two example documents:
    1. Architectural Design Standards (comprehensive example)
    2. UI/UX Design System (alternative discipline example)
    """

    try:
        # Generate architectural example
        arch_output = generate_architectural_did()

        # Generate UI/UX example
        uiux_output = generate_uiux_did()

        print(f"\nBoth sample documents generated successfully!")
        print(f"- Architectural: {arch_output}")
        print(f"- UI/UX: {uiux_output}")

    except Exception as e:
        print(f"Error generating documents: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
