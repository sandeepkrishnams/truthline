# Project Brief: Truthline

**Document Version:** 1.0  
**Created:** 2025-01-27  
**Status:** Draft

---

## Introduction

This Project Brief serves as the foundational input for the Truthline product development effort. Truthline is a Project Timeline Management Application designed as an Event Timeline Tracking System with consensus-based immutability, threading capabilities, and proof/evidence mechanisms.

### Available Inputs

This brief draws from:
- **Brainstorming Session Results** (2025-01-27) - Comprehensive exploration of system requirements, workflows, risks, and opportunities
- **Existing Project Structure** - Full-stack application with React frontend and FastAPI backend
- **Core Concept** - Event timeline tracking system focused on creating immutable audit trails for disputes and traceability

### Project Context

Truthline addresses the critical problem of "forgetting" - where team members forget what was said, where ideas originated, or have different interpretations even after discussions. The system provides immutable proof through a consensus-based acceptance model, ensuring that key events become permanent records once all tagged parties agree.

---

## Executive Summary

**Product Concept:** Truthline is a consensus-based event timeline tracking system that creates immutable audit trails for project teams, enabling proof/evidence mechanisms through threaded event discussions with conditional immutability once all parties accept.

**Primary Problem:** Teams struggle with "forgetting" - losing track of what was said, where ideas originated, or having conflicting interpretations even after discussions. Existing solutions lack the consensus-based immutability needed to create trustworthy proof for disputes and traceability.

**Target Market:** Project teams, product managers, development teams, and organizations that need reliable audit trails and proof mechanisms for key decisions, feature discussions, and event tracking. Primary users include PMs managing multiple projects, developers tracking feature changes, and team leads requiring evidence for accountability.

**Key Value Proposition:** 
- **Immutable Proof:** Events become permanent, unchangeable records once all tagged parties accept, creating trustworthy evidence
- **Consensus-Based:** No event becomes immutable without explicit acceptance from all relevant parties, ensuring accuracy
- **Threaded Discussions:** Slack/Google Chat-style threading keeps root timeline clean while preserving full context
- **Traceability:** Powerful tagging and search capabilities surface historical events for proof and accountability
- **Timeline Hygiene:** Merge capabilities allow cleanup and summarization while preserving complete history

---

## Problem Statement

### Current State and Pain Points

Teams working on projects face a fundamental challenge: **the problem of forgetting**. This manifests in multiple ways:

1. **Memory Loss:** Team members forget what was said, where ideas originated, or who made specific decisions during discussions
2. **Interpretation Conflicts:** Even after discussions, people have different ideas and interpretations of what was agreed upon
3. **Lack of Proof:** When disputes arise (e.g., "I didn't introduce that feature"), there's no immutable evidence to reference
4. **Context Loss:** Important decisions and discussions get lost in chat histories, email threads, or meeting notes that aren't easily searchable or traceable
5. **Timeline Confusion:** Multiple simultaneous events create confusion, and there's no clean way to merge or organize related discussions

### Impact of the Problem

- **Disputes Without Resolution:** Teams waste time arguing about "who said what" without reliable proof
- **Accountability Gaps:** No way to definitively show responsibility or track decision origins
- **Inefficient Traceability:** Finding historical events requires manual searching through multiple communication channels
- **Timeline Clutter:** Root timelines become messy with arguments and discussions, making it hard to see key events
- **Lost Context:** Critical information about why decisions were made gets forgotten over time

### Why Existing Solutions Fall Short

Current project management and communication tools fail to address this because they:

- **Lack Immutability:** Messages and events can be edited or deleted, destroying proof value
- **No Consensus Mechanism:** There's no way to ensure all parties agree before something becomes permanent
- **Poor Threading:** Most tools don't support Slack/Google Chat-style threading that keeps main timelines clean
- **No Proof System:** They're designed for communication, not for creating immutable audit trails
- **Limited Traceability:** Tagging and search capabilities are insufficient for evidence retrieval
- **No Timeline Hygiene:** No merge capabilities to clean up discussions while preserving history

### Primary Use Case: Software Development Lifecycle Project Management

**Target Industry:** Software development teams and organizations managing SDLC projects

**Specific Scenarios:**
- **Feature Introduction Disputes:** PM denies introducing a feature, developer needs proof it was discussed
- **Decision Traceability:** Track who decided to implement a feature, when, and why - critical for retrospectives and accountability
- **Idea Origin Tracking:** Identify where features originated (client request, team brainstorm, bug fix evolution)
- **Release Planning:** Maintain immutable record of what was agreed for each release, preventing scope creep disputes
- **Sprint Planning Conflicts:** Resolve disagreements about what was committed in sprint planning with proof
- **Client Request Tracking:** When PM represents client requests, developers need proof of original requirements
- **Technical Debt Decisions:** Track when and why technical debt was accepted, who approved it
- **Bug Attribution:** Prove when bugs were introduced and by whom through event timeline

