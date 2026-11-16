# Core Intelligence Engine
## Design Thinking Methodology & Foundational Framework

**Version:** 1.0  
**Layer:** Foundation (Layer 1)  
**Purpose:** Establish shared understanding, define success criteria, map constraints, and create the cognitive framework for all downstream design work.

---

## Overview

The Core Intelligence layer is where every project begins. Before discussing specific designs, colors, dimensions, or technical architectures, the design team and stakeholders must establish a shared understanding of what success looks like, what constraints exist, and what trade-offs will need to be made.

This layer operates at the level of **design intent**, **strategic positioning**, **stakeholder alignment**, and **constraint mapping**. It answers: "What problem are we solving? Who are we solving it for? What matters most? What are the absolute boundaries?"

---

## Core Intelligence Components

### 1. Design Brief Parsing

**Purpose:** Transform unstructured design intent into a structured decision framework

**Input:** Raw brief (may be: conversation notes, email summary, executive mandate, feature request, complaint, opportunity observation)

**Process:**

#### Step 1A: Intent Extraction
Identify what the brief is *actually* requesting (often different from what it explicitly states).

**Question framework:**
- What problem or opportunity is being addressed?
- What is the stated goal?
- What is the unstated goal (read between the lines)?
- Who asked for this? (reveals stakeholder priority)
- Why now? (reveals market/timing context)
- What would failure look like?
- What would over-delivery look like?

**Example:**
- **Stated:** "We need a mobile app to sell products online"
- **Actual intent:** "We're losing market share to competitors with mobile presence; we need to demonstrate innovation to investors"
- **Insight:** Success isn't just functionality; it's market perception and investor confidence

#### Step 1B: Success Criteria Definition
Define what "done" and "successful" mean quantitatively and qualitatively.

**Criteria categories:**

| Category | Examples | Type |
|----------|----------|------|
| **Market** | Market share growth, customer acquisition cost, brand awareness | Quantitative |
| **Financial** | Revenue target, margin maintenance, ROI timeline | Quantitative |
| **User** | Task completion rate, user satisfaction, learning curve time | Quantitative |
| **Operational** | Support cost reduction, training time, error rate reduction | Quantitative |
| **Strategic** | Competitive differentiation, platform consolidation, capability foundation | Qualitative |
| **Experience** | Delight, intuitiveness, accessibility, inclusivity | Qualitative |

**Documentation format:**
```
SUCCESS CRITERIA

Quantitative:
- User task completion rate: >85%
- Average task time: <3 minutes
- System uptime: 99.9%
- Support ticket volume: <5% of active users/month

Qualitative:
- Users report design as "intuitive" or better
- No feature requests for tasks core to brief
- Competitive differentiation in [specific area]
```

#### Step 1C: Constraint Mapping
Identify all boundaries, limitations, and non-negotiable constraints.

**Constraint categories:**

| Category | Examples |
|----------|----------|
| **Technical** | Platform requirements, API limitations, legacy system integration, performance budgets |
| **Economic** | Budget cap, cost per unit, margin requirements, timeline impact on costs |
| **Temporal** | Launch deadline, seasonal windows, development phases, support lifecycle |
| **Legal/Regulatory** | Compliance requirements, accessibility standards, data protection, licensing |
| **Physical** | Material properties, manufacturing capability, packaging limits, thermal constraints |
| **Organizational** | Team capability, existing infrastructure, vendor lock-in, skill availability |
| **Aesthetic** | Brand guidelines, style expectations, taboo designs, heritage positioning |

**Documentation format:**
```
CONSTRAINTS

Hard constraints (non-negotiable):
- Must launch Q3 2026
- Cannot exceed $X manufacturing cost
- Must meet WCAG 2.1 AA compliance
- Must use existing backend API

Soft constraints (highly desirable):
- Align with brand refresh direction
- Support future expansion to [feature]
- Use preferred vendor ecosystem
- Enable A/B testing capability
```

---

### 2. Stakeholder Analysis

**Purpose:** Map all parties affected by or influencing the design; understand their potentially conflicting priorities

**Stakeholder categories:**

