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


    # ------------------------------------------------------------------
    # DED (Detail Engineering Design) primitives
    # Indonesian consultant conventions — see references/14-templates-and-examples.md
    # ------------------------------------------------------------------

    def add_daftar_gambar(self, rows: List[Dict[str, Any]]) -> None:
        """
        Add a Daftar Gambar (drawing register) table.

        Args:
            rows: List of dicts with keys:
                no (int), kode (str), judul (str), skala (str),
                jumlah (int), disiplin (str)

        Example:
            >>> gen.add_daftar_gambar([
            ...     {"no": 1, "kode": "00.01", "judul": "SITEPLAN",
            ...      "skala": "1:150", "jumlah": 1, "disiplin": "ARS"},
            ... ])
        """
        headers = ["NO", "KODE", "JUDUL GAMBAR", "SKALA", "JML", "DISIPLIN"]
        table = self.document.add_table(rows=len(rows) + 1, cols=len(headers))
        table.style = "Light Grid Accent 1"

        # Header
        for i, h in enumerate(headers):
            cell = table.rows[0].cells[i]
            cell.text = h
            self._shade_cell(cell, self.config["primary_color"])
            for p in cell.paragraphs:
                for r in p.runs:
                    r.font.bold = True
                    r.font.size = Pt(9)
                    r.font.color.rgb = RGBColor(255, 255, 255)

        # Body
        for row_idx, item in enumerate(rows, start=1):
            cells = table.rows[row_idx].cells
            values = [
                str(item.get("no", row_idx)),
                str(item.get("kode", "")),
                str(item.get("judul", "")),
                str(item.get("skala", "")),
                str(item.get("jumlah", 1)),
                str(item.get("disiplin", "")),
            ]
            for col_idx, val in enumerate(values):
                cells[col_idx].text = val
                for p in cells[col_idx].paragraphs:
                    for r in p.runs:
                        r.font.size = Pt(9)

        logger.info(f"Daftar Gambar added: {len(rows)} rows")

    def add_ded_title_block(
        self,
        kegiatan: str,
        pekerjaan: str,
        lokasi: str,
        tahun: str,
        mengetahui: Optional[str] = None,
        nip_mengetahui: Optional[str] = None,
        konsultan: Optional[str] = None,
        tenaga_ahli: Optional[List[Tuple[str, str]]] = None,
        logo_placeholder: bool = True,
    ) -> None:
        """
        Add an Indonesian DED title block (per-sheet footer/header block).

        Layout (mirroring UIN Walisongo DED reference):
        - Left cell: logo placeholder + kegiatan/pekerjaan/lokasi metadata
        - Right cell: Mengetahui (PA) + Konsultan Perencana + Tenaga Ahli + Paraf

        Args:
            kegiatan: e.g. "Prasarana PTKIN"
            pekerjaan: e.g. "Perencanaan Pembangunan Landmark ..."
            lokasi: e.g. "Kampus 3 Universitas Islam Negeri"
            tahun: e.g. "Tahun 2022"
            mengetahui: Name of Pejabat Penandatangan (optional)
            nip_mengetahui: NIP of signatory (optional)
            konsultan: Consultant name (optional)
            tenaga_ahli: List of (discipline, name) tuples, e.g. [("Arsitektur","Timbul Hadiwidayat,ST,IAI")]
            logo_placeholder: If True, render a shaded "LOGO" cell; if False skip
        """
        tenaga_ahli = tenaga_ahli or []

        # Two-column borderless table
        table = self.document.add_table(rows=1, cols=2)
        table.autofit = True

        # Left cell: logo + metadata
        left = table.rows[0].cells[0]
        left.width = Inches(3.5)

        if logo_placeholder:
            logo_para = left.paragraphs[0]
            logo_para.alignment = WD_ALIGN_PARAGRAPH.CENTER
            logo_run = logo_para.add_run("[LOGO INSTANSI]")
            logo_run.font.bold = True
            logo_run.font.size = Pt(10)
            logo_run.font.color.rgb = RGBColor(150, 150, 150)
            self._apply_shading(logo_para, self.config["light_gray"])

        meta_lines = [
            ("KEGIATAN", kegiatan),
            ("PEKERJAAN", pekerjaan),
            ("LOKASI", lokasi),
            ("TAHUN", tahun),
        ]
        for label, value in meta_lines:
            p = left.add_paragraph()
            p.paragraph_format.space_after = Pt(1)
            r1 = p.add_run(f"{label}: ")
            r1.font.bold = True
            r1.font.size = Pt(8)
            r2 = p.add_run(value)
            r2.font.size = Pt(8)

        # Right cell: signatories
        right = table.rows[0].cells[1]
        right.width = Inches(3.0)

        if mengetahui:
            p = right.add_paragraph()
            p.alignment = WD_ALIGN_PARAGRAPH.CENTER
            r = p.add_run("Mengetahui,")
            r.font.size = Pt(8)
            r.font.italic = True
            p2 = right.add_paragraph()
            p2.alignment = WD_ALIGN_PARAGRAPH.CENTER
            r2 = p2.add_run(mengetahui)
            r2.font.bold = True
            r2.font.size = Pt(8)
            p3 = right.add_paragraph()
            p3.alignment = WD_ALIGN_PARAGRAPH.CENTER
            r3 = p3.add_run("Pejabat Penandatangan")
            r3.font.size = Pt(8)
            if nip_mengetahui:
                p4 = right.add_paragraph()
                p4.alignment = WD_ALIGN_PARAGRAPH.CENTER
                r4 = p4.add_run(f"NIP. {nip_mengetahui}")
                r4.font.size = Pt(8)

        if konsultan:
            p = right.add_paragraph()
            p.alignment = WD_ALIGN_PARAGRAPH.CENTER
            p.paragraph_format.space_before = Pt(6)
            r = p.add_run("KONSULTAN PERENCANA")
            r.font.bold = True
            r.font.size = Pt(8)

        if tenaga_ahli:
            # Two-column mini-table for discipline/name
            ta_table = right.add_table(rows=1, cols=2)
            ta_table.style = "Table Grid"
            header = ta_table.rows[0].cells
            header[0].text = "Disiplin"
            header[1].text = "Nama"
            for cell in header:
                for pr in cell.paragraphs:
                    for rr in pr.runs:
                        rr.font.bold = True
                        rr.font.size = Pt(7)

            # Add one body row per tenaga ahli entry
            for _ in tenaga_ahli:
                ta_table.add_row()
            for row_idx, (disc, name) in enumerate(tenaga_ahli, start=1):
                row = ta_table.rows[row_idx].cells
                row[0].text = disc
                row[1].text = name
                for cell in row:
                    for pr in cell.paragraphs:
                        for rr in pr.runs:
                            rr.font.size = Pt(7)

        # Paraf column
        p = right.add_paragraph()
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p.paragraph_format.space_before = Pt(6)
        r = p.add_run("PARAF")
        r.font.bold = True
        r.font.size = Pt(8)

        logger.debug("DED title block added")

    def add_ded_drawing_sheet(
        self,
        judul_gambar: str,
        skala: str,
        kode: str,
        no_gambar: str,
        jumlah_gambar: int = 1,
        disiplin: str = "",
        image_path: Optional[str] = None,
        image_width: float = 6.0,
        caption: Optional[str] = None,
    ) -> None:
        """
        Add a complete DED drawing sheet (one page per drawing).

        Layout:
        1. Optional drawing image (centered, large)
        2. Caption: JUDUL GAMBAR + SKALA
        3. DED title block (project metadata + signatories)
        4. Drawing register footer row: KODE | NO.GMR | JML.GMR | DISIPLIN

        Args:
            judul_gambar: Drawing title, e.g. "DENAH RENCANA"
            skala: Drawing scale, e.g. "1:150" or "NTS"
            kode: Drawing code, e.g. "00.04"
            no_gambar: Drawing number, e.g. "4"
            jumlah_gambar: Total sheets in set (default 1)
            disiplin: Discipline code: ARS / STR / MEP / LAND
            image_path: Optional path to drawing image
            image_width: Image width in inches
            caption: Optional extra caption text
        """
        # Image
        if image_path:
            try:
                self.add_image(image_path, width=image_width, align="center")
            except FileNotFoundError:
                # Graceful fallback: render placeholder box
                ph = self.document.add_paragraph()
                ph.alignment = WD_ALIGN_PARAGRAPH.CENTER
                run = ph.add_run(f"[GAMBAR: {judul_gambar}]\n(skala {skala})")
                run.font.italic = True
                run.font.size = Pt(12)
                run.font.color.rgb = RGBColor(150, 150, 150)
                self._apply_shading(ph, self.config["light_gray"])
        else:
            ph = self.document.add_paragraph()
            ph.alignment = WD_ALIGN_PARAGRAPH.CENTER
            run = ph.add_run(f"[GAMBAR: {judul_gambar}]\n(skala {skala})")
            run.font.italic = True
            run.font.size = Pt(12)
            run.font.color.rgb = RGBColor(150, 150, 150)
            self._apply_shading(ph, self.config["light_gray"])

        # Caption
        cap = self.document.add_paragraph()
        cap.alignment = WD_ALIGN_PARAGRAPH.CENTER
        cap.paragraph_format.space_before = Pt(6)
        cap.paragraph_format.space_after = Pt(6)
        r = cap.add_run(judul_gambar)
        r.font.bold = True
        r.font.size = Pt(12)
        r2 = cap.add_run(f"   SKALA {skala}")
        r2.font.size = Pt(10)
        if caption:
            p2 = self.document.add_paragraph()
            p2.alignment = WD_ALIGN_PARAGRAPH.CENTER
            r3 = p2.add_run(caption)
            r3.font.italic = True
            r3.font.size = Pt(9)

        # Title block (caller is expected to set project metadata on self._ded_project)
        project = getattr(self, "_ded_project", None)
        if project:
            self.add_ded_title_block(**project)

        # Register row: KODE | NO.GMR | JML.GMR | DISIPLIN
        reg = self.document.add_table(rows=1, cols=4)
        reg.style = "Table Grid"
        labels = ["KODE", "NO.GMR", "JML.GMR", "DISIPLIN"]
        values = [kode, no_gambar, str(jumlah_gambar), disiplin]
        for i, (lbl, val) in enumerate(zip(labels, values)):
            cell = reg.rows[0].cells[i]
            cell.text = f"{lbl}\n{val}"
            cell.width = Inches(1.5)
            for p in cell.paragraphs:
                p.alignment = WD_ALIGN_PARAGRAPH.CENTER
                for r in p.runs:
                    r.font.size = Pt(8)
                    if lbl == p.text.split("\n")[0]:
                        r.font.bold = True

        self.document.add_page_break()
        logger.info(f"DED drawing sheet added: {judul_gambar} ({skala})")

    def set_ded_project(
        self,
        kegiatan: str,
        pekerjaan: str,
        lokasi: str,
        tahun: str,
        mengetahui: Optional[str] = None,
        nip_mengetahui: Optional[str] = None,
        konsultan: Optional[str] = None,
        tenaga_ahli: Optional[List[Tuple[str, str]]] = None,
    ) -> None:
        """
        Set project metadata that will be reused on every subsequent
        add_ded_drawing_sheet() call.
        """
        self._ded_project = {
            "kegiatan": kegiatan,
            "pekerjaan": pekerjaan,
            "lokasi": lokasi,
            "tahun": tahun,
            "mengetahui": mengetahui,
            "nip_mengetahui": nip_mengetahui,
            "konsultan": konsultan,
            "tenaga_ahli": tenaga_ahli or [],
            "logo_placeholder": True,
        }

    def add_ded_legend(self, notasi_items: List[Tuple[str, str]]) -> None:
        """
        Add a NOTASI | KETERANGAN legend table (Indonesian drawing convention).

        Args:
            notasi_items: List of (notation, description) tuples
        """
        table = self.document.add_table(rows=len(notasi_items) + 1, cols=2)
        table.style = "Light Grid Accent 1"

        # Header
        header = table.rows[0].cells
        header[0].text = "NOTASI"
        header[1].text = "KETERANGAN"
        for cell in header:
            self._shade_cell(cell, self.config["primary_color"])
            for p in cell.paragraphs:
                for r in p.runs:
                    r.font.bold = True
                    r.font.size = Pt(9)
                    r.font.color.rgb = RGBColor(255, 255, 255)

        # Body
        for row_idx, (notasi, ket) in enumerate(notasi_items, start=1):
            cells = table.rows[row_idx].cells
            cells[0].text = notasi
            cells[1].text = ket
            for cell in cells:
                for p in cell.paragraphs:
                    for r in p.runs:
                        r.font.size = Pt(9)
                        r.font.name = "Calibri"

        logger.info(f"DED legend added: {len(notasi_items)} items")

    def add_ded_material_table(
        self,
        headers: List[str],
        rows: List[List[str]],
        title: Optional[str] = None,
    ) -> None:
        """
        Add a material / specification / BOQ table for DED.

        Args:
            headers: Column headers
            rows: List of rows (each a list of strings)
            title: Optional table title
        """
        if title:
            p = self.document.add_paragraph()
            p.paragraph_format.space_before = Pt(8)
            r = p.add_run(title)
            r.font.bold = True
            r.font.size = Pt(11)
            self._apply_color(r, self.config["primary_color"])

        table = self.document.add_table(rows=len(rows) + 1, cols=len(headers))
        table.style = "Light Grid Accent 1"

        # Header
        for i, h in enumerate(headers):
            cell = table.rows[0].cells[i]
            cell.text = h
            self._shade_cell(cell, self.config["primary_color"])
            for p in cell.paragraphs:
                for r in p.runs:
                    r.font.bold = True
                    r.font.size = Pt(9)
                    r.font.color.rgb = RGBColor(255, 255, 255)

        # Body
        for row_idx, row_data in enumerate(rows, start=1):
            cells = table.rows[row_idx].cells
            for col_idx, val in enumerate(row_data):
                cells[col_idx].text = str(val)
                for p in cells[col_idx].paragraphs:
                    for r in p.runs:
                        r.font.size = Pt(9)

        logger.info(f"DED material table added: {len(rows)} rows x {len(headers)} cols")

    def add_ded_cover(
        self,
        main_title: str,
        subtitle: Optional[str] = None,
        kegiatan: Optional[str] = None,
        pekerjaan: Optional[str] = None,
        lokasi: Optional[str] = None,
        tahun: Optional[str] = None,
        instansi: Optional[str] = None,
        logo_placeholder: bool = True,
    ) -> None:
        """
        Add an Indonesian DED cover page.

        Layout mirrors Indonesian government/consultant cover:
        - Top: [LOGO INSTANSI]
        - Center: INSTANSI name (all caps)
        - Main title: DETAIL ENGINEERING DESIGN (DED)
        - Subtitle: PEKERJAAN / description
        - Bottom: kegiatan, lokasi, tahun
        """
        # Top spacing
        for _ in range(2):
            self.document.add_paragraph()

        # Logo placeholder
        if logo_placeholder:
            logo_para = self.document.add_paragraph()
            logo_para.alignment = WD_ALIGN_PARAGRAPH.CENTER
            logo_run = logo_para.add_run("[LOGO INSTANSI]")
            logo_run.font.bold = True
            logo_run.font.size = Pt(14)
            logo_run.font.color.rgb = RGBColor(150, 150, 150)
            self._apply_shading(logo_para, self.config["light_gray"])

        # Instansi
        if instansi:
            p = self.document.add_paragraph()
            p.alignment = WD_ALIGN_PARAGRAPH.CENTER
            r = p.add_run(instansi.upper())
            r.font.bold = True
            r.font.size = Pt(14)
            r.font.name = "Times New Roman"

        # Spacer
        self.document.add_paragraph()

        # Main title
        p = self.document.add_paragraph()
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        r = p.add_run(main_title)
        r.font.bold = True
        r.font.size = Pt(22)
        r.font.name = "Times New Roman"
        self._apply_color(r, self.config["primary_color"])

        # Subtitle / pekerjaan
        if subtitle or pekerjaan:
            p = self.document.add_paragraph()
            p.alignment = WD_ALIGN_PARAGRAPH.CENTER
            r = p.add_run(subtitle or pekerjaan or "")
            r.font.size = Pt(12)
            r.font.name = "Times New Roman"

        # Spacer
        for _ in range(3):
            self.document.add_paragraph()

        # Bottom metadata
        meta_items = []
        if kegiatan:
            meta_items.append(("KEGIATAN", kegiatan))
        if pekerjaan:
            meta_items.append(("PEKERJAAN", pekerjaan))
        if lokasi:
            meta_items.append(("LOKASI", lokasi))
        if tahun:
            meta_items.append(("TAHUN", tahun))

        for label, value in meta_items:
            p = self.document.add_paragraph()
            p.alignment = WD_ALIGN_PARAGRAPH.CENTER
            r1 = p.add_run(f"{label}: ")
            r1.font.bold = True
            r1.font.size = Pt(10)
            r2 = p.add_run(value)
            r2.font.size = Pt(10)
            r2.font.name = "Times New Roman"

        self.document.add_page_break()
        self._has_cover = True
        logger.info(f"DED cover page added: {main_title}")

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
