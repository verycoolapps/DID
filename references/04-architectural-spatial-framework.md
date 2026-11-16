# Architectural & Spatial Design Framework
## Spatial Specification System for Physical & Virtual Environments

**Version:** 1.0  
**Layer:** Spatial Specification (Layer 4)  
**Purpose:** Translate spatial requirements into precise architectural specifications that can be built, inhabited, and verified.

---

## Overview

The Spatial Design Framework applies to any project where users navigate through or interact with space—physical architecture, game levels, virtual environments, interior design, or complex spatial information systems. This layer translates requirements from Layer 3 into specifications that define:
- **Topological relationships:** Which spaces connect, in what order, with what transitions
- **Metric specifications:** Exact dimensions, clearances, proportional systems
- **Sensory environments:** Lighting, acoustics, materials, thermal properties
- **Workflow optimization:** How users move through space and what they perceive
- **Modularity:** Repeatable spatial patterns and their constraints

---

## Component 1: Topological Specifications

**Purpose:** Define spatial relationships independent of specific dimensions

### 1A: Adjacency Matrix

An adjacency matrix documents which spaces connect to which other spaces, and the nature of the connection.

**Documentation format:**

```
ADJACENCY MATRIX

Space Legend:
A: Lobby (entry)
B: Reception desk area
C: Waiting area
D: Consultation room 1
E: Consultation room 2
F: Back office
G: Storage
H: Restroom

Adjacency Rules:
       A   B   C   D   E   F   G   H
A   |  -   D   D   -   -   -   -   -  |  Direct, public
B   |  D   -   D   D   D   -   -   -  |  Direct, public circulation
C   |  D   D   -   V   V   -   -   -  |  Visual, no direct
D   |  -   D   V   -   D   D   -   -  |  Direct, semiprivate
E   |  -   D   V   D   -   D   -   -  |  Direct, semiprivate
F   |  -   -   -   D   D   -   D   -  |  Direct, private staff only
G   |  -   -   -   -   -   D   -   -  |  Direct, private staff only
H   |  -   -   -   -   -   -   -   -  |  Separate access from public

Legend:
D = Direct access (door)
V = Visual connection (window, opening)
- = No connection
```

### 1B: Adjacency Rules

Document constraints on connections between spaces.

**Format:**
```
ADJACENCY RULE: [Spaces involved]
Requirement: [From Layer 3]

Connection type: [Direct access / Visual / Proximity / Sequential]
Access control: [Public / Semi-private / Private / Staff-only]
Transition: [Open doorway / Glazed door / Solid wall / Passage]

Rationale: [Why this connection is needed or prohibited]

Constraint violation impact:
- If violated: [What breaks in workflow or user experience]
```

**Example:**
```
ADJACENCY RULE: Waiting area ↔ Consultation rooms
Requirement: REQ-012 "Users should not see into consultation rooms from waiting area"

Connection type: Visual separation required
Access control: Waiting area is public; consultation rooms are semi-private
Transition: Solid opaque wall with no windows into consultation rooms

Rationale: Privacy expectation; patients discussing sensitive health information

Constraint violation impact:
- If violated: Privacy breach; patient discomfort; regulatory non-compliance
```

### 1C: Sequence Diagrams

For projects with prescribed user flows, document the spatial sequence.

**Format:**
```
SPATIAL SEQUENCE: [User journey name]
Description: [What the user is doing]

Sequence:
1. [Space A] → [Transition] → [Space B] → [Transition] → [Space C]
   - User can perceive: [What's visible from each space]
   - Decision point: [What decision is made in this space]
   - Duration: [How long user stays]

2. [Space B] → [Alternative transition] → [Space D] (alternative path)
   - Condition: [When user takes this path instead]

Decision rules:
- [If condition], then [user proceeds to space X]
- [If condition], then [user returns to space Y]
```

---

## Component 2: Metric Specifications

**Purpose:** Define exact dimensions and scale relationships

### 2A: Dimensional Specifications

Document specific measurements for every critical dimension.

