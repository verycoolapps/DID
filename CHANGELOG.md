# Changelog

All notable changes to DID (Document Intelligence Design) are documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.1.0] - 2026-11-20

### Added — DED (Detail Engineering Design) Capability

#### New Discipline: DED
- **DED route** registered in `SKILL.md` Layer 2 (Discipline Router) as a first-class discipline
- **`DEDFormatter`** (alias of `ConstructionFormatter`) plus new formatters:
  - `ConstructionFormatter` / `arsitektur` — architectural DED (disiplin ARS)
  - `StructuralFormatter` / `struktur` — structural drawings & reinforcement (STR)
  - `MEPFormatter` / `mep` — electrical/plumbing layouts (MEP)
  - `LandscapeFormatter` / `landscaping` — vegetasi, hard/soft material (LAND)
- `FormatterFactory.get_all_formatters()` now deduplicates aliases

#### New DOCX Primitives (`utils/docx_generator.py`)
- `add_ded_cover(...)` — Indonesian instansi cover page
- `set_ded_project(...)` — reusable project metadata (kegiatan/pekerjaan/lokasi/tahun + signatories + tenaga ahli)
- `add_ded_title_block(...)` — per-sheet title block: logo, metadata, *Mengetahui* (PA + NIP), *Konsultan Perencana*, *Tenaga Ahli* table, *Paraf*
- `add_daftar_gambar(rows)` — drawing register table (`NO | KODE | JUDUL | SKALA | JML | DISIPLIN`)
- `add_ded_drawing_sheet(...)` — one-page drawing sheet (image + caption + title block + register footer + page break); graceful placeholder when no image
- `add_ded_legend(notasi_items)` — `NOTASI | KETERANGAN` legend table
- `add_ded_material_table(headers, rows, title)` — material/specification/RAB tables

#### Documentation
- `references/14-templates-and-examples.md` — new section **"Indonesian DED Master Template"** with full chapter structure, SNI scales, register/title-block/legend examples, and copy-paste Python usage
- `README.md` rewritten to present DID + DED dual capability
- `examples/generate_sample_ded.py` — runnable end-to-end DED sample producing `output/sample_ded_landmark.docx`

#### Reference
- Indonesian DED convention modeled on UIN Walisongo Landmark Kampus III DED (2022)

---

## [1.0.0] - 2024-11-17

#### Core Features
- **DIDDocumentGenerator**: Production-ready document generation engine
  - Supports 7 design disciplines (UX, UI, Product, Backend, Frontend, DevOps, QA)
  - Multi-section document architecture with customizable templates
  - Intelligent section routing based on design discipline
  - Comprehensive quality assurance pipeline

#### Design Disciplines
- **UX Design**: User research, personas, journeys, interaction patterns
- **UI Design**: Visual systems, component libraries, design tokens, accessibility
- **Product Design**: Strategy, roadmaps, feature specifications, go-to-market
- **Backend Design**: Architecture, API design, database schemas, security
- **Frontend Design**: Component architecture, state management, performance
- **DevOps Design**: Infrastructure, CI/CD, monitoring, disaster recovery
- **QA Design**: Test strategy, automation, quality metrics, risk assessment

#### Document Generation
- Automatic .docx file generation with professional formatting
- Multi-section document structure with customizable content
- Template-based content generation with discipline-specific guidelines
- Quality assurance checks before document generation
- Metadata and document properties management

#### Content Quality
- Design discipline validation
- Content coherence checking
- Professional structure enforcement
- Automatic content suggestions

#### API
- Python class-based API (`DIDDocumentGenerator`)
- Comprehensive method set for document creation
- Flexible configuration options
- Error handling with detailed feedback

#### Documentation
- README with quick start guide
- API reference documentation
- Usage examples for all disciplines
- Getting started guide
- Troubleshooting section

#### Testing
- Comprehensive unit test suite
- Integration tests for document generation
- Quality assurance validation tests
- Mock DOCX generation for testing
- Coverage reporting

#### Developer Experience
- Clear error messages with actionable solutions
- Input validation with helpful feedback
- Configuration validation
- Logging support for debugging

### Design Quality Standards
- **Professional Output**: Enterprise-grade document generation
- **Design Discipline Focus**: Each discipline has specific, targeted guidance
- **Quality Assurance**: Built-in validation for all generated content
- **Consistency**: Standardized section structures across disciplines
- **Flexibility**: Customizable templates and content