**SDLC-Specific Pain Points:**
- Git commits show "what" but not "why" or "who decided"
- JIRA tickets can be edited, losing original context
- Slack/Teams discussions get lost in long threads
- Meeting notes are not searchable or linked to actual work
- No way to prove feature requests came from specific stakeholders
- Sprint retrospectives lack reliable history of decisions

### Urgency and Importance

This problem is **critical** for software development teams because:

- **Disputes are costly:** Time spent arguing about "who said what" directly impacts sprint velocity and delivery timelines
- **Accountability matters:** Teams need proof mechanisms for performance reviews, client disputes, and internal accountability
- **SDLC complexity:** Software projects involve hundreds of decisions that need traceability
- **Scale amplifies the problem:** As teams grow and projects multiply, the forgetting problem compounds exponentially
- **Compliance needs:** Some organizations require audit trails for decisions and feature changes (especially in regulated industries)
- **Trust requires proof:** Teams can't build trust without reliable evidence of what was agreed upon

The solution is **urgent** because every day without it means more lost context, more disputes without resolution, and more time wasted searching for proof that may not exist.

---

## Competitive Validation

### Comparison with Existing Solutions

**Jira / Linear / Asana:**
- ✅ **Strengths:** Excellent for task tracking, sprint planning, issue management
- ❌ **Gaps:** 
  - No consensus-based immutability - tickets can be edited/deleted
  - No proof mechanism for disputes
  - Comments are mutable, losing audit trail value
  - No threading model for timeline hygiene
  - Focus on "what" not "who decided and why"

**Slack / Microsoft Teams:**
- ✅ **Strengths:** Real-time communication, threading, search
- ❌ **Gaps:**
  - Messages can be edited/deleted
  - No consensus mechanism
  - Not designed for immutable proof
  - Discussions get lost in long threads
  - No event acceptance workflow

**Git / GitHub:**
- ✅ **Strengths:** Immutable commit history, traceability
- ❌ **Gaps:**
  - Shows "what" changed, not "who decided" or "why"
  - No consensus mechanism for decisions
  - Technical focus, not business decision tracking
  - No threading or merge for discussions

**Notion / Confluence:**
- ✅ **Strengths:** Documentation, knowledge management
- ❌ **Gaps:**
  - Pages can be edited, losing original context
  - No consensus-based immutability
  - Not designed for event timeline tracking
  - No proof mechanism for disputes

### Truthline's Unique Value Proposition

**What makes Truthline different:**

1. **Consensus-Based Immutability:** Only Truthline requires explicit acceptance from all tagged parties before events become immutable - ensuring accuracy and buy-in
2. **Proof-First Design:** Built specifically for creating immutable audit trails, not just tracking tasks
3. **Threading + Timeline Hygiene:** Unique merge capability keeps root timeline clean while preserving full history
4. **Event Acceptance Workflow:** Every event requires consensus, creating a systematic proof mechanism
5. **SDLC-Specific:** Designed for software development decision tracking, not generic project management

### Market Validation

**Evidence this approach works:**
- Git's immutable commit history proves immutable records are valuable
- Legal/audit systems rely on immutability for trust
- Consensus mechanisms are proven in blockchain and governance systems
- Threading models (Slack, Discord) show users value organized discussions

**Market Gap:**
- No existing tool combines consensus-based immutability + event timeline tracking + proof mechanisms
- This is a **blue ocean opportunity** - creating a new category rather than competing in existing ones

---

## Proposed Solution

### Core Concept and Approach

Truthline is a **consensus-based event timeline tracking system** designed specifically for software development teams. The solution centers on creating **immutable proof** through a unique acceptance workflow where events become permanent records only after all tagged parties explicitly accept them.

**High-Level Architecture:**
- **Event Timeline:** Root timeline showing key events in chronological order
- **Threading System:** Slack/Google Chat-style sub-threads for discussions, keeping root clean
- **Consensus Engine:** Acceptance workflow requiring all tagged parties to agree before immutability
- **Proof System:** Once accepted, events become immutable audit trail records
- **Timeline Hygiene:** Merge capabilities for cleanup and summarization while preserving history

### Key Differentiators from Existing Solutions

1. **Conditional Immutability Model:**
   - Events are **mutable** until all tagged parties accept
   - After acceptance → **immutable forever** (no exceptions, even for owners/admins)
   - Creates trustworthy proof while ensuring accuracy through consensus

