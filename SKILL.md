# DID (Design Instructions Document) Skill
## Universal Design Intelligence & Documentation System

**Version:** 1.0  
**Status:** Operational Framework  
**Purpose:** Comprehensive intelligence system for capturing, structuring, and communicating design requirements across all design disciplines and delivery contexts.

---

## Executive Overview

The DID (Design Instructions Document) skill is a full-stack intelligence system designed to transform ambiguous design intent into precise, actionable specifications that eliminate ambiguity between design teams and implementation partners. It operates as a universal translator that bridges creative vision, technical architecture, and production reality.

### Core Value Proposition

- **Discipline-agnostic:** Works across industrial design, UX/UI, interior architecture, game design, 3D environments, and technical systems
- **Implementation-neutral:** Outputs specifications for any medium (physical, digital, hybrid, real-time)
- **Ambiguity elimination:** Transforms vague briefs into unambiguous technical instructions
- **Quality assurance:** Built-in verification at each layer ensures specifications remain consistent and complete
- **Collaborative intelligence:** Enables effective communication between design teams, architects, engineers, and fabricators

---

## Operational System Architecture

### Layer 1: Core Intelligence Engine
**Reference:** [./references/01-core-intelligence.md](./references/01-core-intelligence.md)

The foundation of the DID system is a methodology based on design thinking principles, structured decision-making, and systematic requirement analysis. This layer provides the cognitive framework for all downstream work.

**Key functions:**
- **Design Brief Parsing:** Transform unstructured design intent into structured decision trees
- **Constraint Mapping:** Identify functional, technical, aesthetic, and practical constraints
- **Stakeholder Analysis:** Map design decisions to stakeholder needs and acceptance criteria
- **Quality Gates:** Define what "complete" looks like for the design phase

**When to use:** Every project begins here. This layer ensures the design team operates from a shared understanding of success criteria before detailed work begins.

---

### Layer 2: Discipline Router
**Reference:** [./references/02-design-discipline-router.md](./references/02-design-discipline-router.md)

The router identifies which design discipline(s) a project requires and loads the appropriate specification frameworks. A single project may traverse multiple disciplines simultaneously.

**Disciplines covered:**
- **Interaction Design:** Digital interfaces, user flows, state management, real-time interaction
- **Spatial Design:** Physical architecture, interior spaces, environmental design, wayfinding
- **Product Design:** Consumer devices, industrial form, mechanical interaction, haptic feedback
- **Environment Design:** Game worlds, virtual spaces, immersive environments, procedural content
- **Service Design:** System behaviors, operational flows, human-machine interaction patterns
- **Information Architecture:** Data models, content structures, navigation systems
- **Detail Engineering Design (DED):** Indonesian consultant-style construction documentation — drawing registers, per-sheet title blocks, denah/tampak/potongan/detail at SNI scales, structural reinforcement schedules, MEP layouts, landscape/vegetasi, RAB/spesifikasi. See [./references/14-templates-and-examples.md](./references/14-templates-and-examples.md) §"Indonesian DED Master Template" for the canonical template and `utils/docx_generator.py` DED primitives (`add_ded_cover`, `add_daftar_gambar`, `add_ded_drawing_sheet`, `add_ded_legend`, `add_ded_material_table`, `set_ded_project`, `add_ded_title_block`).

**Decision criteria:**
The router uses a classification matrix based on: physical vs. digital, static vs. real-time, individual vs. systemic, and atomic vs. compound scope.

**When to use:** Early in the project, after the Core Intelligence layer has been established. Use the router to determine which reference documents from layers 3-7 apply to your project. For DED work, also load `references/14-templates-and-examples.md` §"Indonesian DED Master Template" and use the `ded`/`construction`/`structural`/`mep`/`landscape` formatters in `utils/design_formatter.py`.

---

### Layer 3: Requirement Discovery Engine
**Reference:** [./references/03-requirement-discovery.md](./references/03-requirement-discovery.md)

This layer systematizes the discovery of explicit and implicit requirements that must be satisfied. It moves beyond surface-level requirements to uncover secondary and tertiary implications.

