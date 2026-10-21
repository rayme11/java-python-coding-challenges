# Azure Setup & Cost Safety — READ BEFORE ANY HANDS-ON DAY

Every exercise in this track touches real Azure. That means real money if you're
careless. Follow these rules and your total cost for the entire 20 days should be
**$0–5** (mostly $0 on a free account).

---

## 1. One-time setup

```bash
# Install Azure CLI (macOS)
brew install azure-cli

# Log in (opens browser)
az login

# See your subscriptions
az account list --output table

# Set the one you want to use
az account set --subscription "<name-or-id>"
```

**No subscription?** Create a free one: <https://azure.microsoft.com/free/>
- $200 credit for 30 days, plus 12 months of popular free services.
- A credit card is required for identity verification; you are NOT charged
  unless you explicitly upgrade to pay-as-you-go.

## 2. Verify in VS Code

You also have Azure tooling inside VS Code (Azure extension + MCP server).
Ask Copilot things like *"list my resource groups"* or *"what subscriptions do I
have?"* — it can query your real environment. This makes the exercises faster:
Copilot can run the `az` commands with you and explain each flag.

## 3. The Golden Rules of Cost Safety

| # | Rule | Why |
|---|------|-----|
| 1 | **One resource group per day:** `rg-sre-day03`, `rg-sre-day04`, … | Deleting the group deletes EVERYTHING in it — no orphans |
| 2 | **Every exercise ends with cleanup** — never skip it | Resources bill by the hour |
| 3 | Prefer **free/cheap SKUs**: App Service `F1`, VM `B1s`/`B2s`, Functions Consumption | F1 and Consumption are literally free at this scale |
| 4 | Set a **budget + cost alert** on day one (see below) | Safety net if you forget rule 2 |
| 5 | **Never commit secrets** — no keys, passwords, or connection strings in git | Real-world SRE habit, and protects you |

### Cleanup command (memorize it)

```bash
az group delete --name rg-sre-day03 --yes --no-wait
```

### Verify nothing is left running (weekly habit)

```bash
az resource list --output table
```

If you see anything you don't recognize → investigate → delete.

## 4. Set a budget alert (do this once, today)

Portal: **Cost Management + Billing → Budgets → Add**
- Scope: your subscription
- Amount: **$5/month**
- Alert at 50% and 90% → your email

Or via CLI:

```bash
az consumption budget create \
  --budget-name sre-track-budget \
  --amount 5 \
  --time-grain Monthly \
  --start-date $(date +%Y-%m-01) \
  --end-date 2027-12-01 \
  --category Cost
```

(If `az consumption` complains on a free account, use the portal — same result.)

## 5. What's free vs. what costs money

| Resource | Cost at exercise scale | Notes |
|----------|------------------------|-------|
| App Service F1 (Free tier) | **$0** | 60 min CPU/day — plenty for labs |
| Azure Functions (Consumption) | **$0** | 1M free executions/month |
| Application Insights | **$0** | First 5 GB/month free |
| Log Analytics workspace | **$0** | First 5 GB/month free |
| Azure DevOps (basic) | **$0** | Free for 5 users, 1 free CI parallel job (grant required) |
| VM B1s | **~$0.01/hr** | Delete same day = pennies. 750 hrs/mo free for 12 months |
| Azure Load Balancer (Basic) | **$0** | Basic SKU is free |
| Azure Chaos Studio | ~$0 for tiny experiments | Targets billed per hour — delete experiment after |
| Azure Front Door / Traffic Manager | ⚠️ costs real money | Day 15 offers a free alternative path |

**Rule of thumb:** if a day's exercise needs something that isn't free, the
README for that day says so up front and gives a cheaper alternative.

## 6. When something goes wrong

```bash
# Nuclear option — list every resource group and delete the lab ones
az group list --output table
az group delete --name <rg-name> --yes --no-wait
```

Costs still surprising you? Portal → **Cost Management → Cost analysis**,
group by **Resource group**. The culprit will be obvious within one minute.
