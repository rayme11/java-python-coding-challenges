# SRE Interview Question Bank — with Model Answers

Organized by theme. The "say it out loud" rule: if you can't answer smoothly
without reading, you don't know it yet. Each answer references the day that
builds it.

---

## 1. SRE Fundamentals

**Q: What's the difference between an SLI, SLO, and SLA?** *(Day 02)*
> An **SLI** is the measured indicator — e.g., "percentage of HTTP requests
> returning < 300ms over a rolling 30 days." An **SLO** is the internal target
> on that SLI — "99.9% of requests < 300ms." An **SLA** is the external,
> contractual version with consequences — usually looser than the SLO, because
> the SLO is your early-warning buffer. The gap between 100% and your SLO is
> the **error budget**, which is what lets you ship features aggressively when
> you're healthy and forces you to prioritize reliability when you're burning
> budget.

**Q: How do you balance reliability against shipping speed?** *(Day 02)*
> Error budgets make it objective instead of political. If we're at 99.95%
> against a 99.9% SLO, the budget says yes to risky launches. If we've burned
> the budget, feature work pauses and reliability work takes priority — and
> that policy is agreed with product *before* the incident, not during it.

**Q: What is toil, and what do you do about it?** *(Day 03)*
> Toil is manual, repetitive, automatable work that scales linearly with the
> service — ticket-driven restarts, manual failovers. Google's target is keeping
> toil under 50% of an SRE's time. You track it, then systematically automate it
> away — every repeated manual runbook step is an automation backlog item.

**Q: What is a blameless postmortem?** *(Day 27)*
> A post-incident review that focuses on *what* failed in the system and
> process, never *who*. The assumption: people made reasonable decisions with
> the information they had. Output is action items that change the system —
> better alerts, guardrails, runbooks — not blame. If engineers fear blame,
> they hide mistakes, and incidents repeat.

---

## 2. Observability & Monitoring

**Q: How do you decide what to alert on?** *(Day 07)*
> Alert on **symptoms that affect users**, not causes. "Error rate > 2% for
> 5 minutes" pages someone; "CPU at 80%" usually doesn't — it might be fine.
> Every alert must be actionable: if there's no runbook step, it shouldn't page.
> Causes belong on dashboards for diagnosis; symptoms page humans. Then you
> continuously tune: alerts that fire without action get deleted or
> re-thresholded — that's the alert-fatigue death spiral you must avoid.

**Q: Prometheus vs Azure Monitor — when would you use each?** *(Day 18)*
> Azure Monitor/App Insights is the managed, zero-ops choice — great for Azure
> resources, application traces, and KQL-based log analytics. Prometheus is the
> CNCF standard for Kubernetes-native metrics: pull-based scraping, PromQL,
> huge exporter ecosystem. In practice on AKS you run both: Azure Monitor
> container insights for platform data, Prometheus (often Azure Managed
> Prometheus) + Grafana for app-level metrics and rich dashboards.

**Q: Walk me through debugging "the site is slow."** *(Days 06–07)*
> Start with the SLO dashboard: which SLI is violated — latency, errors,
> saturation? Then drill: App Insights **end-to-end transaction view** shows
> which dependency is slow (DB? downstream API?). Correlate with recent
> deployments — most incidents are change-related. Check saturation metrics
> (CPU, memory, connection pools, queue depth). Form a hypothesis, verify with
> a KQL query, mitigate first (roll back / scale out), root-cause second.

---

## 3. Distributed Systems

**Q: Explain the CAP theorem in practical terms.** *(Day 21)*
> Under a network **partition**, a distributed system must choose between
> **consistency** (reject writes rather than serve stale data) and
> **availability** (keep serving, risk divergence). In practice partitions are
> rare, so the real question is what you trade *during* one: a payments system
> picks consistency; a social feed picks availability. It's also not binary —
> per-operation choices, quorums, and tunable consistency let you mix.

**Q: Why does idempotency matter, and how do you implement it?** *(Day 21)*
> Networks retry, clients double-click, message queues deliver at-least-once —
> so the same operation can arrive twice. An idempotent operation is safe to
> repeat: charging a card with an idempotency key processes once no matter how
> many retries. Implementation: client generates a unique key per logical
> operation; the server stores the key with the result and returns the stored
> result on duplicates instead of re-executing.

**Q: At-least-once vs exactly-once delivery?** *(Day 22)*
> Exactly-once *delivery* across a network is effectively impossible in the
> general case — the Two Generals problem. What systems actually provide is
> at-least-once delivery + idempotent processing, which *behaves* like
> exactly-once. Some brokers (Service Bus sessions, Kafka transactions)
> provide effectively-once within narrow scopes. Design consumers to be
> idempotent and you stop caring which guarantee the broker gives.

**Q: How do you make a service fault-tolerant?** *(Day 14)*
> Assume dependencies fail. Techniques: **timeouts** on every call (no
> unbounded waits), **retries with exponential backoff + jitter** for transient
> faults, **circuit breakers** to stop hammering a failing dependency and fail
> fast, **bulkheads** to isolate failure domains, **fallbacks/degraded mode**
> for non-critical features, and **health probes** so the load balancer routes
> around sick instances. Then prove it with chaos testing, not hope.

---

## 4. Containers & Kubernetes

**Q: Why Kubernetes over just running containers on VMs?** *(Days 16–17)*
> Docker gives you packaging; Kubernetes gives you *operations*: declarative
> desired state, self-healing (restarts crashed pods, reschedules off dead
> nodes), horizontal scaling, service discovery, rolling updates with automatic
> rollback, and bin-packing efficiency. You trade significant complexity for
> that — which is why the honest answer includes "and for small workloads,
> Container Apps or App Service is the right call."

