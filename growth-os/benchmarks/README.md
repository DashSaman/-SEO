# Benchmarks / بنچمارک‌ها

Purpose: compare LLMs, routing policies, crawlers, agents, workflows, cost, latency, reliability, and task quality using repeatable measurements.

هدف: مقایسه مدل‌های AI، Routing، Crawlerها، Agentها، Workflowها، هزینه، سرعت، پایداری و کیفیت بر اساس داده واقعی.

## Benchmark rule
Store the task definition, input class, model/provider/version, context size, latency, token/API cost, local compute time, quality result, failure rate, and date. Do not compare models using undocumented anecdotes.

## Operator documentation contract / قرارداد مستندسازی
Any reusable benchmark tool/component must record: purpose; why selected; version; prerequisites; installation; configuration; ports/network exposure; secret variable names only; verification; normal operation; update procedure; backup/restore; rollback; common failures; removal procedure; upstream repository and license.