| Category | Responsibilities | Typical Concerns |
|----------|------------------|-----------------|
| **Decision Authority** | Budget approval, go/no-go decisions | Risk, ROI, timeline |
| **End Users** | Daily use, dependent on system working | Ease of use, reliability, speed |
| **Operators/Support** | Day-to-day maintenance, troubleshooting | Understandability, consistency, error handling |
| **Implementers** | Build/fabricate the design | Feasibility, clarity, resources |
| **Ecosystem Partners** | Integration, complementary services | API stability, data formats, performance |
| **Compliance/Legal** | Risk management, regulatory adherence | Safety margins, audit trails, documentation |

**Analysis process:**

#### Step 2A: Stakeholder Mapping
Create a matrix identifying:
- Who each stakeholder is (specific person/role, not generic title)
- What they control or influence
- What their success criteria are
- What their constraints are
- Where conflicts might emerge

**Documentation format:**
```
STAKEHOLDER ANALYSIS

Stakeholder: [Name/Role]
Department: [Organization]
Authority: [What they can approve/block]
Success Criteria:
- Metric 1: [specific target]
- Metric 2: [specific target]
Constraints:
- [Specific limitation]
- [Specific limitation]
Potential Conflicts:
- With [other stakeholder]: [description of conflict]
```

#### Step 2B: Conflict Resolution Framework
Identify stakeholder conflicts in advance and define decision rules for resolution.

**Documentation format:**
```
STAKEHOLDER CONFLICT: [Stakeholder A] vs [Stakeholder B]

Conflict: [Describe the conflicting interests]

Decision Rule:
- Priority: [Which stakeholder wins when there's a head-to-head conflict]
- Trade-off: [What the lower-priority stakeholder gets in exchange]
- Verification: [How we know we've achieved the compromise]

Example: If cost and feature completeness conflict, feature completeness wins
for the initial release (satisfying product team and users), but we commit
to cost optimization in V1.1 (satisfying finance).
```

---

### 3. Problem Space Definition

**Purpose:** Thoroughly understand the problem being solved, independent of any solution

**Process:**

#### Step 3A: Problem Decomposition
Break the problem into its component parts.

**Questions:**
- What is the root problem (not the symptom)?
- What are the immediate causes?
- What are the contributing factors?
- Who experiences the problem? (quantify if possible)
- What is the cost of the problem? (quantify in time/money/risk)
- What are unsuccessful attempts to solve it?
- Why did those attempts fail?

**Documentation:**
```
ROOT PROBLEM ANALYSIS

Symptom Presented: [What people initially complain about]

Root Problem: [The underlying issue]

Contributing Factors:
1. [Factor]: [Evidence]
2. [Factor]: [Evidence]

Current Impact:
- Affects [X] users/processes
- Costs ~$[amount] annually
- Causes [secondary problems]

Failed Solutions:
- Attempt 1: [Description] → Failed because [reason]
- Attempt 2: [Description] → Failed because [reason]
```

#### Step 3B: User Context Analysis
Understand the human context in which the problem occurs.

**Analysis dimensions:**
- **Frequency:** How often does the problem occur? In what patterns?
- **Triggers:** What conditions precede the problem?
- **Workarounds:** How do people currently work around the problem?
- **Pain points:** What about the current situation frustrates users?
- **Environment:** What is the physical/organizational/technical environment?
- **Skill level:** What is the user's expertise level?
- **Motivation:** Why should users care about solving this?

---

### 4. Design Vision & Strategic Positioning

**Purpose:** Define the strategic direction and core philosophy that will guide all design decisions

**Vision statement format:**
```
DESIGN VISION

We will create [solution category] that [transforms/enables/prevents] [outcome]
by [core mechanism], resulting in [strategic position].

For [primary user], who [problem/need], [solution name] is a [category] that
[key benefit]. Unlike [alternatives], it [core differentiator].

Core Philosophy:
1. [Design principle 1]: We believe [principle]. Therefore we will [decision rule].
2. [Design principle 2]: We believe [principle]. Therefore we will [decision rule].
3. [Design principle 3]: We believe [principle]. Therefore we will [decision rule].
```