**Format:**
```
DIMENSIONAL SPECIFICATION: [Space or element]
Source requirement: [Which Layer 3 requirement]

Primary dimensions:
- Length: [X] meters ±[tolerance] cm
- Width: [Y] meters ±[tolerance] cm
- Height: [Z] meters ±[tolerance] cm
- Ceiling height: [H] meters (minimum/optimal/maximum)

Critical clearances:
- Door opening width: [X] cm (minimum for accessibility)
- Passage width: [X] cm (allowing two people to pass, or single-file)
- Counter height: [X] cm (ergonomic for standing work)
- Shelf depth: [X] cm (reach distance from path)

Rationale:
- Why these dimensions: [Based on what user/accessibility/code requirement]
- Constraints: [What prevents larger/smaller]
- Tolerances: [Why this precision level, or why flexibility is acceptable]

Verification method:
- How we'll confirm in built environment: [Measuring tape survey, CAD verification]
```

**Example:**
```
DIMENSIONAL SPECIFICATION: ADA-compliant accessible route
Source requirement: REQ-005 "Space must be accessible to wheelchair users"

Primary dimensions:
- Minimum route width: 91.4 cm (36 inches) ±0 cm (ADA minimum)
- Minimum door width: 81.3 cm (32 inches) ±0 cm (ADA minimum)
- Maximum slope: 5% ±0% (ADA maximum for accessible route)
- Minimum ceiling clearance: 213.4 cm (84 inches) ±0 cm

Critical clearances:
- Wheelchair turning radius: 152.4 cm (60 inches) in alcoves minimum
- Pull-side clearance at doors: 60 cm minimum
- Approach clearance at fixtures: 48 cm minimum

Rationale:
- ADA Standards for Accessible Design mandate these minimums
- Wider is more comfortable but increases construction cost
- 5% slope is maximum before ramp transition required

Tolerance: 0 cm—these are legal minimums; going smaller violates ADA
```

### 2B: Proportional Systems

For projects where relative proportions matter more than absolute dimensions, define proportional relationships.

**Format:**
```
PROPORTIONAL SYSTEM: [Name]
Source requirement: [Which requirement drives this]

Base unit: [1 unit = ? meters] OR [Choose one element as 1:1 reference]

Ratios:
- [Element A] : [Element B] = [X] : [Y] (why this ratio)
- [Space A] : [Space B] = [X] : [Y]
- [Height] : [Width] = [X] : [Y] (harmony/visual balance)

Application rules:
- [When to use this ratio]
- [When alternative ratios apply]
- [Exceptions and why]

Example application:
```

**Example:**
```
PROPORTIONAL SYSTEM: Golden ratio spatial harmony
Source requirement: REQ-018 "Space should feel visually harmonious and balanced"

Base unit: Shortest dimension of room = 1 unit

Ratios:
- Room length : width = 1.618 : 1 (golden ratio for perceived harmony)
- Ceiling height : room width = 0.618 : 1 (creates intimate scale)
- Focal wall dimensions : opposite wall = 1 : 0.618 (emphasis and retreat)

Application rules:
- Use when primary focus is aesthetic harmony and not constrained by cost
- Use for luxury retail, hospitality, residential
- Don't use for high-density or utility-focused spaces (hospital, warehouse)

Example application:
- Room is 12m long
- Following golden ratio: width should be 12 / 1.618 = 7.4m
- Ceiling height: 7.4 × 0.618 = 4.57m
```

---

## Component 3: Sensory Environment Specifications

**Purpose:** Define non-visual sensory properties of spaces

### 3A: Lighting Specifications

```
LIGHTING SPECIFICATION: [Space]
Source requirement: [Which requirement]

Daylighting:
- Desired: [Natural daylight / Minimal daylight / Irrelevant]
- Window area: [% of floor area, if applicable]
- Orientation: [Which directions, for seasonal optimization]
- Glare prevention: [Shading strategy for excessive sunlight]

Artificial lighting:
- Illuminance: [Lux level for primary tasks]
- Color temperature: [Kelvin, e.g., 4000K for neutral/active, 2700K for warm/residential]
- CRI (Color Rendering Index): [80+ for general, 90+ for color-sensitive tasks]
- Distribution: [Direct/Indirect/Mixed; diffuse/focused]
- Dimmability: [Fixed / Dimmable / Scenes for different activities]

Lighting zones:
- [Zone A]: [Purpose] requires [Illuminance] lux at [task surface]
- [Zone B]: [Purpose] requires [Illuminance] lux, plus accent lighting

Rationale:
- Illuminance levels based on: [Task requirements, accessibility, energy code]
- Color temperature chosen for: [Circadian rhythm, task performance, mood]

Verification:
- Measurement: Light meter readings at [specific task locations]
- Timing: Measured at [day time, night time, seasonal conditions]
```