2. **Consensus-Based Acceptance:**
   - Every event requires explicit acceptance from tagged parties
   - Rejection mechanism forces resolution before immutability
   - No auto-acceptance, no bypass mechanisms - systematic proof creation

3. **Threading + Merge Architecture:**
   - Root timeline stays clean with key events
   - Sub-threads preserve full discussion context
   - Merge capability allows timeline hygiene without losing history
   - WhatsApp-style reply tagging creates visual event connections

4. **Proof-First Design:**
   - Built specifically for creating immutable audit trails
   - Tagging system surfaces historical events for evidence
   - Search capabilities optimized for proof retrieval
   - Visual navigation for evidence presentation

5. **SDLC-Optimized Workflows:**
   - Designed for software development decision tracking
   - Handles feature introductions, sprint planning, client requests
   - Tracks "who decided" and "why" not just "what changed"
   - Integrates with development workflow needs

### Why This Solution Will Succeed

**Addresses Core Pain Points:**
- ✅ Solves "forgetting" problem with immutable proof
- ✅ Resolves interpretation conflicts through consensus
- ✅ Provides evidence for disputes
- ✅ Maintains timeline cleanliness with threading
- ✅ Enables traceability through tagging/search

**Unique Market Position:**
- No competitor combines all these features
- Fills gap between task tracking (Jira) and communication (Slack)
- Creates new category: "Proof-Based Project Timeline Management"

**Technical Feasibility:**
- Daily/weekly granularity simplifies database design
- Focus on meaningful events reduces complexity
- Progressive enhancement approach (simple search → AI search)
- Leverages proven patterns (threading, consensus, immutability)

**User Experience:**
- Familiar threading model (Slack/Google Chat)
- Intuitive acceptance workflow
- Visual proof presentation
- Timeline hygiene without context loss

### High-Level Vision

**Short-term (MVP):** Core event timeline with consensus-based acceptance, basic threading, tagging, and search - enabling teams to create immutable proof for key decisions.

**Long-term:** Intelligent timeline with pattern detection, risk scoring, AI-powered search, integrations with development tools, and advanced analytics for project insights.

### Competitive Validation - Deeper Analysis

**Comparison with Established Tools:**

**Jira (Atlassian):**
- **Market Position:** Industry standard for agile project management
- **What They Do Well:** Task tracking, sprint planning, workflow customization, extensive integrations
- **Gap Truthline Fills:** 
  - Jira tickets are editable - no immutable proof
  - Comments can be deleted - loses audit trail
  - No consensus mechanism for decisions
  - Focus on "tasks" not "decisions" or "proof"
  - No threading model for timeline hygiene
- **Risk:** Jira could add immutable mode, but unlikely given their focus on flexibility

**Linear:**
- **Market Position:** Modern, developer-focused issue tracking
- **What They Do Well:** Clean UI, fast performance, GitHub integration
- **Gap Truthline Fills:**
  - Still editable/deletable - no proof mechanism
  - No consensus-based acceptance workflow
  - No threading for discussions
  - Focus on issues/tasks, not decision tracking
- **Risk:** Lower - Linear focuses on speed/efficiency, not proof/audit

**Notion:**
- **Market Position:** All-in-one workspace, documentation
- **What They Do Well:** Flexible documentation, knowledge management
- **Gap Truthline Fills:**
  - Pages are editable - loses original context
  - No event timeline model
  - No consensus mechanism
  - Not designed for proof/evidence
- **Risk:** Very low - Different use case entirely

**GitHub Issues/Projects:**
- **Market Position:** Code-centric project management
- **What They Do Well:** Integrated with code, immutable commit history
- **Gap Truthline Fills:**
  - Issues are editable
  - No consensus mechanism
  - Shows "what" changed (commits) but not "who decided why"
  - No threading model
- **Risk:** Medium - GitHub could add decision tracking, but unlikely to add consensus model

**Key Insight:** None of these tools prioritize **immutable proof** or **consensus-based acceptance**. They optimize for flexibility and collaboration, not audit trails. Truthline's focus on proof creates a defensible niche.

### Edge Case Stress Testing

**Critical Edge Cases Identified:**

1. **Infinite Rejection Loops:**
   - **Scenario:** Tagged party keeps rejecting event, creator keeps editing
   - **Mitigation:** Reject limit (configurable per project), after limit reached → permanent rejection, owner can force-close
   - **Status:** ✅ Handled in design

2. **Team Member Departure Mid-Event:**
   - **Scenario:** Person leaves project while event is pending their acceptance
   - **Mitigation:** Tagged events show as "lost" with closed status, only accepted events remain valid proof
   - **Status:** ✅ Handled in design