**Discovery methods:**
- **Functional Requirements:** What the design must enable or prevent
- **Performance Requirements:** Measurable outcomes (speed, accuracy, capacity, durability)
- **Constraint Requirements:** Technical, legal, economic, or temporal boundaries
- **Quality Attributes:** Reliability, maintainability, accessibility, scalability, usability
- **Implicit Requirements:** Unstated needs inferred from stakeholder context, market conditions, or technical realities

**Dependency tracking:**
Requirements are mapped to their sources, their dependent requirements, and their relationship to design decisions. This creates a traceability matrix that ensures no requirement is orphaned.

**When to use:** Conduct discovery after discipline identification. Output feeds directly into the specification frameworks in layers 4-7.

---

### Layer 4: Spatial Design Framework
**Reference:** [./references/04-architectural-spatial-framework.md](./references/04-architectural-spatial-framework.md)

For projects involving physical or virtual space (architecture, game environments, interior design, complex information spaces), this layer provides structured spatial specifications.

**Components:**
- **Topological definitions:** Room/zone/area relationships and adjacencies
- **Metric specifications:** Dimensions, clearances, scale relationships, proportional systems
- **Sensory specifications:** Lighting, acoustics, material qualities, thermal properties
- **Workflow spatial mapping:** How users/actors move through space and what they can perceive from each location
- **Modular spatial units:** Repeatable spatial patterns and their constraints
- **Hierarchy and emphasis:** Which spaces are primary, secondary, support, or utility

**Output artifacts:**
Specifications, section diagrams, adjacency matrices, lighting models, acoustic profiles, sequence diagrams, and decision rule tables.

**When to use:** Any project with a spatial component—whether physical architecture, game level design, interior specification, or virtual environment.

---

### Layer 5: 2D Design Framework
**Reference:** [./references/05-2d-design-framework.md](./references/05-2d-design-framework.md)

For surface-level visual design (UI design, graphic design, documentation layout, interface specifications), this layer provides comprehensive 2D specifications.

**Components:**
- **Visual hierarchy system:** Typography scale, weight relationships, color hierarchy, spatial emphasis
- **Grid and layout systems:** Modular grids, responsive breakpoints, composition rules, alignment systems
- **Color and tone:** Color palette derivation, usage rules, contrast requirements, accessibility compliance
- **Typography specifications:** Typeface selection criteria, size/weight/line-height relationships, language-specific rendering
- **Component specifications:** Buttons, cards, forms, tables, navigation with variants, states, and responsive behavior
- **Animation and transition:** Timing functions, duration specifications, state transition logic, performance constraints
- **Accessibility standards:** WCAG compliance mapping, keyboard navigation, screen reader compatibility, semantic structure

**Output artifacts:**
Design systems, component libraries, specification sheets, state diagrams, animation timelines, and usage examples.

**When to use:** Digital products, user interfaces, graphic design, documentation design, any project requiring precise 2D visual specifications.

---

### Layer 6: 3D Design Framework
**Reference:** [./references/06-3d-design-framework.md](./references/06-3d-design-framework.md)

For volumetric design (product design, 3D environments, game asset design, industrial design, sculpture), this layer provides comprehensive 3D specifications.

**Components:**
- **Geometric specifications:** Form decomposition, curves and surfaces, topology, polygonal budget and LOD systems
- **Material and texture specifications:** Roughness/metallic/detail maps, shader requirements, procedural texture rules, UV mapping strategies
- **Lighting and visibility:** Lighting requirements, shadow casting, reflection probes, visibility culling, draw call optimization
- **Physics and interaction:** Collision surfaces, physics material properties, constraint hierarchies, animation rigs, behavior trees
- **Performance and optimization:** Triangle budgets, texture memory targets, shader complexity, real-time constraints, mobile/console requirements
- **Modular composition:** How 3D elements assemble, transformation spaces, hierarchy structures, scale relationships

**Output artifacts:**
Modeling guidelines, shader specifications, rigging documentation, animation blueprints, LOD rules, and technical art requirements.

**When to use:** Games, real-time 3D applications, 3D product visualization, architectural visualization, procedurally generated content, game asset design.

---

### Layer 7: Technical Specification Engine
**Reference:** [./references/07-technical-specification-engine.md](./references/07-technical-specification-engine.md)

This layer translates design requirements into precise technical specifications that engineers and developers can implement without ambiguity.

