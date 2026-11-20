"""
Design Discipline Formatters for DID DOCX Generation

Provides discipline-specific formatting rules and utilities for different
design disciplines (Architecture, Interior Design, Graphic Design, 3D Design, UI/UX).

Each formatter class contains styling rules, color palettes, and best practices
specific to that design discipline.

Classes:
    BaseDesignFormatter: Abstract base for all formatters
    ArchitecturalFormatter: For architectural documentation
    InteriorFormatter: For interior design documentation
    GraphicFormatter: For graphic design documentation
    3DFormatter: For 3D design documentation
    UIUXFormatter: For UI/UX design documentation
"""

from typing import Dict, Tuple, Optional, List, Any
from abc import ABC, abstractmethod
import logging


logger = logging.getLogger(__name__)


class BaseDesignFormatter(ABC):
    """
    Abstract base class for design discipline-specific formatters.

    Defines interface for discipline-specific styling, color palettes,
    and formatting guidelines.
    """

    def __init__(self, name: str):
        """
        Initialize base formatter.

        Args:
            name: Formatter name/discipline
        """
        self.name = name
        self.primary_color: Tuple[int, int, int] = (51, 51, 51)
        self.accent_color: Tuple[int, int, int] = (100, 100, 100)
        self.secondary_colors: List[Tuple[int, int, int]] = []
        self.styling_rules: Dict[str, Any] = {}

    @abstractmethod
    def get_color_palette(self) -> Dict[str, Tuple[int, int, int]]:
        """
        Get discipline-specific color palette.

        Returns:
            Dictionary mapping color names to RGB tuples
        """
        pass

    @abstractmethod
    def get_styling_guidelines(self) -> Dict[str, Any]:
        """
        Get discipline-specific styling guidelines.

        Returns:
            Dictionary containing formatting rules and best practices
        """
        pass

    @abstractmethod
    def get_section_structure(self) -> List[str]:
        """
        Get recommended section structure for this discipline.

        Returns:
            List of recommended top-level section titles
        """
        pass

    def get_config(self) -> Dict[str, Any]:
        """
        Get complete formatter configuration.

        Returns:
            Dictionary with colors, guidelines, and structure
        """
        return {
            "name": self.name,
            "primary_color": self.primary_color,
            "accent_color": self.accent_color,
            "secondary_colors": self.secondary_colors,
            "palette": self.get_color_palette(),
            "guidelines": self.get_styling_guidelines(),
            "sections": self.get_section_structure(),
        }


class ArchitecturalFormatter(BaseDesignFormatter):
    """
    Formatter for Architectural Design Instructions Documents.

    Specializes in:
    - Building codes and standards
    - Structural guidelines
    - Material specifications
    - Technical drawings
    - Construction details
    """

    def __init__(self):
        """Initialize Architectural formatter with professional palette."""
        super().__init__("Architectural Design")
        self.primary_color = (41, 128, 185)      # Professional blue
        self.accent_color = (52, 73, 94)          # Dark blue-gray
        self.secondary_colors = [
            (149, 165, 166),    # Light gray
            (22, 160, 133),     # Teal
            (241, 196, 15),     # Gold
        ]

    def get_color_palette(self) -> Dict[str, Tuple[int, int, int]]:
        """Return architectural color palette."""
        return {
            "primary": self.primary_color,
            "accent": self.accent_color,
            "material_concrete": (127, 127, 127),
            "material_steel": (192, 192, 192),
            "material_wood": (139, 69, 19),
            "material_glass": (173, 216, 230),
            "safety": (220, 20, 60),
            "approved": (34, 139, 34),
        }

    def get_styling_guidelines(self) -> Dict[str, Any]:
        """Return architectural styling guidelines."""
        return {
            "font_family": "Calibri",
            "technical_sections": ["Design Standards", "Material Specifications", "Construction Details"],
            "include_scales": True,
            "include_dimensions": True,
            "safety_highlights": True,
            "code_references": True,
            "detail_drawings": True,
            "section_headings": {
                1: {"size": 24, "bold": True, "color": "primary"},
                2: {"size": 16, "bold": True, "color": "accent"},
                3: {"size": 13, "bold": True, "color": "primary"},
            },
        }

    def get_section_structure(self) -> List[str]:
        """Return recommended section structure for architectural docs."""
        return [
            "Design Philosophy",
            "Building Codes and Standards",
            "Material Specifications",
            "Structural Guidelines",
            "Construction Details",
            "Quality Assurance",
            "Sustainability Requirements",
            "Fire Safety and Egress",
            "Accessibility Requirements",
        ]


