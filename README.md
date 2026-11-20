# DID — Design Instructions & Detail Engineering Design (DED) Document Engine

**DID** adalah skill + Python engine untuk menghasilkan dokumen desain teknis profesional dalam format **Microsoft Word (.docx)**. Kini diperluas dengan kemampuan **DED (Detail Engineering Design)** mengikuti konvensi konsultan perencana Indonesia.

> **Dua mode dalam satu engine:**
> - **DID (produk/desain)** — design system, komponen, guideline UI/UX, arsitektur, interior, 3D, grafis
> - **DED (konstruksi/engineering)** — gambar kerja, denah, tampak, potongan, detail, struktur, MEP, landscape, RAB

## Fitur

### DID (Design Instructions Document)
- Cover page dengan branding
- Auto Table of Contents
- Heading hierarchy (H1–H3)
- Tabel profesional, list, gambar + caption, code block, highlight box
- Footer dengan page numbering
- Discipline formatter: `architecture`, `interior`, `graphic`, `3d`, `uiux`

### DED (Detail Engineering Design)
- **Cover ala instansi Indonesia** (`add_ded_cover`) — logo placeholder, instansi, kegiatan, pekerjaan, lokasi, tahun
- **Daftar Gambar** register (`add_daftar_gambar`) — `NO | KODE | JUDUL | SKALA | JML | DISIPLIN`
- **Drawing sheet per halaman** (`add_ded_drawing_sheet`) — gambar + caption + title block + register footer `KODE | NO.GMR | JML.GMR | DISIPLIN`
- **Title block konsisten** (`set_ded_project` + `add_ded_title_block`) — logo, metadata proyek, blok *Mengetahui* (Pejabat Penandatangan + NIP), *Konsultan Perencana*, tabel *Tenaga Ahli* per disiplin, kolom *Paraf*
- **Legend notasi** (`add_ded_legend`) — tabel `NOTASI | KETERANGAN` untuk material finish
- **Tabel material/RAB/spesifikasi** (`add_ded_material_table`)
- **Discipline formatter DED**: `ded`, `construction`/`arsitektur`, `structural`/`struktur`, `mep`, `landscape`/`landscaping`
- **Skala SNI**: `1:150` siteplan, `1:100` denah, `1:50` tampak/detail, `1:20`–`1:25` detail & penulangan, `NTS` perspektif
- **Struktur bab DED Indonesia**: Identitas → Daftar Gambar → Site/Master → Hard/Soft Material + Vegetasi → Arsitektur per Zona → Struktur → MEP → Landscape → Visualisasi → RAB/Spesifikasi/Kuesioner

## Instalasi

```bash
pip install -r requirements.txt   # python-docx>=0.8.11, pillow, lxml, python-dotenv
cp .env.example .env              # opsional — kustomisasi font/warna/margin
```

## Quick Start

### DID — Design Instructions Document

```python
from utils.docx_generator import DIDDocumentGenerator

gen = DIDDocumentGenerator(title="Design Standards", author="Design Team")
gen.add_cover_page("My Design Standards", "1.0", subtitle="Professional Guide")
gen.add_table_of_contents()
gen.add_heading("Chapter 1: Design Principles", level=1)
gen.add_paragraph("Your content here...")
gen.add_footer_with_page_numbers()
gen.save("output/my_did.docx")
```

### DED — Detail Engineering Design

