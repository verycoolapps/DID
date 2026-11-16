"""
DID DOCX Generator - Professional Design Instructions Document Generator

A production-ready DOCX generation engine for creating professional Design
Instructions Documents (DIDs). Supports comprehensive styling, table of contents,
headers/footers, page numbering, images, and multi-discipline formatting.

Classes:
    DIDDocumentGenerator: Main document generation engine with comprehensive styling

Example:
    >>> generator = DIDDocumentGenerator(title="Architectural Guidelines")
    >>> generator.add_cover_page("My Architecture", "v1.0")
    >>> generator.add_heading("Chapter 1: Design Principles", level=1)
    >>> generator.add_paragraph("Design content here...")
    >>> generator.save("output.docx")
"""

from docx import Document
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml.ns import qn
from docx.oxml import OxmlElement
from pathlib import Path
from typing import Optional, List, Tuple, Dict, Any
from datetime import datetime
import logging


logger = logging.getLogger(__name__)


class DIDDocumentGenerator:
    """
    Production-ready DOCX document generator for Design Instructions Documents.

    Handles:
    - Professional document styling and formatting
    - Cover pages with custom branding
    - Table of contents (auto-generated)
    - Headers and footers with page numbering
    - Multiple heading levels with proper hierarchy
    - Paragraphs with custom formatting
    - Professional table formatting
    - Image insertion with captions
    - Page breaks and sections
    - Style management and consistency

    Attributes:
        document: The underlying python-docx Document object
        title: Document title
        author: Document author
        config: Configuration dictionary for styling
    """

    # Default configuration values
    DEFAULT_CONFIG = {
        "primary_color": (41, 128, 185),  # Professional blue
        "accent_color": (231, 76, 60),     # Accent red
        "text_color": (51, 51, 51),        # Dark gray
        "light_gray": (242, 242, 242),     # Light gray
        "font_family": "Calibri",
        "font_size_body": 11,
        "font_size_heading1": 24,
        "font_size_heading2": 16,
        "font_size_heading3": 13,
        "line_spacing": 1.15,
        "margin_top": 1.0,
        "margin_bottom": 1.0,
        "margin_left": 1.0,
        "margin_right": 1.0,
    }

    def __init__(
        self,
        title: str,
        author: Optional[str] = None,
        config: Optional[Dict[str, Any]] = None,
    ):
        """
        Initialize a new DID document generator.

        Args:
            title: Document title (required)
            author: Document author name (optional)
            config: Custom configuration dictionary (optional, merged with defaults)

        Raises:
            ValueError: If title is empty or None
        """
        if not title or not isinstance(title, str):
            raise ValueError("Title must be a non-empty string")

        self.document = Document()
        self.title = title
        self.author = author or "Design Team"
        self.creation_date = datetime.now()

        # Merge custom config with defaults
        self.config = self.DEFAULT_CONFIG.copy()
        if config:
            self.config.update(config)

        # Set document margins
        self._set_document_margins()

        # Track sections for TOC
        self._sections: List[Dict[str, Any]] = []
        self._has_cover = False

        logger.info(f"DIDDocumentGenerator initialized with title: {title}")

    def _set_document_margins(self) -> None:
        """Set document-wide margins based on configuration."""
        sections = self.document.sections
        for section in sections:
            section.top_margin = Inches(self.config["margin_top"])
            section.bottom_margin = Inches(self.config["margin_bottom"])
            section.left_margin = Inches(self.config["margin_left"])
            section.right_margin = Inches(self.config["margin_right"])

    def _apply_color(self, run, color: Tuple[int, int, int]) -> None:
        """Apply RGB color to a text run."""
        run.font.color.rgb = RGBColor(*color)

    def _apply_shading(self, paragraph, color: Tuple[int, int, int]) -> None:
        """Apply background shading to a paragraph."""
        shading_elm = OxmlElement("w:shd")
        shading_elm.set(qn("w:fill"), f"{color[0]:02x}{color[1]:02x}{color[2]:02x}")
        paragraph._element.get_or_add_pPr().append(shading_elm)

    def add_cover_page(
        self,
        main_title: str,
        version: str,
        subtitle: Optional[str] = None,
        company: Optional[str] = None,
    ) -> None:
        """
        Add a professional cover page to the document.

        Args:
            main_title: Main title for the cover
            version: Version number/string
            subtitle: Optional subtitle
            company: Optional company name

        Example:
            >>> generator.add_cover_page("Architectural Standards", "v2.1", "Global Design", "ACME Corp")
        """
        if self._has_cover:
            logger.warning("Cover page already exists, skipping")
            return

        # Add cover page section
        cover = self.document.add_paragraph()
        cover.paragraph_format.space_before = Pt(100)
        cover.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.CENTER

        # Main title
        title_run = cover.add_run(main_title)
        title_run.font.size = Pt(self.config["font_size_heading1"] + 6)
        title_run.font.bold = True
        title_run.font.name = self.config["font_family"]
        self._apply_color(title_run, self.config["primary_color"])

        # Subtitle
        if subtitle:
            self.document.add_paragraph()
            subtitle_para = self.document.add_paragraph(subtitle)
            subtitle_para.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.CENTER
            subtitle_run = subtitle_para.runs[0]
            subtitle_run.font.size = Pt(16)
            subtitle_run.font.italic = True
            subtitle_run.font.name = self.config["font_family"]

        # Company (if provided)
        if company:
            self.document.add_paragraph()
            company_para = self.document.add_paragraph(company)
            company_para.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.CENTER
            company_run = company_para.runs[0]
            company_run.font.size = Pt(12)
            company_run.font.name = self.config["font_family"]

        # Spacing
        self.document.add_paragraph()
        self.document.add_paragraph()

        # Metadata section
        metadata = self.document.add_paragraph()
        metadata.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.CENTER
        metadata.paragraph_format.space_before = Pt(60)

        version_run = metadata.add_run(f"Version: {version}\n")
        version_run.font.size = Pt(11)
        version_run.font.name = self.config["font_family"]

        date_run = metadata.add_run(f"Date: {self.creation_date.strftime('%B %d, %Y')}\n")
        date_run.font.size = Pt(11)
        date_run.font.name = self.config["font_family"]

        author_run = metadata.add_run(f"Author: {self.author}")
        author_run.font.size = Pt(11)
        author_run.font.name = self.config["font_family"]

        # Page break after cover
        self.document.add_page_break()
        self._has_cover = True
        logger.info(f"Cover page added: {main_title}")

    def add_table_of_contents(self) -> None:
        """
        Add a table of contents page.

        Note: In python-docx, TOC is a field code that Word updates on opening.
        This creates the structure for Word to recognize and update.

        Example:
            >>> generator.add_table_of_contents()
        """
        # Add TOC heading
        toc_heading = self.document.add_paragraph()
        toc_heading.style = "Heading 1"
        toc_run = toc_heading.add_run("Table of Contents")
        toc_run.font.size = Pt(self.config["font_size_heading1"])
        toc_run.font.color.rgb = RGBColor(*self.config["primary_color"])

        # Create field for TOC (Word will auto-populate on open)
        paragraph = self.document.add_paragraph()
        run = paragraph.add_run()

        # Insert TOC field code
        fldChar1 = OxmlElement("w:fldChar")
        fldChar1.set(qn("w:fldCharType"), "begin")

        instrText = OxmlElement("w:instrText")
        instrText.set(qn("xml:space"), "preserve")
        instrText.text = "TOC \\o '1-3' \\h \\z \\u"

        fldChar2 = OxmlElement("w:fldChar")
        fldChar2.set(qn("w:fldCharType"), "end")

        run._r.append(fldChar1)
        run._r.append(instrText)
        run._r.append(fldChar2)

        # Placeholder for TOC (Word updates this)
        placeholder = self.document.add_paragraph("Table of Contents will be generated by Word")
        placeholder.style = "Normal"
        placeholder.paragraph_format.left_indent = Inches(0.25)

        self.document.add_page_break()
        logger.info("Table of Contents added")

    def add_heading(
        self,
        text: str,
        level: int = 1,
        add_to_toc: bool = True,
    ) -> None:
        """
        Add a styled heading with proper hierarchy.

        Args:
            text: Heading text
            level: Heading level (1-3), where 1 is largest
            add_to_toc: Whether this heading should appear in TOC (default: True)

        Raises:
            ValueError: If level not in 1-3

        Example:
            >>> generator.add_heading("Chapter 1: Design Principles", level=1)
            >>> generator.add_heading("Section 1.1: Color Theory", level=2)
        """
        if level not in [1, 2, 3]:
            raise ValueError("Heading level must be 1, 2, or 3")

        style_name = f"Heading {level}"
        heading = self.document.add_paragraph(text, style=style_name)

        # Apply custom styling
        font_size_key = f"font_size_heading{level}"
        heading.runs[0].font.size = Pt(self.config[font_size_key])
        heading.runs[0].font.bold = True
        heading.runs[0].font.name = self.config["font_family"]
        self._apply_color(heading.runs[0], self.config["primary_color"])

        # Spacing
        heading.paragraph_format.space_before = Pt(12 if level == 1 else 8)
        heading.paragraph_format.space_after = Pt(6)

        # Track for TOC
        if add_to_toc:
            self._sections.append({"level": level, "text": text})

        logger.debug(f"Heading added (Level {level}): {text}")

    def add_paragraph(
        self,
        text: str,
        style: str = "Normal",
        bold: bool = False,
        italic: bool = False,
        indent: float = 0.0,
    ) -> None:
        """
        Add a styled paragraph to the document.

        Args:
            text: Paragraph text
            style: Paragraph style (default: "Normal")
            bold: Whether text should be bold
            italic: Whether text should be italic
            indent: Left indent in inches

        Example:
            >>> generator.add_paragraph("This is important", bold=True)
        """
        paragraph = self.document.add_paragraph(text, style=style)
        paragraph.paragraph_format.line_spacing = self.config["line_spacing"]
        paragraph.paragraph_format.space_after = Pt(6)

        if indent > 0:
            paragraph.paragraph_format.left_indent = Inches(indent)

        for run in paragraph.runs:
            run.font.size = Pt(self.config["font_size_body"])
            run.font.name = self.config["font_family"]
            if bold:
                run.font.bold = True
            if italic:
                run.font.italic = True
            self._apply_color(run, self.config["text_color"])

        logger.debug(f"Paragraph added: {text[:50]}...")

    def add_bulleted_list(
        self,
        items: List[str],
        level: int = 0,
    ) -> None:
        """
        Add a bulleted list to the document.

        Args:
            items: List of text items
            level: Indentation level (0 or 1)

        Example:
            >>> generator.add_bulleted_list(["Point 1", "Point 2", "Point 3"])
        """
        for item in items:
            paragraph = self.document.add_paragraph(item, style="List Bullet")
            if level > 0:
                paragraph.style = "List Bullet 2"

            for run in paragraph.runs:
                run.font.size = Pt(self.config["font_size_body"])
                run.font.name = self.config["font_family"]
                self._apply_color(run, self.config["text_color"])

        logger.debug(f"Added bulleted list with {len(items)} items")

    def add_numbered_list(
        self,
        items: List[str],
    ) -> None:
        """
        Add a numbered list to the document.

        Args:
            items: List of text items

        Example:
            >>> generator.add_numbered_list(["First step", "Second step", "Third step"])
        """
        for item in items:
            paragraph = self.document.add_paragraph(item, style="List Number")

            for run in paragraph.runs:
                run.font.size = Pt(self.config["font_size_body"])
                run.font.name = self.config["font_family"]
                self._apply_color(run, self.config["text_color"])

        logger.debug(f"Added numbered list with {len(items)} items")

    def add_table(
        self,
        rows: int,
        cols: int,
        header_row: Optional[List[str]] = None,
        data: Optional[List[List[str]]] = None,
    ) -> None:
        """
        Add a professional table to the document.

        Args:
            rows: Number of rows
            cols: Number of columns
            header_row: Optional header row text (list of strings)
            data: Optional table data (list of lists)

        Raises:
            ValueError: If dimensions don't match data

        Example:
            >>> headers = ["Column 1", "Column 2", "Column 3"]
            >>> data = [["Cell 1", "Cell 2", "Cell 3"], ["Cell 4", "Cell 5", "Cell 6"]]
            >>> generator.add_table(2, 3, header_row=headers, data=data)
        """
        # Validate dimensions
        total_rows = (1 if header_row else 0) + (len(data) if data else 0)
        if header_row and len(header_row) != cols:
            raise ValueError(f"Header row length {len(header_row)} doesn't match columns {cols}")
        if data and any(len(row) != cols for row in data):
            raise ValueError("All data rows must have the same number of columns")

        # Create table
        table = self.document.add_table(rows=rows, cols=cols)
        table.style = "Light Grid Accent 1"

        # Set column widths
        col_width = Inches((6.5 / cols))
        for row in table.rows:
            for cell in row.cells:
                cell.width = col_width

        # Add header row if provided
        if header_row:
            header_cells = table.rows[0].cells
            for i, header_text in enumerate(header_row):
                cell = header_cells[i]
                cell.text = header_text

                # Style header
                for paragraph in cell.paragraphs:
                    for run in paragraph.runs:
                        run.font.bold = True
                        run.font.size = Pt(11)
                        run.font.name = self.config["font_family"]
                        run.font.color.rgb = RGBColor(255, 255, 255)

                # Header background color
                self._shade_cell(cell, self.config["primary_color"])

        # Add data rows
        if data:
            start_row = 1 if header_row else 0
            for row_idx, row_data in enumerate(data):
                row_cells = table.rows[start_row + row_idx].cells
                for col_idx, cell_text in enumerate(row_data):
                    cell = row_cells[col_idx]
                    cell.text = cell_text

                    # Style cell
                    for paragraph in cell.paragraphs:
                        for run in paragraph.runs:
                            run.font.size = Pt(10)
                            run.font.name = self.config["font_family"]

        logger.info(f"Table added: {rows}x{cols}")

    def _shade_cell(self, cell, color: Tuple[int, int, int]) -> None:
        """Apply background shading to a table cell."""
        shading_elm = OxmlElement("w:shd")
        shading_elm.set(qn("w:fill"), f"{color[0]:02x}{color[1]:02x}{color[2]:02x}")
        cell._element.get_or_add_tcPr().append(shading_elm)

    def add_image(
        self,
        image_path: str,
        width: float = 5.5,
        caption: Optional[str] = None,
        align: str = "center",
    ) -> None:
        """
        Add an image to the document with optional caption.

        Args:
            image_path: Path to image file
            width: Image width in inches (default: 5.5)
            caption: Optional image caption
            align: Alignment ("left", "center", or "right")

        Raises:
            FileNotFoundError: If image file doesn't exist
            ValueError: If alignment is invalid

        Example:
            >>> generator.add_image("design.png", width=4.5, caption="Figure 1: Design Mockup")
        """
        path = Path(image_path)
        if not path.exists():
            raise FileNotFoundError(f"Image not found: {image_path}")

        if align not in ["left", "center", "right"]:
            raise ValueError("Alignment must be 'left', 'center', or 'right'")

        # Add image paragraph
        image_para = self.document.add_paragraph()
        alignment_map = {
            "left": WD_ALIGN_PARAGRAPH.LEFT,
            "center": WD_ALIGN_PARAGRAPH.CENTER,
            "right": WD_ALIGN_PARAGRAPH.RIGHT,
        }
        image_para.alignment = alignment_map[align]

        # Add image
        run = image_para.add_run()
        run.add_picture(str(path), width=Inches(width))

        # Add caption
        if caption:
            caption_para = self.document.add_paragraph(caption)
            caption_para.alignment = alignment_map[align]
            caption_para.paragraph_format.space_before = Pt(3)
            caption_para.paragraph_format.space_after = Pt(12)

            for run in caption_para.runs:
                run.font.italic = True
                run.font.size = Pt(10)
                run.font.name = self.config["font_family"]
                self._apply_color(run, self.config["text_color"])

        logger.info(f"Image added: {path.name}")

    def add_page_break(self) -> None:
        """Add a page break to the document."""
        self.document.add_page_break()
        logger.debug("Page break added")

    def add_section_break(self, section_title: Optional[str] = None) -> None:
        """
        Add a visual section break with optional title.

        Args:
            section_title: Optional title for the section

        Example:
            >>> generator.add_section_break("Part 2: Advanced Topics")
        """
        self.document.add_paragraph()

        if section_title:
            section_para = self.document.add_paragraph(section_title)
            section_para.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.CENTER
            section_para.paragraph_format.space_before = Pt(24)
            section_para.paragraph_format.space_after = Pt(24)

            for run in section_para.runs:
                run.font.size = Pt(14)
                run.font.italic = True
                run.font.name = self.config["font_family"]
                self._apply_color(run, self.config["accent_color"])

        self.document.add_paragraph()

    def add_code_block(self, code: str, language: str = "text") -> None:
        """
        Add a code block with monospace font.

        Args:
            code: Code text
            language: Programming language (for reference, doesn't apply syntax highlighting)

        Example:
            >>> generator.add_code_block("function hello() { console.log('world'); }", "javascript")
        """
        code_para = self.document.add_paragraph(code, style="Normal")
        code_para.paragraph_format.left_indent = Inches(0.25)

        for run in code_para.runs:
            run.font.name = "Courier New"
            run.font.size = Pt(9)
            self._apply_color(run, (41, 41, 41))

        logger.debug(f"Code block added ({language})")

    def add_highlight_box(self, text: str, box_type: str = "info") -> None:
        """
        Add a highlighted information box.

        Args:
            text: Box content
            box_type: Type of box ("info", "warning", "note")

        Example:
            >>> generator.add_highlight_box("Important: Review before deployment", box_type="warning")
        """
        color_map = {
            "info": (52, 152, 219),      # Blue
            "warning": (230, 126, 34),   # Orange
            "note": (155, 89, 182),      # Purple
        }

        color = color_map.get(box_type, color_map["info"])

        box_para = self.document.add_paragraph()
        box_para.paragraph_format.left_indent = Inches(0.25)
        box_para.paragraph_format.right_indent = Inches(0.25)
        box_para.paragraph_format.space_before = Pt(6)
        box_para.paragraph_format.space_after = Pt(6)

        # Add background
        self._apply_shading(box_para, (240, 240, 240))

        run = box_para.add_run(text)
        run.font.size = Pt(10)
        run.font.name = self.config["font_family"]
        self._apply_color(run, color)
        run.font.bold = True

        logger.debug(f"Highlight box added ({box_type})")

    def add_footer_with_page_numbers(self, text: str = "") -> None:
        """
        Add footer with page numbering to all sections.

        Args:
            text: Custom footer text (page number is added automatically)

        Example:
            >>> generator.add_footer_with_page_numbers("Design Guidelines v1.0")
        """
        for section in self.document.sections:
            footer = section.footer
            footer_para = footer.paragraphs[0] if footer.paragraphs else footer.add_paragraph()

            # Add custom text
            if text:
                run = footer_para.add_run(text)
                run.font.size = Pt(9)
                run.font.name = self.config["font_family"]
                self._apply_color(run, self.config["text_color"])

                footer_para.add_run(" | ")

            # Add page number
            page_run = footer_para.add_run("Page ")
            page_run.font.size = Pt(9)

            # Insert page number field
            fldChar1 = OxmlElement("w:fldChar")
            fldChar1.set(qn("w:fldCharType"), "begin")

            instrText = OxmlElement("w:instrText")
            instrText.set(qn("xml:space"), "preserve")
            instrText.text = "PAGE"

            fldChar2 = OxmlElement("w:fldChar")
            fldChar2.set(qn("w:fldCharType"), "end")

            page_run._r.append(fldChar1)
            page_run._r.append(instrText)
            page_run._r.append(fldChar2)

            # Center alignment for footer
            footer_para.alignment = WD_ALIGN_PARAGRAPH.CENTER

        logger.info("Footer with page numbers added")

    def save(self, output_path: str) -> Path:
        """
        Save the document to a file.

        Args:
            output_path: Output file path (should end with .docx)

        Returns:
            Path object of saved file

        Raises:
            ValueError: If output_path doesn't end with .docx

        Example:
            >>> output = generator.save("output/design_guide.docx")
            >>> print(f"Document saved to: {output}")
        """
        if not output_path.endswith(".docx"):
            raise ValueError("Output file must have .docx extension")

        output = Path(output_path)
        output.parent.mkdir(parents=True, exist_ok=True)

        self.document.save(str(output))
        logger.info(f"Document saved: {output}")

        return output

    def get_summary(self) -> Dict[str, Any]:
        """
        Get a summary of the document structure.

        Returns:
            Dictionary containing document metadata and section info

        Example:
            >>> summary = generator.get_summary()
            >>> print(f"Sections: {summary['section_count']}")
        """
        return {
            "title": self.title,
            "author": self.author,
            "creation_date": self.creation_date.isoformat(),
            "section_count": len(self._sections),
            "sections": self._sections,
            "paragraph_count": len(self.document.paragraphs),
            "table_count": len(self.document.tables),
            "has_cover": self._has_cover,
        }