class InteriorFormatter(BaseDesignFormatter):
    """
    Formatter for Interior Design Instructions Documents.

    Specializes in:
    - Space planning
    - Material selections
    - Color schemes
    - Lighting design
    - Furniture specifications
    - Aesthetic guidelines
    """

    def __init__(self):
        """Initialize Interior Design formatter."""
        super().__init__("Interior Design")
        self.primary_color = (142, 68, 173)      # Purple
        self.accent_color = (155, 89, 182)       # Light purple
        self.secondary_colors = [
            (231, 76, 60),      # Red
            (241, 196, 15),     # Gold
            (52, 152, 219),     # Blue
            (46, 204, 113),     # Green
        ]

    def get_color_palette(self) -> Dict[str, Tuple[int, int, int]]:
        """Return interior design color palette."""
        return {
            "primary": self.primary_color,
            "accent": self.accent_color,
            "warm": (245, 176, 65),
            "cool": (52, 152, 219),
            "neutral_light": (236, 240, 241),
            "neutral_dark": (44, 62, 80),
            "highlight": (231, 76, 60),
            "accent_gold": (241, 196, 15),
        }

    def get_styling_guidelines(self) -> Dict[str, Any]:
        """Return interior design styling guidelines."""
        return {
            "font_family": "Calibri",
            "aesthetic_focus": True,
            "material_finish_descriptions": True,
            "color_swatches": True,
            "lighting_specifications": True,
            "furniture_selections": True,
            "spatial_flow": True,
            "section_headings": {
                1: {"size": 24, "bold": True, "color": "primary"},
                2: {"size": 16, "bold": True, "color": "accent"},
                3: {"size": 13, "bold": True, "color": "primary"},
            },
        }

    def get_section_structure(self) -> List[str]:
        """Return recommended section structure for interior design docs."""
        return [
            "Design Vision and Concept",
            "Space Planning",
            "Color Palette and Mood",
            "Material Selections",
            "Furniture and Fixtures",
            "Lighting Design",
            "Flooring Specifications",
            "Wall Treatments",
            "Accessories and Styling",
            "Implementation Timeline",
        ]


class GraphicFormatter(BaseDesignFormatter):
    """
    Formatter for Graphic Design Instructions Documents.

    Specializes in:
    - Branding guidelines
    - Typography systems
    - Logo usage
    - Color systems
    - Layout grids
    - Visual hierarchy
    """

    def __init__(self):
        """Initialize Graphic Design formatter."""
        super().__init__("Graphic Design")
        self.primary_color = (231, 76, 60)       # Bold red
        self.accent_color = (52, 152, 219)       # Blue
        self.secondary_colors = [
            (46, 204, 113),     # Green
            (241, 196, 15),     # Yellow
            (230, 126, 34),     # Orange
        ]

    def get_color_palette(self) -> Dict[str, Tuple[int, int, int]]:
        """Return graphic design color palette."""
        return {
            "primary": self.primary_color,
            "accent": self.accent_color,
            "secondary_green": (46, 204, 113),
            "secondary_yellow": (241, 196, 15),
            "secondary_orange": (230, 126, 34),
            "text_dark": (44, 62, 80),
            "text_light": (236, 240, 241),
            "error": (192, 57, 43),
        }

    def get_styling_guidelines(self) -> Dict[str, Any]:
        """Return graphic design styling guidelines."""
        return {
            "font_family": "Calibri",
            "typography_system": True,
            "grid_system": True,
            "logo_usage": True,
            "color_specifications": True,
            "hierarchy_examples": True,
            "do_dont_sections": True,
            "section_headings": {
                1: {"size": 24, "bold": True, "color": "primary"},
                2: {"size": 16, "bold": True, "color": "accent"},
                3: {"size": 13, "bold": True, "color": "primary"},
            },
        }

    def get_section_structure(self) -> List[str]:
        """Return recommended section structure for graphic design docs."""
        return [
            "Brand Vision",
            "Logo and Mark Usage",
            "Color System",
            "Typography Guidelines",
            "Visual Grid System",
            "Imagery and Photography Style",
            "Icon System",
            "Layout Principles",
            "Application Examples",
            "Common Mistakes",
        ]