### 3B: Acoustic Specifications

```
ACOUSTIC SPECIFICATION: [Space or transition]
Source requirement: [Which requirement]

Sound isolation (from outside):
- Target: [STC rating or dB reduction required]
- Priority noise source: [Traffic, HVAC, adjacent spaces]
- Solution: [Wall/window/material specifications that achieve target]

Internal acoustic environment:
- Reverberation time (RT60): [X seconds] (time for sound to decay 60dB)
- Background noise level: [X dB(A)] at [task location]
- Speech intelligibility: [Percentage or qualitative requirement]

Sound absorption:
- Materials: [Specific materials and their absorption coefficients]
- Coverage: [% of walls/ceiling to be absorptive]
- Placement: [Where absorption is needed most]

Mechanical systems:
- HVAC noise target: [X dB(A)]
- Control methods: [Vibration isolation, flexible ductwork, lined plenums]

Verification:
- Acoustic testing: [Standards and measurement locations]
- Timing: Before occupancy and annually
```

### 3C: Material & Tactile Specifications

```
MATERIAL SPECIFICATION: [Surface or element]
Source requirement: [Which requirement]

Material selection:
- Primary material: [What + why]
- Finish: [Matte/Satin/Gloss + why]
- Tactile quality: [Smooth/Textured + why for user comfort]

Durability and maintenance:
- Expected lifespan: [X years]
- Maintenance requirement: [Frequency and method]
- Stain/wear resistance: [Rating or specification]
- Cleanability: [How easily cleaned, cleaning agents acceptable]

Sustainability (if required):
- Certifications: [FSC, GREENGUARD, etc.]
- Embodied carbon: [kg CO2e, if quantified]
- Recycled content: [%]

Accessibility:
- Slip resistance (if flooring): [Static coefficient of friction > X]
- Texture (if wayfinding): [Tactile guidance for visually impaired]

Specifications by location:
- [High-traffic area]: Use durable, washable [material]
- [Task surface]: Use non-glare [material]
- [Visual accent]: Use [material] for color and character
```

---

## Component 4: Workflow Spatial Mapping

**Purpose:** Optimize space for how people actually use it

### 4A: Movement Path Optimization

```
WORKFLOW PATH SPECIFICATION: [Named workflow]
Source requirement: [Which requirement]

Actor: [Who performs this workflow; include accessibility needs]
Frequency: [How often this workflow occurs]
Duration: [How long it typically takes]

Path details:
1. Start at [Space A]
2. Move to [Space B] via [route]; distance [X meters]
3. Perform [action] in [Space B]
4. Move to [Space C] via [route]; distance [Y meters]
...

Path optimizations:
- Distance: [Current] meters; target [desired] meters (why)
- Transitions: [Smooth/requires waiting/requires decision]
- Obstacle avoidance: [Current obstacles and removal plan]

Perception requirements:
- From [Point A], user should perceive: [What's visible]
- From [Point B], user should NOT perceive: [Privacy/surprise maintenance]

Verification:
- Workflow trace: [Time-lapse observation of actual workflow]
- Distance measurement: [Calculate from final spatial specifications]
```

### 4B: Wayfinding Specifications

```
WAYFINDING SPECIFICATION: [Space or zone]
Source requirement: [Which requirement for navigation/orientation]

Decision points:
- Location: [Where users must make navigation decision]
- Choice: [Multiple directions available]
- Wayfinding aid: [Signage / Color coding / Architectural cue / Lighting]
- Required information: [Destination distance, direction, estimated time]

Destination visibility:
- [Destination] should be visible from [Point A] at [distance]
- OR [Destination] indicated by [signage/landmark] from [Point A]
- Rationale: [Why visibility is needed; accessibility considerations]

Landmark-based navigation:
- Landmark 1: [Description + location]; visible from [distance]
- Landmark 2: [Description + location]; visible from [distance]
- Cognitive load: [Users need to remember X landmarks to navigate]

Verification:
- Wayfinding audit: [How we'll test navigation with unfamiliar users]
- Accessibility testing: [Include users with cognitive/visual disabilities]
```