**Example:**
```
DESIGN VISION

We will create a game experience that enables solo players to experience
meaningful multiplayer moments through asynchronous interaction, resulting
in a bridge between single-player intimacy and multiplayer community.

For casual players, who lack time for real-time multiplayer but crave
social connection, our game is an asynchronous action-RPG that delivers
the thrill of competition without synchronized playtime requirements.
Unlike traditional multiplayer games requiring real-time presence, it
enables achievement of social goals through strategic positioning and
discovery of others' play patterns.

Core Philosophy:
1. Asynchrony as feature: We believe meaningful moments don't require real-time
presence. Therefore we will design every interaction to work with 1-hour to
1-week delays between actions.

2. Discovery over direction: We believe the best moments are unexpected. Therefore
we will minimize explicit competition invitations and maximize serendipitous
encounters.

3. Time respect: We believe players' real-world time is valuable. Therefore we
will design zero-grind progression and provide meaningful gameplay in <30-minute
sessions.
```

---

### 5. Assumption Documentation

**Purpose:** Explicitly state all assumptions about users, technology, market, and operations

**Assumption categories:**

| Category | Examples |
|----------|----------|
| **User Assumptions** | Target user demographics, user mental models, learning ability, accessibility needs |
| **Market Assumptions** | Market size, adoption rate, competitive positioning, price elasticity |
| **Technical Assumptions** | Platform maturity, API availability, performance feasibility, integration compatibility |
| **Organizational Assumptions** | Team capability, vendor reliability, infrastructure availability, timeline feasibility |
| **Economic Assumptions** | Cost estimates, revenue potential, margin targets, timeline impact on costs |

**Documentation format:**
```
ASSUMPTION: [Description]
Type: [Category]
Confidence Level: [High/Medium/Low]
Evidence: [What supports this assumption]
Risk if wrong: [What breaks if this assumption is incorrect]
Verification method: [How we'll validate this assumption]
Timeline: [When we need this assumption validated]
```

**Example:**
```
ASSUMPTION: Users have internet connectivity at point of use
Type: Technical
Confidence Level: Medium
Evidence: 92% of target market has smartphone, 85% have home internet
Risk if wrong: 15% of market segment cannot use product
Verification method: Conduct usage testing in lower-connectivity areas
Timeline: Before Beta launch (need 2 weeks minimum testing)
```

---

### 6. Requirements Hierarchy Definition

**Purpose:** Establish priority framework for conflicting requirements

**MoSCoW framework:**
- **Must have:** Non-negotiable; product doesn't ship without it
- **Should have:** Highly desirable; major value loss if absent; must ship V1
- **Could have:** Nice to have; ships in V1.1 or later
- **Won't have:** Explicitly deferred or rejected; potential for future reconsideration

**Example:**

| Priority | Requirement | Rationale |
|----------|-------------|-----------|
| **Must** | Load time <2 seconds | Performance critical for adoption; above this is unusable for target users |
| **Should** | Mobile responsiveness | 60% of traffic is mobile; must work for primary user segment |
| **Could** | Offline mode | Useful, but 95% of usage is in connected environments |
| **Won't** | Localization | English-only market initially; reconsider with market expansion |

---

### 7. Decision Documentation Framework

**Purpose:** Create a record of major design decisions and their rationale

**Documentation format:**
```
DESIGN DECISION: [Title]
Date: [Date]
Stakeholders: [Who participated]
Decision: [What was decided]
Alternatives considered: [Other options evaluated]
Rationale: [Why this decision]
Tradeoffs: [What we gave up]
Reversibility: [How hard is it to change this later]
Assumptions: [What needs to be true for this decision to remain valid]
Verification: [How we'll know if this was the right choice]
```

**Example:**
```
DESIGN DECISION: Mobile-first architecture vs. desktop-first
Date: 2026-02-15
Stakeholders: Product Manager, Lead Designer, Lead Engineer, Analytics
Decision: Implement mobile-first responsive design with progressive enhancement
to desktop features

Alternatives considered:
1. Desktop-first with mobile compromise
2. Separate mobile app + responsive web
3. Single responsive design with mobile limitations

Rationale:
- 65% of target users access via mobile exclusively
- Engineering team has React Native expertise but limited desktop experience
- Market trends show declining desktop usage in target demographic

Tradeoffs:
- Desktop experience not fully optimized (acceptable per stakeholder agreement)
- Requires responsive CSS expertise (we have this in-house)
- Future desktop feature additions require responsive rethinking

Reversibility: Moderate difficulty. Would require redesign, not code restructure.
Timeline: 3-4 weeks if reconsidered post-launch

Assumptions:
- Target user demographics remain skewed toward mobile
- Responsive CSS frameworks remain stable and performant

Verification:
- Monitor desktop user growth; if >40% by Q4, reconsider
- A/B test desktop feature completeness; if >40% adoption, expand desktop
```