class ThreeDFormatter(BaseDesignFormatter):
    """
    Formatter for 3D Design Instructions Documents.

    Specializes in:
    - Mesh specifications
    - Texture and material guidelines
    - Lighting setups
    - Animation principles
    - Export standards
    - Performance optimization
    """

    def __init__(self):
        """Initialize 3D Design formatter."""
        super().__init__("3D Design")
        self.primary_color = (52, 152, 219)      # Cyan blue
        self.accent_color = (41, 128, 185)       # Darker blue
        self.secondary_colors = [
            (46, 204, 113),     # Green
            (230, 126, 34),     # Orange
            (155, 89, 182),     # Purple
        ]

    def get_color_palette(self) -> Dict[str, Tuple[int, int, int]]:
        """Return 3D design color palette."""
        return {
            "primary": self.primary_color,
            "accent": self.accent_color,
            "positive": (46, 204, 113),
            "warning": (230, 126, 34),
            "technical": (52, 73, 94),
            "ambient": (236, 240, 241),
            "shadow": (44, 62, 80),
        }

    def get_styling_guidelines(self) -> Dict[str, Any]:
        """Return 3D design styling guidelines."""
        return {
            "font_family": "Calibri",
            "technical_specifications": True,
            "mesh_requirements": True,
            "texture_guidelines": True,
            "export_formats": True,
            "performance_targets": True,
            "animation_principles": True,
            "section_headings": {
                1: {"size": 24, "bold": True, "color": "primary"},
                2: {"size": 16, "bold": True, "color": "accent"},
                3: {"size": 13, "bold": True, "color": "primary"},
            },
        }

    def get_section_structure(self) -> List[str]:
        """Return recommended section structure for 3D design docs."""
        return [
            "3D Design Philosophy",
            "Mesh Specifications and Topology",
            "Texture and Material Guidelines",
            "Lighting and Rendering",
            "Animation Principles",
            "File Structure and Organization",
            "Export Standards and Formats",
            "Performance Optimization",
            "Quality Assurance Checklist",
        ]


class UIUXFormatter(BaseDesignFormatter):
    """
    Formatter for UI/UX Design Instructions Documents.

    Specializes in:
    - Component systems
    - Interaction patterns
    - Accessibility guidelines
    - Responsive design
    - User flows
    - Prototyping standards
    """

    def __init__(self):
        """Initialize UI/UX Design formatter."""
        super().__init__("UI/UX Design")
        self.primary_color = (46, 204, 113)      # Green
        self.accent_color = (52, 152, 219)       # Blue
        self.secondary_colors = [
            (231, 76, 60),      # Red
            (241, 196, 15),     # Yellow
            (155, 89, 182),     # Purple
        ]

    def get_color_palette(self) -> Dict[str, Tuple[int, int, int]]:
        """Return UI/UX color palette."""
        return {
            "primary": self.primary_color,
            "accent": self.accent_color,
            "success": (46, 204, 113),
            "warning": (230, 126, 34),
            "error": (231, 76, 60),
            "text_primary": (44, 62, 80),
            "text_secondary": (127, 140, 141),
            "background": (236, 240, 241),
        }

    def get_styling_guidelines(self) -> Dict[str, Any]:
        """Return UI/UX styling guidelines."""
        return {
            "font_family": "Calibri",
            "component_system": True,
            "interaction_states": True,
            "accessibility_wcag": True,
            "responsive_breakpoints": True,
            "user_flows": True,
            "animation_guidelines": True,
            "section_headings": {
                1: {"size": 24, "bold": True, "color": "primary"},
                2: {"size": 16, "bold": True, "color": "accent"},
                3: {"size": 13, "bold": True, "color": "primary"},
            },
        }

    def get_section_structure(self) -> List[str]:
        """Return recommended section structure for UI/UX docs."""
        return [
            "Design System Overview",
            "Visual Design Principles",
            "Component Library",
            "Interaction Patterns",
            "Responsive Design Guidelines",
            "Accessibility Requirements",
            "Typography and Text Styles",
            "Spacing and Layout",
            "Animation and Transitions",
            "User Flow Documentation",
            "Prototyping Standards",
        ]