3. **Acceptance with Misunderstanding:**
   - **Scenario:** Person accepts event but misunderstood what they're accepting
   - **Mitigation:** Can create new event referencing original, requires their acceptance or owner handles
   - **Status:** ✅ Handled in design

4. **Owner Leaves Project:**
   - **Scenario:** Project owner departs, leaving events in limbo
   - **Mitigation:** Ownership transfer required, super admin can assign new owner if transfer fails
   - **Status:** ✅ Handled in design

5. **Grace Period Abuse:**
   - **Scenario:** Teams configure too-short grace periods, causing premature auto-locking
   - **Mitigation:** Minimum 7 days enforced, system-wide fallback ensures consistency
   - **Status:** ✅ Handled in design

6. **Merge Conflicts:**
   - **Scenario:** Two users create events simultaneously, need to merge
   - **Mitigation:** System shows as distinct initially, merge option available (like git rebase)
   - **Status:** ✅ Handled in design

7. **Tagging After Lock:**
   - **Scenario:** User wants to tag event after it's locked/closed
   - **Mitigation:** Tagging not possible once event locked/closed - prevents post-hoc manipulation
   - **Status:** ✅ Handled in design

8. **Soft Deletion Abuse:**
   - **Scenario:** Creator deletes event to avoid accountability
   - **Mitigation:** Deleted events remain visible, can still be used as proof, restore workflow requires owner confirmation
   - **Status:** ✅ Handled in design

9. **Clarification Sprawl:**
   - **Scenario:** System becomes cluttered with clarification events
   - **Mitigation:** Clarifications solved outside system, only outcomes updated in system
   - **Status:** ✅ Handled in design

10. **Unmergeable Merges:**
   - **Scenario:** User merges events incorrectly, wants to undo
   - **Mitigation:** Merges are irreversible (by design) - prevents timeline manipulation
   - **Status:** ✅ Handled in design

**Unresolved Edge Cases Requiring Further Design:**

1. **Event Priority Conflicts:**
   - **Scenario:** Multiple high-priority events need acceptance simultaneously
   - **Question:** Should there be prioritization in acceptance queue?
   - **Recommendation:** MVP: First-come-first-served, Future: Priority-based inbox

2. **Cross-Project Event References:**
   - **Scenario:** Event in Project A references event in Project B
   - **Question:** Should cross-project tagging be allowed?
   - **Recommendation:** MVP: No, Future: Yes with permissions

3. **Bulk Acceptance:**
   - **Scenario:** PM wants to accept 50 events at once
   - **Question:** Should bulk acceptance be allowed?
   - **Recommendation:** MVP: No (ensures careful review), Future: Yes with confirmation

4. **Event Dependencies:**
   - **Scenario:** Event B depends on Event A being accepted first
   - **Question:** Should dependency chains be enforced?
   - **Recommendation:** MVP: No, Future: Optional dependency tracking

5. **Mobile vs Web Feature Parity:**
   - **Scenario:** Complex merge operations difficult on mobile
   - **Question:** Should mobile have reduced feature set?
   - **Recommendation:** MVP: Web-first, Mobile: View-only, Future: Full parity

**Assumption Stress Tests:**

✅ **Assumption:** Teams will adopt consensus workflow
- **Stress Test:** What if teams find it too slow?
- **Mitigation:** Grace periods and auto-locking prevent blocking, bulk operations available

✅ **Assumption:** Immutability is more valuable than editability
- **Stress Test:** What if teams need to correct mistakes?
- **Mitigation:** Can create correction events, soft deletion allows restoration

✅ **Assumption:** Threading model is familiar enough
- **Stress Test:** What if users don't understand threading?
- **Mitigation:** Progressive disclosure, clear visual indicators, familiar patterns (Slack/Google Chat)

⚠️ **Assumption:** Daily/weekly granularity is sufficient
- **Stress Test:** What if teams need hourly tracking?
- **Risk:** Low - design supports any granularity, but daily/weekly recommended for simplicity

⚠️ **Assumption:** All events need acceptance
- **Stress Test:** What if some events are too trivial?
- **Risk:** Medium - might need "auto-accept" for low-priority events in future
- **Recommendation:** MVP: All events require acceptance (consistent model), Future: Optional auto-accept

---

## Target Users

### Primary User Segment: Product Managers (PMs)

**Demographic/Firmographic Profile:**
- Role: Product Managers, Product Owners, Project Managers in software development organizations
- Experience: Mid to senior level, managing multiple projects/features simultaneously
- Organization Size: Small to enterprise software development teams
- Industry: Software development, SaaS companies, tech startups, digital agencies