```python
from utils.docx_generator import DIDDocumentGenerator
from utils.design_formatter import FormatterFactory

fmt = FormatterFactory.get_formatter("ded")
gen = DIDDocumentGenerator(
    title="DED - Pembangunan Gedung",
    author="Konsultan Perencana",
    config={"primary_color": fmt.primary_color, "accent_color": fmt.accent_color},
)

gen.add_ded_cover(
    main_title="DETAIL ENGINEERING DESIGN (DED)",
    subtitle="PEKERJAAN PEMBANGUNAN GEDUNG",
    kegiatan="Pembangunan Infrastruktur",
    pekerjaan="Pembangunan Gedung Perpustakaan Daerah",
    lokasi="Kecamatan Contoh, Kabupaten Contoh",
    tahun="Tahun 2026",
    instansi="DINAS PEKERJAAN UMUM KABUPATEN CONTOH",
)

gen.set_ded_project(
    kegiatan="Pembangunan Infrastruktur",
    pekerjaan="Pembangunan Gedung Perpustakaan Daerah",
    lokasi="Kecamatan Contoh, Kabupaten Contoh",
    tahun="Tahun 2026",
    mengetahui="Drs. H. NAMA PEJABAT, M.Si",
    nip_mengetahui="197001011990011001",
    konsultan="PT. KONSULTAN PERENCANA",
    tenaga_ahli=[("Arsitektur", "Nama Ahli Arsitektur, ST, IAI"),
                ("Struktur", "Nama Ahli Struktur, ST")],
)

gen.add_daftar_gambar([
    {"no": 1, "kode": "00.01", "judul": "SITEPLAN", "skala": "1:150", "jumlah": 1, "disiplin": "ARS"},
    {"no": 2, "kode": "02.01", "judul": "DENAH KOLOM", "skala": "1:150", "jumlah": 1, "disiplin": "STR"},
])

gen.add_ded_drawing_sheet(
    judul_gambar="DENAH RENCANA",
    skala="1:150",
    kode="00.03",
    no_gambar="3",
    jumlah_gambar=28,
    disiplin="ARS",
    image_path="denah.png",   # opsional — None render placeholder
)

gen.add_ded_legend([("FIN.CAT DINDING PUTIH", "Cat putih matte")])
gen.add_footer_with_page_numbers("DED - Pembangunan Gedung")
gen.save("output/ded.docx")
```

## Menjalankan Contoh

```bash
# DID — contoh desain arsitektur & UI/UX
python examples/generate_sample_did.py

# DED — contoh Detail Engineering Design Indonesia
python examples/generate_sample_ded.py
# → output/sample_ded.docx  (28 sheet, ~45 KB)
```

## Struktur Proyek

```
DID/
├── SKILL.md                          # Skill definition + workflow (termasuk route DED)
├── README.md                         # File ini
├── ARCHITECTURE.md
├── QUICK_START.md / PACKAGING_GUIDE.md / DEPLOYMENT_GUIDE.md
├── CHANGELOG.md / CONTRIBUTING.md / LICENSE
├── requirements.txt / .env.example
├── utils/
│   ├── docx_generator.py             # DIDDocumentGenerator — DID + DED primitives
│   └── design_formatter.py           # 5 DID + 5 DED discipline formatters
├── references/
│   ├── 01..13-*.md                   # DID intelligence layers
│   └── 14-templates-and-examples.md  # DID templates + Indonesian DED Master Template
├── examples/
│   ├── generate_sample_did.py        # Contoh DID arsitektur + UI/UX
│   └── generate_sample_ded.py        # Contoh DED lengkap (28 sheet)
└── docs/
    ├── GETTING_STARTED.md / API_REFERENCE.md / EXAMPLES.md / FAQ.md
```

## API DED (ringkas)

```python
add_ded_cover(main_title, subtitle, kegiatan, pekerjaan, lokasi, tahun, instansi, logo_placeholder=True)
set_ded_project(kegiatan, pekerjaan, lokasi, tahun, mengetahui, nip_mengetahui, konsultan, tenaga_ahli)
add_daftar_gambar(rows=[{no, kode, judul, skala, jumlah, disiplin}])
add_ded_drawing_sheet(judul_gambar, skala, kode, no_gambar, jumlah_gambar, disiplin, image_path=None, image_width=6.0, caption=None)
add_ded_title_block(kegiatan, pekerjaan, lokasi, tahun, mengetahui, nip_mengetahui, konsultan, tenaga_ahli, logo_placeholder=True)
add_ded_legend(notasi_items=[(notasi, keterangan)])
add_ded_material_table(headers, rows, title=None)
```

## Referensi

- `references/14-templates-and-examples.md` § *Indonesian DED Master Template* — struktur bab, skala, contoh register/title block/legend
- `SKILL.md` § Layer 2 (Discipline Router) — DED sebagai first-class discipline
- `examples/generate_sample_ded.py` — runnable end-to-end

## Lisensi

Lihat `LICENSE`.