class ConstructionFormatter(BaseDesignFormatter):
    """
    Formatter for Detail Engineering Design (DED) — Indonesian consultant convention.

    Covers architectural documentation for building/construction projects:
    site plans, floor plans, elevations, sections, details, material schedules.
    Typical discipline code: ARS.
    """

    def __init__(self):
        """Initialize Construction formatter."""
        super().__init__("Construction / DED")
        self.primary_color = (41, 128, 185)      # Professional blue
        self.accent_color = (52, 73, 94)          # Dark blue-gray
        self.secondary_colors = [
            (127, 127, 127),    # Concrete gray
            (139, 69, 19),      # Wood brown
            (46, 204, 113),     # Approved green
        ]

    def get_color_palette(self) -> Dict[str, Tuple[int, int, int]]:
        """Return construction/DED color palette."""
        return {
            "primary": self.primary_color,
            "accent": self.accent_color,
            "concrete": (127, 127, 127),
            "steel": (192, 192, 192),
            "brick": (178, 34, 34),
            "glass": (173, 216, 230),
            "approved": (34, 139, 34),
            "waterproofing": (30, 144, 255),
        }

    def get_styling_guidelines(self) -> Dict[str, Any]:
        """Return construction/DED styling guidelines."""
        return {
            "font_family": "Calibri",
            "drawing_scales": ["1:20", "1:25", "1:50", "1:100", "1:150", "NTS"],
            "include_title_block": True,
            "include_daftar_gambar": True,
            "include_legend_notasi": True,
            "include_dimensions": True,
            "material_callouts_inline": True,
            "indonesian_convention": True,
            "section_headings": {
                1: {"size": 24, "bold": True, "color": "primary"},
                2: {"size": 16, "bold": True, "color": "accent"},
                3: {"size": 13, "bold": True, "color": "primary"},
            },
        }

    def get_section_structure(self) -> List[str]:
        """Return recommended DED section structure (Indonesian convention)."""
        return [
            "Identitas Dokumen",
            "Daftar Gambar",
            "Site Plan dan Master Plan",
            "Denah Rencana Arsitektur",
            "Tampak dan Potongan",
            "Detail Arsitektur",
            "Denah Struktur dan Penulangan",
            "Detail Pondasi dan Sloof",
            "Denah MEP (Elektrikal/Plumbing)",
            "Landscape dan Vegetasi",
            "Visualisasi 3D",
            "RAB / Spesifikasi / Kuesioner",
        ]


