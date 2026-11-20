#!/usr/bin/env python3
"""
Sample DED (Detail Engineering Design) Document Generator — Indonesian consultant convention.

Generates a complete, small DED .docx package following the layout observed
in the UIN Walisongo DED reference (ppid.walisongo.ac.id). No real images are
required — drawing sheets render a shaded placeholder when no image is given.

Run:
    python examples/generate_sample_ded.py

Output:
    output/sample_ded_landmark.docx
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from utils.docx_generator import DIDDocumentGenerator
from utils.design_formatter import FormatterFactory
import logging


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)


def generate_sample_ded():
    """Build a small but complete DED document in Indonesian consultant style."""

    # DED formatter provides colors + recommended section structure
    formatter = FormatterFactory.get_formatter("ded")
    config = formatter.get_config()
    palette = config["palette"]

    generator = DIDDocumentGenerator(
        title="DED - Perencanaan Pembangunan Landmark Kampus III",
        author="Konsultan Perencana",
        config={
            "primary_color": palette["primary"],
            "accent_color": palette["accent"],
        },
    )

    # ------------------------------------------------------------------
    # 1. Cover (Indonesian government/consultant style)
    # ------------------------------------------------------------------
    generator.add_ded_cover(
        main_title="DETAIL ENGINEERING DESIGN (DED)",
        subtitle="PEKERJAAN PERENCANAAN PEMBANGUNAN LANDMARK",
        kegiatan="Prasarana PTKIN",
        pekerjaan="Perencanaan Pembangunan Landmark Kampus III",
        lokasi="Kampus 3 Universitas Islam Negeri",
        tahun="Tahun 2026",
        instansi="UNIVERSITAS ISLAM NEGERI (UIN) CONTOH",
        logo_placeholder=True,
    )

    # Set project metadata once — reused by every drawing sheet
    generator.set_ded_project(
        kegiatan="Prasarana PTKIN",
        pekerjaan="Perencanaan Pembangunan Landmark Kampus III",
        lokasi="Kampus 3 Universitas Islam Negeri",
        tahun="Tahun 2026",
        mengetahui="Drs. H. TEGUH SARWONO, M.Si",
        nip_mengetahui="196512141985031001",
        konsultan="PT. KONSULTAN PERENCANA",
        tenaga_ahli=[
            ("Arsitektur", "Timbul Hadiwidayat, ST, IAI"),
            ("Struktur", "Sabdho Tri Manggolo, ST"),
        ],
    )

    # ------------------------------------------------------------------
    # 2. Daftar Gambar (drawing register)
    # ------------------------------------------------------------------
    generator.add_heading("DAFTAR GAMBAR", level=1)
    generator.add_daftar_gambar([
        {"no": 1, "kode": "00.01", "judul": "SITEPLAN", "skala": "1:150", "jumlah": 1, "disiplin": "ARS"},
        {"no": 2, "kode": "00.02", "judul": "SITUASI", "skala": "1:150", "jumlah": 1, "disiplin": "ARS"},
        {"no": 3, "kode": "00.03", "judul": "DENAH RENCANA", "skala": "1:150", "jumlah": 1, "disiplin": "ARS"},
        {"no": 4, "kode": "00.04", "judul": "TAMPAK DEPAN", "skala": "1:150", "jumlah": 1, "disiplin": "ARS"},
        {"no": 5, "kode": "00.05", "judul": "TAMPAK BELAKANG", "skala": "1:150", "jumlah": 1, "disiplin": "ARS"},
        {"no": 6, "kode": "00.06", "judul": "TAMPAK KANAN", "skala": "1:100", "jumlah": 1, "disiplin": "ARS"},
        {"no": 7, "kode": "00.07", "judul": "TAMPAK KIRI", "skala": "1:100", "jumlah": 1, "disiplin": "ARS"},
        {"no": 8, "kode": "00.08", "judul": "POTONGAN 01", "skala": "1:150", "jumlah": 1, "disiplin": "ARS"},
        {"no": 9, "kode": "00.09", "judul": "DENAH RENCANA HARD & SOFT MATERIAL", "skala": "1:150", "jumlah": 1, "disiplin": "LAND"},
        {"no": 10, "kode": "00.10", "judul": "DENAH RENCANA VEGETASI", "skala": "1:150", "jumlah": 1, "disiplin": "LAND"},
        {"no": 11, "kode": "01.01", "judul": "DENAH SETTING GROUP", "skala": "1:150", "jumlah": 1, "disiplin": "ARS"},
        {"no": 12, "kode": "01.02", "judul": "TAMPAK & DETAIL SETTING GROUP", "skala": "1:50", "jumlah": 1, "disiplin": "ARS"},
        {"no": 13, "kode": "01.03", "judul": "DETAIL SCULPTURE LOGO UIN", "skala": "1:20", "jumlah": 1, "disiplin": "ARS"},
        {"no": 14, "kode": "01.04", "judul": "DETAIL KINCIR ANGIN SCULPTURE", "skala": "1:20", "jumlah": 1, "disiplin": "ARS"},
        {"no": 15, "kode": "01.05", "judul": "DETAIL PENDESTRIAN & PLAFON", "skala": "1:100", "jumlah": 1, "disiplin": "ARS"},
        {"no": 16, "kode": "01.06", "judul": "PERSPEKTIF 3D 1 - 5", "skala": "NTS", "jumlah": 5, "disiplin": "ARS"},
        {"no": 17, "kode": "02.01", "judul": "DENAH KOLOM", "skala": "1:150", "jumlah": 1, "disiplin": "STR"},
        {"no": 18, "kode": "02.02", "judul": "DETAIL PENULANGAN KOLOM", "skala": "1:20", "jumlah": 1, "disiplin": "STR"},
        {"no": 19, "kode": "02.03", "judul": "DENAH BALOK", "skala": "1:100", "jumlah": 1, "disiplin": "STR"},
        {"no": 20, "kode": "02.04", "judul": "DETAIL PENULANGAN RING BALK", "skala": "1:20", "jumlah": 1, "disiplin": "STR"},
        {"no": 21, "kode": "02.05", "judul": "DENAH PONDASI BATU KALI", "skala": "1:150", "jumlah": 1, "disiplin": "STR"},
        {"no": 22, "kode": "02.06", "judul": "DETAIL PONDASI", "skala": "1:20", "jumlah": 1, "disiplin": "STR"},
        {"no": 23, "kode": "02.07", "judul": "DENAH SLOOF", "skala": "1:150", "jumlah": 1, "disiplin": "STR"},
        {"no": 24, "kode": "02.08", "judul": "DETAIL SLOOF", "skala": "1:20", "jumlah": 1, "disiplin": "STR"},
        {"no": 25, "kode": "MEP-01.01", "judul": "DENAH STOP KONTAK", "skala": "1:150", "jumlah": 1, "disiplin": "MEP"},
        {"no": 26, "kode": "MEP-01.02", "judul": "DENAH ELEKTRIKAL 1", "skala": "1:150", "jumlah": 1, "disiplin": "MEP"},
        {"no": 27, "kode": "MEP-01.03", "judul": "DENAH ELEKTRIKAL 2 (DETAIL)", "skala": "1:25", "jumlah": 1, "disiplin": "MEP"},
        {"no": 28, "kode": "MEP-01.04", "judul": "DENAH ELEKTRIKAL 3", "skala": "1:150", "jumlah": 1, "disiplin": "MEP"},
    ])
    generator.add_page_break()

    # ------------------------------------------------------------------
    # 3. Master plan sheets (placeholder images)
    # ------------------------------------------------------------------
    generator.add_heading("SITE PLAN DAN MASTER PLAN", level=1)

    sheets = [
        ("SITEPLAN", "1:150", "00.01", "1", "ARS"),
        ("SITUASI", "1:150", "00.02", "1", "ARS"),
        ("DENAH RENCANA", "1:150", "00.03", "1", "ARS"),
        ("TAMPAK DEPAN", "1:150", "00.04", "1", "ARS"),
        ("TAMPAK BELAKANG", "1:150", "00.05", "1", "ARS"),
        ("TAMPAK KANAN", "1:100", "00.06", "1", "ARS"),
        ("TAMPAK KIRI", "1:100", "00.07", "1", "ARS"),
        ("POTONGAN 01", "1:150", "00.08", "1", "ARS"),
    ]
    for judul, skala, kode, no, dis in sheets:
        generator.add_ded_drawing_sheet(
            judul_gambar=judul,
            skala=skala,
            kode=kode,
            no_gambar=no,
            jumlah_gambar=28,
            disiplin=dis,
            caption=f"Denah utama {judul.lower()} — penempatan zona dan sirkulasi",
        )

    # ------------------------------------------------------------------
    # 4. Hard/Soft Material + Vegetasi + legend
    # ------------------------------------------------------------------
    generator.add_heading("DENAH RENCANA HARD & SOFT MATERIAL", level=1)
    generator.add_ded_drawing_sheet(
        judul_gambar="DENAH RENCANA HARD & SOFT MATERIAL LANDMARK",
        skala="1:150",
        kode="00.09",
        no_gambar="9",
        jumlah_gambar=28,
        disiplin="LAND",
        caption="Pembagian zona material keras dan lunak",
    )
    generator.add_paragraph("KETERANGAN NOTASI MATERIAL:")
    generator.add_ded_legend([
        ("FIN.CAT DINDING EXTERIOR WARNA PUTIH", "Cat dinding eksterior warna putih matte"),
        ("BATU TEMPEL BANJAR + FIN. STONE COAT", "Finishing batu tempel banjar dengan stone coat"),
        ("ORNAMEN GRC ISLAMI FIN.CAT EXTERIOR WARNA PUTIH", "Ornamen GRC motif Islami finishing cat putih"),
        ("PAS.BATA MERAH FIN.PLESTER ACI", "Pasangan bata merah finishing plester acian"),
        ("PLAT BETON T=10CM + FIN. BATU TEMPEL BANJAR & FIN.STONE COAT", "Plat beton setebal 10 cm finishing batu tempel banjar"),
    ])

    generator.add_page_break()
    generator.add_heading("DENAH RENCANA VEGETASI", level=1)
    generator.add_ded_drawing_sheet(
        judul_gambar="DENAH RENCANA VEGETASI LANDMARK",
        skala="1:150",
        kode="00.10",
        no_gambar="10",
        jumlah_gambar=28,
        disiplin="LAND",
        caption="Penempatan vegetasi dan area taman",
    )
    generator.add_ded_material_table(
        headers=["NO", "JENIS TANAMAN", "JUMLAH", "UKURAN POT", "KETERANGAN"],
        rows=[
            ["1", "Pohon Pucuk Merah (Ficus benjamina)", "12", "Ø60", "Tanaman peneduh"],
            ["2", "Palem Sawit (Licuala grandis)", "20", "Ø40", "Tanaman kolaborasi"],
            ["3", "Semak Bambu Kuning", "30", "P8", "Ground cover"],
        ],
        title="SPESIFIKASI TANAMAN",
    )
    generator.add_page_break()

    # ------------------------------------------------------------------
    # 5. Per-zone architecture — Setting Group example
    # ------------------------------------------------------------------
    generator.add_heading("DETAIL SETTING GROUP", level=1)
    generator.add_paragraph(
        "Zona Setting Group mencakup elemen monumen/logo UIN, sculpture, "
        "dan elemen pendukung. Denah, tampak, dan detail disajikan pada skala "
        "1:150 (denah), 1:50 (tampak/detail), dan 1:20 (detail elemen)."
    )

    generator.add_ded_drawing_sheet(
        judul_gambar="DENAH RENCANA SETTING GROUP",
        skala="1:150",
        kode="01.01",
        no_gambar="11",
        jumlah_gambar=28,
        disiplin="ARS",
        caption="Denah zona setting group dengan keterangan elevasi",
    )

    generator.add_ded_drawing_sheet(
        judul_gambar="TAMPAK DEPAN & SAMPING SETTING GROUP",
        skala="1:50",
        kode="01.02",
        no_gambar="12",
        jumlah_gambar=28,
        disiplin="ARS",
    )
    generator.add_ded_legend([
        ("CAT WARNA TEMBAGA MATTE", "Finishing cat warna tembaga matte"),
        ("CAT WARNA PUTIH MATTE", "Finishing cat warna putih matte"),
        ("CAT WARNA EMAS MATTE", "Finishing cat warna emas matte"),
        ("CAT WARNA HITAM MATTE", "Finishing cat warna hitam matte"),
        ("SIKU 50.50.5 FIN.ZINC CHROMATE", "Baja siku 50×50×5 finishing zinc chromate"),
    ])

    generator.add_ded_drawing_sheet(
        judul_gambar="DETAIL SCULPTURE LOGO UIN DEPAN & BELAKANG",
        skala="1:20",
        kode="01.03",
        no_gambar="13",
        jumlah_gambar=28,
        disiplin="ARS",
        caption="Detail sculpture logo UIN dengan material GRC",
    )
    generator.add_ded_legend([
        ("GRC BATU ANDESIT 20X40", "GRC dengan motif batu andesit ukuran 20×40 cm"),
        ("ORNAMEN GRC MOTIF ISLAMI", "Ornamen GRC dengan motif Islami"),
        ("LATER NAME WARNA TEMBAGA", "Later name/latar nama warna tembaga"),
    ])

    generator.add_ded_drawing_sheet(
        judul_gambar="DETAIL KINCIR ANGIN SCULPTURE LOGO UIN",
        skala="1:20",
        kode="01.04",
        no_gambar="14",
        jumlah_gambar=28,
        disiplin="ARS",
    )
    generator.add_page_break()

    # Pedestrian + visualisasi
    generator.add_heading("DETAIL PENDESTRIAN & PLAFON", level=1)
    generator.add_ded_drawing_sheet(
        judul_gambar="DENAH & DETAIL ISOMETRI PLAFOND PENDESTRIAN",
        skala="1:100",
        kode="01.05",
        no_gambar="15",
        jumlah_gambar=28,
        disiplin="ARS",
    )

    for i in range(1, 6):
        generator.add_ded_drawing_sheet(
            judul_gambar=f"PERSPEKTIF 3D {i}",
            skala="NTS",
            kode="01.06",
            no_gambar=str(15 + i),
            jumlah_gambar=28,
            disiplin="ARS",
            caption="Visualisasi perspektif 3D",
        )
    generator.add_page_break()

    # ------------------------------------------------------------------
    # 6. Structural drawings
    # ------------------------------------------------------------------
    generator.add_heading("STRUKTUR — DENAH DAN DETAIL PENULANGAN", level=1)

    structural_sheets = [
        ("DENAH KOLOM", "1:150", "02.01", "17"),
        ("DETAIL PENULANGAN KOLOM", "1:20", "02.02", "18"),
        ("DENAH BALOK", "1:100", "02.03", "19"),
        ("DETAIL PENULANGAN RING BALK", "1:20", "02.04", "20"),
        ("DENAH PONDASI BATU KALI", "1:150", "02.05", "21"),
        ("DETAIL PONDASI", "1:20", "02.06", "22"),
        ("DENAH SLOOF", "1:150", "02.07", "23"),
        ("DETAIL SLOOF", "1:20", "02.08", "24"),
    ]
    for judul, skala, kode, no in structural_sheets:
        generator.add_ded_drawing_sheet(
            judul_gambar=judul,
            skala=skala,
            kode=kode,
            no_gambar=no,
            jumlah_gambar=28,
            disiplin="STR",
        )
    generator.add_page_break()

    # ------------------------------------------------------------------
    # 7. MEP
    # ------------------------------------------------------------------
    generator.add_heading("MEP — DENAH ELEKTRIKAL", level=1)

    mep_sheets = [
        ("DENAH STOP KONTAK", "1:150", "MEP-01.01", "25"),
        ("DENAH ELEKTRIKAL 1", "1:150", "MEP-01.02", "26"),
        ("DENAH ELEKTRIKAL 2", "1:25", "MEP-01.03", "27"),
        ("DENAH ELEKTRIKAL 3", "1:150", "MEP-01.04", "28"),
    ]
    for judul, skala, kode, no in mep_sheets:
        generator.add_ded_drawing_sheet(
            judul_gambar=judul,
            skala=skala,
            kode=kode,
            no_gambar=no,
            jumlah_gambar=28,
            disiplin="MEP",
            caption="Denah instalasi listrik — stop kontak dan lampu",
        )
    generator.add_page_break()

    # ------------------------------------------------------------------
    # 8. RAB / Spesifikasi / Kuesioner
    # ------------------------------------------------------------------
    generator.add_heading("RAB / REKAPITULASI BIAYA", level=1)
    generator.add_paragraph(
        "Rekapitulasi biaya pekerjaan disajikan dalam format RAB (Rencana Anggaran "
        "Biaya) per item pekerjaan. Rincian volume dan harga satuan mengacu pada "
        "spesifikasi teknis pada bagian berikutnya."
    )
    generator.add_ded_material_table(
        headers=["NO", "URAIAN PEKERJAAN", "SATUAN", "VOLUME", "HARGA SATUAN", "JUMLAH"],
        rows=[
            ["1", "Galian pondasi batu kali", "m3", "120.00", "250,000", "30,000,000"],
            ["2", "Beton K-225 pondasi", "m3", "45.00", "750,000", "33,750,000"],
            ["3", "Penulangan kolom D13", "kg", "1,250", "18,000", "22,500,000"],
            ["4", "Pasangan bata merah 1:4", "m2", "380", "95,000", "36,100,000"],
            ["5", "Plester acian 1:3", "m2", "450", "45,000", "20,250,000"],
            ["6", "Cat tembok 2 lapis", "m2", "480", "35,000", "16,800,000"],
            ["7", "Paving block pedestrian", "m2", "620", "180,000", "111,600,000"],
            ["8", "Lampu taman LED + tiang", "buah", "24", "1,250,000", "30,000,000"],
        ],
        title="REKAPITULASI RAB (ILUSTRASI)",
    )

    generator.add_heading("SPESIFIKASI TEKNIS", level=1)
    generator.add_paragraph(
        "Spesifikasi teknis pekerjaan mengacu pada SNI yang berlaku dan "
        "ketentuan dalam dokumen ini. Material dan finishing mengikuti "
        "daftar gambar serta legend notasi pada masing-masing lembar."
    )
    generator.add_ded_material_table(
        headers=["NO", "ITEM", "SPESIFIKASI", "SATUAN"],
        rows=[
            ["1", "Beton", "K-225, slump 8-12 cm", "m3"],
            ["2", "Baja tulangan", "BJTS 280, diameter sesuai gambar", "kg"],
            ["3", "Bata merah", "Ukuran 20×10×5 cm, kuat tekan ≥15 N/mm2", "biji"],
            ["4", "Semen", "Semen portland tipe I/II", "kg"],
            ["5", "Pasir beton", "Pasir sungai/kali, gradasi sesuai SNI", "m3"],
            ["6", "Koral", "Koral 1x2, 2x3 sesuai gradasi", "m3"],
        ],
        title="SPESIFIKASI MATERIAL UTAMA",
    )

    generator.add_heading("KUESIONER / BERITA ACARA", level=1)
    generator.add_paragraph(
        "Berita acara penyerahan dokumen DED beserta tanggapan dan masukan "
        "dari Kuasa Pengguna Jasa (KPJ) dicatat dalam lembar terpisah."
    )

    # ------------------------------------------------------------------
    # Footer + save
    # ------------------------------------------------------------------
    generator.add_footer_with_page_numbers(
        text="DED - Perencanaan Pembangunan Landmark Kampus III"
    )

    output_path = generator.save("output/sample_ded_landmark.docx")
    print(f"\nDED document generated: {output_path}")
    print(f"Sections: {generator.get_summary()['section_count']}")
    print(f"Tables: {generator.get_summary()['table_count']}")
    return output_path


if __name__ == "__main__":
    generate_sample_ded()
