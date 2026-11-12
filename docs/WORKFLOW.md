# A+ Work Management Workflow

Version: 1.0  
Owner: CEO  
Status: Active — manual pilot, no automation yet

## 1. Single source of truth

- GitHub Issues are the authoritative task records.
- GitHub Pull Requests are the authoritative code-change handoff and review records.
- Files under `team/<name>/TASKS.md` are personal entry points, not duplicate task databases.
- Do not assign work only in chat. If a decision is made in chat, CEO records it as an Issue.
- GitHub Projects board is a useful visual layer; until it is configured, use Issues + labels + assignees as the working queue.

## 2. Task lifecycle

Use exactly one lifecycle label per task:

1. `status:backlog` — idea or unrefined request; nobody should start.
2. `status:ready` — sufficiently specified and available to claim/start.
3. `status:claimed` — assignee acknowledged and confirmed understanding.
4. `status:in-progress` — work has started.
5. `status:review` — deliverable submitted; waiting for reviewer.
6. `status:revision` — reviewer requested changes.
7. `status:done` — accepted and closed by CEO or delegated approver.

A task must have only one `status:*` label. GitHub Issue open/closed state is not a substitute for lifecycle labels: keep it open until accepted, then close it.

## 3. CEO creates and releases work

Every task must include:
- one Directly Responsible Individual (DRI);
- objective and context;
- scope and explicit exclusions;
- inputs/dependencies;
- deliverables and destination path/PR;
- acceptance criteria that can be checked;
- priority and deadline (or explicitly "no fixed deadline");
- reviewer / domain approver.

Create the Issue with `status:backlog` if it needs clarification. Change to `status:ready` only when all essential details are present. Assign one DRI. Collaborators may be listed in the body.

## 4. Staff self-service routine

Each team member is responsible for checking their assigned work:
- At the start of each working session, open their personal TASKS.md and follow its GitHub Issues query.
- Check assigned open Issues and read the full description, comments, linked dependencies and latest decisions.
- For a READY task, comment: `CLAIMED — I understand the objective, deliverables and acceptance criteria. I will flag blockers here.`
- Update labels from `status:ready` to `status:claimed`, then to `status:in-progress` when actual work begins.
- Post a concise progress update when a meaningful milestone is reached, when scope/estimate changes, or when blocked.
- Never silently wait on an unclear requirement. Ask a specific question in the Issue and set/ask CEO to set `status:backlog` if work cannot proceed.
- Before starting, check for newer comments/decisions to avoid working from stale instructions.

For recurring manual pilot, staff should check at the beginning of each work session and at least once each working day when active. This is a process expectation, not an automated notification.

## 5. Collaboration and ownership

- One Issue = one DRI. A collaborator is not a second owner.
- DRI coordinates inputs and integrates feedback.
- Domain claims must be approved by the relevant specialist: Vân Anh for customer psychology, A Long for product-domain truth, Hoàng for technical implementation.
- Trâm Anh prepares research/data and flags uncertainty; specialists validate specialist conclusions.
- If a task crosses domains, CEO names one DRI and one or more reviewers.
- Do not duplicate an existing task; comment on or link the existing Issue.

## 6. Handoff and acceptance

When ready for review, DRI must:
1. add `status:review`;
2. post a handoff comment with summary, changed files/links, evidence/sources, tests/checks, known limitations and unresolved questions;
3. link PRs or artifacts;
4. identify the requested reviewer.

Reviewer checks the acceptance criteria, not just whether a file exists. If changes are needed, write actionable feedback and set `status:revision`. If accepted, CEO or delegated approver sets `status:done` and closes the Issue.

## 7. Priority

- `priority:p0`: urgent project blocker / material integrity or security risk.
- `priority:p1`: current milestone critical path.
- `priority:p2`: useful, but can wait.
- `priority:p3`: backlog / exploration.

Priority does not override dependencies or domain approval.

## 8. Labels

Use team labels: `team:van-anh`, `team:a-long`, `team:hoang`, `team:tram-anh`.  
Use type labels: `type:research`, `type:customer-psychology`, `type:product`, `type:engineering`, `type:operations`, `type:content`, `type:qa`.  
Use lifecycle labels listed in section 2 and priority labels listed in section 7.

If a label has not yet been created in the repository, CEO/repository maintainer must create it before relying on label-based filtering. Do not invent a label and assume GitHub accepted it.

## 9. CEO review cadence

- Daily/each active workday: inspect READY, CLAIMED, IN PROGRESS and blocked tasks.
- Weekly: review each DRI's progress, overdue tasks, dependencies and next deliverables.
- At milestone end: accept/reject outputs, update project decisions and release next tasks.
- Do not create work for staff just to keep them busy; tasks must advance a project decision or deliverable.

## 10. Manual pilot before automation

Run this workflow manually for at least one complete task cycle per staff member. Record friction points (missed tasks, unclear templates, duplicate work, late updates, review bottlenecks). Only then automate notifications, reminders, assignment routing or scheduled polling.

## 11. Useful GitHub queries

Replace the username with the actual GitHub login:
- Assigned open work: `is:open assignee:@me`
- Ready work: `is:open label:"status:ready"`
- In review: `is:open label:"status:review"`
- Blocked/needs clarification: `is:open label:"status:backlog"`
- Overdue tasks: `is:open assignee:@me` plus sort by oldest / inspect due dates.

GitHub Issue due dates are not assumed to exist in this manual workflow; put deadlines in the Issue body and title only when useful.
