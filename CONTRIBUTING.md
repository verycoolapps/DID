# Contributing to DID (Document Intelligence Design)

Thank you for your interest in contributing to DID. We welcome contributions from all levels of experience.

## Code of Conduct

We are committed to providing a welcoming and inspiring community for all. All contributors are expected to:
- Be respectful and inclusive
- Welcome diverse perspectives
- Focus on constructive feedback
- Report violations confidentially

## How to Contribute

### Reporting Issues

Found a bug or have a feature request? Please open an issue with:
- Clear, descriptive title
- Detailed description of the problem
- Steps to reproduce (for bugs)
- Expected vs. actual behavior
- Python version and OS information
- Code samples if applicable

### Submitting Pull Requests

1. **Fork and Branch**
   - Fork the repository
   - Create a feature branch: `git checkout -b feature/your-feature`

2. **Development Setup**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -e .
   pip install -r requirements-dev.txt
   ```

3. **Make Your Changes**
   - Follow coding standards (see below)
   - Write/update tests for your changes
   - Update documentation as needed
   - Keep commits focused and atomic

4. **Testing**
   ```bash
   pytest tests/
   pytest --cov=src tests/  # With coverage
   ```

5. **Code Quality**
   ```bash
   black src/
   flake8 src/
   mypy src/
   ```

6. **Submit PR**
   - Push to your fork
   - Create pull request against `main`
   - Provide clear description of changes
   - Reference any related issues
   - Ensure CI/CD pipeline passes

## Development Setup

### Prerequisites
- Python 3.8+
- pip or conda
- Git

### Local Installation
```bash
git clone <repository-url>
cd did-skill
python -m venv venv
source venv/bin/activate
pip install -e .[dev]
```

### Running Tests
```bash
# All tests
pytest

# Specific test file
pytest tests/test_generator.py

# With coverage report
pytest --cov=src --cov-report=html tests/

# Watch mode (requires pytest-watch)
ptw
```

## Testing Requirements

All contributions must include:
- Unit tests for new functions
- Integration tests for new features
- Documentation of test cases
- Minimum 80% code coverage
- All existing tests must pass

### Writing Tests
```python
import pytest
from did import DIDDocumentGenerator

def test_generator_initialization():
    """Test generator initializes with valid config."""
    gen = DIDDocumentGenerator(design_discipline="UX")
    assert gen.discipline == "UX"

def test_invalid_discipline():
    """Test generator rejects invalid disciplines."""
    with pytest.raises(ValueError):
        DIDDocumentGenerator(design_discipline="INVALID")
```

## Coding Standards

### Python Style
- Follow PEP 8
- Use `black` for formatting: `black src/`
- Use `flake8` for linting: `flake8 src/`
- Use `mypy` for type hints: `mypy src/`

### Type Hints
All functions must include type hints:
```python
from typing import Dict, List, Optional
from pathlib import Path

def generate_document(
    discipline: str,
    sections: Optional[List[str]] = None,
    output_path: Optional[Path] = None
) -> Dict[str, str]:
    """Generate a design document."""
    ...
```

### Naming Conventions
- Classes: `PascalCase` (e.g., `DIDDocumentGenerator`)
- Functions/variables: `snake_case` (e.g., `generate_document`)
- Constants: `UPPER_SNAKE_CASE` (e.g., `MAX_RETRIES`)
- Private members: `_leading_underscore`

### Documentation Standards

#### Docstrings
Use Google-style docstrings:
```python
def generate_section(self, section_type: str) -> str:
    """Generate a single document section.
    
    Applies design discipline guidelines to create
    professionally formatted content.
    
    Args:
        section_type: Type of section (intro, body, conclusion)
    
    Returns:
        Formatted section content.
    
    Raises:
        ValueError: If section_type is not recognized.
    
    Example:
        >>> gen = DIDDocumentGenerator("UX")
        >>> gen.generate_section("intro")
    """
    ...
```

#### Comments
- Explain the "why", not the "what"
- Use block comments for complex logic
- Keep comments up-to-date with code

### File Organization
```
src/did/
├── __init__.py
├── generator.py          # Main generation logic
├── disciplines/          # Design discipline modules
│   ├── __init__.py
│   ├── base.py
│   ├── ux_design.py
│   ├── ui_design.py
│   └── ...
├── templates/            # Document templates
├── utils/                # Utility functions
└── config.py             # Configuration management
```

## Documentation Standards

### README Updates
If your change affects user documentation:
- Update relevant sections
- Include examples if behavior changed
- Keep it concise and actionable

### New Features
Document new features in:
- `docs/API_REFERENCE.md` - API changes
- `docs/EXAMPLES.md` - Usage examples
- `CHANGELOG.md` - Version history
- Docstrings in code

### API Documentation
Follow these guidelines:
- Clear parameter descriptions
- Complete return type documentation
- Real-world usage examples
- Error conditions and exceptions

## Pull Request Process

1. **Before submitting:**
   - Rebase on latest `main`
   - Run all tests locally
   - Run code quality checks
   - Update CHANGELOG.md

2. **PR Description Template:**
   ```markdown
   ## Description
   Brief explanation of changes.
   
   ## Type of Change
   - [ ] Bug fix
   - [ ] New feature
   - [ ] Documentation update
   
   ## Motivation and Context
   Why are these changes needed?
   
   ## Testing
   How was this tested?
   
   ## Checklist
   - [ ] Tests pass locally
   - [ ] Code quality checks pass
   - [ ] Documentation updated
   - [ ] CHANGELOG.md updated
   ```

3. **Review Process:**
   - Code review by maintainers
   - Automated CI/CD checks
   - Merge once approved and tests pass

## Commit Message Guidelines

Write clear, descriptive commit messages:

```
[scope]: Brief description under 50 characters

Longer explanation if needed, wrapped at 72 characters.
Explain what changed and why, not how.

Fixes #123
```

### Scope Examples
- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation
- `test`: Tests
- `refactor`: Code refactoring
- `perf`: Performance improvement

## Questions?

- **Documentation:** See [docs/](docs/) folder
- **Issues:** Check existing issues or create new one
- **Discussion:** Open a discussion thread

## Recognition

Contributors are recognized in:
- CHANGELOG.md (version history)
- GitHub contributors page
- Project documentation

Thank you for making DID better!