### Known Limitations (v1.0.0)

1. **Template Customization**: While templates are customizable, advanced template logic is limited
2. **Localization**: English language only in v1.0
3. **Multi-language Support**: Not included; planned for v1.2
4. **Document Styling**: Basic formatting; advanced styling available in v1.1
5. **Image Embedding**: Text-based content only; image support planned for v1.1
6. **Real-time Collaboration**: Document generation is single-user; multi-user features planned for v2.0
7. **Large Documents**: Performance may vary with documents exceeding 100 sections
8. **Advanced Analytics**: No built-in analytics; can be integrated externally

### Dependencies
- python-docx 0.8.11+ (DOCX generation)
- pydantic 2.0+ (Validation)
- pytest 7.0+ (Testing)

### Breaking Changes
None - Initial release

### Migration Guide
Not applicable - Initial release

---

## Future Roadmap

### v1.0.1 (Q1 2025) - Bug Fixes & Polish
- [ ] Address community-reported issues
- [ ] Performance optimization
- [ ] Enhanced error messages
- [ ] Documentation improvements

### v1.1 (Q2 2025) - Enhanced Styling & Features
- [ ] Advanced document styling options
- [ ] Image and diagram embedding
- [ ] Table of contents generation
- [ ] Index generation
- [ ] Cross-reference linking
- [ ] Custom footer/header support

### v1.2 (Q3 2025) - Localization & Internationalization
- [ ] Multi-language support (Spanish, French, German, Mandarin)
- [ ] Localized templates per discipline
- [ ] Currency and unit localization
- [ ] RTL language support

### v2.0 (Q4 2025) - Major Expansion
- [ ] Web UI for document generation
- [ ] Real-time collaboration features
- [ ] Team workspaces
- [ ] Document version control
- [ ] Export to multiple formats (PDF, Markdown, HTML)
- [ ] API server for remote document generation
- [ ] Advanced analytics and usage tracking

### v2.1+ (Future)
- [ ] Machine learning for content suggestions
- [ ] Automated design review and feedback
- [ ] Integration with popular design tools (Figma, Adobe XD)
- [ ] Template marketplace
- [ ] Enterprise features (SSO, audit logs, compliance)

---

## Semantic Versioning Explanation

DID follows Semantic Versioning (SEMVER) for version numbering:

### Format: MAJOR.MINOR.PATCH

- **MAJOR** (1.0.0): Incompatible API changes
  - Example: Removing a core method or changing method signatures
  - Requires code updates for users

- **MINOR** (1.1.0): New features, backward compatible
  - Example: Adding new methods or optional parameters
  - No breaking changes; existing code continues to work

- **PATCH** (1.0.1): Bug fixes, backward compatible
  - Example: Fixing a bug or improving performance
  - No new features; maintains existing API

### Pre-release Versions
- **Alpha** (1.0.0-alpha.1): Early development, unstable
- **Beta** (1.0.0-beta.1): Feature-complete, testing phase
- **Release Candidate** (1.0.0-rc.1): Ready for release, final testing

### Version Stability Guarantee

For v1.0.0 and beyond:
- API stability guaranteed within MAJOR versions
- Deprecation notices provided 2 versions in advance
- Clear migration guides for breaking changes
- Backward compatibility support for 2 previous MINOR versions

---

## Upgrade Guide

### Upgrading to v1.0.0
If migrating from earlier beta versions:

1. Install latest version:
   ```bash
   pip install --upgrade did-skill
   ```

2. Verify installation:
   ```bash
   python -c "from did import DIDDocumentGenerator; print(DIDDocumentGenerator.__version__)"
   ```

3. Review API changes in [docs/API_REFERENCE.md](docs/API_REFERENCE.md)

4. Test with existing code:
   ```bash
   pytest tests/
   ```

---

## Credits

DID v1.0.0 was created with contributions from:
- Design architecture and discipline guidance
- Testing and quality assurance
- Documentation and examples
- Community feedback and suggestions

---

## Support

- **Documentation**: [docs/](docs/)
- **Issues**: GitHub Issues
- **Discussions**: GitHub Discussions
- **Contributing**: [CONTRIBUTING.md](CONTRIBUTING.md)