---

## Quality Gates: Core Intelligence Level

Before moving to the Discipline Router (Layer 2), verify:

- [ ] Design brief has been parsed into explicit intent, not just rephrased
- [ ] Success criteria are quantified (or explicitly noted as qualitative with subjective validation method)
- [ ] All stakeholders have been identified and their success criteria documented
- [ ] Stakeholder conflicts have been explicitly identified and resolution rules established
- [ ] Root problem has been defined (not symptoms)
- [ ] Design vision is documented and approved by decision authority
- [ ] All major assumptions have been documented with confidence levels and verification methods
- [ ] Requirements have been prioritized using MoSCoW or similar framework
- [ ] Constraints have been explicitly mapped and severity assessed
- [ ] At least 3 major design decisions have been anticipated and documented with rationale

---

## Common Pitfalls

### Pitfall 1: Skipping the Brief
**Symptom:** "We've already done discovery, let's just start designing"  
**Risk:** Design decisions made without shared understanding; rework when stakeholders see drafts  
**Recovery:** Invest 1-2 weeks in Core Intelligence; it prevents 3-4 weeks of rework

### Pitfall 2: Implicit Assumptions
**Symptom:** "Everyone knows the target user is busy professionals"  
**Risk:** Design optimized for wrong persona; major rework when real users differ  
**Recovery:** Document all assumptions explicitly; test at least 3 before detailed design

### Pitfall 3: Unacknowledged Conflicts
**Symptom:** Stakeholder pushback mid-project: "This isn't what I expected"  
**Risk:** Scope creep, timeline delays, stakeholder frustration  
**Recovery:** Conduct explicit conflict identification and resolution framework upfront

### Pitfall 4: Vague Success Criteria
**Symptom:** "The design should feel modern and intuitive"  
**Risk:** Cannot verify success; scope creep from differing interpretations  
**Recovery:** Translate every qualitative criterion to measurable proxy; define subjective validation method

---

## Integration with Downstream Layers

### Outputs that feed Layer 2 (Discipline Router)
- Design vision and strategic positioning
- Problem definition and scope
- User context understanding
- Assumption inventory

### Outputs that feed Layer 3 (Requirement Discovery)
- Success criteria
- Stakeholder needs and constraints
- Decision framework and priorities
- Traceability: requirements back to this layer's decisions

---

## Revisiting Core Intelligence

For ongoing projects, return to this layer when:
- Stakeholder composition changes (new decision authority, new user segment)
- Market conditions shift (new competitor, regulatory change)
- Assumption validation contradicts initial assumptions
- Major mid-project pivots are proposed

Minor feature additions don't require Core Intelligence review; major scope changes do.

---

## Tools & Templates

### Template 1: Design Brief Canvas
A one-page summary of all Core Intelligence work:
```
PROJECT: [Name]
VISION: [1-2 sentences]
PRIMARY USER: [Description]
PROBLEM: [What we're solving]
SUCCESS METRICS: [3-5 quantified criteria]
KEY CONSTRAINTS: [3-5 hard constraints]
STAKEHOLDER CONFLICTS: [Known conflicts and resolution rules]
MAJOR ASSUMPTIONS: [3-5 critical assumptions to validate]
```

### Template 2: Stakeholder Priority Matrix
Map stakeholder needs in a decision-making framework:
```
            User Value    Business Value    Feasibility
Feature A       High          Medium           High
Feature B       Medium        High            Low
Feature C       High          Low             Medium
...
Priority: Features in (High, High) quadrant are Must-Have
```

---

## Conclusion

The Core Intelligence layer is where design discipline begins. By establishing shared understanding, explicit success criteria, stakeholder alignment, and decision frameworks before detailed design work begins, teams eliminate the ambiguity that causes rework and conflict. This layer takes 10-15% of project time upfront but saves 20-30% of time downstream through eliminated rework and faster decision-making.

