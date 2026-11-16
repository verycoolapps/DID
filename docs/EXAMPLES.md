# DID Examples

Comprehensive examples demonstrating DID capabilities.

## Table of Contents

1. [Basic Examples](#basic-examples)
2. [Discipline-Specific Examples](#discipline-specific-examples)
3. [Advanced Examples](#advanced-examples)
4. [Error Handling Examples](#error-handling-examples)
5. [Batch Processing](#batch-processing)

---

## Basic Examples

### Example 1: Minimal Document Generation

Create a document with just 3 lines of code.

```python
from did import DIDDocumentGenerator

gen = DIDDocumentGenerator("UX", "My Project")
doc_path = gen.generate_document()
print(f"Done! Document: {doc_path}")
```

**Output:**
```
Done! Document: /current/dir/My Project_UX.docx
```

---

### Example 2: Check Document Quality

Generate and inspect quality metrics.

```python
from did import DIDDocumentGenerator

gen = DIDDocumentGenerator("Backend", "API Service")

# Check quality before generation
pre_report = gen.validate_content()
print(f"Pre-generation score: {pre_report.score}/100")

if pre_report.passed:
    doc_path = gen.generate_document()
    
    # Check final quality
    final_report = gen.get_quality_report()
    print(f"Final score: {final_report.score}/100")
    print(f"Coherence: {final_report.coherence_score}/100")
    print(f"Structure: {final_report.structure_score}/100")
```

---

### Example 3: Custom Output Location

Save documents to a specific directory.

```python
from did import DIDDocumentGenerator
from pathlib import Path

# Create output directory
output_dir = Path.home() / "Documents" / "Design Documents"
output_dir.mkdir(parents=True, exist_ok=True)

# Generate document there
gen = DIDDocumentGenerator("UI", "Design System")
doc_path = gen.generate_document(output_path=str(output_dir))

print(f"Saved to: {doc_path}")
```

---

## Discipline-Specific Examples

### Example 4: UX Design Document

Complete UX design document with custom research content.

```python
from did import DIDDocumentGenerator

gen = DIDDocumentGenerator("UX", "Mobile App Redesign")

# Customize research section with actual findings
gen.customize_section(
    "Research & Discovery",
    """
    Research Methods Used:
    - User interviews (n=12)
    - Usability testing
    - Competitive analysis
    
    Key Findings:
    - Users struggle with onboarding (82% drop-off)
    - Navigation hierarchy unclear (avg. 3.2 taps to goal)
    - Mobile experience disconnected from desktop
    
    Recommendations:
    - Streamline onboarding to 3 steps
    - Redesign information architecture
    - Ensure responsive design consistency
    """
)

# Generate document
doc_path = gen.generate_document()

# Check generated sections
sections_info = gen.get_sections_info()
for section_name, info in sections_info.items():
    print(f"{section_name}: {info['word_count']} words, Quality: {info['quality_score']}/100")
```

---

### Example 5: Backend Design Document

Backend architecture and API design document.

```python
from did import DIDDocumentGenerator

gen = DIDDocumentGenerator("Backend", "Payment Processing Service")

# Customize system architecture
gen.customize_section(
    "System Architecture",
    """
    Architecture Overview:
    - Microservices architecture
    - 5 core services: Auth, Payment, Ledger, Notification, Settlement
    - PostgreSQL for transactional data
    - Redis for caching
    - RabbitMQ for event streaming
    - Kubernetes for orchestration
    
    Key Components:
    - API Gateway (nginx reverse proxy)
    - Service mesh (Istio)
    - Distributed logging (ELK stack)
    - Metrics collection (Prometheus + Grafana)
    """
)

# Customize API design
gen.customize_section(
    "API Design",
    """
    REST API Standards:
    - Base URL: api.example.com/v1
    - JSON request/response
    - Bearer token authentication
    - Versioning: semantic versioning
    
    Key Endpoints:
    - POST /payments - Initiate payment
    - GET /payments/{id} - Get payment status
    - POST /refunds - Process refund
    - GET /reports - Payment reports
    """
)

doc_path = gen.generate_document()
print(f"Backend design document: {doc_path}")
```

---

### Example 6: Product Design Document

Product strategy and feature specification.

```python
from did import DIDDocumentGenerator

gen = DIDDocumentGenerator("Product", "AI Assistant Launch")

# Customize strategy
gen.customize_section(
    "Strategy",
    """
    Vision:
    Make AI assistance accessible to every professional.
    
    Target Market:
    - Knowledge workers (5M+ potential users)
    - Enterprise (B2B SaaS focus)
    - Focus on healthcare and finance first
    
    Success Metrics:
    - 100K DAU by month 6
    - 80% feature adoption
    - 4.5+ app store rating
    - $1M ARR by end of year
    """
)

# Customize roadmap
gen.customize_section(
    "Roadmap",
    """
    Q1 2024: MVP Release
    - Core chat interface
    - 5 specialized models
    - Basic API
    
    Q2 2024: Enterprise Features
    - Team collaboration
    - Admin console
    - SSO integration
    
    Q3 2024: Advanced Capabilities
    - Custom model fine-tuning
    - Advanced analytics
    - Workflow automation
    """
)

doc_path = gen.generate_document()
metadata = gen.get_document_metadata()
print(f"Product document: {doc_path}")
print(f"Sections: {metadata['section_count']}, Pages: {metadata['estimated_pages']}")
```

---

### Example 7: Frontend Architecture Document

Frontend system design and component architecture.

```python
from did import DIDDocumentGenerator

gen = DIDDocumentGenerator("Frontend", "React App Architecture")

# Customize architecture
gen.customize_section(
    "Component Architecture",
    """
    Directory Structure:
    src/
    ├── components/
    │   ├── common/           # Reusable components
    │   ├── features/         # Feature-specific
    │   └── layouts/          # Layout components
    ├── hooks/                # Custom React hooks
    ├── contexts/             # Context providers
    ├── services/             # API services
    ├── utils/                # Utilities
    └── styles/               # Global styles
    
    Key Decisions:
    - React 18 with Concurrent Features
    - TypeScript for type safety
    - Zustand for state management
    - React Router v6 for navigation
    - TailwindCSS for styling
    """
)

# Customize state management
gen.customize_section(
    "State Management",
    """
    State Architecture:
    - Zustand for global app state
    - React Query for server state
    - Local component state for UI
    
    Data Flow:
    - User actions → Zustand store → API call
    - API response → React Query cache
    - Cache invalidation on mutations
    
    Performance Optimizations:
    - Code splitting with React.lazy
    - Memoization with useMemo/useCallback
    - Virtual scrolling for large lists
    """
)

doc_path = gen.generate_document()
print(f"Frontend architecture: {doc_path}")
```

---

### Example 8: DevOps Infrastructure Document

Infrastructure and deployment design.

```python
from did import DIDDocumentGenerator

gen = DIDDocumentGenerator("DevOps", "Kubernetes Migration")

# Customize infrastructure
gen.customize_section(
    "Infrastructure Design",
    """
    Cloud Platform: AWS
    
    Compute:
    - EKS for Kubernetes management
    - 3-node production cluster (m5.xlarge)
    - 1-node staging cluster (m5.large)
    - Auto-scaling (2-10 nodes)
    
    Database:
    - RDS Aurora PostgreSQL (Multi-AZ)
    - Read replicas for scaling
    - Automated backups (30-day retention)
    - Encryption at rest and in transit
    
    Storage:
    - S3 for object storage
    - CloudFront CDN
    - Versioning enabled
    - Cross-region replication
    
    Networking:
    - VPC with public/private subnets
    - NAT gateways for outbound traffic
    - Security groups and NACLs
    - Application Load Balancer
    """
)

# Customize CI/CD
gen.customize_section(
    "CI/CD Pipeline",
    """
    GitHub Actions Workflow:
    
    1. Build Stage (5 min)
       - Run tests
       - Lint code
       - Build Docker image
    
    2. Push Stage (2 min)
       - Push to ECR
       - Create image tags
       - Trigger deployment
    
    3. Deploy Stage (10 min)
       - Deploy to staging
       - Run smoke tests
       - Manual approval required
       - Deploy to production (blue-green)
    
    4. Monitor Stage
       - Health checks
       - Performance metrics
       - Automated rollback if needed
    
    Deployment Frequency: 10+ per day
    Lead Time: < 1 hour
    MTTR: < 15 minutes
    """
)

doc_path = gen.generate_document()
print(f"DevOps design: {doc_path}")
```

---

### Example 9: QA Testing Strategy Document

Quality assurance and testing plan.

```python
from did import DIDDocumentGenerator

gen = DIDDocumentGenerator("QA", "Mobile App Testing Strategy")

# Customize test strategy
gen.customize_section(
    "Test Strategy",
    """
    Testing Pyramid:
    
    Unit Tests (60%)
    - 1200+ tests
    - Coverage: 85%
    - Tools: Jest, Vitest
    - CI: Run on every commit
    
    Integration Tests (25%)
    - 500+ tests
    - API integration
    - Database integration
    - Tools: Supertest, testcontainers
    - CI: Run on PR
    
    E2E Tests (15%)
    - 300+ tests
    - User workflows
    - Cross-browser testing
    - Tools: Playwright, Cypress
    - CI: Run nightly + pre-release
    
    Test Environments:
    - Local development
    - Staging (pre-production)
    - Production (canary testing)
    """
)

# Customize quality metrics
gen.customize_section(
    "Quality Metrics",
    """
    Defect Metrics:
    - Target: < 1 critical bug / release
    - Target: < 5 high-severity bugs / release
    - Regression rate: < 2%
    
    Performance Metrics:
    - Page load: < 2 seconds (p95)
    - API response: < 200ms (p99)
    - Mobile FCP: < 1.8s
    
    Release Metrics:
    - Deployment frequency: 10+ per day
    - Lead time for changes: < 1 hour
    - Mean time to recovery: < 15 minutes
    - Change failure rate: < 15%
    """
)

doc_path = gen.generate_document()
print(f"QA testing document: {doc_path}")
```

---

## Advanced Examples

### Example 10: Batch Processing Multiple Documents

Generate documents for all disciplines.

```python
from did import DIDDocumentGenerator
from pathlib import Path

# Output directory
output_dir = Path.home() / "Documents" / "Design Docs"
output_dir.mkdir(parents=True, exist_ok=True)

# All disciplines
disciplines = ["UX", "UI", "Product", "Backend", "Frontend", "DevOps", "QA"]

# Generate a document for each discipline
documents = {}

for discipline in disciplines:
    print(f"Generating {discipline}...")
    
    gen = DIDDocumentGenerator(
        design_discipline=discipline,
        project_name="Complete Project Design"
    )
    
    # Generate document
    doc_path = gen.generate_document(output_path=str(output_dir))
    
    # Store path and quality score
    quality = gen.get_quality_report()
    documents[discipline] = {
        "path": doc_path,
        "quality": quality.score
    }
    
    print(f"  ✓ {discipline} (Quality: {quality.score}/100)")

# Summary
print("\nGeneration complete!")
print(f"Documents saved to: {output_dir}")
print("\nQuality Summary:")
for discipline, info in documents.items():
    quality_status = "✓" if info['quality'] >= 75 else "⚠"
    print(f"  {quality_status} {discipline}: {info['quality']}/100")
```

---

### Example 11: Conditional Customization

Customize sections based on project type.

```python
from did import DIDDocumentGenerator

def create_design_document(discipline, project_name, project_type="standard"):
    gen = DIDDocumentGenerator(discipline, project_name)
    
    if project_type == "startup":
        # Lean approach
        gen.customize_section(
            "Next Steps",
            "MVP launch in 4 weeks. Focus on core user flows."
        )
    elif project_type == "enterprise":
        # Formal approach
        gen.customize_section(
            "Next Steps",
            """
            Phase 1 (Weeks 1-4): Stakeholder alignment
            Phase 2 (Weeks 5-12): Design refinement
            Phase 3 (Weeks 13-20): Development
            Phase 4 (Weeks 21+): Testing and launch
            """
        )
    
    return gen.generate_document()

# Generate documents for different project types
startup_doc = create_design_document("Product", "AI Startup", "startup")
enterprise_doc = create_design_document("Product", "BigCorp Initiative", "enterprise")

print(f"Startup doc: {startup_doc}")
print(f"Enterprise doc: {enterprise_doc}")
```

---

### Example 12: Quality-Driven Generation

Regenerate until quality threshold is met.

```python
from did import DIDDocumentGenerator
from did.exceptions import QualityThresholdError

def generate_with_quality_check(discipline, project_name, min_quality=80):
    gen = DIDDocumentGenerator(discipline, project_name)
    
    max_attempts = 3
    for attempt in range(1, max_attempts + 1):
        print(f"Attempt {attempt}...")
        
        try:
            # Try to generate
            doc_path = gen.generate_document()
            report = gen.get_quality_report()
            
            if report.score >= min_quality:
                print(f"✓ Quality target met: {report.score}/100")
                return doc_path
            else:
                print(f"⚠ Quality below target: {report.score}/100")
                if attempt < max_attempts:
                    print("  Retrying...")
                    
        except QualityThresholdError as e:
            print(f"⚠ Generation quality too low")
            if attempt < max_attempts:
                print("  Retrying...")
    
    print("✗ Failed to meet quality threshold")
    return None

doc = generate_with_quality_check("UI", "Design System", min_quality=80)
if doc:
    print(f"Document ready: {doc}")
```

---

## Error Handling Examples

### Example 13: Comprehensive Error Handling

Handle all possible errors gracefully.

```python
from did import DIDDocumentGenerator
from did.exceptions import (
    InvalidDisciplineError,
    InvalidProjectNameError,
    ConfigValidationError,
    ContentGenerationError,
    QualityThresholdError,
    FileWriteError,
)

def safe_document_generation(discipline, project_name, output_path=None):
    try:
        # Validate inputs
        print(f"Creating {discipline} document for {project_name}...")
        
        # Initialize
        gen = DIDDocumentGenerator(
            design_discipline=discipline,
            project_name=project_name,
            output_path=output_path
        )
        
        # Validate content
        print("Validating content...")
        report = gen.validate_content()
        print(f"Pre-generation quality: {report.score}/100")
        
        # Generate
        print("Generating document...")
        doc_path = gen.generate_document()
        
        # Success
        print(f"✓ Document created: {doc_path}")
        return {"success": True, "path": doc_path}
        
    except InvalidDisciplineError as e:
        return {
            "success": False,
            "error": f"Invalid discipline. Use: UX, UI, Product, Backend, Frontend, DevOps, QA"
        }
    except InvalidProjectNameError as e:
        return {
            "success": False,
            "error": f"Invalid project name. Use 1-50 alphanumeric characters."
        }
    except ConfigValidationError as e:
        return {
            "success": False,
            "error": f"Configuration error: {e}"
        }
    except ContentGenerationError as e:
        return {
            "success": False,
            "error": f"Failed to generate content: {e}"
        }
    except QualityThresholdError as e:
        return {
            "success": False,
            "error": f"Content quality too low. Please customize sections."
        }
    except FileWriteError as e:
        return {
            "success": False,
            "error": f"Cannot write file. Check output directory permissions."
        }
    except Exception as e:
        return {
            "success": False,
            "error": f"Unexpected error: {e}"
        }

# Usage
result = safe_document_generation("UI", "My Project")
if result["success"]:
    print(f"Document: {result['path']}")
else:
    print(f"Error: {result['error']}")
```

---

### Example 14: Validation with Fallback

Provide fallback content if validation fails.

```python
from did import DIDDocumentGenerator

def generate_with_fallback(discipline, project_name):
    gen = DIDDocumentGenerator(discipline, project_name)
    
    # Try to generate
    report = gen.validate_content()
    
    if not report.passed:
        print(f"⚠ Quality score: {report.score}/100")
        print("Customizing sections with fallback content...")
        
        # Add fallback content to low-scoring sections
        sections_info = gen.get_sections_info()
        
        for section_name, info in sections_info.items():
            if info['quality_score'] < 70:
                fallback = f"[Placeholder for {section_name}]\n\nThis section requires specialized input.\n\nTODO: Add specific content here."
                gen.customize_section(section_name, fallback)
                print(f"  - Added fallback to {section_name}")
    
    # Generate with fallbacks in place
    doc_path = gen.generate_document(validate=False)
    return doc_path

doc = generate_with_fallback("Product", "New Feature")
print(f"Document: {doc}")
```

---

## Batch Processing

### Example 15: Process Multiple Projects

Generate documents for multiple projects efficiently.

```python
from did import DIDDocumentGenerator
from pathlib import Path
import json

def batch_generate_documents(projects, output_base):
    """Generate documents for multiple projects."""
    
    output_base = Path(output_base)
    output_base.mkdir(parents=True, exist_ok=True)
    
    results = []
    
    for project in projects:
        project_name = project["name"]
        disciplines = project["disciplines"]
        
        project_dir = output_base / project_name
        project_dir.mkdir(exist_ok=True)
        
        print(f"\nProcessing: {project_name}")
        
        for discipline in disciplines:
            try:
                gen = DIDDocumentGenerator(discipline, project_name)
                doc_path = gen.generate_document(output_path=str(project_dir))
                quality = gen.get_quality_report().score
                
                results.append({
                    "project": project_name,
                    "discipline": discipline,
                    "path": str(doc_path),
                    "quality": quality,
                    "status": "success"
                })
                
                print(f"  ✓ {discipline} (Quality: {quality}/100)")
                
            except Exception as e:
                results.append({
                    "project": project_name,
                    "discipline": discipline,
                    "error": str(e),
                    "status": "failed"
                })
                
                print(f"  ✗ {discipline} - {e}")
    
    # Save results
    results_file = output_base / "batch_results.json"
    with open(results_file, 'w') as f:
        json.dump(results, f, indent=2)
    
    return results

# Define projects
projects = [
    {
        "name": "Project Alpha",
        "disciplines": ["UX", "UI", "Backend", "Frontend"]
    },
    {
        "name": "Project Beta",
        "disciplines": ["Product", "DevOps", "QA"]
    },
    {
        "name": "Project Gamma",
        "disciplines": ["UX", "Backend", "DevOps"]
    }
]

# Generate all documents
results = batch_generate_documents(
    projects,
    "/home/user/documents/batch_output"
)

# Print summary
print("\n" + "="*50)
print("BATCH PROCESSING SUMMARY")
print("="*50)
successful = sum(1 for r in results if r["status"] == "success")
failed = sum(1 for r in results if r["status"] == "failed")
print(f"Successful: {successful}")
print(f"Failed: {failed}")
```

---

## See Also

- [API_REFERENCE.md](API_REFERENCE.md) - Complete API documentation
- [GETTING_STARTED.md](GETTING_STARTED.md) - Quick start guide
- [FAQ.md](FAQ.md) - Common questions
- [../ARCHITECTURE.md](../ARCHITECTURE.md) - Technical design