**Q: Explain a Kubernetes deployment rolling update.** *(Day 17)*
> A Deployment declaratively manages ReplicaSets. On update it creates a new
> ReplicaSet, scales it up gradually while scaling the old one down, governed
> by `maxSurge` (extra pods allowed) and `maxUnavailable` (pods that can be
> down). Readiness probes gate traffic to new pods; if probes fail, the rollout
> pauses. `kubectl rollout undo` reverts to the previous ReplicaSet instantly.

---

## 5. CI/CD & DevOps

**Q: Deploy a change to production with zero downtime — walk me through it.** *(Day 11)*
> Depends on risk tolerance. **Blue-green:** run two identical environments,
> deploy to idle green, smoke test, flip the router, keep blue warm for instant
> rollback. **Canary:** route 1–5% of traffic to the new version, watch SLIs
> (error rate, latency) with automated analysis, progressively raise to 100% or
> auto-rollback on regression. **Feature flags** decouple deploy from release —
> code ships dark, features turn on per-cohort. In all three, the database
> schema must be backward compatible (expand/contract migrations) so old and
> new code coexist.

**Q: What's the difference between CI and CD?** *(Day 10)*
> **CI** — every commit triggers build + automated tests, so integration
> problems surface in minutes, and `main` is always releasable. **CD** has two
> meanings: continuous *delivery* (every green build is deployable, a human
> pushes the button) and continuous *deployment* (green builds go straight to
> prod behind gates). The pipeline: commit → build → unit tests → package →
> deploy to staging → integration tests → approval gate → production.

**Q: How do you keep secrets out of pipelines and code?** *(Day 10)*
> Never in source, never in plain pipeline variables. Use Azure Key Vault
> linked into pipeline variable groups, or Azure DevOps secret variables
> (masked, write-only). Best practice: managed identity + RBAC so the pipeline
> authenticates to Azure with no stored credential at all. Add secret scanning
> (e.g., in PR checks) as a backstop.

---

## 6. Data & Scale

**Q: What is a data lake, and how is it different from a warehouse?** *(Day 23)*
> A data lake (ADLS Gen2) stores raw data in open formats — Parquet, JSON,
> images — schema-on-read, cheap, infinite scale. A warehouse stores curated,
> schema-on-write, SQL-optimized data. Modern pattern is **medallion
> architecture**: bronze (raw landing) → silver (cleaned, typed, deduped) →
> gold (aggregated, business-ready) — usually with Spark/Fabric/Databricks
> transforming between layers.

---

## 7. Agentic AI in the SDLC *(the differentiator)*

**Q: How have you used AI agents in a real development workflow?** *(Day 24)*
> Three concrete places: (1) **Generation** — agents scaffold boilerplate:
> Bicep templates, pipeline YAML, test cases from API specs. (2) **Review** —
> AI-assisted PR review catches mechanical issues so human reviewers focus on
> design. (3) **Validation** — this is the subtle one: LLM-generated code and
> tests are syntactically right but semantically wrong ~a third of the time, so
> I built an evaluation step: generated tests pass through schema validation,
> an LLM-judge for semantic quality, and sandboxed execution before they enter
> the suite. That cut low-quality tests reaching the suite by ~40%.

**Q: How do you trust AI-generated code in production?** *(Day 25)*
> Same way you trust a junior engineer's code: you don't — you verify. Treat
> the agent as a fast junior with infinite stamina: small scoped tasks,
> mandatory tests it didn't write for itself, static analysis gates in CI,
> human review for anything touching auth/payments/data. Measure it like a
> team member: acceptance rate of generated PRs, defect rate of AI-touched
> code vs baseline. The pipeline is the safety net, not the prompt.

---

## 8. Leadership & Behavioral *(for the "5 years leadership" requirement)*

**Q: How do you mentor engineers at different levels?** *(Day 29)*
> Match the mode to the person: juniors get pairing and concrete feedback on
> artifacts (PRs, designs); mid-levels get stretch ownership with a safety net
> — "you own this service's reliability, I'm your escalation path"; seniors get
> problems, not tasks. Universal rule: never just answer — ask what they've
> tried, guide them to the answer. It scales you and grows them.

**Q: Tell me about a time you delivered a complex project on time.** *(Day 29)*
> Structure: scope ruthlessly (what's the smallest thing that's still a win?),
> identify the riskiest unknown and spike it in week one, decompose into
> independently shippable milestones, and communicate status in terms of
> *confidence*, not percent-done. When we slipped, we cut scope — never
> quality or testing — and told stakeholders early with options, not late with
> surprises.

**Q: How do you explain a technical tradeoff to non-technical stakeholders?** *(Day 29)*
> Translate to money, risk, and time. Not "we need to add a circuit breaker"
> but "when the payments provider has an outage — they had two last year — our
> checkout currently hangs for 30 seconds and we lose the sale. For two days of
> work, we can degrade gracefully and keep 95% of those sales." Lead with the
> business outcome, offer the decision, own the recommendation.

**Q: Tell me about a time you responded to an incident.** *(Days 26–28 — after
your game day you can answer with a real one)*
> STAR format: **Situation** (what broke, blast radius), **Task** (your role —
> incident commander? hands-on?), **Action** (how you triaged, what you
> mitigated first vs root-caused later), **Result** (MTTR, what the postmortem
> changed). The game-day exercise on Day 28 gives you a genuine story:
> injected failure → detection via your own alerts → response → postmortem doc.
