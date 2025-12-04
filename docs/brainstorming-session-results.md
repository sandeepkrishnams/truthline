**Session Date:** 2025-01-27
**Facilitator:** Business Analyst Mary
**Participant:** User

# Brainstorming Session Results

## Executive Summary

**Topic:** Project Timeline Management Application - Event Timeline Tracking System

**Session Goals:** 
- Deep, structured brainstorm of system requirements, workflows, risks, opportunities, and missing assumptions
- Challenge assumptions, identify contradictions, surface gaps that would cause wasted implementation effort
- Produce actionable insights that reshape assumptions

**Techniques Used:** 
1. Assumption Reversal - Challenged core assumptions about event model
2. Role Playing - Explored stakeholder perspectives
3. Question Storming - Surfaces missing requirements (partial)

**Total Ideas Generated:** 50+ insights across event model, consensus system, permissions, and workflows

### Key Themes Identified:
- **Consensus-Based Immutability:** Events require acceptance from tagged parties, become immutable proof after acceptance
- **Threading Model:** Slack/Google Chat-style threading with root timeline and sub-threads
- **Proof/Evidence System:** Core value proposition - creating immutable audit trail for disputes
- **Grace Periods & Auto-Locking:** Configurable time-based event closure and locking mechanisms
- **Role-Based Permissions:** Selective permissions (merge for PM/Manager/Lead) while keeping bulk operations simple
- **Soft Deletion:** Deleted events remain visible with restoration workflows
- **Merge for Timeline Hygiene:** Summarization and cleanup while preserving full history

---

## Technique Sessions

### Technique 1: Assumption Reversal - "Events as Continuous Streams"

**Description:** Challenged the core assumption that events are discrete points by exploring the reversal: events as continuous streams.

**Key Insights Discovered:**

1. **Core Problem Clarification:**
   - Primary pain: People forget what they said or where ideas originated
   - System purpose: Traceability and memory preservation, not real-time activity monitoring
   - Focus on KEY events (feature changes, ideas introduced) not granular activity (5 commits)

2. **Event Granularity:**
   - Track meaningful business events, not technical minutiae
   - Project lifecycle: May end after production release, but future changes continue
   - Daily/weekly granularity sufficient (not hourly) - simpler DB requirements

3. **Stream Merging Requirement:**
   - Need capability to merge streams when 2 users send different events at same moment
   - System should show these as distinct initially, with merge option

4. **Context Preservation Architecture:**
   - Threading/navigation system: Can create threads for sections, dive into timeline sections, return to root
   - No context loss - full history preserved with navigation capability
   - Timeline sections can be explored independently while maintaining root connection

5. **Technical Simplification:**
   - Daily/weekly basis tracking (not hourly) enables simpler database design
   - Focus on meaningful events reduces storage/complexity concerns

**Notable Connections:**
- The "forgetting" problem suggests need for powerful search/discovery features
- Threading model implies hierarchical event relationships (parent/child)
- Merge capability indicates need for conflict resolution UI/UX
- Daily/weekly granularity suggests batch processing opportunities vs real-time

**Additional Clarifications:**

1. **Search Strategy:**
   - Start with simple search functionality
   - AI-powered search as future enhancement
   - Progressive enhancement approach

