# Design Discipline Router
## Discipline Identification & Framework Selection

**Version:** 1.0  
**Layer:** Routing & Classification (Layer 2)  
**Purpose:** Identify which design disciplines a project requires and load the appropriate specification frameworks from Layers 4-7.

---

## Overview

The Design Discipline Router is a classification system that maps projects to the specific design methodologies they require. A single project often traverses multiple disciplines simultaneously. For example:
- A mobile banking app requires Interaction Design and Technical Specifications
- A consumer product requires Product Design (physical), Interaction Design (touchscreen UI), and 3D Design (form modeling)
- A game world requires Spatial Design (level layout), 3D Design (assets), Interaction Design (controls), and Technical Specifications (systems architecture)

This layer's job is to:
1. **Identify** which disciplines are relevant to your project
2. **Avoid** applying irrelevant frameworks (which creates unnecessary work)
3. **Ensure** all project aspects are covered by at least one discipline
4. **Sequence** the work (some disciplines have dependencies)

---

## The Six Core Design Disciplines

### Discipline 1: Interaction Design
**Applies to:** Systems where humans make decisions and control digital experiences

**What it covers:**
- User flows and task sequences
- State management and conditional branching
- Form design and data input
- Error handling and recovery
- Real-time feedback and responsiveness
- Decision trees and conditional logic
- Accessibility and assistive technology support

**Indicators this discipline is needed:**
- Project involves digital UI (mobile, web, desktop, VR/AR, embedded screens)
- Project involves complex user decision-making or task flows
- Project requires real-time responsiveness or animation
- Project is explicitly called an "app," "website," "software," "platform," or "system"

**Example projects:**
- Mobile apps (banking, fitness, social, productivity)
- Web applications and dashboards
- VR/AR experiences
- Smart device interfaces (thermostats, fitness trackers, IoT)
- Game UI systems (menus, HUD, inventory)

**Output specification documents:**
- Interaction flows and storyboards
- State diagrams (for every interactive element)
- Form specifications with validation rules
- Animation and transition timing
- Error state catalogs with recovery paths
- Accessibility compliance maps

**Reference document:** Layer 5: 2D Design Framework (covers interactive surface design)

---

### Discipline 2: Spatial Design
**Applies to:** Systems where users navigate or move through physical or virtual space

**What it covers:**
- Room/zone/area layout and adjacencies
- Wayfinding and navigation systems
- Sensory environments (lighting, acoustics, materials)
- Scale relationships and proportions
- Ergonomic accessibility and clearances
- Workflow spatial optimization
- Modularity and repeatable spatial units

**Indicators this discipline is needed:**
- Project involves architecture (buildings, rooms, spaces)
- Project involves game level design or environment layout
- Project involves interior design or space planning
- Project involves information architecture with spatial metaphors (3D browsing, spatial databases)
- Project requires people/assets to move through space

**Example projects:**
- Building architecture (offices, retail, hospitality, healthcare)
- Game level design (dungeons, open worlds, multiplayer arenas)
- Interior design and space planning
- Museum/exhibition/wayfinding design
- City planning and urban design
- Virtual world design (metaverse spaces, procedurally generated worlds)

**Output specification documents:**
- Topological diagrams (adjacency matrices)
- Scale and proportion systems
- Lighting design specifications
- Acoustic profiles and material specifications
- Sensory environment specs (temperature, air flow, smell)
- Wayfinding and signage systems
- Workflow path optimization diagrams

**Reference document:** Layer 4: Architectural Spatial Framework

---

### Discipline 3: Product Design
**Applies to:** Tangible physical objects users interact with or use

**What it covers:**
- Form and industrial design aesthetics
- Mechanical interaction and haptic feedback
- Ergonomic fit and usability
- Manufacturing feasibility and tolerances
- Material selection and durability
- Assembly and disassembly logic
- Repairability and lifecycle considerations

**Indicators this discipline is needed:**
- Project involves designing a physical consumer product
- Project involves designing hardware devices
- Project involves mechanical interaction or controls
- Project is about form, feel, and tactile experience
- Project requires manufacturing specifications

**Example projects:**
- Consumer electronics (smartphones, earbuds, smartwatches)
- Furniture and furnishings
- Kitchen appliances and tools
- Sports equipment
- Gaming controllers and peripherals
- Medical devices
- Packaging and unboxing experiences

**Output specification documents:**
- Form language and aesthetic system
- Ergonomic specifications (grip, reach, force requirements)
- Material and finish specifications
- Manufacturing process requirements
- Assembly and disassembly procedures
- Tolerances and precision requirements
- Repairability and spare parts strategy

**Reference document:** Layer 6: 3D Design Framework

---

### Discipline 4: Environment Design
**Applies to:** Real-time 3D worlds, games, and immersive experiences

**What it covers:**
- 3D asset modeling and optimization
- Material definition and shader authoring
- Real-time rendering and performance budgets
- Procedural content generation (if applicable)
- Animation rigging and state machines
- Particle effects and visual communication
- Performance optimization and LOD systems