---

## Component 5: Modularity & Repeating Spatial Units

**Purpose:** Enable efficient replication and variation within constraints

```
MODULAR SPATIAL UNIT: [Name]
Repeatable in projects of [scale]: [How it repeats]

Base dimensions:
- Length: [X] m ±[tolerance]
- Width: [Y] m ±[tolerance]
- Height: [Z] m ±[tolerance]

Adjacency rules within module:
- [Element A] connects to [Element B] with [Y cm] transition
- [Element B] connects to [Element C] via [method]
- [Element C] must NOT connect to [Element A] (why)

Variations:
- Orientation: [Can be rotated 0°/90°/180°/270°; constraints]
- Size: [Can scale 0.8x to 1.2x base dimensions]
- Material: [Options available; impact on adjacency]

Nesting rules:
- [Module A] fits inside [Module B] with [X cm] clearance
- [Module A] can connect to [Module C] only via [specific orientation]
- [Module A] requires [supporting infrastructure] from parent space

Assembly logic:
- Primary axis: [Module aligns to this grid/direction]
- Connections: [How modules physically connect; mechanical/spatial tolerance]

Constraints:
- Cannot be: [Specific forbidden configurations]
- Maximum: [How many can nest/repeat before structural/functional issues]

Examples:
- [Configuration 1]: [Diagram] - good for [use case]
- [Configuration 2]: [Diagram] - good for [use case]
```

---

## Component 6: Hierarchy & Emphasis

**Purpose:** Define which spaces are primary, secondary, or utilitarian

```
SPATIAL HIERARCHY SPECIFICATION

Primary (destination) spaces:
- [Space A]: [Function]; receives [X% of traffic]
- [Space B]: [Function]; receives [Y% of traffic]
Emphasis cues: [How these spaces are made prominent]

Secondary (circulation) spaces:
- [Space C]: [Function]; connects [Space A] to [Space B]
- [Space D]: [Function]; supports primary spaces

Utility spaces:
- [Space E]: [Function]; should not be destination; screen/hide
- [Space F]: [Function]; should be unobtrusive

Visual emphasis:
- [Space A] receives: [Higher ceilings / Better lighting / Distinctive materials]
- [Space C] is subordinate: [Lower ceiling / Neutral materials / Transitional]

Scale relationship:
- Primary: [Scale relative to human]
- Secondary: [Scale relative to primary]
- Utility: [Scale as small as function allows]

Verification:
- Visitor navigation: [First-time visitors naturally gravitate to primary spaces]
- Space usage: [Time-lapse tracking shows expected use patterns]
```

---

## Quality Gates: Spatial Design Level

Before moving to other layers (Interaction, 2D, 3D), verify spatial specifications:

- [ ] Adjacency matrix complete; all spaces documented
- [ ] All spatial connections have documented access control rules
- [ ] Critical dimensions specified with appropriate tolerances
- [ ] All sensory specifications (lighting, acoustics, materials) documented
- [ ] Workflow paths optimized and verified against requirements
- [ ] Wayfinding strategy documented and testable
- [ ] All modular units defined with assembly logic
- [ ] Spatial hierarchy clear and reinforced by design
- [ ] Accessibility requirements (ADA, local codes) explicitly addressed
- [ ] No conflicting requirements; all constraints documented

---

## Integration with Implementation

### For Architects/Builders:
- Specifications in this layer are binding; deviations require design approval
- Tolerance levels indicate precision required; use appropriate measurement tools
- Verify adjacency rules and workflow paths during construction

### For Game Designers:
- Topological specifications translate to level layout and navigation
- Metric specifications scale to in-game units; document scale factor
- Workflow optimization ensures engaging exploration and pacing
- Modular units enable efficient asset creation and performance budgeting

### For Information Architects:
- Spatial specifications apply to virtual "spaces" (screens, states, information zones)
- Topological relationships define navigation between information spaces
- Workflow optimization ensures efficient information discovery

---

## Conclusion

The Spatial Design Framework translates spatial requirements into precise, implementable specifications that define topology, metrics, sensory properties, workflows, and hierarchy. By systematically specifying these dimensions, teams ensure that built or virtual spaces support required workflows, satisfy accessibility requirements, and deliver intended user experiences.