**Components:**
- **Data model specifications:** Entity relationships, state definitions, data types, validation rules, consistency guarantees
- **Algorithm specifications:** Decision logic, computation complexity, numerical precision, error handling, edge cases
- **API specifications:** Request/response structures, rate limiting, authentication, error codes, versioning strategies
- **Performance specifications:** Response time budgets, throughput targets, latency requirements, resource utilization limits
- **Concurrency and synchronization:** Race condition prevention, consistency models, transaction semantics, distributed coordination
- **Error handling and recovery:** Failure modes, graceful degradation, circuit breaker patterns, retry strategies, monitoring requirements

**Output artifacts:**
OpenAPI/GraphQL specifications, state diagrams, sequence diagrams, error handling matrices, performance budgets, and monitoring specifications.

**When to use:** Any digital product requiring backend/API implementation, complex business logic, data persistence, or real-time synchronization.

---

## Operational Workflows

### Workflow 1: Green-Field Project (Starting from scratch)

```
1. Brief Analysis
   └─ Layer 1: Core Intelligence Engine
      ├─ Parse design intent
      ├─ Map stakeholders
      ├─ Define success criteria
      └─ Create constraint map

2. Discipline Identification
   └─ Layer 2: Design Discipline Router
      └─ Select applicable frameworks

3. Requirement Discovery
   └─ Layer 3: Requirement Discovery Engine
      └─ Output: Complete requirements matrix

4. Framework Application
   ├─ Layer 4: Spatial Design (if applicable)
   ├─ Layer 5: 2D Design (if applicable)
   ├─ Layer 6: 3D Design (if applicable)
   └─ Layer 7: Technical Specifications (if applicable)

5. Quality Assurance
   ├─ Traceability verification
   ├─ Consistency checking
   ├─ Completeness audit
   └─ Stakeholder validation
```

**Duration:** 2-4 weeks depending on scope
**Team:** Design lead, architect, subject matter experts
**Output:** Complete DID package + project brief

### Workflow 2: Existing Project Refinement

```
1. Gap Analysis
   └─ Identify missing specifications
      └─ Layer 2: Determine which layers are incomplete

2. Targeted Discovery
   └─ Layer 3: Discover missing requirements

3. Targeted Specification
   └─ Apply only relevant layers for gaps

4. Integration
   └─ Merge new specifications with existing DID
   └─ Verify no contradictions

5. Handoff
   └─ Update traceability matrix
   └─ Communicate changes to implementation team
```

**Duration:** 1-2 weeks
**Team:** Design lead, 1-2 specialists
**Output:** Updated DID package

### Workflow 3: Implementation Review

```
1. Specification Audit
   └─ Layer 7: Technical Specification Engine
      └─ Verify requirements are testable

2. Test Strategy Development
   └─ Create acceptance criteria for each requirement
   └─ Define test cases and verification methods

3. Implementation Checkpoint Reviews
   └─ At 25%, 50%, 75% milestones
   └─ Verify built output matches specifications
   └─ Identify deviations early

4. Acceptance Testing
   └─ Execute against requirements matrix
   └─ Document any specification gaps discovered during implementation
```

**Duration:** Ongoing throughout implementation
**Team:** Design lead + QA team
**Output:** Acceptance test results, specification corrections

---

## Quality Assurance Framework

### Level 1: Specification Completeness
- All requirements have corresponding specifications
- All specifications reference source requirements
- No orphaned specifications without requirements

### Level 2: Specification Consistency
- No contradictory specifications across layers
- Shared terminology consistently applied
- Design decisions aligned across all layers

### Level 3: Specification Precision
- No ambiguous language ("should", "try", "attempt" flagged for review)
- All measurable properties have exact values
- All categorical properties have exhaustive enumerations

### Level 4: Stakeholder Alignment
- Design rationale documented for all major decisions
- Stakeholder sign-offs collected before handoff
- Change request process defined

### Level 5: Implementation Feasibility
- Technical review completed before handoff
- Resource requirements and timelines realistic
- Risk assessment completed and mitigations defined

---

## Cross-Layer Integration Points

The DID system works as an integrated whole through these critical connection points:

**Core Intelligence ↔ Discipline Router**
- Requirements discovered in Layer 1 inform which disciplines are needed
- Discipline selection determines which specialized requirements to explore