**Indicators this discipline is needed:**
- Project involves game development
- Project involves real-time 3D applications
- Project requires real-time performance considerations
- Project involves VR/AR applications
- Project requires procedurally generated content
- Project involves complex 3D animation

**Example projects:**
- Video game assets and environments
- Real-time 3D visualization (architecture, product, medical)
- VR/AR experiences
- Metaverse and virtual world design
- Procedurally generated game content
- Real-time CGI and motion graphics

**Output specification documents:**
- Modeling guidelines and topology specifications
- Shader/material specifications
- Animation blueprints and rigging guides
- Performance budgets (polygon count, draw calls, memory)
- LOD (level-of-detail) rules
- Procedural generation algorithms (if applicable)
- Real-time constraint specifications

**Reference document:** Layer 6: 3D Design Framework

---

### Discipline 5: Service Design
**Applies to:** Operational systems, workflows, and human-machine interaction patterns

**What it covers:**
- Multi-step user journeys across touchpoints
- Operational workflow optimization
- System behavior and decision logic
- Error prevention and graceful degradation
- Escalation paths and exception handling
- Consistency across multiple interfaces/channels
- Organizational capability requirements

**Indicators this discipline is needed:**
- Project involves multiple touchpoints (digital + physical, online + offline)
- Project involves backend operations or business processes
- Project requires consistent experience across channels
- Project involves complex decision logic or automation
- Project is about how a service or organization operates

**Example projects:**
- Omnichannel retail experiences (web, app, physical store)
- Healthcare patient journeys (appointment, visit, followup)
- Financial services onboarding and transactions
- Subscription management systems
- Logistics and delivery services
- Customer support and ticketing systems
- Marketplace platforms with multiple actor types

**Output specification documents:**
- End-to-end journey maps
- Operational workflow diagrams
- Decision trees and automation rules
- Multi-channel consistency matrices
- Exception handling and escalation paths
- Role-based capability matrices
- System integration specifications

**Relationship to other disciplines:**
- Interaction Design handles individual touchpoint experiences
- Service Design ensures consistency across all touchpoints
- Technical Specifications define how services are automated

---

### Discipline 6: Information Architecture
**Applies to:** Systems where data must be organized, navigated, and understood

**What it covers:**
- Data model design and entity relationships
- Taxonomy and categorization systems
- Navigation and wayfinding through information
- Search and discovery mechanisms
- Metadata and labeling systems
- Information hierarchy and emphasis
- Consistency across data presentations

**Indicators this discipline is needed:**
- Project involves organizing large amounts of information
- Project requires navigation through data/content
- Project involves search functionality
- Project requires categorization or taxonomy
- Project has complex data relationships
- Project involves content management or CMS

**Example projects:**
- Websites and content platforms
- Database design and query interfaces
- Document management systems
- E-commerce catalogs and product searches
- Library and archive systems
- Research and analytics platforms
- Knowledge bases and wikis

**Output specification documents:**
- Entity-relationship diagrams
- Taxonomy and categorization hierarchies
- Navigation maps and information hierarchies
- Labeling and metadata standards
- Search and filter specifications
- Content model definitions
- API data structure specifications

**Integration with Technical Specifications:**
- Data models in Information Architecture are translated to database schemas in Technical Specifications
- Taxonomy rules become validation and categorization logic

---

## Discipline Selection Matrix

Use this matrix to quickly identify which disciplines apply to your project:

| Discipline | Physical Space | Interaction | 3D Assets | Real-time Perf | Multi-touchpoint | Data Organization |
|-----------|---|---|---|---|---|---|
| **Interaction Design** | — | ✓ | ✓ (UI) | — | — | ✓ (UI) |
| **Spatial Design** | ✓ | — | — | — | — | ✓ (wayfinding) |
| **Product Design** | ✓ | ✓ | — | — | — | — |
| **Environment Design** | — | ✓ (VR/AR) | ✓ | ✓ | — | — |
| **Service Design** | ✓ | ✓ | — | — | ✓ | — |
| **Information Architecture** | — | ✓ | — | — | — | ✓ |

---

## Application Examples

### Example 1: Mobile Fitness App
**Project description:** App for tracking workouts, social challenges, and nutrition

**Analysis:**
- Digital interface → **Interaction Design** (required)
- User data storage and organization → **Information Architecture** (required)
- Backend operations and user journeys → **Service Design** (required)
- Backend implementation → **Technical Specifications** (required)
- Physical products (wearables, sensors) → Product Design (optional, if designing hardware)

**Applicable disciplines:** Interaction Design, Information Architecture, Service Design, Technical Specifications

---

### Example 2: Commercial Kitchen Design
**Project description:** Design a commercial kitchen for a 150-seat restaurant

**Analysis:**
- Kitchen layout and equipment placement → **Spatial Design** (required)
- Workflow optimization (prep, cooking, plating) → **Service Design** (required)
- Equipment selection and ergonomics → **Product Design** (required)
- 3D visualization and VR walkthrough → **Environment Design** (optional, for visualization)

**Applicable disciplines:** Spatial Design, Service Design, Product Design

---

### Example 3: Multiplayer Online Game
**Project description:** 100-player battle royale game with dynamic environments

