#!/usr/bin/env python3
"""
AWS EC2 p5.48xlarge vs Vast.ai 8x H100 SXM5 Pricing & TCO Benchmark 2026.
Analyzes foundational LLM pre-training and high-throughput fine-tuning cluster budgets.
"""
import argparse

def calculate_cluster_costs(hours, aws_hourly, vastai_hourly):
    aws_total = hours * aws_hourly
    vastai_total = hours * vastai_hourly
    net_savings = aws_total - vastai_total
    savings_pct = (net_savings / aws_total * 100.0) if aws_total > 0 else 0.0
    annual_aws = aws_total * 12.0
    annual_vastai = vastai_total * 12.0
    annual_savings = net_savings * 12.0
    return {
        "aws_total": aws_total,
        "vastai_total": vastai_total,
        "net_savings": net_savings,
        "savings_pct": savings_pct,
        "annual_aws": annual_aws,
        "annual_vastai": annual_vastai,
        "annual_savings": annual_savings
    }

def main():
    parser = argparse.ArgumentParser(description="AWS p5 vs Vast.ai 8x H100 Cluster Cost Comparison")
    parser.add_argument("--hours", type=float, default=100.0, help="Training run hours (default: 100)")
    parser.add_argument("--aws-rate", type=float, default=98.32, help="AWS p5.48xlarge on-demand hourly rate in USD (default: $98.32)")
    parser.add_argument("--vastai-rate", type=float, default=23.92, help="Vast.ai 8x H100 SXM5 cluster hourly rate in USD (default: $23.92)")
    args = parser.parse_args()

    res = calculate_cluster_costs(args.hours, args.aws_rate, args.vastai_rate)
    print(f"AWS p5.48xlarge Total:   ${res['aws_total']:.2f}")
    print(f"Vast.ai 8x H100 Total:   ${res['vastai_total']:.2f}")
    print(f"Net Workload Savings:    ${res['net_savings']:.2f}")
    print(f"Cost Reduction:          {res['savings_pct']:.1f}%")
    print(f"Annual Projected AWS:    ${res['annual_aws']:.2f}")
    print(f"Annual Projected Vast.ai:${res['annual_vastai']:.2f}")
    print(f"Annual Net Savings:      ${res['annual_savings']:.2f}")

if __name__ == "__main__":
    main()
