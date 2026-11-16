# Requirement Discovery Engine
## Systematic Discovery of Explicit & Implicit Requirements

**Version:** 1.0  
**Layer:** Requirements (Layer 3)  
**Purpose:** Discover, document, and prioritize all requirements that must be satisfied by the design and implementation.

---

## Overview

Requirement Discovery transforms the strategic intent from Layer 1 and discipline identification from Layer 2 into a comprehensive matrix of testable, traceable requirements. The output is not a requirements document alone, but a **requirements graph** where each requirement is connected to:
- Its source (which stakeholder, which design decision, which constraint)
- Its dependencies (which other requirements must be satisfied first)
- Its conflicts (which requirements are in tension with it)
- Its verification method (how we know when it's satisfied)
- Its priority level (MoSCoW categorization)

---

## Requirement Categories

### Category 1: Functional Requirements
**What users/systems must be able to do**

Functional requirements describe capabilities—what the design must enable or prevent.

**Question framework:**
- What tasks must users be able to accomplish?
- What decisions must systems be able to make?
- What actions must be preventable or restricted?
- What workflows must be supported?
- What data must be accessible?
- What integrations with external systems are required?

**Documentation format:**
```
FUNCTIONAL REQUIREMENT: [Short name]
Description: User must be able to [action] in order to [achieve goal]

Acceptance Criteria:
- Given [precondition], when [action], then [result]
- [Additional acceptance criteria]

Related to:
- Stakeholder need: [Which stakeholder's success criteria this serves]
- Source requirement: [Design decision from Layer 1]
- Dependencies: [Other requirements that must be satisfied first]

Conflict: [Other requirements that compete with this]
```

**Example:**
```
FUNCTIONAL REQUIREMENT: Offline work capability
Description: Users must be able to view cached content and compose messages offline,
to maintain productivity in areas with poor connectivity

Acceptance Criteria:
- Given: App is opened in airplane mode
  When: User navigates to previously-viewed article
  Then: Article displays from local cache with <500ms load time
- Given: User is offline
  When: User composes message and taps Send
  Then: Message queues locally and displays "Pending" status

Related to:
- Stakeholder need: "Users need to work during commute" (Product Manager)
- Source requirement: MoSCoW Should-Have from Layer 1
- Dependencies: Local database schema must be designed; sync logic must be robust

Conflict: Offline capability increases app size (20MB vs. 50MB offline-capable)
        Trade-off: Accept larger size for target user segment
```

---

### Category 2: Performance Requirements
**What measurable outcomes must be achieved**

Performance requirements define quantifiable properties: speed, accuracy, capacity, reliability, durability.

**Performance dimensions:**

| Dimension | Examples | Measurement |
|-----------|----------|-------------|
| **Speed** | Load time, response time, rendering framerate | Milliseconds, seconds, FPS |
| **Throughput** | Requests per second, transactions per minute | Operations / time unit |
| **Capacity** | Concurrent users, data storage, file sizes | Count, GB, MB |
| **Accuracy** | Error rate, precision, false positive rate | Percentage, PPM |
| **Reliability** | Uptime, mean time to failure, recovery time | Percentage, hours |
| **Durability** | Product lifespan, data persistence, wear | Years, cycles |
| **Latency** | Network delay, database query time, synchronization | Milliseconds |

**Documentation format:**
```
PERFORMANCE REQUIREMENT: [What property]
Metric: [Specific measurement]
Target: [Quantified goal]
Measurement method: [How we'll verify]

Rationale: [Why this target matters]
- Impact if missed: [Consequence of underperformance]
- Impact if over-specified: [Cost of unnecessary excess]

Verification:
- Testing method: [How we'll test this in development]
- Production monitoring: [How we'll track this post-launch]
- SLA: [Service level agreement for production]

Trade-offs: [What we give up to achieve this]
```

**Example:**
```
PERFORMANCE REQUIREMENT: Page load time
Metric: First Contentful Paint (FCP) on 4G network
Target: <1.5 seconds for 90th percentile of users
Measurement method: RUM (Real User Monitoring) data

Rationale:
- 1.5 seconds chosen based on research: conversion rates drop ~7% per second of delay
- Target users on mobile 4G (not fiber); 1.5s realistic but demanding
- Impact if missed: 10%+ conversion loss; $500K annual revenue impact
- Impact if over-specified: Requires aggressive image optimization, expensive CDN

Verification:
- Development: Lighthouse CI on every commit; must maintain green
- Staging: Load testing with realistic traffic patterns
- Production: Real User Monitoring dashboard; alert on <85th percentile crossing
- SLA: 95% of page loads <2 seconds; alert on 100 consecutive loads >2s

Trade-offs:
- Requires 10MB CDN budget annually (vs. $0 for unoptimized)
- Restricts feature additions that increase payload
- Requires mobile-first development discipline
```

---

### Category 3: Constraint Requirements
**What boundaries cannot be crossed**

Constraint requirements are hard limits set by technical, economic, legal, or organizational factors.

**Constraint sources:**
- Technical: API limitations, platform capabilities, legacy system compatibility
- Economic: Budget cap, cost per unit, margin requirements
- Temporal: Deadline, project phases, release schedule
- Legal: Compliance requirements, accessibility standards, data protection
- Organizational: Team capability, vendor availability, infrastructure limits
- Physical: Material properties, manufacturing capability, space availability

**Documentation format:**
```
CONSTRAINT: [What is bounded]
Type: [Technical/Economic/Temporal/Legal/Organizational/Physical]
Boundary: [The limit]
Enforcer: [Who/what sets this constraint]

Severity: [Hard/Soft]
- Hard: Non-negotiable; feature doesn't ship without respecting this
- Soft: Highly desirable; ships with constraint violation only as last resort

Verification:
- How we'll verify constraint is respected: [Testing or review method]
- Consequence if violated: [What breaks]
- Mitigation if unavoidable: [Plan if constraint must be violated]

Flexibility: [Can this constraint change? Under what conditions?]
```

**Example:**
```
CONSTRAINT: Manufacturing cost per unit
Type: Economic
Boundary: $45 maximum cost of goods sold (COGS)
Enforcer: Finance (margin target: 60% gross margin)

Severity: Hard
- Consequence if violated: Business model broken; cannot sell at target price
- Mitigation: If material costs exceed $45, project pauses until cost-down engineering complete

Verification:
- Design review must include cost estimates for all custom parts
- Supplier quotes obtained for all major components before design finalization

Flexibility:
- Can increase to $50 only with explicit approval from CFO
- Can decrease to $40 to unlock new price point; requires engineering timeline extension
- Review quarterly as supplier costs change
```

---

### Category 4: Quality Attributes
**How well requirements must be satisfied**

Quality attributes describe non-functional properties: how well the system performs, how easy it is to maintain, how accessible it is, how well it scales.

**Quality attribute categories:**

| Attribute | Definition | Examples |
|-----------|-----------|----------|
| **Usability** | How easily users learn and use the system | Learnability, error prevention, accessibility |
| **Reliability** | How consistently the system works | Error rate, uptime, mean time to failure |
| **Maintainability** | How easily developers modify the system | Code clarity, test coverage, documentation |
| **Scalability** | How well it grows with demand | Concurrent users, data volume, geographic scale |
| **Security** | How well it protects data and user privacy | Encryption, authentication, audit trails |
| **Performance** | How fast and responsive it is | Load time, latency, throughput |
| **Portability** | How well it works across platforms | iOS/Android, web browsers, devices |
| **Interoperability** | How well it integrates with external systems | API compatibility, data formats, standards |

**Documentation format:**
```
QUALITY ATTRIBUTE: [Attribute name]
Definition: [What this means for our project]

Target level: [Specific, measurable target]

Implications:
- Design impact: [How this affects design decisions]
- Technical impact: [How this affects architecture]
- Cost impact: [Budget or timeline implications]

Verification:
- How we'll measure or evaluate this: [Assessment method]
- When we'll evaluate: [During development? Pre-launch? Both?]
```

**Example:**
```
QUALITY ATTRIBUTE: Accessibility (WCAG 2.1 AA compliance)
Definition: All users, including those with disabilities, can operate the interface
           and understand all content without adaptation

Target level: 100% WCAG 2.1 AA compliance; no WCAG AAA requirements

Implications:
- Design impact: Color contrast ratios constrained (4.5:1 for normal text);
                 require keyboard navigation for all interactions; alt-text
                 for every image
- Technical impact: Semantic HTML required; screen reader testing each release;
                   automated accessibility testing in CI/CD
- Cost impact: ~15% design and development time; ongoing QA effort

Verification:
- Automated testing (axe DevTools) on every commit
- Manual screen reader testing (NVDA, JAWS) monthly
- Annual third-party accessibility audit
- Pre-launch: 1-week accessibility testing with disabled users
- Production: User feedback tracking for accessibility issues
```

---

### Category 5: Implicit Requirements
**What must be true for stated requirements to work**

Implicit requirements are often unspoken; they're the tacit knowledge that makes explicit requirements feasible.

**Discovery questions:**
- What infrastructure must exist for this requirement to work?
- What knowledge or capability must the user/operator have?
- What external systems must function reliably?
- What data must be accurate and current?
- What assumptions underlie this requirement?

**Common implicit requirements:**
- Data quality and freshness requirements
- User knowledge and training requirements
- Infrastructure and operational requirements
- Integration and synchronization requirements
- Maintenance and support requirements

**Documentation format:**
```
IMPLICIT REQUIREMENT: [Name]
Description: [What must be true, often unstated]

Underlying explicit requirement: [Which explicit requirement depends on this]

Who/what provides this: [Who's responsible for this]

Verification:
- How we'll know this is provided: [Assessment method]
- Consequence if not provided: [Impact on explicit requirement]

Documentation: [Where is this documented/validated]
```

**Example:**
```
IMPLICIT REQUIREMENT: Real-time customer data currency
Description: Customer profile data displayed in UI must be less than 1 minute stale,
            even under high concurrent user load

Underlying explicit requirement:
- "Users can view their current account balance"
- "Users can update profile in app and see changes immediately"

Who/what provides this:
- Backend sync service (must push updates to cache within 1 minute)
- Database replication (must keep read replicas <1 minute behind primary)
- CDN cache (must invalidate when customer data updates)

Verification:
- Measure cache staleness: max acceptable age = 60 seconds
- Load test: 1000 concurrent users; verify 95th percentile staleness < 60s
- Production monitoring: dashboard showing current cache age

Consequence if not provided:
- If data is 5+ minutes stale: users see incorrect balances; trust eroded
- If system can't handle concurrent load: response times degrade; timeouts
```

---

## Requirement Discovery Process

### Phase 1: Stakeholder Requirements Mining (Week 1)
**Conduct interviews with each stakeholder** (identified in Layer 1) to surface their requirements.

**Interview structure:**
1. **Context setting:** "What problem are you trying to solve?"
2. **Existing state:** "How do you currently handle this?"
3. **Desired state:** "What would ideal look like?"
4. **Pain points:** "What about current state frustrates you?"
5. **Success criteria:** "How would you know this succeeded?"
6. **Constraints:** "What must stay the same? What can't change?"
7. **Dependencies:** "What else needs to happen for this to work?"

**Output:** Raw requirements list (often contradictory, unstructured)

### Phase 2: Discipline-Specific Requirements (Week 2-3)
**For each discipline identified in Layer 2**, conduct systematic requirements discovery.

**Method:** Refer to Layer 4-7 reference documents for discipline-specific discovery frameworks.

**Example discovery activities by discipline:**
- **Interaction Design:** User flow mapping, task analysis, accessibility audit
- **Spatial Design:** Ergonomic studies, clearance requirements, workflow observation
- **Service Design:** Journey mapping, service blueprint creation, touchpoint analysis
- **Information Architecture:** Taxonomy development, metadata requirements, search term analysis
- **Product Design:** Ergonomic testing, material analysis, manufacturing capability review
- **Technical Specifications:** API capability audit, performance characterization, infrastructure review

**Output:** Discipline-specific requirement sets

### Phase 3: Requirements Synthesis (Week 3)
**Consolidate** stakeholder and discipline-specific requirements into unified matrix.

**Activities:**
1. Identify overlapping requirements (combine into single requirement)
2. Identify conflicting requirements (flag for stakeholder decision)
3. Categorize requirements (Functional, Performance, Constraint, Quality Attribute, Implicit)
4. Assign priorities (MoSCoW: Must/Should/Could/Won't)
5. Create traceability links (requirement → stakeholder → design decision)

### Phase 4: Requirements Validation (Week 4)
**Verify requirements are complete, unambiguous, and feasible.**

**Validation activities:**
1. **Completeness audit:** Every project aspect covered? Every stakeholder represented?
2. **Ambiguity check:** Every requirement testable/measurable? No "should"/"might"/"try" language?
3. **Feasibility review:** Technical review confirms no obviously infeasible requirements?
4. **Consistency check:** No contradictions? Conflicts explicitly acknowledged?
5. **Stakeholder sign-off:** Decision authority approves final requirements matrix?

**Output:** Validated requirements matrix, ready for specification layer work (Layers 4-7)

---

## Traceability Matrix Structure

```
TRACEABILITY MATRIX

Requirement ID: REQ-001
Category: Functional
Priority: Must Have
Description: [Requirement statement]

Source:
- Stakeholder: [Who needs this]
- Design Decision: [Which decision from Layer 1]
- Design Principle: [Which principle guides this]

Dependencies:
- Requires: [Other requirements that must be satisfied first]
- Enables: [Which requirements this unblocks]
- Conflicts with: [Contradictory requirements; resolution method]

Verification:
- Test method: [How we'll verify this is satisfied]
- Acceptance criteria: [Definition of success]
- Measurement: [How we'll know if it's working post-launch]

Implementation mapping:
- Specification layer: [Which layer 4-7 addresses this]
- Component: [Which component implements this]
- Test case: [Which test verifies this]
```

---

## Common Pitfalls

### Pitfall 1: Implicit → Explicit Gap
**Symptom:** "The requirement seems clear to us but the implementation team interprets it differently"  
**Root cause:** Implicit assumptions not documented  
**Fix:** For every requirement, ask "what must be true for this to work?" and document answers

### Pitfall 2: Unmeasurable Requirements
**Symptom:** "The system should be fast and intuitive"  
**Root cause:** Qualitative requirements without quantitative translation  
**Fix:** Translate every qualitative requirement to measurable proxy; define subjective validation method

### Pitfall 3: Orphaned Requirements
**Symptom:** "We discovered a requirement but no one knows if it's addressed in the design"  
**Root cause:** Broken traceability links  
**Fix:** Maintain traceability matrix throughout project; every requirement maps to implementation

### Pitfall 4: Conflicting Requirements Without Resolution
**Symptom:** "One stakeholder wants X, another wants Y; we can't satisfy both"  
**Root cause:** Conflicts not escalated to decision authority early  
**Fix:** Identify and document conflicts; require stakeholder decision before moving forward

---

## Integration with Specification Layers (4-7)

Each specification layer should:
1. Take input from this layer's requirements matrix
2. Add layer-specific detail and decision-making
3. Trace every specification back to source requirement (maintaining traceability)
4. Flag any requirement that cannot be addressed within the layer's scope

---

## Quality Gates: Requirement Discovery Level

Before moving to specification layers (4-7), verify:

- [ ] All stakeholders have been interviewed
- [ ] All disciplines have contributed requirements
- [ ] Every requirement is testable or has measurable proxy
- [ ] No "should," "might," "try" language in requirements
- [ ] Conflicts identified and resolution methods documented
- [ ] All implicit requirements surfaced and documented
- [ ] Traceability matrix complete (every requirement → source)
- [ ] Feasibility review completed by technical team
- [ ] Stakeholder sign-off obtained
- [ ] MoSCoW prioritization complete

---

## Conclusion

Requirements discovery is where ambiguous intent becomes testable criteria. By systematically discovering functional, performance, constraint, and quality attribute requirements, by identifying implicit assumptions, and by maintaining traceability throughout the project, teams ensure that implementation work produces designs that satisfy stakeholders and users. This layer typically takes 3-4 weeks and prevents 4-8 weeks of rework from missed requirements.

