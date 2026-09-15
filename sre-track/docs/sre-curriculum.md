# SRE Track — Day-by-Day Curriculum

Each day: 📖 reading (Microsoft Learn) → 📝 concepts → 🛠️ hands-on → 🎤 interview drill.
Estimated 45–75 min/day unless noted. Cost estimates assume you run the cleanup step.

---

## Phase 1 — SRE Foundations (Days 01–04)

### Day 01 — What is SRE
- 📖 Read: [Introduction to SRE](https://learn.microsoft.com/en-us/training/modules/intro-to-site-reliability-engineering/) units 1–4 (Intro, What is SRE, SRE in context, Virtuous cycles)
- 📝 Concepts: SRE = "what happens when you ask a software engineer to run operations"; SRE vs DevOps vs traditional ops; the virtuous cycle (measure → analyze → improve)
- 🛠️ Exercise: **self-assessment worksheet** — score a system you know against SRE practices; write your personal SRE learning objectives mapped to the job description
- 🎤 Drill: "What is SRE and why does it matter?"
- 💰 Cost: $0

### Day 02 — SLIs, SLOs & Error Budgets
- 📖 Read: same module, units 5–7 (human side of SRE, getting started, summary) + skim [SLO guidance](https://learn.microsoft.com/en-us/azure/well-architected/reliability/metrics)
- 📝 Concepts: SLI/SLO/SLA hierarchy; error budget math; why 100% is the wrong target; the "happiness test" for choosing SLIs
- 🛠️ Exercise: **error budget calculator** (Python, worked example in `day-02-sli-slo-error-budget/`) — compute budget windows, burn rates, and answer "can we ship this week?"
- 🎤 Drill: "SLI vs SLO vs SLA?" + "Why is 100% reliability the wrong goal?"
- 💰 Cost: $0

### Day 03 — Toil, Automation & the SRE Mindset
- 📖 Read: [Google SRE book, Ch. 5 "Eliminating Toil"](https://sre.google/sre-book/eliminating-toil/) (free online) — the canonical text
- 📝 Concepts: toil definition (manual, repetitive, automatable, scales with service); the 50% toil cap; automation as the leverage of SRE
- 🛠️ Exercise: **toil audit** — list 10 repetitive tasks you do (or have done); classify toil vs. engineering; pick one and automate it today with a script in this repo (candidate: the git branch/commit/merge dance from your coding-challenges track → `automation/day-commit.sh`)
- 🎤 Drill: "What is toil and what do you do about it?"
- 💰 Cost: $0

### Day 04 — Azure Setup & Cost Guardrails
- 📖 Read: [docs/azure-setup-and-cost-safety.md](azure-setup-and-cost-safety.md) in this repo (your own study material)
- 📝 Concepts: Azure account structure (subscription → resource group → resource); why resource groups are your cost-safety unit
- 🛠️ Exercise: install/verify Azure CLI, `az login`, set a **$5 budget with alerts**, create and delete your first resource group end-to-end. Verify VS Code Azure tooling can list your resources.
- 🎤 Drill: "How do you keep cloud lab costs under control?" (real interview question for senior roles — cost ownership)
- 💰 Cost: $0

---

## Phase 2 — Observability (Days 05–07, 18)

### Day 05 — Azure Monitor: Metrics & VM Insights
- 📖 Read: [Monitor your Azure VMs with Azure Monitor](https://learn.microsoft.com/en-us/training/modules/monitor-azure-vm-using-diagnostic-data/) (has sandbox exercises — do them)
- 📝 Concepts: metrics vs logs; host vs guest metrics; VM insights; data collection rules
- 🛠️ Exercise: deploy a `B1s` VM (~$0.01/hr), enable VM insights, open Metrics Explorer, generate CPU load (`stress` or a loop), watch it live. Cleanup.
- 🎤 Drill: "Metrics vs logs — when do you use each?"
- 💰 Cost: ~$0.05

### Day 06 — Application Insights: Instrument a Live App
- 📖 Read: [Manage site reliability](https://learn.microsoft.com/en-us/training/modules/manage-site-reliability/) units 1–3 (reliability engineering, App Insights) + [App Insights instrumentation docs](https://learn.microsoft.com/en-us/azure/azure-monitor/app/app-insights-overview)
- 📝 Concepts: requests/dependencies/exceptions/traces; the end-to-end transaction view; sampling; connection strings
- 🛠️ Exercise: deploy a small **FastAPI app to App Service F1 (free)**, add the `opencensus`/`azure-monitor-opentelemetry` SDK, generate traffic + errors, find your traces in the portal. Keep it deployed — Days 07, 13 build on it.
- 🎤 Drill: "Walk me through debugging 'the site is slow.'"
- 💰 Cost: $0 (F1 + free App Insights tier)

### Day 07 — KQL, Log Analytics & SLO Dashboard
- 📖 Read: [KQL quick reference](https://learn.microsoft.com/en-us/azure/data-explorer/kql-quick-reference) + [Manage site reliability](https://learn.microsoft.com/en-us/training/modules/manage-site-reliability/) units 4–5 (alert tuning, baselines)
- 📝 Concepts: Log Analytics tables; `where | summarize | render`; the symptom-vs-cause alerting rule; baselining alert noise
- 🛠️ Exercise: write 5 KQL queries against your Day-06 app: error rate over time, p95 latency by endpoint, top exceptions, availability %, dependency failures. Pin them to an **Azure Workbook = your SLO dashboard**. Create ONE symptom alert (error rate > 2%) with an action group to your email.
- 🎤 Drill: "How do you decide what to alert on?"
- 💰 Cost: $0
- 📁 You now have: a live instrumented app + SLO dashboard + alert. Screenshot-worthy portfolio piece.

---

## Phase 3 — DevOps & Delivery (Days 08–12)

### Day 08 — API Design + API Management
- 📖 Read: [API design guidance (Azure Architecture Center)](https://learn.microsoft.com/en-us/azure/architecture/best-practices/api-design)
- 📝 Concepts: REST resource modeling; versioning strategies (path vs header); idempotency keys on POSTs; rate limiting; why a gateway (APIM) sits in front; the API contract a mobile (Flutter/RN) client depends on
- 🛠️ Exercise: extend your Day-06 app into a proper `orders-api` (versioned `/v1/orders`, idempotent POST). Free path: deploy APIM **Consumption tier** in front with a rate-limit policy, test the throttling with a loop. If Consumption is slow to provision, simulate the policies in-app and deploy APIM on Day 30 only.
- 🎤 Drill: "How do you version an API without breaking mobile clients?"
- 💰 Cost: $0 (Consumption APIM is per-call, pennies)

### Day 09 — Azure DevOps: Org, Project, Repo, Boards
- 📖 Read: [AZ-400 CI path](https://learn.microsoft.com/en-us/training/paths/az-400-implement-ci-azure-pipelines-github-actions/), first module units on Azure DevOps structure
- 📝 Concepts: org → project → repo/boards/pipelines; work items → your "user story" vocabulary for interviews; the free parallel-job grant (request early — takes 2–3 business days!)
- 🛠️ Exercise: create org + project at dev.azure.com, push this repo, create 3 work items ("instrument orders-api", "add CI", "SLO dashboard"), link one to a commit. **Request the free hosted parallelism grant TODAY** (form link in day README) so Day 10 isn't blocked.
- 🎤 Drill: "How do you structure work tracking for a team?"
- 💰 Cost: $0

### Day 10 — CI Pipeline in YAML
- 📖 Read: [AZ-400 CI path](https://learn.microsoft.com/en-us/training/paths/az-400-implement-ci-azure-pipelines-github-actions/) — build/test module units
- 📝 Concepts: pipeline anatomy (trigger → pool → steps); CI definition (every commit builds+tests); secrets via Key Vault / secret variables; build badges
- 🛠️ Exercise: `azure-pipelines.yml` for `orders-api`: restore → build → unit tests → publish artifact. Break a test on purpose, watch CI go red, fix it. Add a status badge to the day README.
- 🎤 Drill: "CI vs CD?" + "How do you keep secrets out of pipelines?"
- 💰 Cost: $0

### Day 11 — Release Strategies: Blue-Green, Canary, Rings
- 📖 Read: [AZ-400: Design & implement a release strategy](https://learn.microsoft.com/en-us/training/paths/az-400-design-implement-release-strategy/)
- 📝 Concepts: deployment patterns comparison; expand/contract DB migrations (old + new code must coexist); rollback vs roll-forward
- 🛠️ Exercise: deploy `orders-api` to an App Service with a **staging slot** (blue-green on a budget): deploy → smoke test slot → swap → instant rollback by swapping back. Then simulate a canary: route 20% of traffic to the slot via slot routing rules, watch App Insights split.
- 🎤 Drill: "Zero-downtime deploy — walk me through it." ← the classic
- 💰 Cost: $0–0.10 (slots need S1 tier ~$0.10/hr — use for 1–2 hrs, then delete; or do slot concepts on F1 with manual verification)

### Day 12 — CD with Approvals, Gates & Feature Flags
- 📖 Read: [AZ-400: Implement secure continuous deployment](https://learn.microsoft.com/en-us/training/paths/az-400-implement-secure-continuous-deployment/)
- 📝 Concepts: environments with approvers; pre/post-deployment gates (query App Insights alerts as a gate!); feature flags decouple deploy from release
- 🛠️ Exercise: extend the pipeline: `staging` environment (auto) → gate querying your Day-07 alert → `prod` environment with your approval. Add one feature flag (env-var driven) to `orders-api`, ship a feature dark, flip it on.
- 🎤 Drill: "What's the difference between continuous delivery and continuous deployment?"
- 💰 Cost: $0
- 📁 You now have: full CI/CD with gates — screenshot the pipeline for your portfolio.

---

## Phase 4 — Resilience & Distributed Systems (Days 13–15, 19–20)

### Day 13 — Elasticity & Autoscale
- 📖 Read: [Scale your cloud resources with elasticity](https://learn.microsoft.com/en-us/training/modules/cmu-cloud-elasticity/)
- 📝 Concepts: vertical vs horizontal scaling; scale-out rules (metric + schedule); cooldown; why statelessness is the prerequisite
- 🛠️ Exercise: put your `orders-api` on an S1 plan with a CPU-based autoscale rule; hammer it with a load script (`load/hammer.py` — provided pattern: async loop firing requests); watch instance count climb in the portal; stop the load, watch it scale in. Cleanup/downgrade.
- 🎤 Drill: "Design for a 10x traffic spike."
- 💰 Cost: ~$0.20 (S1 for 2–3 hrs)

### Day 14 — Fault Tolerance in Code: Retry, Backoff, Circuit Breaker
- 📖 Read: [Transient fault handling guidance](https://learn.microsoft.com/en-us/azure/architecture/best-practices/transient-faults)
- 📝 Concepts: transient vs permanent faults; exponential backoff + jitter; circuit breaker states (closed/open/half-open); timeouts on EVERYTHING; bulkheads
- 🛠️ Exercise: **pure code day** (Python): given a flaky fake dependency (`flaky_server.py` — fails 50% of the time), implement in order: (1) timeout, (2) retry with exponential backoff + jitter, (3) circuit breaker, and measure success rate after each layer. This is a coding-interview classic AND a design-interview talking point.
- 🎤 Drill: "How do you make a service fault-tolerant?"
- 💰 Cost: $0

### Day 15 — Load Balancing + Message Queues
- 📖 Read: [Build applications on the cloud](https://learn.microsoft.com/en-us/training/modules/cmu-build-apps-cloud/) (load balancing, scaling, latency units)
- 📝 Concepts: L4 vs L7 load balancing; health probes; decoupling with queues — producer/consumer; peek-lock semantics; poison messages & dead-letter queues
- 🛠️ Exercise: split `orders-api` into producer (API) + consumer (worker) over a **Storage Queue** (free tier of a storage account). Kill the worker, watch messages accumulate, restart, watch drain. Push a poison message, watch it dead-letter after 5 attempts.
- 🎤 Drill: "Why put a queue between services?"
- 💰 Cost: $0 (storage queues ~free at this scale)

### Day 19 — Infrastructure as Code with Bicep
- 📖 Read: [AZ-400: Manage infrastructure as code](https://learn.microsoft.com/en-us/training/paths/az-400-manage-infrastructure-as-code-using-azure/) (Bicep modules)
- 📝 Concepts: declarative vs imperative; idempotent deployments; `what-if`; why IaC is an SRE practice (reproducible environments, drift detection, audit trail)
- 🛠️ Exercise: author `main.bicep` that recreates your Day-06 stack (App Service plan + app + App Insights + alert rule). `az deployment group what-if`, then deploy, verify, delete, redeploy — prove reproducibility.
- 🎤 Drill: "Why does IaC matter for reliability?" (answer: reproducibility + no snowflake servers)
- 💰 Cost: $0

### Day 20 — Chaos Engineering
- 📖 Read: [Azure Chaos Studio overview](https://learn.microsoft.com/en-us/azure/chaos-studio/chaos-studio-overview) + [principles of chaos engineering](https://principlesofchaos.org/)
- 📝 Concepts: hypothesis-driven failure injection; blast radius control; steady state first; game days
- 🛠️ Exercise: Chaos Studio experiment against your Day-13 app: inject CPU pressure / kill an instance. Hypothesis written down FIRST ("p95 latency stays < 500ms because autoscale compensates"), then run, observe, conclude. Delete the experiment.
- 🎤 Drill: "What is chaos engineering and when is it appropriate?"
- 💰 Cost: ~$0.10 (chaos targets bill per hour — keep it short)

---

## Phase 5 — Containers & Kubernetes (Days 16–18)

### Day 16 — Docker: Build, Tag, Push
- 📖 Read: [AZ-400 CI path — container build strategy module](https://learn.microsoft.com/en-us/training/paths/az-400-implement-ci-azure-pipelines-github-actions/)
- 📝 Concepts: image layers & caching; multi-stage builds; Dockerfile best practices (small base images, non-root user, .dockerignore); image tagging discipline
- 🛠️ Exercise: containerize `orders-api` (multi-stage Dockerfile provided as skeleton, you fill in). Run locally, then create an **Azure Container Registry** and push. Pull and run from ACR to prove it.
- 🎤 Drill: "How do you keep images small and secure?"
- 💰 Cost: ~$0.01 (Basic ACR ~$0.17/day — delete after Day 18)

### Day 17 — AKS: Deploy, Scale, Self-Heal
- 📖 Read: [Introduction to Kubernetes on Azure](https://learn.microsoft.com/en-us/training/paths/intro-to-kubernetes-on-azure/)
- 📝 Concepts: pods/deployments/services; readiness vs liveness probes; `maxSurge`/`maxUnavailable`; resource requests/limits
- 🛠️ Exercise: provision a minimal AKS cluster (1 node, cheapest SKU), deploy `orders-api` from ACR with probes set, then: kill a pod (watch self-heal), scale to 3 replicas, do a rolling update, roll it back. ~90 min day.
- 🎤 Drill: "Explain a Kubernetes rolling update." + "Readiness vs liveness?"
- 💰 Cost: ~$3–4/day for the node VM — **delete the cluster when done** (or run Days 17–18 back-to-back)

### Day 18 — Prometheus + Grafana on AKS
- 📖 Read: [Monitor AKS with Managed Prometheus & Grafana](https://learn.microsoft.com/en-us/azure/azure-monitor/containers/kubernetes-monitoring-enable)
- 📝 Concepts: pull vs push metrics; PromQL basics; scrape configs; exporters; Grafana dashboards; Prometheus vs Azure Monitor (interview answer in the question bank)
- 🛠️ Exercise: enable Azure Monitor **managed Prometheus + managed Grafana** on your Day-17 cluster (this is the free/cheap path), explore the prebuilt dashboards, write 3 PromQL queries (request rate, error ratio, p95 latency). Then delete the cluster AND ACR.
- 🎤 Drill: "Prometheus vs Azure Monitor — when each?"
- 💰 Cost: shared with Day 17 cluster

---

## Phase 6 — Data, AI & Incidents (Days 21–30)

### Day 21 — Distributed Systems Theory
- 📖 Read: [Azure Architecture Center: distributed system patterns](https://learn.microsoft.com/en-us/azure/architecture/patterns/) (pick: Circuit Breaker, Retry, Queue-Based Load Leveling, Compensating Transaction)
- 📝 Concepts: CAP in practical terms; consistency models; idempotency (keys, dedup); the fallacies of distributed computing; backpressure
- 🛠️ Exercise: **no Azure** — write a one-page "distributed systems cheat sheet" in your own words with one diagram per concept, then add an idempotency key to the Day-08 `POST /v1/orders` endpoint and write a test that double-submits.
- 🎤 Drill: "Explain CAP practically." + "How do you implement idempotency?"
- 💰 Cost: $0

### Day 22 — Messaging Patterns
- 📖 Read: [Azure messaging services overview](https://learn.microsoft.com/en-us/azure/event-grid/compare-messaging-services)
- 📝 Concepts: queue vs pub/sub vs event streaming; at-least-once + idempotent consumer ≈ exactly-once; ordering & sessions; dead-lettering (revisited from Day 15); Event Grid vs Service Bus vs Event Hubs
- 🛠️ Exercise: upgrade Day-15's Storage Queue to **Service Bus** (Basic tier ~$0.05): topics + subscriptions (pub/sub), two subscribers with different filters, dead-letter inspection in the portal.
- 🎤 Drill: "At-least-once vs exactly-once delivery?"
- 💰 Cost: ~$0.05

### Day 23 — Data Lakes & Scaled Data Systems
- 📖 Read: [ADLS Gen2 overview](https://learn.microsoft.com/en-us/azure/storage/blobs/data-lake-storage-introduction) + medallion architecture docs
- 📝 Concepts: schema-on-read vs on-write; bronze/silver/gold layers; Parquet & partitioning; hierarchical namespace; lake vs warehouse
- 🛠️ Exercise: create an ADLS Gen2 account, build bronze/silver/gold containers, have your Day-15 worker write order events as JSON files partitioned `yyyy/MM/dd` into bronze; write a small Python transform (pandas or polars) that produces a silver "clean orders" parquet. Query it with a DuckDB one-liner.
- 🎤 Drill: "Data lake vs warehouse?" + "Explain medallion architecture."
- 💰 Cost: $0 (storage at this scale is pennies)

### Day 24 — Agentic AI in the SDLC
- 📖 Read: [GitHub Copilot coding agent docs](https://docs.github.com/en/copilot/concepts/coding-agent/coding-agent) + Microsoft Foundry agent docs
- 📝 Concepts: where agents fit in the SDLC (generate → review → test → document); scoping tasks for agents; the pipeline as the safety net, not the prompt
- 🛠️ Exercise: use Copilot coding agent (or an agent here) to complete a real, scoped task end-to-end — e.g., "add a GET /v1/orders/{id} endpoint with tests" via an issue → PR flow. You review it like a tech lead: what did it get right/wrong? Document your rubric.
- 🎤 Drill: "How have you used AI agents in a real workflow?" — answer with TODAY's story
- 💰 Cost: $0

### Day 25 — AI Quality Evaluation (your differentiator)
- 📖 Read: evaluation patterns in [Microsoft Foundry docs](https://learn.microsoft.com/en-us/azure/ai-foundry/) (evaluation section)
- 📝 Concepts: LLM-as-judge; evaluation rubrics; schema → semantic → execution validation pipeline; measuring AI contribution quality (acceptance rate, defect rate)
- 🛠️ Exercise: build a mini evaluator (Python) that scores AI-generated tests for `orders-api`: (1) schema check, (2) rubric-scored LLM review, (3) actually run them. Feed it 5 good + 5 bad tests (write the bad ones yourself), verify it separates them. This is your "40% reduction" story, made real and demonstrable.
- 🎤 Drill: "How do you trust AI-generated code in production?"
- 💰 Cost: $0

### Day 26 — Incident Management & On-Call
- 📖 Read: [Manage site reliability](https://learn.microsoft.com/en-us/training/modules/manage-site-reliability/) units 1–2 (revisited) + incident command overview
- 📝 Concepts: severity levels; incident commander vs comms lead vs ops; mitigate first, root-cause later; MTTR and why it's the metric that matters; on-call health
- 🛠️ Exercise: **tabletop drill** — I give you an incident scenario (p95 latency spike on orders-api), you narrate your full response: detection → triage → mitigation → comms → resolution. Written timeline in the day folder.
- 🎤 Drill: "Walk me through your incident response process."
- 💰 Cost: $0

### Day 27 — Blameless Postmortems
- 📖 Read: [Manage site reliability — unit 6: Blameless postmortems](https://learn.microsoft.com/en-us/training/modules/manage-site-reliability/)
- 📝 Concepts: just culture; "what failed in the system, not who"; action items with owners; the postmortem template
- 🛠️ Exercise: write a complete postmortem (template provided) for yesterday's tabletop incident — timeline, root cause (5-whys), what went well/poorly, 3+ action items. This becomes an interview artifact.
- 🎤 Drill: "What makes a postmortem blameless, and why does it matter?"
- 💰 Cost: $0

### Day 28 — Game Day
- 📖 Read: review your Day 20 chaos notes + Day 26 process
- 📝 Concepts: putting it together — detect (your Day-07 alerts), respond (Day-26 process), learn (Day-27 template)
- 🛠️ Exercise: **full dress rehearsal.** Redeploy your stack via Day-19 Bicep, have a "chaos monkey" script inject a fault at a random time (you don't know which), respond for real: alerts fire → you triage → mitigate → write the postmortem. This is your interview story, end to end.
- 🎤 Drill: "Tell me about a time you responded to an incident." ← you now answer with a real one
- 💰 Cost: ~$0.10

### Day 29 — Leadership & Communication
- 📖 Read: no Learn module — this is craft. (Optional: [Azure Well-Architected operational excellence](https://learn.microsoft.com/en-us/azure/well-architected/operational-excellence/))
- 📝 Concepts: mentoring modes by seniority; estimation & scope-cutting; communicating in money/risk/time; writing design docs
- 🛠️ Exercise: (1) Write a one-page design doc for the capstone system as if proposing it to a team. (2) Record yourself answering the three leadership questions from the question bank — out loud, ≤ 2 min each. (3) Rewrite one technical concept from this track for a "non-technical stakeholder."
- 🎤 Drill: all three leadership questions
- 💰 Cost: $0

### Day 30 — 🏆 Capstone
- 🛠️ The full system, one deployment:
  1. Deploy everything via Bicep (Day 19): APIM-fronted `orders-api` (containerized, AKS) + Service Bus worker + ADLS sink
  2. CI/CD via Azure DevOps with gates (Days 10–12)
  3. Observability: App Insights + SLO workbook + Prometheus/Grafana (Days 06–07, 18)
  4. Prove resilience: run the chaos experiment, watch autoscale + circuit breakers respond (Days 13–14, 20)
  5. Write the capstone README: architecture diagram, SLO definitions, one incident story, cost summary
- 🎤 Final drill: present the whole system in 10 minutes, out loud, as if to a hiring panel. Then delete everything and confirm with `az resource list`.
- 📁 **This README + your postmortem + pipeline screenshots = your portfolio.**
- 💰 Cost: ~$5 for the full day (AKS is the bulk) — then $0 again.

---

## Parallel Track Reminder

Your `java-python-coding-challenges` day folders continue in parallel — coding
interviews and system-design/SRE interviews are separate loops, and this job
description expects both. Suggested split: coding challenge on Mon/Wed/Fri,
SRE track on Tue/Thu/Sat.