**Analysis:**
- Game levels and environments → **Spatial Design** (required)
- 3D character and world assets → **Environment Design** (required)
- Real-time asset optimization → **Environment Design** (required)
- UI menus, HUD, inventory → **Interaction Design** (required)
- Backend game state and player progression → **Information Architecture** (required)
- Server architecture and synchronization → **Technical Specifications** (required)
- Multi-player interaction flows → **Service Design** (required)

**Applicable disciplines:** All six disciplines

---

### Example 4: Hospital Patient Check-in Redesign
**Project description:** Improve check-in experience across digital and physical touchpoints

**Analysis:**
- Registration desk layout and workflow → **Spatial Design** (required)
- Check-in app interface → **Interaction Design** (required)
- End-to-end check-in journey → **Service Design** (required)
- Patient data organization (insurance, medical history) → **Information Architecture** (required)
- Backend patient record integration → **Technical Specifications** (required)

**Applicable disciplines:** Spatial Design, Interaction Design, Service Design, Information Architecture, Technical Specifications

---

## Discipline Sequencing

Some disciplines have dependencies and should be sequenced in a specific order:

### Critical Path:
1. **Information Architecture** (if needed) - Define data structures and organization before designing interactions or services
2. **Spatial Design** (if needed) - Define space organization before designing interactions within those spaces
3. **Service Design** (if needed) - Define multi-touchpoint workflows before detailed individual interaction design
4. **Interaction Design** (if needed) - Design individual interaction contexts based on service and spatial frameworks
5. **Environment Design** (if needed) - Design 3D assets based on established interactions and spatial layouts
6. **Product Design** (if needed) - Design physical form based on interaction and spatial requirements
7. **Technical Specifications** - Translate all higher-level specifications into implementation detail

### Parallelization opportunities:
- Interaction Design and Product Design can proceed in parallel (if independent)
- Service Design and Information Architecture can proceed in parallel
- Environment Design and other disciplines can proceed in parallel (if dependencies are clear)

### Feedback loops:
- Technical Specifications often reveal infeasibility → feeds back to design layers for revision
- Product Design constraints (manufacturing) → feeds back to Interaction Design (changing available controls)
- Environment Design performance constraints → feeds back to Spatial Design (changing asset complexity)

---

## Discipline Coordination

For multi-discipline projects, establish coordination points:

### Weekly Discipline Sync
30-minute meeting with leads from each discipline:
- **Agenda:** Review specifications for conflicts, dependencies, and integration points
- **Decision:** When one discipline's output constrains another, make explicit trade-off decisions
- **Documentation:** Record all cross-discipline decisions and their rationale

### Specification Review Checklist
When one discipline's work is complete, have all relevant disciplines review:
- [ ] No contradictions with other disciplines' specifications
- [ ] All dependencies clearly documented
- [ ] All assumptions from other disciplines documented
- [ ] Performance, feasibility, and cost implications reviewed
- [ ] Integration points clearly defined for implementation teams

---

## Common Mistakes

### Mistake 1: Missing Disciplines
**Symptom:** "We're designing a smart fridge. We need Interaction Design and Product Design."  
**Reality:** Smart fridge also requires Information Architecture (managing recipes, inventory, shopping lists) and Service Design (integration with smart home ecosystem, retailer partnerships)  
**Fix:** Use the Discipline Selection Matrix systematically; don't rely on intuition alone

### Mistake 2: Wrong Sequence
**Symptom:** "Let's design the UI first, then figure out the data model"  
**Risk:** UI designed for impossible data structures; costly rework  
**Fix:** Sequence disciplines per the Critical Path; use dependencies to guide work order

### Mistake 3: Discipline Conflicts
**Symptom:** "Interaction Design wants a 100-button interface, but Product Design can only fit a 6-button physical device"  
**Risk:** Unresolvable conflict mid-project; blame game between teams  
**Fix:** Identify such constraints upfront via Discipline Coordination; make explicit trade-off decisions with stakeholders

---

## Integration with Layer 3 (Requirement Discovery)

The disciplines you identify in Layer 2 determine:
- **Which discovery methods** you'll use in Layer 3
- **Which stakeholders** must participate in requirements work
- **Which constraint categories** matter most to your project

For example, if Spatial Design is a discipline, constraint discovery must include physical dimensions, clearances, and manufacturing tolerances.

---

## Quality Gates: Discipline Router Level

Before moving to Requirement Discovery (Layer 3), verify:

- [ ] All project aspects map to at least one discipline
- [ ] No contradictions between selected disciplines' scope (overlaps are OK; contradictions are not)
- [ ] Work sequence established based on discipline dependencies
- [ ] Coordination method defined for multi-discipline projects
- [ ] Stakeholders understand which disciplines apply and why
- [ ] Resource requirements assessed based on disciplinary complexity

---

## Conclusion

The Design Discipline Router prevents wasted effort on irrelevant frameworks and ensures comprehensive coverage of all project aspects. By systematically identifying which disciplines apply and in what sequence, teams move efficiently from strategic intent (Layer 1) to detailed requirements discovery (Layer 3) with clarity about scope and coverage.