**Current Behaviors and Workflows:**
- Manage multiple projects and features concurrently
- Use tools like Jira, Linear, or Asana for task tracking
- Communicate via Slack, Teams, or email for discussions
- Create and track feature requests, client requirements, sprint planning decisions
- Represent client needs to development teams
- Need to prove decisions were made and by whom (especially for client disputes)
- Use # tags to categorize features and track across projects
- Perform bulk operations (closing multiple events) for efficiency

**Specific Needs and Pain Points:**
- **Pain:** Can't prove who introduced a feature when disputes arise
- **Pain:** Client requests get lost or misremembered
- **Pain:** Sprint planning decisions are forgotten or disputed
- **Pain:** Multiple communication channels make it hard to find proof
- **Pain:** Timeline gets cluttered with discussions, hard to see key events
- **Need:** Immutable proof for accountability and client disputes
- **Need:** Clean timeline view with ability to dive into discussions
- **Need:** Search functionality to find historical events quickly
- **Need:** Ability to merge/clean timeline while preserving history
- **Need:** Bulk operations for efficiency (closing events in bulk)

**Goals They're Trying to Achieve:**
- Maintain accountability and proof for all decisions
- Track feature origins and decision history
- Resolve disputes quickly with evidence
- Keep timelines clean and organized
- Efficiently manage multiple projects
- Prove client requests were communicated correctly
- Document sprint planning decisions immutably

**Key Capabilities Needed:**
- Create events and tag relevant team members
- Use # tags for categorization
- Search and find events across projects
- Merge events for timeline hygiene
- Close events in bulk
- Rename threads (doesn't create new event)
- View acceptance status and history

### Secondary User Segment: Developers & Team Leads

**Demographic/Firmographic Profile:**
- Role: Software Developers, Engineering Leads, Tech Leads, Senior Engineers
- Experience: Mid to senior level, working on feature development
- Organization Size: Same as PMs - small to enterprise teams
- Industry: Software development organizations

**Current Behaviors and Workflows:**
- Receive feature requests and requirements from PMs
- Track work in Jira/GitHub/Linear
- Communicate via Slack/Teams for clarifications
- Need to understand "why" decisions were made, not just "what" to build
- Prioritize work manually ("use their brain") - no automated prioritization
- Self-service prioritization expected
- May need to prove bugs weren't their responsibility
- Track when features were introduced and by whom

**Specific Needs and Pain Points:**
- **Pain:** Can't prove PM introduced a feature when PM denies it
- **Pain:** Requirements change but no proof of original agreement
- **Pain:** Sprint commitments disputed after planning
- **Pain:** Need to understand decision context ("why" not just "what")
- **Pain:** Bugs attributed incorrectly without proof
- **Need:** Proof mechanism for accountability
- **Need:** Clear acceptance workflow for requirements
- **Need:** Ability to reject events until requirements are clear
- **Need:** Tag events as proof of decisions
- **Need:** Visual navigation to related events

**Goals They're Trying to Achieve:**
- Prove accountability and responsibility
- Understand decision context and rationale
- Ensure requirements are clear before accepting
- Track feature introductions and origins
- Resolve disputes with evidence
- Maintain clean development workflow

**Key Capabilities Needed:**
- Accept or reject events
- Tag events as proof
- Create events for feature introductions
- View event history and acceptance status
- Navigate threaded discussions
- Search for historical events

### User Segment: Project Owners / Super Admins

**Demographic/Firmographic Profile:**
- Role: Project Owners, Organization Admins, Super Admins
- Experience: Senior level, responsible for project oversight
- Organization Size: Enterprise or multi-project organizations

**Current Behaviors and Workflows:**
- Oversee multiple projects
- Need audit trails for compliance
- Handle ownership transfers
- Escalate abandoned projects

**Specific Needs and Pain Points:**
- **Pain:** No audit trail for decisions
- **Pain:** Projects abandoned when owner leaves
- **Pain:** No way to transfer ownership cleanly
- **Need:** Complete audit trail
- **Need:** Ownership transfer mechanisms
- **Need:** Escalation paths for abandoned projects

**Goals They're Trying to Achieve:**
- Maintain compliance and audit trails
- Ensure project continuity
- Handle edge cases (owner departure, abandoned projects)

**Key Capabilities Needed:**
- Transfer project ownership
- Assign new owners (super admin)
- View complete audit trails
- Handle edge cases

### User Exclusions

**Explicitly NOT Target Users:**
- **Clients/External Stakeholders:** Clients are NOT included in the system. PMs or team members represent client requests internally. No external client access/interface needed.

---