class StructuralFormatter(BaseDesignFormatter):
    """
    Formatter for structural engineering drawings within a DED.

    Covers: column plans, beam plans, foundation plans, reinforcement details,
    sloof/ring beam. Typical discipline code: STR.
    """

    def __init__(self):
        """Initialize Structural formatter."""
        super().__init__("Structural Engineering")
        self.primary_color = (44, 62, 80)        # Dark slate
        self.accent_color = (127, 127, 127)      # Concrete gray
        self.secondary_colors = [
            (192, 192, 192),    # Steel
            (139, 69, 19),      # Wood formwork
            (41, 128, 185),     # Annotation blue
        ]

    def get_color_palette(self) -> Dict[str, Tuple[int, int, int]]:
        """Return structural color palette."""
        return {
            "primary": self.primary_color,
            "accent": self.accent_color,
            "concrete": (127, 127, 127),
            "steel": (105, 105, 105),
            "rebar": (178, 34, 34),
            "formwork": (210, 180, 140),
            "annotation": (41, 128, 185),
        }

    def get_styling_guidelines(self) -> Dict[str, Any]:
        """Return structural styling guidelines."""
        return {
            "font_family": "Calibri",
            "drawing_scales": ["1:20", "1:25", "1:50", "1:100", "1:150", "NTS"],
            "include_reinforcement_schedule": True,
            "include_concrete_grade": True,
            "include_steel_grade": True,
            "include_dimensions_mm": True,
            "section_headings": {
                1: {"size": 24, "bold": True, "color": "primary"},
                2: {"size": 16, "bold": True, "color": "accent"},
                3: {"size": 13, "bold": True, "color": "primary"},
            },
        }

    def get_section_structure(self) -> List[str]:
        """Return structural DED section structure."""
        return [
            "Denah Kolom",
            "Detail Penulangan Kolom",
            "Denah Balok",
            "Detail Penulangan Balok / Ring Balk",
            "Denah Pondasi",
            "Detail Pondasi",
            "Denah Sloof",
            "Detail Sloof",
            "Spesifikasi Beton dan Baja",
            "Perhitungan Struktur (jika ada)",
        ]


class MEPFormatter(BaseDesignFormatter):
    """
    Formatter for MEP (Mechanical, Electrical, Plumbing) drawings in a DED.

    Covers: electrical layouts, stop-contact plans, roof drainage, plumbing.
    Typical discipline code: MEP.
    """

    def __init__(self):
        """Initialize MEP formatter."""
        super().__init__("MEP Engineering")
        self.primary_color = (230, 126, 34)      # Orange (electrical convention)
        self.accent_color = (41, 128, 185)       # Blue (water)
        self.secondary_colors = [
            (155, 89, 182),     # Sewage purple
            (46, 204, 113),     # Approved green
            (44, 62, 80),       # Dark slate
        ]

    def get_color_palette(self) -> Dict[str, Tuple[int, int, int]]:
        """Return MEP color palette."""
        return {
            "primary": self.primary_color,
            "accent": self.accent_color,
            "electrical": (230, 126, 34),
            "water": (52, 152, 219),
            "sewage": (155, 89, 182),
            "gas": (231, 76, 60),
            "approved": (46, 204, 113),
        }

    def get_styling_guidelines(self) -> Dict[str, Any]:
        """Return MEP styling guidelines."""
        return {
            "font_family": "Calibri",
            "drawing_scales": ["1:20", "1:25", "1:50", "1:100", "1:150", "NTS"],
            "include_circuit_diagrams": True,
            "include_equipment_schedules": True,
            "include_wire_sizes": True,
            "include_pipe_diameters": True,
            "section_headings": {
                1: {"size": 24, "bold": True, "color": "primary"},
                2: {"size": 16, "bold": True, "color": "accent"},
                3: {"size": 13, "bold": True, "color": "primary"},
            },
        }

    def get_section_structure(self) -> List[str]:
        """Return MEP DED section structure."""
        return [
            "Denah Stop Kontak",
            "Denah Pencahayaan",
            "Denah Elektrikal (Power)",
            "Detail Panel dan Stop Kontak",
            "Denah Plumbing Air Bersih",
            "Denah Plumbing Air Kotor / Resap",
            "Denah Roof Drain",
            "Single Line Diagram",
            "Daftar Peralatan MEP",
        ]