2. **Threading Model (Slack/Google Chat Style):**
   - Root = main thread (like chat conversation root)
   - Can create sub-threads from any event
   - Threads can be closed, return to main thread
   - PM can rename threads (doesn't create new event)
   - Thread IDs usable for tagging
   - **Critical Use Case:** Proof/Evidence system - PM denies introducing feature, Lead can tag thread event as proof
   - **Core Problem Refined:** Not just forgetting - people have different ideas/interpretations even after discussion, need immutable proof

3. **Merge Functionality:**
   - Like git rebase - clean history, summarize to single event
   - Used for history cleanup and summarization
   - Merge operation creates consolidated event

4. **"Key Event" Definition:**
   - Not a project management term
   - An event that needs tracking for proof/evidence purposes
   - System must support tracking events specifically for audit trail

5. **Tagging for Historical Events:**
   - Tags can surface very old events
   - Tagging system critical for evidence retrieval

**Deep Dive: Consensus-Based Immutability Model**

1. **Conditional Immutability:**
   - Events are mutable UNTIL both parties accept
   - Once accepted by both parties → immutable, no changes allowed
   - Before acceptance: can edit, delete, modify
   - After acceptance: locked for proof/evidence purposes

2. **View Tracking & Approval System:**
   - Track who viewed events (like modern chat apps)
   - Track who approved events
   - Visibility and approval history visible to all parties

3. **Thread Management:**
   - Can merge event chats within threads
   - Can close events if thread opener AND event owner agree
   - Thread closure requires dual consent

4. **Consensus Requirement:**
   - Event only valid when ALL parties related to event agree
   - Parties can be careful about what they post
   - Other party can reject until all points cleared/added
   - Rejection mechanism forces resolution before event becomes immutable

5. **Soft Deletion Pattern:**
   - Owner can delete event
   - Event remains visible to all parties
   - System shows "deleted by owner" indicator
   - Deletion doesn't remove from timeline, just marks status

6. **Merge for Timeline Hygiene:**
   - Merge creates summarization event
   - Used when arguments/discussions mess up main (root) timeline
   - Owner can merge and create new thread
   - Parties continue chat in new thread
   - All chat history visible to all parties
   - Preserves full context while cleaning root timeline

**Consensus Model Deep Dive:**

1. **Party Definition & Acceptance:**
   - Only tagged people need to agree (not all project members)
   - Owner can close event independently
   - Auto-close: Event closes after new event registered after grace period
   - Auto-lock: Event locks after certain time if no one tagged
   - Grace period mechanism for automatic closure

2. **Rejection Workflow:**
   - Event stays in rejected state, creator can edit and resubmit
   - Reject limit exists - once reached, event stays rejected forever
   - If reject continues, owner can force close
   - Prevents infinite rejection loops

3. **Party Management:**
   - Parties = tagged people
   - Creator can edit to add new tags (people)
   - If someone leaves project mid-event: their tagged events show as "lost" with closed status
   - Handles team member departure gracefully

4. **Merge & Tagging Rules:**
   - Owner or person with permission can merge
   - Once merged, no unmerge possible (irreversible)
   - Tagging works like WhatsApp reply - can tag in main thread or sub-thread
   - Tagging possible after creation BUT not possible once event locked/closed
   - Tagging creates reference links between events

5. **Soft Deletion & Restore:**
   - Deleted events: can still tag, use as proof, comment
   - Restore workflow: Creator can restore within time limit, then owner must confirm
   - All history stored in event metadata
   - Owner responsible if deleted before confirmation
   - Accountability mechanism built in

6. **Acceptance Misunderstanding Resolution:**
   - If someone accepts with misunderstanding: can add new event referencing original
   - New event requires that person to accept OR owner handles
   - Creates correction/clarification event chain
   - Prevents false acceptance from blocking progress

**Configuration & Edge Case Handling:**

1. **Grace Periods & Auto-Locking:**
   - Configurable per project, fallback to system-wide defaults
   - Minimum 7 days enforced (cannot configure less)
   - Prevents too-short grace periods that could cause issues
   - System-wide fallback ensures consistency

2. **Reject Limit:**
   - Configurable per project
   - After permanent rejection, can tag as new event for follow-up
   - Allows fresh start without losing context
   - Prevents infinite loops while preserving ideas

3. **Lost Events (Person Leaves Project):**
   - Only accepted events remain valid proof
   - Rejected events become rejected person's issue/responsibility
   - Accepted events shown before person left remain usable
   - Clear ownership of rejected items

4. **Restore Workflow & Ownership Transfer:**
   - Owner responsibility to handle restores
   - Owner can assign permissions to new person
   - If owner leaving project: ownership must transfer
   - Super admin can add new owner if transfer never happens
   - Escalation path for abandoned projects

5. **Clarification Resolution:**
   - Clarifications should be solved outside the system
   - Final results updated in system by tagging parties
   - Prevents clarification sprawl within system
   - System captures outcomes, not all discussion details

6. **Tagging Mechanics:**
   - Only one event per tag (no multi-event tagging)
   - WhatsApp-style visual connection with movement to event
   - Can show proof that issue is not their responsibility
   - Visual navigation important for proof/evidence use case

---

### Technique 2: Role Playing - Stakeholder Perspectives

**Description:** Exploring the system from different user role perspectives to identify unique needs, pain points, and contradictions.

**Key Insights from Role Exploration:**

1. **PM Capabilities:**
   - Use # tags to categorize features
   - Search functionality for finding events
   - Can close events in bulk
   - Manages multiple projects and features efficiently

2. **Developer Experience:**
   - Prioritization is manual ("use their brain") - no automated prioritization
   - Escalation possible but deferred for simplicity (future feature)
   - Self-service prioritization expected

3. **Client Representation:**
   - Client is NOT included in the system
   - PM or any team member can represent client requests
   - Client-facing events created by internal team members
   - No external client access/interface needed

4. **Event Acceptance Model - CLARIFIED:**
   - ALL events need acceptance - NO EXCEPTIONS
   - Every event requires consensus from tagged parties
   - Consistent model across all event types
   - No auto-acceptance, no bypass mechanisms

5. **Role Equality & Immutability:**
   - All roles are same to the system (no role-based special permissions once locked)
   - Once event becomes permanent/locked: no changes possible
   - Even owner or super admin cannot modify locked events
   - True immutability after lock - no exceptions

6. **Permission Model Clarification:**
   - **Merge:** Role-based permission (PM, Manager, Lead can merge)
   - Merge history tracked: "PM X merged this event" stored in metadata
   - Audit trail for merge operations
   - **Bulk Close:** Available to everyone (simplicity - everyone is busy)
   - Bulk operations kept simple for efficiency
   - Permission complexity minimized where possible

---

### Technique 3: Question Storming - Surface Missing Requirements

**Description:** Generating critical questions to identify gaps, contradictions, and missing requirements before implementation.

**Status:** Session paused - questions generated but not yet explored in depth.

**Critical Questions Identified:**
- Event lifecycle states and transitions
- Event relationships (parent/child, duplicates)
- Timeline intelligence (pattern detection, risk scoring)
- Integration priorities and conflict resolution
- UX details (timeline visualization, mobile vs web)
- Unified inbox prioritization logic

---

## Session Summary

### Major Insights Discovered

1. **Core Value Proposition Clarified:** System is primarily a proof/evidence mechanism, not just a tracker. The "forgetting" problem extends to people having different interpretations even after discussion - system provides immutable proof.

2. **Consensus Model Fully Defined:** 
   - All events require acceptance from tagged parties
   - Conditional immutability (mutable until acceptance, immutable after)
   - Rejection limits and force-close mechanisms
   - Grace periods and auto-locking

3. **Threading Architecture:** Slack/Google Chat model with root timeline, sub-threads, merge capability, and WhatsApp-style reply tagging.

4. **Permission Model:** Selective role-based permissions (merge for leadership roles) while keeping common operations (bulk close) available to all for simplicity.

5. **Edge Cases Handled:** Lost events when people leave, soft deletion with restore workflows, ownership transfer mechanisms, super admin escalation paths.

### Areas Requiring Further Exploration

- Event lifecycle state machine (exact states and transitions)
- Event relationship model (parent/child, duplicates, dependencies)
- Timeline intelligence algorithms (pattern detection, risk scoring formulas)
- Integration architecture (priority, conflict resolution, email-to-event)
- UX specifications (timeline visualization details, mobile feature set)
- Data model (storage strategy, indexing, multi-tenancy)

### Next Steps Recommended

1. Create detailed event lifecycle state diagram
2. Define event relationship model and constraints
3. Specify timeline intelligence requirements
4. Prioritize integrations for MVP
5. Design UX mockups for timeline visualization
6. Design data model schema

---

*Session facilitated using the BMAD-METHOD™ brainstorming framework*