**Layer 3 ↔ Layers 4-7**
- Requirements matrix from Layer 3 feeds into all specification layers
- Each specification layer must trace back to source requirements

**Layers 4-6 ↔ Layer 7**
- Spatial, 2D, and 3D specifications are translated into technical requirements
- Technical specifications define implementation of design intent

**All Layers → Quality Assurance**
- Every layer output passes through consistency and completeness checks
- Cross-layer conflicts identified and resolved at integration points

---

## Common Pitfalls & Recovery

### Pitfall 1: Skipping Core Intelligence
**Symptom:** Specifications conflict because different team members have different success criteria
**Recovery:** Return to Layer 1; rebuild shared understanding before continuing

### Pitfall 2: Over-specification
**Symptom:** Specifications so detailed they constrain implementation unnecessarily
**Recovery:** Review each specification; remove constraints that don't serve requirements; focus on outcomes, not methods

### Pitfall 3: Under-specification
**Symptom:** Ambiguous language that allows multiple valid interpretations
**Recovery:** Use Layer 7 Technical Specification Engine to convert qualitative descriptions to quantitative requirements

### Pitfall 4: Stale Specifications
**Symptom:** Specifications become disconnected from actual project needs as scope evolves
**Recovery:** Establish change control; require all scope changes to flow through traceability matrix; track specification versions

### Pitfall 5: Missing Discipline Coverage
**Symptom:** Important design aspects slip through gaps between disciplines
**Recovery:** Create a "discipline coverage checklist" for your project; ensure all project aspects map to at least one discipline layer

---

## Skill Integration with Implementation Teams

### For Developers/Engineers
The DID becomes a contract. Requirements in Layer 7 (Technical Specifications) are binding acceptance criteria. Any ambiguity in Layers 7 flows back through the traceability matrix to source requirements in Layer 3. Developers should:
1. Read the Technical Specification layer first
2. For any ambiguity, trace back to source requirements
3. Flag contradictions immediately
4. Propose alternative implementations only if feasible within all constraints

### For Fabricators/Manufacturers
Spatial Design (Layer 4) and 3D Design (Layer 6) specifications are production instructions. Measurements, tolerances, and material specifications are binding. All decisions affecting form, function, or cost must be escalated to design team for approval.

### For QA/Testing Teams
Requirements matrix from Layer 3 is the acceptance criteria. Each requirement must have one or more test cases. Test results directly verify specification compliance. Failed tests indicate either implementation issues or specification gaps.

---

## Document Structure & Maintenance

### Canonical References
This skill package includes 15 reference documents:
- Layer 1: Core Intelligence (01-core-intelligence.md)
- Layer 2: Discipline Router (02-design-discipline-router.md)
- Layer 3: Requirement Discovery (03-requirement-discovery.md)
- Layer 4: Spatial Design (04-architectural-spatial-framework.md)
- Layer 5: 2D Design (05-2d-design-framework.md)
- Layer 6: 3D Design (06-3d-design-framework.md)
- Layer 7: Technical Specifications (07-technical-specification-engine.md)
- Layers 8-15: Project-specific toolkits (forthcoming in Part 2)

### Project DID Template
When starting a project, create a project-specific DID document that:
1. Instantiates each relevant reference layer with project-specific content
2. Cross-references source requirements for every specification
3. Maintains version history with change dates and approvers
4. Tracks sign-offs from all stakeholders

### Maintenance Workflow
- Review specifications every 2 weeks during active design
- After handoff to implementation, freeze specifications (track changes only)
- Document discovered deviations during implementation
- Post-project, extract lessons learned and update reference documents

---

## Conclusion

The DID skill is a comprehensive intelligence system that transforms design ambiguity into actionable precision. It bridges the gap between creative vision and technical reality by providing structured methodologies for each phase of design communication. Use this skill to eliminate the rework that comes from miscommunication, to establish clear success criteria, and to create specifications that implementation teams can follow with confidence.

---

**Next Steps:**
1. Read [./references/01-core-intelligence.md](./references/01-core-intelligence.md) to understand the foundational methodology
2. Use Layer 2 (Discipline Router) to identify which layers apply to your project
3. Create a project-specific DID that instantiates relevant frameworks
4. Use quality gates from the QA framework to verify completeness before handoff