class LandscapeFormatter(BaseDesignFormatter):
    """
    Formatter for landscape / site works drawings in a DED.

    Covers: vegetation plans, hard/soft material, paving, drainage, site details.
    Typical discipline code: LAND.
    """

    def __init__(self):
        """Initialize Landscape formatter."""
        super().__init__("Landscape / Site Works")
        self.primary_color = (39, 174, 96)       # Green
        self.accent_color = (44, 62, 80)         # Dark slate
        self.secondary_colors = [
            (127, 127, 127),    # Paving gray
            (139, 69, 19),      # Wood brown
            (52, 152, 219),     # Water blue
        ]

    def get_color_palette(self) -> Dict[str, Tuple[int, int, int]]:
        """Return landscape color palette."""
        return {
            "primary": self.primary_color,
            "accent": self.accent_color,
            "vegetation": (39, 174, 96),
            "paving": (127, 127, 127),
            "water": (52, 152, 219),
            "wood": (139, 69, 19),
            "soil": (160, 82, 45),
        }

    def get_styling_guidelines(self) -> Dict[str, Any]:
        """Return landscape styling guidelines."""
        return {
            "font_family": "Calibri",
            "drawing_scales": ["1:50", "1:100", "1:150", "NTS"],
            "include_plant_schedule": True,
            "include_hard_soft_material": True,
            "include_drilling_details": True,
            "section_headings": {
                1: {"size": 24, "bold": True, "color": "primary"},
                2: {"size": 16, "bold": True, "color": "accent"},
                3: {"size": 13, "bold": True, "color": "primary"},
            },
        }

    def get_section_structure(self) -> List[str]:
        """Return landscape DED section structure."""
        return [
            "Denah Rencana Vegetasi",
            "Indeks Rencana Vegetasi",
            "Denah Rencana Hard & Soft Material",
            "Indeks Rencana Hard & Soft Material",
            "Detail Paving dan Drainase",
            "Detail Lampu Taman",
            "Detail Furniture Taman",
            "Spesifikasi Tanaman",
        ]


class DEDFormatter(ConstructionFormatter):
    """
    Convenience alias: DED is produced primarily through the ConstructionFormatter.
    Provides the canonical Indonesian DED discipline entry point.
    """

    def __init__(self):
        super().__init__()
        self.name = "DED (Detail Engineering Design)"


class FormatterFactory:
    """
    Factory class for creating discipline-specific formatters.

    Provides simple interface for getting formatters by discipline name.
    """

    _formatters = {
        "architecture": ArchitecturalFormatter,
        "interior": InteriorFormatter,
        "graphic": GraphicFormatter,
        "3d": ThreeDFormatter,
        "uiux": UIUXFormatter,
        "ui/ux": UIUXFormatter,  # Alternative name
        "ded": DEDFormatter,
        "detail-engineering-design": DEDFormatter,
        "construction": ConstructionFormatter,
        "arsitektur": ConstructionFormatter,
        "structural": StructuralFormatter,
        "struktur": StructuralFormatter,
        "mep": MEPFormatter,
        "landscape": LandscapeFormatter,
        "landscaping": LandscapeFormatter,
    }

    @classmethod
    def get_formatter(cls, discipline: str) -> BaseDesignFormatter:
        """
        Get a formatter for the specified discipline.

        Args:
            discipline: Design discipline name (case-insensitive)

        Returns:
            Formatter instance for the discipline

        Raises:
            ValueError: If discipline not recognized

        Example:
            >>> formatter = FormatterFactory.get_formatter("architecture")
            >>> colors = formatter.get_color_palette()
        """
        discipline_lower = discipline.lower().strip()

        if discipline_lower not in cls._formatters:
            available = ", ".join(cls._formatters.keys())
            raise ValueError(
                f"Unknown discipline '{discipline}'. Available: {available}"
            )

        formatter_class = cls._formatters[discipline_lower]
        logger.info(f"Created formatter: {discipline}")
        return formatter_class()

    @classmethod
    def list_disciplines(cls) -> List[str]:
        """
        Get list of available disciplines.

        Returns:
            List of discipline names

        Example:
            >>> disciplines = FormatterFactory.list_disciplines()
            >>> print(f"Available: {', '.join(disciplines)}")
        """
        return list(cls._formatters.keys())

    @classmethod
    def get_all_formatters(cls) -> Dict[str, BaseDesignFormatter]:
        """
        Get all available formatters.

        Returns:
            Dictionary mapping discipline names to formatter instances

        Example:
            >>> formatters = FormatterFactory.get_all_formatters()
            >>> for name, formatter in formatters.items():
            ...     print(f"{name}: {formatter.get_color_palette()}")
        """
        # Canonical keys only (skip aliases pointing to same formatter class)
        seen = set()
        result = {}
        for name, formatter_class in cls._formatters.items():
            if formatter_class in seen:
                continue
            seen.add(formatter_class)
            result[name] = formatter_class()
        return result
